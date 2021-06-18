// import the data
const tableData = draftPredictions;
console.log(tableData);

// Select tbody in the HTML file
var tbody = d3.select("tbody");

// Function to create header and table for the data in draft picks
function buildTable(data) {
    // First, clear out any existing data
    tbody.html("");

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
}

buildTable(tableData);