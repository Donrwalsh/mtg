
$(document).ready(function () {

    $('#bCard').click(function() {
        var call = "/v0/card";
        if( $('#pCard').val() ) {
            call += "?id=" + $('#pCard').val();
        }
        $.ajax({
            type: "GET",
            url: call,
            success: function (response) {
                var resJSON = "";
                console.log(response)
                $.each(response, function (i, response) {
                    // resJSON += "id: " + response.id + "<br>" +
                    // "name: " + response.name + "<br>";
                    // if ( response.names.length > 0) {
                    //     resJSON += "names: " + response.names + "<br>";
                    // }
                    resJSON += JSON.stringify(response) + "<br>";
                });
                if( resJSON == "") {
                    resJSON = "{Empty Response}";
                }
                $('#rCard').empty();
                $('#rCard').append(resJSON);
            },
            error: function (errmsg, txtstatus) {
                var msg = JSON.parse(errmsg.responseText).message;
                console.log(msg);
            }
        });
    });

    $('#bCards').click(function() {
        var call = "/v0/cards";
        if( $('#pCards').val() ) {
            call += "?name=" + $('#pCards').val();
        }
        $.ajax({
            type: "GET",
            url: call,
            success: function (response) {
                var resJSON = "";
                console.log(response)
                $.each(response, function (i, response) {
                    resJSON += JSON.stringify(response) + "<br>";
                });
                if( resJSON == "") {
                    resJSON = "{Empty Response}";
                }
                $('#rCards').empty();
                $('#rCards').append(resJSON);
            },
            error: function (errmsg, txtstatus) {
                var msg = JSON.parse(errmsg.responseText).message;
                console.log(msg);
            }
        });
    });

    console.log("Look at me, I'm Javascript!")
});