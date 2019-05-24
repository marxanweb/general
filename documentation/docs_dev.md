# Developer Documentation
* Will be replaced with the ToC, excluding the "Contents" header
{:toc}  

[Back to documentation](docs_overview.html)

The Developer Documentation is aimed at software developers who want to: extend Marxan Web with new features; create new websites from the data or want to use desktop GIS tools to link directly to the Marxan Web database. Each of these topics is described below.  

## Overview of extending Marxan Web
Marxan Web is a piece of client-server software with the client running in a Web Browser and the server running cross-platform on any operating system. The high level architecture is a loosely-coupled application that uses REST Services and WebSockets to communicate between the marxan-client and marxan-server. This loosely coupled system means that from the developers point of view the system is open and can be extended quickly and easily using the marxan-server API.  

Components on marxan-server include the PostGIS spatial database, the Tornado Web Server, the DOS-based Marxan software and the marxan-server custom software written in Python. The components of marxan-client are a web application written in React, the MapboxGL Javascript Mapping Library and a set of Vector Tile services to provide the mapping layers. These are all open-source technologies and can be customised and extended without restrictions. 

To create new features in Marxan Web it is necessary to create new user interface components in the marxan-client and then (if necessary) to provide the necessary services in marxan-server to either get/set any user data or undertake some kind of analysis or processing. Once these new features have been developed and tested they can be pulled back into the repo as part of the core Marxan Web and updated wherever they have been installed.  For more information see the [Administrator Documentation - Updates](docs_admin.html#updates).  

It is not necessary to create new user interface components in marxan-client if you want to develop completely new applications for the web. These new tools can use the same underlying marxan-server API to interact with the storage and processing, but within an entirely new application. In these cases it may be necessary to authenticate with the marxan-server using secure cookie authentication - for more information see [Authentication](#authentication).  

### Technologies
#### marxan-server
marxan-server uses the Tornado Web Server for communication between the marxan-client and marxan-server. Tornado is a lightweight server that supports SSL, WebSockets and server extensions and allows you to define endpoints that map a REST url endpoint to an internal Python class. For more information see [Creating REST services](#creating-rest-services). The implementation of these REST endpoints is in the webAPI_tornado.py file in the marxan-server folder and when you run this file you are starting marxan-server. For more information see the [Adminstrator Documentation - Starting/stopping marxan-server](docs_admin.html#startingstopping-marxan-server).  

The PostGIS database is used to manage all of the spatial data that is created in Marxan Web and is the main processing engine for any intersections or other analyses. This fully-featured database means that any future spatial requirements can be met easily with the existing bundled database. Within marxan-server the connections to the database are managed using the psycopg2 Python library and the connection settings are set in the server.dat file. For more information see [Administrator Documentation - Database configuration](docs_admin.html#database-configuration) and [Interacting with PostGIS](#interacting-with-postgis).  

The DOS-based Marxan software is still the heart of Marxan Web and it is this software that does the systematic conservation planning. All of the various *.dat files that are used in the DOS-version are managed in the marxan-client and marxan-server - for more information see [Migration Guide - Where are all the .dat files?](docs_migration.html#where-are-all-the-dat-files).  

#### marxan-client

### Architecture
#### Understanding the architecture
The following figure shows the high-level architecture of marxan-server.

#### Typical workflow

## marxan-server development
### Creating REST services
### Interacting with PostGIS
### Interacting with Mapbox

## marxan-client development
### Building 
### Deploying

## Building new user interfaces on Marxan data
### marxan-server API
### Authentication

## Linking desktop GIS to the Marxan database
