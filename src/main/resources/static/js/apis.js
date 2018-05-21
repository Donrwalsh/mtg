$(function () {
    "use strict";

    let $outputTabLinks = $(".output-tabs").children('li').children('a');

    $outputTabLinks.click(function() {
        select_response_tab($outputTabLinks.index(this));
    });

    $('.apiButton').keyup(function(event) {
        if (event.keyCode === 13) {
            $(this).parent().siblings().children('button').click();
        }
    });

    $('#bCard').click(function() {
        let call = "/v0/card";
        if( $("#idCard").val() ) {
            call += "?id=" + $("#idCard").val();
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
        if( $('#idCards').val() ) {
            call += "?name=" + $('#idCards').val();
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
});