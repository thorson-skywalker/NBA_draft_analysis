/*jshint esversion: 6 */

// Function to create header and table for the data in draft picks
function buildTable() {
    // Select tbody in the HTML file
    var tbody = d3.select("tbody");

    // First, clear out any existing data
    tbody.html("");

    // Load in the data
    d3.json("../static/data/cleaned_predictions.json", function(data) {
        console.log(data);
    
        // Next, loop through each object in the data
        // and append a row and cells for each value in the row
        data.forEach((dataRow) => {
            // Append a row to the table body
            let row = tbody.append("tr");

            // Loop through each field in the dataRow and add
            // each value as a table cell (td)
            Object.values(dataRow).forEach((val) => {
            let cell = row.append("td");
            cell.text(val);
            });
        });
    });
}

buildTable();