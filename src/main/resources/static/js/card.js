
var getUrlParameter = function getUrlParameter(sParam) {
    var sPageURL = decodeURIComponent(window.location.search.substring(1)),
        sURLVariables = sPageURL.split('&'),
        sParameterName,
        i;

    for (i=0; i < sURLVariables.length; i++) {
        sParameterName = sURLVariables[i].split('=');

        if (sParameterName[0] === sParam) {
            return sParameterName[1] === undefined ? true : sParameterName[1];
        }
    }
};

var id = getUrlParameter('id');
console.log(id);
if (!$.isNumeric(id)) {
    $(window).attr('location', '/');
}
$.ajax({
    type: "GET",
    url: '/v0/card?id=' + id,
    success: function (response) {
        $.each(response, function (i, response) {
            $('#cardID').append(response.id);
            $('#cardName').append(response.name);
        });
    },
    error: function (errmsg, txtstatus) {
        var msg = JSON.parse(errmsg.responseText).message;
        console.log(msg);
    }
});

console.log("Look at me, I'm Javascript!")