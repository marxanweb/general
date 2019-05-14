# Background
Marxan Web is a software tool for doing Systematic Conservation Planning over the web and for sharing the results amongst the conservation community and other stakeholders. It builds upon the existing DOS-based Marxan software and offers the following new features and benefits:  
bla bla bla  
# Systematic Conservation Planning with Marxan Web
## Achieving conservation targets 
## Making Marxan more accessible  
## Sharing results with the conservation community
# Tutorial 1: Case study from British Columbia
# Tutorial 2: Creating a simple project in 4 steps
# The Marxan User Interface
The section provides a brief overview of the main elements in the Marxan User Interface and introduces some of the terminology in use. For more detailed information visit the individual sections further on.
## Log in window
When Marxan Web is first loaded the login screen is presented as shown in the image below. The login screen allows you to select a Marxan Server and to login to that server. It also allows you to register as a new user.

Marxan Servers are the databases that contain all of the Marxan projects that are distributed around the world in different organisations. Users can connect to these servers to view those projects that have been created in those organisations. In addition, if those organisations have granted access, these projects can be edited and run by those users. Hovering over a server shows a brief description of that server and the domain on which it is hosted. An icon to the left of the name shows the current status of that server according to the following symbols:  
- <no symbol> Read/write - projects can be viewed and edited (by users with those permissions)
- <padlock> Read only - project can be viewed only (by the guest user)
- <broken link> - server currently offline - no connection is possible. This could be due to a number of reasons: the server could be down, the server may be inaccessible due to firewall restrictions or the network connection may have been lost.  

Once a server has been selected, the user must enter their credentials to login to that server. The user will be logged in according to their role: read-only user, user or admin user. Each of these roles have a different set of features that they have access to in the application with admin users having access to all features. All of the screen shots in the following sections show the application as an admin user and hence not all elements may be visible if logged in as a different user.  

