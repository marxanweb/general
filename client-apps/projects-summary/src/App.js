import React, { Component } from 'react';
import ReactMapboxGl, { Layer, Feature } from "react-mapbox-gl";
import './App.css';
import jsonp from 'jsonp-promise';
import parse from 'wellknown';

// test server here http://marxan-web-blishten.c9users.io/marxan-web/public/index.html

const Map = ReactMapboxGl({
  accessToken: 'pk.eyJ1IjoiYmxpc2h0ZW4iLCJhIjoiMEZrNzFqRSJ9.0QBRA2HxTb8YHErUFRMPZg'
});

class App extends Component {
  constructor(props){
    super(props);
    this.state = {features:[]};
  }
  loadProjects() {
    jsonp("https://marxan-server-blishten.c9users.io/marxan-server/getProjectsWithGrids?&callback=__jp2").promise.then((response) => {
      console.log(parse(response.data[0].envelope).coordinates);
      this.setState({features: parse(response.data[0].envelope).coordinates});
    });
  }
  render() {
    return (
      <div className="App">
      <Map
      // eslint-disable-next-line
        style="mapbox://styles/mapbox/streets-v10"
        containerStyle={{
          height: "800px",
          width: "1000px"
        }}
        onStyleLoad={this.loadProjects.bind(this)}
        zoom={[0.7]}
        >
    <Layer
      type="fill"
      id="marker"
      paint={{
        "fill-color": "rgba(0,0,0,0)",
        "fill-outline-color": "rgba(255,0,0,0.9)"
      }}
      >
      <Feature coordinates={this.state.features}/>
    </Layer>
      </Map>      
    </div>
    );
  }
}

export default App;
