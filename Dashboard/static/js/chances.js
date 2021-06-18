// Create dictionary to hold inputs
var stats = {};

// Create function to collect inputs and add them into a dictionary
function collectStats() {

    // select input and save a variable
    let stat = d3.select(this);
    // save input value as a variable
    let statValue = stat.property("value");
    // console.log(statValue);

    // Save id of input as variable
    let statID = stat.attr("id");
    // console.log(statID);

    // For each input add statID and statValue to stats dict
    if (statValue) {
        stats[statID] = statValue;
    }
    else {
        delete stats[statID];
    }
}

// Create event listener to 
d3.selectAll("input").on("change", collectStats);

// Create function the predicts draftability based on 'stats' dict
function calculateStats(data) {

    // Create variable to be used in app.py for prediction
    let ppg = data["ppg"];
    let rpg = data["rpg"];
    let apg = data["apg"];
    let spg = data["spg"];
    let tov = data["tov"];
    let fg_percent = data["fg_percent"];
    let threes = data["threes"];
    let freeThrows = data["freeThrows"];
    fetch('http://127.0.0.1/prediction?ppg='+ppg+'&rpg='+rpg+'&apg='+apg+'&spg='+spg+'&tov='+tov+'&fg_percent='+fg_percent+'&threes='+threes+'&freeThrows='+freeThrows)
        .then((response) => {
            return response.json();
        })
        .then((myJson) => {
            console.log(myJson.result)
        })
}

d3.select("#btn").on("click", calculateStats(stats));