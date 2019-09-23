# Errors List
  
[Back to documentation](docs_overview.html)

## The input shapefile does not have a coordinate system defined  
Any spatial data imported into Marxan Web must have the necessary projection information file present (a *.prj file in a shapefile) so that the feature can be projected internally to an equal area projection. This internal reprojection is necessary so that spatial operations can be done (e.g. intersection) and so that Marxan can run using the data.  

## The input shapefile has invalid geometries
Spatial data needs to be topologically valid to be used within Marxan Web. This essentially means that the polygon must conform to a set of rules regarding its shape, the location of its vertices and how they relate to each other. Different software tools have different rules for validating the topology of polygons and Marxan Web uses the PostGIS rules (as it uses the PostGIS database internally for managing and analysing spatial data). If the spatial data does not conform to these rules then it will not be imported as it is likely to fail any spatial analysis. For more information on how to repair invalid geometries, see [here](https://postgis.net/workshops/postgis-intro/validity.html).  

Tools are available in common GIS packages to help repair geometries so that they can be imported into Marxan Web. For ArcGIS, the geoprocessing tool [Repair Geometry](https://pro.arcgis.com/en/pro-app/tool-reference/data-management/repair-geometry.htm) can be used. The OGC validation method is likely to be more successful in repairing the geometry so that it can be imported into Marxan Web. For QGIS, you can use the [Fix geometries](https://docs.qgis.org/testing/en/docs/user_manual/processing_algs/qgis/vectorgeometry.html#qgisfixgeometries) tool in the Vector geometry toolbox. Finally, if you are using PostGIS, you can fix topological errors using the [ST_MakeValid](https://postgis.net/docs/ST_MakeValid.html) function.  

## The tileset from source \<source\> was not found
A tileset is used to show a layer of data within the map that represents a feature, a planning grid or a protected area and this error is shown when the respective tileset cannot be found. The error message gives more information about the source for the tileset that cannot be found. If it is 'wdpa_source' then that protected area tileset cannot be loaded from the JRC hosted tilesets for that location. By default a Marxan Server only comes with protected area information for Africa, the Caribbean and the Pacific (ACP) - although it can be updated at any time to the global dataset (see [here](docs_user.html#server-details)). The project location maybe outside this region in this case and that is why there is an error. If it is within the ACP region, then there is a problem in connecting to the server (it may be down).  

If the source is something other than 'wdpa_source' then the tilesets are not available from MapBox. In this case there may be a problem in connecting to the server, the tileset may not have finished uploading or the tileset may have been deleted from Mapbox.  

## The field 'puid' does not exist in the shapefile
In order for a planning grid to be used within Marxan Web, it must contain the mandatory column called 'puid' which should be an integer type. Update the shapefile to include this field and zip the shapefile and try again.  

## The *.\<extension\> file is missing in the zipfile
All shapefiles must have the following files included in the zip file to be able to be imported: shp, shx, dbf. Without any one of these files an error will be thrown on import.  

## Planning grids cannot be created for countries that span the meridian
Currently Marxan Web cannot create planning grids that span the meridian (at 180 degree longitude). These countries are Fiji, Kiribati, New Zealand, Russia, Tuvalu, USA and Wallis and Fortuna. As a workaround, planning grids can be created and uploaded from other GIS tools, e.g. ArcGIS or QGIS. For more information see [Importing existing planning grids](docs_user.html#importing-existing-planning-grids).  

## The zip file contains multiple shapefiles
When uploading and importing zipped shapefiles, the zip files must only contain a single shapefile - i.e. a set of files all with the same name but with different extensions.  

## Not all planning units have been added
When protected areas are intersected with the planning units in a project the results of that intersection are shown on the map as locked-in to the network. These planning units are outlined in blue. However, if the project already has some planning units that have been manually edited individually, these will be left as they are.  

## The project is already running
Another user has started the project and it is currently running. If you are an admin user you can use the Run Log to see the progress of all projects that are being run - see [The Run Log](docs_user.html#the-run-log) and stop them if necessary. Once the project has finished running you can run it.  