Once you are logged in you will see the Marxan User Interface. This comprises three main elements which are part of a single page web application: the map, the project window (on the left) and the results window (on the right). Other windows are shown as and when they are required. This single page will remain the main user interface until logging out and all tasks are completed in this interface.  
## Project window
On the left hand side of the application user interface is the project window which comprises three tabs: the project tab, the features tab and the planning units tab. These tabs taken together represent the inputs to the analysis: which project, which features are part of that project and what planning units will be used. For more information on projects see the [Projects](#projects] section.  

## Results window
On the right hand side of the application user interface is the results window which also comprises three tabs: the legend tab, the solutions tab and the log tab. These tabs taken together represent the outputs of the Marxan analysis and allow the user to change what results are shown and how they are visualised. For more information on project outputs see the [Running projects](#running-projects) section.  
## The Map
The main part of the application user interface is taken up by the interactive map. The map is the main way of visualising the outputs from any Marxan analyses and is a powerful and flexible tool for visualising hundreds of thousands of individual planning units on-the-fly in three dimensions. The map can be zoomed, panned, rotated and tilted to find the best viewing perspective for a particular run. For more information see the [Mapping](#mapping) section.  
# Projects
## Understanding projects
Projects are the main way of organising any Marxan Web analyses and are the logical starting point for any conservation planning. Each project contains a set of conservation features (i.e the things that you are interesting in protecting); a set of planning units which represent the geographic domain over which the analysis will be done and a set of run parameters that are used to fine-tune the analysis to get the best results. A project also has a limited set of metadata including the project name, a description and the date that it was created. Users with read/write permissions can create any number of projects which are limited only by the amount of disk storage on the server machine.  
### Types of project
Marxan Web projects can be created from scratch using the New Project wizard, or they can be imported from previous DOS-based Marxan projects. Both types of projects can be run and visualised in the map, but imported projects have less capabilities than new projects. The preferred method of creating projects is to create them using the New Project wizard where possible. The main difference is that features cannot be added or removed in imported projects and those features can't be visualied on the map.  
## The projects window
![Image of Projects Windows](marxan_projects.png)  
The projects window is the main way you manage projects on a server and depending on your user role you can manage your own projects or everybodys projects. The projects window lists the projects on the server together with their metadata including the user, project name, description and creation date (the actual columns that are shown will depend on the user role). The view of projects can be sorted by any of the columns by clicking on the column header to sort in ascending or descending order. At the bottom of the window is a toolbar that contains the common tasks associated with managing projects - the actual buttons that are shown will depend on the user role. The functioning of these buttons is described in the following sections.  
## Included case studies
In a default installation of Marxan Web on a desktop machine, there are a number of pre-loaded case studies that will be shown in the projects window. These have been created to help you get up and running quickly by providing example start projects and specific tutorials for working through real-world conservation planning scenarios. These will be available from the 'localhost' server. In addition, case studies can be opened from other Marxan servers when the user is logging in. This is the true power of Marxan Web in being able to open projects from other organisations and share your own projects to your stakeholders.  
## Managing projects
This section contains information on the common tasks associated with managing projects.  
### Creating new projects
The preferred way to create new projects in Marxan Web is to create them with the New Project wizard. This wizard takes the user through a simple set of steps to create a fully functioning Marxan Web project. The user creates the project metadata; selects the conservation features that will be included in the project and chooses the planning grid that will form the geographic extend and resolution for the analysis.  
  
To create a new project using the New Project wizard:  
1. Click on the New button in the projects window
2. Enter the project metadata and click Next
3. Choose a planning grid from the drop down list - when you choose an item the map zooms to the extend of the grid and shows the planning units. If the required planning grid is not shown, then it can be created in from the Planning Grids window (see the [Planning Grids](#planning-grids) section) and then the wizard can be restarted. Click Next
4. Choose the conservation features that will be part of your project
5. Select a cost surface (not currently implemented) and click Finish  

The project will now be created and opened and can be run immediately.  
### Importing existing Marxan projects
Existing DOS-based Marxan projects can also be imported to Marxan Web using the Import Project window (currently only supported on Google Chrome). Imported projects share some of the features of projects created with the New Project wizard, but there are a number of important differences that may influence which method you use. In particular, the following capabilities are not supported on imported projects:  
- Project features cannot be added or removed
- Showing the project features on the map is not supported
- Zooming to project features on the map is not supported
- Project features have only basic metadata, e.g. simple names and no descriptions  
  
To import a DOS-based Marxan project:  
1. Click on the Import button in the Projects window
2. Specify the Marxan Project Folder which should point to the folder that contains the input.dat file
3. Zip up the planning grid shapefile that was used in the DOS-based Marxan project - this shapefile should have a field called 'puid' which is the unique value for the planning unit. All of the individual files that make up a shapefile should be included (e.g. shp, shx, dbf etc.)
4. Upload the zipped shapefile
5. Specify the name of the planning grid - this will be the name of the planning grid that is created from the zipped up shapefile
6. Click Next and enter the project metadata
7. Click Finish.  

The project will now be imported and the shapefile will be uploaded to Mapbox (for more information see [Understanding mapping](#understanding-mapping)). Once this process has finished the new Marxan Web project will be shown in the project window with the text 'Imported Project' at the bottom. The project can be run immediately.  
### Duplicating a project
Duplicating a project copies all of the project information to a new project with the same project name but with a '\_copy' suffix. The project can then be opened, edited and run. This provides a mechanism for iterating and improving projects until they are fit-for-purpose.
### Deleting a project
To delete a project, select a project and click on the delete button. Deleting a project will not delete any features or planning grids.
### Controlling access to a project
By default projects are created as public which means that they can be viewed by any other Marxan user. In order to restrict access to the project, it can be flagged as private and it will then only be visible to the project author.
### Editing project metadata
To edit the name or description for a project, simply click on the name or description in the project tab and then edit it. When you are finished press ENTER.
## Managing features within a project
The features that are included in a project are shown in the features tab and for each feature there is a target icon (on the left), a status bar (underneath the feature name) and a context menu (on the right).  

The target icon shows the target that has been set for that particular species and its color reflects the status of the feature. If the project has been run and the target has been achieved for the feature then it is white. If the target has not been achieved it is shown in pink.  

The status bar shows a scale from 0 to 100% which shows the amount of the feature that needs to be protected (in grey) and the amount protected in the current run (in blue). If the amount protected in the current run does not reach the amount to be protected then the target icon is shown in pink.  

The context menu provides a set of functions that apply to the feature and the precise set of functions depends on whether the project was created using the New Project wizard or imported and also on whether the feature was uploaded to Mapbox (see the [Mapping](#mapping) section).  

The following list is the full set of functions that are available in the context menu:  
- Properties - this opens the Feature Properties window - for more information see [Feature Properties window](#feature-properties-window)  
- Remove from project - this is a shortcut to remove that feature from the project
- Add to map - the features geometry will be added to the map as a polygon - currently only one feature at a time can be shown on the map
- Outline planning units where the feature occurs - this shows those planning units which intersect the features polygon. Only one feature can be shown at a time with its planning units.
- Zoom to feature extent - zooms the map to the extent of the features geometry
- Preprocess - intersects the feature with the planning grid which is a prerequisite for a Marxan run. For more information see [Preprocessing features](#preprocessing-features).  
### Adding and removing features  
To add or remove conservation features in a project click on the +/- button in the features tab and select which features you want to include in the project. Features that are included in the project will be listed in alphabetical order. Features can only be added or removed in projects that were created with the New Project Wizard and not for imported projects. For more information see [Why do imported projects have less functions available?](#why-do-imported-projects-have-less-functions-available)
### Viewing feature metadata  
In the context menu click Properties to view all of the feature metadata. For more information see [Feature Properties window](#feature-properties-window).  
### Changing feature targets  
Feature targets can be changed in one of two ways:  
- In the features tab, double click on the target icon of the feature whos target you want to change, type the new target percent and press ENTER
- In the Feature Properties window, enter a new value in the Target Percent field and click OK  
### Changing feature penalty factor  
In the Feature Properties window, enter a new value in the Species Penalty Factor field and click OK  
## Running projects
### Changing run settings
#### Changing the number of runs
#### Choosing how much clumping
### Stopping runs
### Viewing results
### The log window
#### Output from preprocessing
#### Output from runs
### The run log
# Features
## Understanding features
## The features window
## Managing features
### Creating new features
#### Importing existing features
#### Drawing features on screen
#### Adding features from the Global Biodiversity Information Facility (GBIF)
#### Adding features from the IUCN Red List of Threatened Species
### Deleting features
## Preprocessing features
## Feature properties window
## Showing features on the map
# Planning grids
## Understanding planning grids
## The planning grids window
## Managing planning grids
### Creating new planning grids
### Importing existing planning grids
### Deleting planning grids
## Including/excluding individual planning units
## Including/excluding already protected areas
### Protected areas information
### Preprocessing protected areas
# Users
## Understanding users
## The users window
## Managing users
## Roles
### Guest users
### Users
### Admin users
## The user menu
### Settings 
### Profile
### Change password
### Logout
# Mapping
## Understanding mapping
Describe why Mapbox is used
## Interacting with the map
## Changing how the results are displayed
## Changing the basemap
# Help 
## Server details
## Help item
## About item
# Providing Feedback
# FAQ
## Why do imported projects have less functions available?
