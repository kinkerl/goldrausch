$( document ).ready(function() {

    // harmonies from adobe kuler
    var harmonies = [
            [
                '#0a7b83',
                '#2aa876',
                '#ffd265',
                '#f19c65',
                '#ce4d45'
            ],
            [
                '#0a7b83',
                '#2aa876',
                '#ffd265',
                '#f19c65',
                '#ce4d45'
            ]// ],
            // [
            //     '#2c3e50',
            //     '#fc4c3c',
            //     '#ecf0f1',
            //     '#3498db',
            //     '#2980b9'
            // ]
        ],
        randomHarmony = harmonies[Math.floor(Math.random() * harmonies.length)],
        randomColor = randomHarmony[Math.floor(Math.random() * randomHarmony.length)],
        lastHarmony = 0;

    // IP/update/<agentid>/<colorid>/<colorcode>/<secret>
    var requestParams = {
            'ip' : 'http://' + window.location.hostname + ':' + window.location.port,
            'agentId' : 1,
            'secret' : 'secret'
        },
        requestUrl = '';

    // init color plugin
    $("#color-picker").ColorPickerSliders({
        flat: true,
        invalidcolorsopacity: 0,
        color: randomColor || '#000',
        swatches: false,
        order: {
            preview: 1,
            rgb: 2,
            hsl: 3
        },
        connectedinput: '.output-field'
    });

    // on form submit
    $('#submit-form').submit(function(e) {

        e.preventDefault();

        // get rgb color values
        var rgbValues = $('.output-field').val().match(/\d+/g);
        var count = 0;
        var countFail = 0;

        // loop rgb values
        for(var i=0; i<rgbValues.length; i++) {

            // build url
            requestUrl = requestParams['ip'] + '/update/' + requestParams['agentId'] + '/' + (i+1) + '/' + rgbValues[i] + '/' + requestParams['secret'];

            // send
            $.when(
                sendRgbValue( requestUrl )
            ).done(function( url ) {
                if( count < rgbValues.length - 1) {
                    count++;
                } else {
                    $('#dialog-success').find('.ui-content').html( 'Changes were saved. (' + url + ')' );
                    $.mobile.changePage("#dialog-success", {
                        transition: "pop",
                        role: "dialog",
                        resizable: false,
                        modal: true
                    });
                }
            }).fail(function( url ) {

                if( countFail === 0 ) {
                    $('#dialog-error').find('.ui-content').html( 'Can\'t save changes. (' + url + ')' );
                    $.mobile.changePage("#dialog-error", {
                        transition: "pop",
                        role: "dialog",
                        resizable: false,
                        modal: true
                    });
                }

                countFail++;

                return false;
            });

            // if( sendRgbValue( requestUrl ) ) {
            //     console.log('test');
            //     if( count < rgbValues.length) {
            //         count++;
            //     } else {
            //         $('#dialog-success').find('.ui-content').html( 'Changes were saved. (' + $('.output-field').val() + ')<br><br>' + requestUrl );
            //         $.mobile.changePage("#dialog-success", {
            //             transition: "pop",
            //             role: "dialog",
            //             resizable: false,
            //             modal: true
            //         });
            //     }
            // } else {
            //     $('#dialog-error').find('.ui-content').html( 'Can\'t save changes. (' + $('.output-field').val() + ')<br><br>' + requestUrl );
            //     $.mobile.changePage("#dialog-error", {
            //         transition: "pop",
            //         role: "dialog",
            //         resizable: false,
            //         modal: true
            //     });
            //     return;
            // }
        }

        return false;

    });

    function send() {



    }


    // set harmony color
    $('#footer .harmony-button').on('click touchstart', function(e) {

        e.preventDefault();

        // get harmony
        var harmony = tinycolor.tetrad( $('.output-field').val() ).reverse();

        // remove last array element to prevent double colors
        harmony.pop();

        // set color value
        $("#color-picker").trigger("colorpickersliders.updateColor", harmony[lastHarmony].toHex());

        // set new index
        if( lastHarmony < harmony.length - 1 ) {
            lastHarmony++;
        } else {
            lastHarmony = 0;
        }

    });

    // ajax call
    function sendRgbValue( url ) {

        return $.Deferred( function ( dfd ) {

            $.ajax({
                type: "GET",
                url: url,
                //cache: false,
                //async: false,
                success: function(responseData) {
                    //console.log('success', url);
                    dfd.resolve( url );
                },
                error: function() {
                    //console.log('error', url);
                    dfd.reject( url );
                }
            });

        }).promise();




    }

});
