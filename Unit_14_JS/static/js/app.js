// from data.js
var tableData = data;
console.log(tableData);
// YOUR CODE HERE!

// Get a reference to the table body
var tbody = d3.select("tbody");

// Console.log the weather data from data.js

// BONUS: Refactor to use Arrow Functions!
tableData.forEach((sheepleReport) => {
  var row = tbody.append("tr");
  Object.values(sheepleReport).forEach((value) => {
    var cell = row.append("td");
    cell.text(value);
  });
});

// 

// Select the button
var button = d3.select("#filter-btn");

button.on("click", function() {
     // Select the input element and get the raw HTML node
    var inputElement = d3.select("#datetime");
    // Get the value property of the input element
    var inputValue = inputElement.property("value");

    // input to lower case
    var inputCity = d3.select("#city").property("value").toLowerCase();
    var inputState = d3.select("#state").property("value").toLowerCase();
    var inputCountry = d3.select("#country").property("value").toLowerCase();
    var inputShape = d3.select("#shape").property("value").toLowerCase();

//   if(inputCity !== ""){
//     alert(inputCity);
//   }
//   if(inputValue !== ""){
//     alert(inputValue);
//   }
//   if(inputState !== ""){
//     alert(inputState);
//   }
//   if(inputCountry !== ""){
//     alert(inputCountry);
//   }if(inputShape !== ""){
//     alert(inputShape);
//   }

    //remove all table data values
    d3.select("tbody").selectAll("tr").remove();

    let filteredData = tableData;
    if(inputValue !== ""){
        filteredData=filteredData.filter(ufoRow => ufoRow.datetime === inputValue);
    }
    if(inputCity !== ""){
        filteredData =  filteredData.filter(ufoRow => ufoRow.city === inputCity);
    }
    if(inputState !== ""){
        filteredData=filteredData.filter(ufoRow => ufoRow.state === inputState);
    }
    if(inputCountry !== ""){
        filteredData =  filteredData.filter(ufoRow => ufoRow.country === inputCountry);
    } 
    if(inputShape !== ""){
        filteredData=filteredData.filter(ufoRow => ufoRow.shape === inputShape);
    }
    

    filteredData.forEach((sheepleReport) => {
        var row = tbody.append("tr");
        Object.values(sheepleReport).forEach((value) => {
          var cell = row.append("td");
          cell.text(value);
        });
    });
});