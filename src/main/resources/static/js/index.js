
$(document).ready(function () {

    $('#bQuestion').click(function() {
        var call = "/v1/question";
        if( $('#pQuestion').val() ) {
            call += "?id=" + $('#pQuestion').val();
        }
        $.ajax({
            type: "GET",
            url: call,
            success: function (response) {
                var resJSON = "";
                $.each(response, function (i, response) {
                    resJSON += JSON.stringify(response) + "<br>";
                });
                if( resJSON == "") {
                    resJSON = "{Empty Response}";
                }
                $('#rQuestion').empty();
                $('#rQuestion').append(resJSON);
            },
            error: function (errmsg, txtstatus) {
                var msg = JSON.parse(errmsg.responseText).message;
                console.log(msg);
            }
        });
    });

    $('#bUser').click(function() {
        var call = "/v1/user";
        if( $('#pUser').val() ) {
            call += "?id=" + $('#pUser').val();
        }
        $.ajax({
            type: "GET",
            url: call,
            success: function (response) {
                var resJSON = "";
                $.each(response, function (i, response) {
                    resJSON += JSON.stringify(response) + "<br>";
                });
                if( resJSON == "") {
                    resJSON = "{Empty response}";
                }
                $('#rUser').empty();
                $('#rUser').append(resJSON)
            },
            error: function (errmsg, txtstatus) {
                var msg = JSON.parse(errmsg.responseText).message;
                console.log(msg);
            }
        });
    });

    $('#bUsers').click(function() {
        var call = "/v1/users";
        $.ajax({
            type: "GET",
            url: call,
            success: function (response) {
                var resText = "";
                var resJSON = "";
                //console.log(response)
                $.each(response, function (i, response) {
                    resText += "<p style='margin:0'>" + response.id + ", ";
                    resText += response.firstname + ", ";
                    resText += response.lastname + ", ";
                    resText += response.email; + "</p>";
                    resJSON += JSON.stringify(response) + "<br>";
                });
                //$('#rUsers').append(resText)
                $('#rUsers').empty();
                $('#rUsers').append(resJSON);
            },
            error: function (errmsg, txtstatus) {
                var msg = JSON.parse(errmsg.responseText).message;
                console.log(msg);
            }
        });
    });

    console.log("Look at me, I'm Javascript!")
});