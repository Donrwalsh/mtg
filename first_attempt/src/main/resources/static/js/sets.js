$(document).ready(function() {
    $.ajax({
        type: "GET",
        url: "/v0/sets",
        success: function (response) {
            $.each(response, function (i, response) {
                let code = response.code === "con" ? "_con" : response.code;
                let thing = "<tr>" +
                    "<td><img class='set-icon' src='../images/sets/" + code + ".svg'></td>" +
                    "<td>" + response.name + "</td>";
                thing += "<td class='caps'>" + response.code + "</td>";
                thing += "<td>" + response.type + "</td>";
                thing += "<td>" + response.release_date + "</td></tr>";
                $('#sets-table').append(thing);
            });
            $('.container-fluid').show();
        },
        error: function (errmsg, txtstatus) {
            let msg = JSON.parse(errmsg.responseText).message;
            console.log(msg)
        }
    });

    }
);


// $.each(response, function (i, response) {
//     let resJSON = "";
//     if (response === "") {
//         resJSON = "{Empty Response}";
//     } else {
//         switch(objectType) {
//             case 'card':
//                 resJSON = display_card(response);
//                 break;
//             case 'set':
//                 resJSON = display_set(response);
//                 break;
//         }
//     }
//     $('.response-output:eq(' + i + ')').empty().append(resJSON);