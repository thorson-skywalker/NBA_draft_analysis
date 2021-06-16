// Create dictionary to hold inputs
var stats = {};

// Create function to collect inputs and add them into a dictionary
function collectStats() {

    // select input and save a variable
    let stat = d3.select(this);
    // save input value as a variable
    let statValue = stat.property("value");
    console.log(statValue);

    // Save id of input as variable
    let statID = stat.attr("id");
    console.log(statID);

    // For each input add statID and statValue to stats dict
    if (statValue) {
        stats[statID] = statValue;
    }
    else {
        delete stats[statID];
    }
    // write stats to readable csv to be used in the prediction model
    let ObjectToCsv = require('objects-to-csv')
    new ObjectToCsv(stats).toDisk('./data/player_data.csv')
}

// Create event listener to 
d3.selectAll("input").on("change", collectStats);

// Create function the predicts draftability based on 'stats' dict
function calculateStats() {

    // Run prediction model on stats data to return a boolean

    // Use the resulting boolean term to display "draftable" or "Not Draftable"

}