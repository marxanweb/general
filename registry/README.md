## Description
The files in this folder manage a number of globally useful functions and variables as outlined below:

## Files list
### marxan.js file
#### Description  
Holds a number of global variables for the Marxan Web application which are loaded on application startup. If the load fails then the application reverts to a local copy (which could be out of date). The variables in this file relate to externally provided services which are available through static urls which could change over time. If these urls were changed then all of the application instances would break and users would have to reinstall from an updated built project. Managing them this way through a CDN allows easy maintenance of these external services.
#### Variables
`MAPBOX_BASEMAPS`  
Array of Mapbox basemap styles that are available to Marxan users. This list is extensible and any new items will be immediately available to Marxan clients. Each object has the following keys:  
 - name: The name to show in the drop-down box in Marxan
 - description: The text description to show as a hover in the drop-down box in Marxan
 - id: The Mapbox identifier of the style including the username, e.g. mapbox/outdoors-v9 or blishten/cjg6jk8vg3tir2spd2eatu5fd
 - provider: The organisation or person who created the style

## Contact
Andrew Cottam, Joint Research Centre :email:

