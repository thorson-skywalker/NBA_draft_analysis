// import the data from the csv
// const tableData = d3.csv("../static/js/07-20_MBB_StatsAndDraft.csv", function(data){
//     console.log(data);
// });


// Select thead in the HTML file
var tbody = d3.select("tbody");

// Function to create header and table for the data in draft picks
function buildTable(data) {
    // Clear out existing data
    tbody.html("");

    data.forEach ((dataRow) => {
        //  Append a row to the table body
        let row = tbody.append("tr");

        // Loop through each field in the dataRow and add each value as a table cell (td)
        Object.values(dataRow).forEach((val) => {
            let cell = row.append("td");
            cell.text(val);
            }
    );
    });
}

// buildTable(tableData);