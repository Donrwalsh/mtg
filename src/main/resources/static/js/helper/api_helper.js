let $outputTabLinks = $(".output-tabs").children('li').children('a');
let $outputNavTabs = $(".output-tabs").children('li');
let $outputResponseDivs = $(".response-output");

let $bCard = $("#bCard");
let $bCardParam1 = $("#pCard");

function display_card_val(field_name, type, value) {
    switch(type) {
        case 'int':
            return "<strong>" + field_name + "</strong>: " + value + ",<br>";
        case 'string':
            return "<strong>" + field_name + "</strong>: \"" + value + "\",<br>"
        case 'multi-string':
            let msResult = "<strong>" + field_name + "</strong>: [";
            $.each(value, function (i, item) {
                if (i === (value).length-1) {
                    msResult += "\"" + item + "\"";
                } else {
                    msResult += "\"" + item + "\",";
                }
            });
            return msResult + "],<br>";
        case 'multi-int':
            let miResult = "<strong>" + field_name + "</strong>: [";
            $.each(value, function (i, item) {
                if (i === (value).length-1) {
                    miResult += item;
                } else {
                    miResult += "" + item + ",";
                }
            });
            return miResult + "],<br>";
    }
}

function display_card(card) {
    let result = "";
    result += "<p>";
    result += display_card_val('id', 'int', card.id);
    result += display_card_val('name', 'string', card.name);
    result += display_card_val('names', 'multi-string', card.names);
    result += display_card_val('colors', 'multi-string', card.colors);
    result += display_card_val('colorIdentity', 'multi-string', card.colorIdentity);
    result += display_card_val('manaCost', 'string', card.manaCost);
    result += display_card_val('cmc', 'int', card.cmc);
    result += display_card_val('set', 'int', card.set);
    result += display_card_val('rarity', 'string', card.rarity);
    result += display_card_val('text', 'string', card.text);
    result += display_card_val('flavor', 'string', card.flavor);
    result += display_card_val('supertypes', 'multi-string', card.supertypes);
    result += display_card_val('types', 'multi-string', card.types);
    result += display_card_val('subtypes', 'multi-string', card.subtypes);
    result += display_card_val('variations', 'multi-int', card.variations);
    result += display_card_val('artist', 'string', card.artist);
    result += display_card_val('number', 'string', card.number);
    result += display_card_val('power', 'string', card.power);
    result += display_card_val('toughness', 'string', card.toughness);
    result += display_card_val('loyalty', 'int', card.loyalty);
    result += display_card_val('multiverseid', 'int', card.multiverseid);
    result += display_card_val('watermark', 'string', card.watermark);
    result += display_card_val('border', 'string', card.border);
    result += display_card_val('layout', 'string', card.layout);
    result += display_card_val('timeshifted', 'string', card.timeshifted);
    result += display_card_val('reserved', 'string', card.reserved);
    result += display_card_val('starter', 'string', card.starter);
    result += "</p>";
    return result;
}

function select_response_tab(i) {
    $outputTabLinks.removeClass('active');
    $outputTabLinks.eq(i).addClass('active');
    $outputResponseDivs.css("display", "none");
    $outputResponseDivs.eq(i).css("display", "block");
}

function handle_successful_response(response) {
    $('.output-navigation').css("border-bottom-width","1px");
    $outputNavTabs.css("display","none");
    $outputNavTabs.each(function( i ) {
        if (i < response.length) {
            this.style.display = "block";
        }
    });
    $.each(response, function (i, response) {
        let resJSON = "";
        if (response === "") {
            resJSON = "{Empty Response}";
        } else {
            resJSON = display_card(response);
        }
        $('.response-output:eq(' + i + ')').empty().append(resJSON);
    });
    select_response_tab(0);
}