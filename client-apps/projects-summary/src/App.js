import React, {Component} from 'react';
import ReactMapboxGl, { Layer, Feature } from "react-mapbox-gl";
import './App.css';
import jsonp from 'jsonp-promise';

const Map = ReactMapboxGl({
  accessToken: 'pk.eyJ1IjoiYmxpc2h0ZW4iLCJhIjoiMEZrNzFqRSJ9.0QBRA2HxTb8YHErUFRMPZg'
});

class App extends Component {
  loadProjects(){
    jsonp("https://marxan-server-blishten.c9users.io:8081/marxan-server/getProjectsWithGrids?&callback=__jp2").promise.then((response) => {
      console.log(response);
    });
  }
  render() {
    return (
      <div className="App">
      <Map
      // eslint-disable-next-line
        style="mapbox://styles/mapbox/streets-v9"
        containerStyle={{
          height: "800px",
          width: "800px"
        }}
        onStyleLoad={this.loadProjects()}>
      </Map>      
    </div>
    );
  }
}

export default App;
