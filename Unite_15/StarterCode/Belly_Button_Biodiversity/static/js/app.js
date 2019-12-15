function buildMetadata(sample) {
  
  
    // @TODO: Complete the following function that builds the metadata panel

    // Use d3 to select the panel with id of `#sample-metadata`

    d3.json("/metadata/" + sample).then((metaData) => {
      console.log(metaData)  
      
      

      d3.select("#sample-metadata")
          
        // Use `.html("") to clear any existing metadata
        .html("")
      // Use `Object.entries` to add each key and value pair to the panel
      
      for (let [key, value] of Object.entries(metaData)) {
        console.log(`${key}: ${value}`);

        d3.select("#sample-metadata")
          .append("span")
          .text(`${key}: ${value}`)
          .append("br");
      }


      // Hint: Inside the loop, you will need to use d3 to append new
      // tags for each key-value in the metadata.
      d3.json("/samples/" + sample).then((sampleData) => {

        console.log(sampleData);
  
        var data = [{
          values: sampleData.sample_values.slice(0, 10),
          labels: sampleData.otu_ids.slice(0, 10),
          type: 'pie'
        }];
        
        var layout = {
          title: "Belly Button Biodiversity Top Ten Bacteria",
          height: 400,
          width: 500,
          hovertext:sampleData.otu_labels
        };

        Plotly.newPlot("pie", data, layout);
        // HINT: You will need to use slice() to grab the top 10 sample_values,
        // otu_ids, and labels (10 each).
      });



      // BONUS: Build the Gauge Chart
      // buildGauge(data.WFREQ);
    });
  }


  function buildCharts(sample) {
    d3.select("#bubble")
          
    // Use `.html("") to clear any existing metadata
    .html("")

    d3.json("/samples/" + sample).then((sampleData) =>{
      var trace = {
        type: "Scatter",
        name: "Belly Button Biodiversity",
        x: sampleData.otu_ids,
        y: sampleData.sample_values,
        mode:'markers',
        marker:{
          color:sampleData.otu_ids,
          size:sampleData.sample_values
         },          
        hovertext:sampleData.otu_labels
        
      };
      
      var data = [trace];
  
      var layout = {
        title: 'Belly Button Biodiversity',
        xaxis: {
          title: 'Bacteria ID',
          showgrid: false,
          zeroline: false
        },
        yaxis: {
          title: 'Values',
          showline: false
        }
      };
  
      Plotly.newPlot("bubble", data, layout);
  
    
    
      }).catch(function(error) {
        console.log(error);
      });
  }
      
  function init() {
    // Grab a reference to the dropdown select element
    var selector = d3.select("#selDataset");
  
    // Use the list of sample names to populate the select options
    d3.json("/names").then((sampleNames) => {
      sampleNames.forEach((sample) => {
        selector
          .append("option")
          .text(sample)
          .property("value", sample);
      });
  
      // Use the first sample from the list to build the initial plots
      const firstSample = sampleNames[0];
      buildCharts(firstSample);
      buildMetadata(firstSample);
    });
  }
  
  function optionChanged(newSample) {
    // Fetch new data each time a new sample is selected
    buildCharts(newSample);
    buildMetadata(newSample);
  }
  
  // Initialize the dashboard
  init();