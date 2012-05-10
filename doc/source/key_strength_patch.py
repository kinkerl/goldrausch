"""
Adds key strengthening (via sha384 + large number of hash iterations) to the
default Django password implementation.

The number of iterations is stored along with the hash so that in the future,
the number of rounds can be increased for new passwords in the same system.

Standard Django hashes look like:
algo$salt$hash

Hashes using this file's method will look like:
algo$salt$rounds$hash

Where `rounds` is an integer for the number of key strengthening hash
iterations to perform. `check_password` handles both cases by checking for
the extra `$` character.
"""

from hashlib import sha384
def hard_sha384(s, salt, rounds=50000):
    """
    50000 rounds approximately costs 0.1-0.8 seconds on circa 2010 hardware.
    
    sha384 used so that algo+salt+size+hash fits into 128 characters (Django
    length for User.password field.)
    """
    h = sha384("%s%s"%(s,salt))
    
    r = 0
    while r < rounds:
        h = sha384("%s%s"%(
            h.digest(),
            salt
        ))
        r = r+1
    
    return h.hexdigest()


# ===============================================================


# Imported so we may monkey patch it.
from django.contrib.auth import models as auth_models

from django.utils.encoding import smart_str
from hashlib import md5 as md5_constructor, sha1 as sha_constructor

def get_hexdigest(algorithm, salt, raw_password, rounds=50000):
    """ Adds support for our 'hard-sha384' method to get_hexdigest in auth.models """
    raw_password, salt = smart_str(raw_password), smart_str(salt)
    if algorithm == 'crypt':
        try:
            import crypt
        except ImportError:
            raise ValueError('"crypt" password algorithm not supported in this environment')
        return crypt.crypt(raw_password, salt)

    if algorithm == 'md5':
        return md5_constructor(salt + raw_password).hexdigest()
    elif algorithm == 'sha1':
        return sha_constructor(salt + raw_password).hexdigest()
    elif algorithm == "hard-sha384":
        return hard_sha384(raw_password, salt, rounds)
    
    raise ValueError("Got unknown password algorithm type in password.")

auth_models.get_hexdigest = get_hexdigest

def check_password(raw_password, enc_password):
    """
    Returns a boolean of whether the raw_password was correct. Handles
    encryption formats behind the scenes.
    """
    algo, salt, hsh = enc_password.split('$', 2)
    rounds = 1
    
    # New detection for the `rounds` parameter.
    if "$" in hsh:
        rounds, hsh = hsh.split('$', 1)
        rounds = int(rounds)
    
    return hsh == get_hexdigest(algo, salt, raw_password, rounds)

auth_models.check_password = check_password

def _user_set_password(self, raw_password, rounds=None):
    if type(rounds) != int:
        from django.conf import settings
        rounds = getattr(settings, 'PASSWORD_KEYSTRENGTH_ROUNDS', 50000)
    
    if raw_password is None:
        self.set_unusable_password()
    else:
        # By default use the new, key-strengthened `hard-sha384` method.
        import random
        algo = 'hard-sha384'
        salt = get_hexdigest(algo, str(random.random()), str(random.random()), 1)[:5]
        hsh = get_hexdigest(algo, salt, raw_password)
        self.password = '%s$%s$%d$%s' % (algo, salt, rounds, hsh)

auth_models.User.set_password = _user_set_password
