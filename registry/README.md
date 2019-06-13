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

`MARXAN_SERVERS`
Array of Marxan Servers that are listed in the login dialog in all instances of Marxan Web. Each object has the following keys:
- name: The name of the Marxan Server that is shown in the Marxan Server drop-down box in the login dialog  
- description: The text description to show for the Marxan Server in the hover on the drop-down box 
- host: The host for the Marxan Server (omitting the protocol) and the port (if a non-default port is specified in the Server Configuration), e.g. andrewcottam.com or andrewcottam.com:8081. For more information see [Administration Guide - Enabling Guest Users](https://andrewcottam.github.io/marxan-web/documentation/docs_admin.html#port)  
- type: Either remote or local

## Contact
Andrew Cottam, Joint Research Centre :email:

