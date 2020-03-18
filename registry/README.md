## Description
The files in this folder manage a number of globally useful functions and variables as outlined below:

## Files list
### marxan.js file
#### Description  
Holds a number of global variables for the Marxan Web application which are loaded on application startup. The variables in this file relate to externally provided services which are available through static urls which could change over time. If these urls were changed then all of the application instances would break and users would have to reinstall from an updated built project. Managing them this way through a CDN allows easy maintenance of these external services.
#### Variables
`CLIENT_VERSION`  
The latest version number for the marxan-client software.

`SERVER_VERSION`  
The latest version number for the marxan-server software.

`MAPBOX_BASEMAPS`  
Array of Mapbox basemap styles that are available to Marxan users. This list is extensible and any new items will be immediately available to Marxan clients. Each object has the following keys:  
 - name: The unique name that identifies the basemap in Marxan Web
 - alias: The name to show in the drop-down box for Basemap style
 - description: The text description to show as a hover in the drop-down box in Marxan
 - id: The Mapbox identifier of the style including the username, e.g. mapbox/outdoors-v9 or blishten/cjg6jk8vg3tir2spd2eatu5fd
 - provider: The organisation or person who created the style

`MARXAN_SERVERS`  
Array of Marxan Servers that are listed in the login dialog in all instances of Marxan Web. Each object has the following keys:
- name: The name of the Marxan Server that is shown in the Marxan Server drop-down box in the login dialog  
- description: The text description to show for the Marxan Server in the hover on the drop-down box 
- host: The host for the Marxan Server (omitting the protocol)  
- port: The port that the Marxan Server is listening on. By default Marxan Servers listen on port 8080, but if a non-default port is specified in the Server Configuration, then this must also be set here. e.g.8081. For more information see [Administration Guide - Port setting](https://andrewcottam.github.io/marxan-web/documentation/docs_admin.html#port) 
- protocol: Either http or https
- type: Either remote or local
- project: The Google Cloud Platform project that hosts the marxan-server VM.
- zone: The Google Cloud Platform zone for the marxan-server VM.
- instanceName: Specifies the name of the Virtual Machine on Google Cloud Platform (in the marxancloud@gmail.com account). Setting this value provides a mechanism to start/stop and configure the VM from the Marxan Web website directly.  

`WDPA`  
Holds information about the latest version of the World Database of Protected Areas (WDPA) so that Marxan Web can be updated to new version of the WDPA once they become available. The object has the following keys:
- latest_version: The month and year of the latest version that is available for download from the website of the UN Environment World Conservation Monitoring Centre. 
- downloadUrl: The url that links to the download of the new version as a shapefile from the WCMC website.  
- tilesUrl: The url endpoint to the vector tiles for the latest version which must have been produced using the same downloaded shapefile. The vector tiles should be published in a workspace called 'marxan' and must have the layer name of 'wdpa_\<mmm\>_\<yyyy\>_polygons' where mmm is the abbreviated month and yyyy is the full year, e.g. wdpa_aug_2019_polygons.  
- metadataUrl: The url that links to the WCMC metadata page for this update and includes a full description of which countries data have changed since the previous month.  

`NOTIFICATIONS`  
Array of notification objects where are used to show notifications when users log on to Marxan Web.

## Contact
Andrew Cottam, Joint Research Centre :email:

