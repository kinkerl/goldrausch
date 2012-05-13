goldrausch
==========

a simple event node. receives status updates of tasks from agents over http, stores the status and creates a small xml from all the informations for further handling.


setup
----------

 * start the server
 * create agents and tasks of the agents you want to track
 * take a look at the /overview page to see the resulting xml
 * supply the agents with the security secret entered in the admin interface
 * make the agents call the /update uri with the needed parameters to set the status
 * profit!
 
overview: 
----------

![illustration](https://github.com/kinkerl/goldrausch/raw/master/doc/images/overview.png)

