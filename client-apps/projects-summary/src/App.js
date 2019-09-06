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
  constructor(props) {
    super(props);
    this.state = { features: [] };
  }
  _handleMouseEnter(cursor, item) {
    console.log(cursor && cursor.features && cursor.features[0] && cursor.features[0].properties && cursor.features[0].properties.alias);
  }
  _handleMouseLeave(cursor) {

  }
  loadProjects() {
    jsonp("https://andrewcottam.com:8080/marxan-server/getProjectsWithGrids?&callback=__jp2").promise.then((response) => {
      this.setState({ features: response.data });
    });
  }
  render() {
    var c = [this.state.features.map((item) => { 
      return <Feature coordinates={parse(item.envelope).coordinates} properties={item}/>;
    })];
    return (
      <div className="App">
      <Map
      // eslint-disable-next-line
        style="mapbox://styles/mapbox/light-v9"
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
            "fill-color": "rgba(88,194,255,0.3)",
            "fill-outline-color": "rgba(202,88,255,0.6)"
          }}
          onMouseEnter={(cursor, item) => this._handleMouseEnter(cursor, item)}
          onMouseLeave={cursor => this._handleMouseLeave(cursor)}
          children={c}
          />
      </Map>      
    </div>
    );
  }
}

export default App;
