$(document).ready(function() {
    $.ajax({
        type: "GET",
        url: "/v0/sets",
        success: function (response) {
            $.each(response, function (i, response) {
                let thing = "<tr>" +
                    "<td><img src='../images/sets/lea.svg'></td>" +
                    "<td>" + response.name + "</td>";
                thing += "<td>" + response.code + "</td>";
                thing += "<td>" + response.type + "</td>";
                thing += "<td>" + response.release_date + "</td></tr>";
                $('#sets-table').append(thing);
            });
            $('.container-fluid').show();
        },
        error: function (errmsg, txtstatus) {
            let msg = JSON.parse(errms.responseText).message;
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