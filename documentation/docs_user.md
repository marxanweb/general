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
On the left hand side of the application user interface is the project window which comprises three tabs: the project tab, the features tab and the planning units tab. These tabs taken together represent the inputs to the analysis: which project, which features are part of that project and what planning units will be used. For more information on projects see the projects section.

## Results window
On the right hand side of the application user interface is the results window which also comprises three tabs: the legend tab, the solutions tab and the log tab. These tabs taken together represent the outputs of the Marxan analysis and allow the user to change what results are shown and how they are visualised. For more information on project outputs see the running projects section.
## The Map
The main part of the application user interface is taken up by the interactive map. The map is the main way of visualising the outputs from any Marxan analyses and is a powerful and flexible tool for visualising hundreds of thousands of individual planning units on-the-fly in three dimensions. The map can be zoomed, panned, rotated and tilted to find the best viewing perspective for a particular run. For more information see the mapping section.
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
### Importing existing Marxan projects
### Duplicating a project
### Deleting a project
### Controlling access to a project
By default projects are created as public which means that they can be viewed by any other Marxan user. In order to restrict access to the project, it can be flagged as private and it will then only be visible to the project author.
### Editing project metadata
## Managing features within a project
### Adding and removing features
### Viewing feature metadata
### Changing feature targets
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
## Interacting with the map
## Changing how the results are displayed
## Changing the basemap
# Help 
## Server details
## Help item
## About item
# Providing Feedback
