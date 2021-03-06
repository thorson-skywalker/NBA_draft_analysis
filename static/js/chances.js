/*jshint esversion: 6 */

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
    console.log(stats);


}

// Create event listener to 
d3.selectAll("input").on("change", collectStats);

// Create function the predicts draftability based on 'stats' dict
function calculateStats() {
    // Create a selector for tbody
    let tbody = d3.select("tbody");

    // Create variable to be used in app.py for prediction
    let ppg = stats.ppg;
    let rpg = stats.rpg;
    let apg = stats.apg;
    let spg = stats.spg;
    let tov = stats.tov;
    let fg_percent = stats["fg%"];
    let threes = stats["3p%"];
    let freeThrows = stats["ft%"];
    // This would need to be different for the heroku app
    fetch('https://nba-draft-predictor.herokuapp.com/prediction?ppg='+ppg+'&rpg='+rpg+'&apg='+apg+'&spg='+spg+'&tov='+tov+'&fg_percent='+fg_percent+'&threes='+threes+'&freeThrows='+freeThrows)
    // fetch('http://127.0.0.1:5000/prediction?ppg='+ppg+'&rpg='+rpg+'&apg='+apg+'&spg='+spg+'&tov='+tov+'&fg_percent='+fg_percent+'&threes='+threes+'&freeThrows='+freeThrows)
        .then((response) => {

            console.log(response);
            if (response.ok == true) {
                let react = tbody.append("tr");
                react.text("draftable");
            }
            else {
                let react = tbody.append("tr");
                react.text("undraftable");
            }
        });
        // .then((myJson) => {
        //     console.log(myJson.prediction);
        // });
}

d3.selectAll("#analysis-btn").on("click", calculateStats);