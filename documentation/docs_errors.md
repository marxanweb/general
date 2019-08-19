# Errors List
  
[Back to documentation](docs_overview.html)

## The input shapefile does not have a coordinate system defined  
Any spatial data imported into Marxan Web must have the necessary projection information file present (a *.prj file in a shapefile) so that the feature can be projected internally to an equal area projection. This internal reprojection is necessary so that spatial operations can be done (e.g. intersection) and so that Marxan can run using the data.  

## The input shapefile has invalid geometries
spatial data needs to be topologically valid to be used within Marxan Web. This essentially means that the polygon must conform to a set of rules regarding its shape, the location of its vertices and how they relate to each other. Different software tools have different rules for validating the topology of polygons and Marxan Web uses the PostGIS rules (as it uses the PostGIS database internally for managing and analysing spatial data). If the spatial data does not conform to these rules then it will not be imported as it is likely to fail any overlay analysis. For more information on how to repair invalid geometries, see [here](https://postgis.net/workshops/postgis-intro/validity.html).

## The tileset from source \<source\> was not found
A tileset is used to show a layer of data within the map that represents a feature, a planning grid or a protected area and this error is shown when the respective tileset cannot be found. The source gives more information about the tileset that cannot be found and if it is wdpa_source then that tileset cannot be loaded from the JRC hosted tilesets, otherwise it is not available from MapBox. In either case the server could be down, or the tileset may have been deleted.

## The field 'puid' does not exist in the shapefile
In order for a planning grid to be used within Marxan Web, it must contain the mandatory column called 'puid' which should be an integer type.  
