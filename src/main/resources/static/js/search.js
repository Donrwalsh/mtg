$(function () {
    "use strict";

    $('#header-search').bind("input change", function () {
        $.ajax({
            type: "GET",
            url: "/v0/cards?name=" + $('#header-search').val(),
            success: function (response) {
                console.log(response);
            },
            error: function (errmsg, txtstatus) {
                let msg = JSON.parse(errmsg.responseText).message;
                console.log(msg);
            }
        });
    });
});