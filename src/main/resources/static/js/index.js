function display_card_val(field_name, type, value) {
    switch(type) {
        case 'int':
            return "<strong>" + field_name + "</strong>: " + value + ",<br>";
        case 'string':
            return "<strong>" + field_name + "</strong>: \"" + value + "\",<br>"
        case 'multi-string':
            var result = "<strong>" + field_name + "</strong>: [";
            $.each(value, function (i, item) {
                if (i === (value).length-1) {
                    result += "\"" + item + "\"";
                } else {
                    result += "\"" + item + "\",";
                }
            });
            return result + "],<br>";
        case 'multi-int':
            var result = "<strong>" + field_name + "</strong>: [";
            $.each(value, function (i, item) {
                if (i === (value).length-1) {
                    result += item;
                } else {
                    result += "" + item + ",";
                }
            });
            return result + "],<br>";
    }
}

$(document).ready(function () {

    $('.nav-link').click(function() {
        $('.nav-link').removeClass('active');
        $(this).addClass('active');
    });

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
                    resJSON += "<p>";
                    resJSON += display_card_val('id', 'int', response.id);
                    resJSON += display_card_val('name', 'string', response.name);
                    resJSON += display_card_val('names', 'multi-string', response.names);
                    resJSON += display_card_val('colors', 'multi-string', response.colors);
                    resJSON += display_card_val('colorIdentity', 'multi-string', response.colorIdentity);
                    resJSON += display_card_val('manaCost', 'string', response.manaCost);
                    resJSON += display_card_val('cmc', 'int', response.cmc);
                    resJSON += display_card_val('set', 'int', response.set);
                    resJSON += display_card_val('rarity', 'string', response.rarity);
                    resJSON += display_card_val('text', 'string', response.text);
                    resJSON += display_card_val('flavor', 'string', response.flavor);
                    resJSON += display_card_val('supertypes', 'multi-string', response.supertypes);
                    resJSON += display_card_val('types', 'multi-string', response.types);
                    resJSON += display_card_val('subtypes', 'multi-string', response.subtypes);
                    resJSON += display_card_val('variations', 'multi-int', response.variations);
                    resJSON += display_card_val('artist', 'string', response.artist);
                    resJSON += display_card_val('number', 'string', response.number);
                    resJSON += display_card_val('power', 'string', response.power);
                    resJSON += display_card_val('toughness', 'string', response.toughness);
                    resJSON += display_card_val('loyalty', 'int', response.loyalty);
                    resJSON += display_card_val('multiverseid', 'int', response.multiverseid);
                    resJSON += display_card_val('watermark', 'string', response.watermark);
                    resJSON += display_card_val('border', 'string', response.border);
                    resJSON += display_card_val('layout', 'string', response.layout);
                    resJSON += display_card_val('timeshifted', 'string', response.timeshifted);
                    resJSON += display_card_val('reserved', 'string', response.reserved);
                    resJSON += display_card_val('starter', 'string', response.starter);
                    resJSON += "</p>";
                    // resJSON += JSON.stringify(response) + "<br>";
                });
                if( resJSON == "") {
                    resJSON = "{Empty Response}";
                }
                $('#output').empty();
                $('#output').append(resJSON);
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
                $('#output').empty();
                $('#output').append(resJSON);
            },
            error: function (errmsg, txtstatus) {
                var msg = JSON.parse(errmsg.responseText).message;
                console.log(msg);
            }
        });
    });

    console.log("Look at me, I'm Javascript!")
});