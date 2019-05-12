import React, {Component} from 'react';
import ReactMapboxGl, { Layer, Feature } from "react-mapbox-gl";
import './App.css';

const Map = ReactMapboxGl({
  accessToken: 'pk.eyJ1IjoiYmxpc2h0ZW4iLCJhIjoiMEZrNzFqRSJ9.0QBRA2HxTb8YHErUFRMPZg'
});

class App extends Component {
  render() {
    return (
      <div className="App">
      <Map
      // eslint-disable-next-line
        style="mapbox://styles/mapbox/streets-v9"
        containerStyle={{
          height: "100vh",
          width: "100vw"
        }}>
          <Layer
            type="symbol"
            id="marker"
            layout={{ "icon-image": "marker-15" }}>
            <Feature coordinates={[-0.481747846041145, 51.3233379650232]}/>
          </Layer>
      </Map>      
    </div>
    );
  }
}

export default App;
