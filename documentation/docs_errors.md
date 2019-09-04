# Errors List
  
[Back to documentation](docs_overview.html)

## The input shapefile does not have a coordinate system defined  
Any spatial data imported into Marxan Web must have the necessary projection information file present (a *.prj file in a shapefile) so that the feature can be projected internally to an equal area projection. This internal reprojection is necessary so that spatial operations can be done (e.g. intersection) and so that Marxan can run using the data.  

## The input shapefile has invalid geometries
Spatial data needs to be topologically valid to be used within Marxan Web. This essentially means that the polygon must conform to a set of rules regarding its shape, the location of its vertices and how they relate to each other. Different software tools have different rules for validating the topology of polygons and Marxan Web uses the PostGIS rules (as it uses the PostGIS database internally for managing and analysing spatial data). If the spatial data does not conform to these rules then it will not be imported as it is likely to fail any spatial analysis. For more information on how to repair invalid geometries, see [here](https://postgis.net/workshops/postgis-intro/validity.html).  

Tools are available in common GIS packages to help repair geometries so that they can be imported into Marxan Web. For ArcGIS, the geoprocessing tool [Repair Geometry](https://pro.arcgis.com/en/pro-app/tool-reference/data-management/repair-geometry.htm) can be used. The OGC validation method is likely to be more successful in repairing the geometry so that it can be imported into Marxan Web. For QGIS, you can use the [Fix geometries](https://docs.qgis.org/testing/en/docs/user_manual/processing_algs/qgis/vectorgeometry.html#qgisfixgeometries) tool in the Vector geometry toolbox. Finally, if you are using PostGIS, you can fix topological errors using the [ST_MakeValid](https://postgis.net/docs/ST_MakeValid.html) function.  

## The tileset from source \<source\> was not found
A tileset is used to show a layer of data within the map that represents a feature, a planning grid or a protected area and this error is shown when the respective tileset cannot be found. The source gives more information about the tileset that cannot be found and if it is wdpa_source then that tileset cannot be loaded from the JRC hosted tilesets, otherwise it is not available from MapBox. In either case the server could be down, or the tileset may have been deleted.

## The field 'puid' does not exist in the shapefile
In order for a planning grid to be used within Marxan Web, it must contain the mandatory column called 'puid' which should be an integer type. Update the shapefile to include this field and zip the shapefile and try again.  

## The *.\<extension\> file is missing in the zipfile
All shapefiles must have the following files included in the zip file to be able to be imported: shp, shx, dbf. Without any one of these files an error will be thrown on import.  

## Planning grids cannot be created for countries that span the meridian
Currently Marxan Web cannot create planning grids that span the meridian (at 180 degree longitude). These countries are Fiji, Kiribati, New Zealand, Russia, Tuvalu, USA and Wallis and Fortuna. As a workaround, planning grids can be created and uploaded from other GIS tools, e.g. ArcGIS or QGIS. For more information see [Importing existing planning grids](docs_user.html#importing-existing-planning-grids).  

## The zip file contains multiple shapefiles
When uploading and importing zipped shapefiles, the zip files must only contain a single shapefile - i.e. a set of files all with the same name but with different extensions.  
