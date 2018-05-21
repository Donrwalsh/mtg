$(function () {
    "use strict";

    $responseNavAs.click(function() {
        select_response_tab($responseNavAs.index(this));
    });

    $bCard.click(function() {
        let call = "/v0/card";
        if( $bCardParam1.val() ) {
            call += "?id=" + $bCardParam1.val();
        }
        $.ajax({
            type: "GET",
            url: call,
            success: function (response) {
                handle_successful_response(response);
            },
            error: function (errmsg, txtstatus) {
                let msg = JSON.parse(errmsg.responseText).message;
                console.log(msg);
            }
        });
    });

    $('#bCards').click(function() {
        let call = "/v0/cards";
        if( $('#pCards').val() ) {
            call += "?name=" + $('#pCards').val();
        }
        $.ajax({
            type: "GET",
            url: call,
            success: function (response) {
                handle_successful_response(response);
            },
            error: function (errmsg, txtstatus) {
                var msg = JSON.parse(errmsg.responseText).message;
                console.log(msg);
            }
        });
    });
});