$(document).ready(function() {
    console.log("Page Loaded");

    $("#submit").click(function() {
        // alert("button clicked!");
        makePredictions();
    });
});


// call Flask API endpoint
function makePredictions() {
    let boardgame_name = $("#boardgame_name").val();
    let min_rating = $("#min_rating").val();
    let max_owners = $("#max_owners").val();



    // check if inputs are valid

    // create the payload
    let payload = {
        "boardgame_name": boardgame_name,
        "min_rating": min_rating,
        "max_owners": max_owners,
    }

    // Perform a POST request to the query URL
    $.ajax({
        type: "POST",
        url: "/makePredictions",
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({ "data": payload }),
        success: function(returnedData) {
            // print it
            console.log(returnedData);
            renderTable(returnedData["prediction"]);

        },
        error: function(XMLHttpRequest, textStatus, errorThrown) {
            alert("Status: " + textStatus);
            alert("Error: " + errorThrown);
        }
    });

}

function renderTable(inp_data) {
    // init html string
    let html = "";

    // destroy datatable
    $('#sql_table').DataTable().clear().destroy();

    // loop through all rows
    inp_data.forEach(function(row) {
        html += "<tr>";

        // loop through each cell (order matters)
        html += `<td>${row.id}</td>`;
        html += `<td>${row.name_clean}</td>`;
        html += `<td>${row.category_clean}</td>`;
        html += `<td>${row.mechanic_clean}</td>`;
        html += `<td>${row.category_count}</td>`;
        html += `<td>${row.mechanic_count}</td>`;
        html += `<td>${row.designer_count}</td>`;
        html += `<td>${row.average_rating.toFixed(2)}</td>`;
        html += `<td>${row.total_owners}</td>`;
        html += `<td>${row.total_weights.toFixed(2)}</td>`;
        html += `<td>${row.age}</td>`;
        html += `<td>${row.minplayers}</td>`;
        html += `<td>${row.maxplayers}</td>`;
        html += `<td>${row.maxplaytime}</td>`;
        html += `<td>${row.distance.toFixed(2)}</td>`;

        // close the row
        html += "</tr>";
    });

    // shove the html in our elements
    console.log(html);
    $("#sql_table tbody").html("");
    $("#sql_table tbody").append(html);

    // remake data table
    $('#sql_table').DataTable({order: [[14, 'asc']]});
}

