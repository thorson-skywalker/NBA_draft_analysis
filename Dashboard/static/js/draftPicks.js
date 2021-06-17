// import the data from the csv
const tableData = d3.csv("../static/data/2021_predictions.csv");

console.log(tableData);

// Select tbody in the HTML file
var tbody = d3.select("tbody");

// Function to create header and table for the data in draft picks
function buildTable(tableData) {
    
    // Loop through the data to append row and cell data
    tableData.forEach((dataRow) => {
        console.log(dataRow);
        //  Append a row to the table body
        let row = tbody.append("tr");

        // Loop through each field in the dataRow and add each value as a table cell (td)
        Object.values(dataRow).forEach((val) => {
            let cell = row.append("td");
            cell.text(val);
        });
    });
}

buildTable(tableData);