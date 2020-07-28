Client application for managing marxan-servers. The following files are contained in the folder:
- batchHelpers.py  Python classes for simplifying the discovery and authentication to marxan-server hosted instances. These are used in all client apps.
- getServerVersions.py  Client app to retrieve the versions of all of the marxan-server hosted instances.  
- update_config.py  Client app to update the *.dat fileson all of the marxan-server hosted instances (either user, project or server configuration files).  
- update_database.py  Client app to update the PostGIS database on all of the marxan-server hosted instances with a batch SQL file (useful for patches).  
- update.sql  Test file for use with the update_database.py client app.  
