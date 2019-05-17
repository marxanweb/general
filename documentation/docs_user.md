* A markdown unordered list which will be replaced with the ToC, excluding the "Contents header" from above
{:toc}
# User Guide  
Marxan Web is a software tool for doing Systematic Conservation Planning over the web and for sharing the results amongst the conservation community and other stakeholders. It builds upon the existing DOS-based Marxan software and offers the following new features and benefits:  
- It can installed locally or used directly online (hosted version)
- It includes the latest version of the WDPA
- It is great
- It is fantastic etc

For more information about migrating from the existing version of Marxan see the [Migration Guide](https://andrewcottam.github.io/marxan-web/documentation/docs_migration.html)

## Systematic Conservation Planning with Marxan Web
### Achieving conservation targets 
### Making Marxan more accessible  
### Sharing results with the conservation community
## Tutorial 1: Case study from British Columbia
## Tutorial 2: Creating a simple project in 4 steps
## The Marxan User Interface
The section provides a brief overview of the main elements in the Marxan User Interface and introduces some of the terminology in use. For more detailed information visit the individual sections further on.
### Log in window
When Marxan Web is first loaded the login screen is presented as shown in the image below. The login screen allows you to select a Marxan Server and to login to that server. It also allows you to register as a new user. For more information see [New User Registration](#new-user-registration).  

Marxan Servers are the databases that contain all of the Marxan projects that are distributed around the world in different organisations and, in the case of local installations, they include the local server (shown as localhost). Users can connect to these servers to view those projects that have been created in those organisations. In addition, if those organisations have granted access, these projects can be edited and run by those users. Hovering over a server shows a brief description of that server and the domain on which it is hosted. An icon to the left of the name shows the current status of that server according to the following symbols:  
- <no symbol> Read/write - projects can be viewed and edited (by users with those permissions)
- <padlock> Read only - project can be viewed only (by the guest user)
- <broken link> - server currently offline - no connection is possible. This could be due to a number of reasons: the server could be down, the server may be inaccessible due to firewall restrictions or the network connection may have been lost.  

Once a server has been selected, the user must enter their credentials to login to that server. The user will be logged in according to their role: read-only user, user or admin user. Each of these roles have a different set of features that they have access to in the application with admin users having access to all features. All of the screen shots in the following sections show the application as an admin user and hence not all elements may be visible if logged in as a different user. For more information see [Roles](#roles).

Once you are logged in you will see the Marxan User Interface. This comprises three main elements which are part of a single page web application: the map, the project window (on the left) and the results window (on the right). Other windows are shown as and when they are required. This single page will remain the main user interface until logging out and all tasks are completed in this interface.  

### Project window
On the left hand side of the application user interface is the project window which comprises three tabs: the project tab, the features tab and the planning units tab. These tabs taken together represent the inputs to the analysis: which project, which features are part of that project and what planning units will be used. For more information on projects see the [Projects](#projects) section.  

### Results window
On the right hand side of the application user interface is the results window which also comprises three tabs: the legend tab, the solutions tab and the log tab. These tabs taken together represent the outputs of the Marxan analysis and allow the user to change what results are shown and how they are visualised. For more information on project outputs see the [Running projects](#running-projects) section.  
### The Map
The main part of the application user interface is taken up by the interactive map. The map is the main way of visualising the outputs from any Marxan analyses and is a powerful and flexible tool for visualising hundreds of thousands of individual planning units on-the-fly in three dimensions. The map can be zoomed, panned, rotated and tilted to find the best viewing perspective for a particular run. For more information see the [Mapping](#mapping) section.  
## Projects
### Understanding projects
Projects are the main way of organising any Marxan Web analyses and are the logical starting point for any conservation planning. Each project contains a set of conservation features (i.e the things that you are interesting in protecting); a set of planning units which represent the geographic domain over which the analysis will be done and a set of run parameters that are used to fine-tune the analysis to get the best results. A project also has a limited set of metadata including the project name, a description and the date that it was created. Users with read/write permissions can create any number of projects which are limited only by the amount of disk storage on the server machine.  
#### Types of project
Marxan Web projects can be created from scratch using the New Project wizard, or they can be imported from previous DOS-based Marxan projects. Both types of projects can be run and visualised in the map, but imported projects have less capabilities than new projects. The preferred method of creating projects is to create them using the New Project wizard where possible. The main difference is that features cannot be added or removed in imported projects and those features can't be visualised on the map.  
### The projects window
![Image of Projects Windows](marxan_projects.png)  
The projects window is the main way you manage projects on a server and depending on your user role you can manage your own projects or everybodys projects. The projects window lists the projects on the server together with their metadata including the user, project name, description and creation date (the actual columns that are shown will depend on the user role). The view of projects can be sorted by any of the columns by clicking on the column header to sort in ascending or descending order. At the bottom of the window is a toolbar that contains the common tasks associated with managing projects - the actual buttons that are shown will depend on the user role. The functioning of these buttons is described in the following sections.  
### Included case studies
In a default installation of Marxan Web on a desktop machine, there are a number of pre-loaded case studies that will be shown in the projects window. These have been created to help you get up and running quickly by providing example start projects and specific tutorials for working through real-world conservation planning scenarios. These will be available from the 'localhost' server. In addition, case studies can be opened from other Marxan servers when the user is logging in. This is the true power of Marxan Web in being able to open projects from other organisations and share your own projects to your stakeholders.  
### Managing projects
This section contains information on the common tasks associated with managing projects.  
#### Creating new projects
The preferred way to create new projects in Marxan Web is to create them with the New Project wizard. This wizard takes the user through a simple set of steps to create a fully functioning Marxan Web project. The user creates the project metadata; selects the conservation features that will be included in the project and chooses the planning grid that will form the geographic extend and resolution for the analysis.  
  
To create a new project using the New Project wizard:  
1. Click on the New button in the projects window
2. Enter the project metadata and click Next
3. Choose a planning grid from the drop down list - when you choose an item the map zooms to the extend of the grid and shows the planning units. If the required planning grid is not shown, then it can be created in from the Planning Grids window (see the [Planning Grids](#planning-grids) section) and then the wizard can be restarted. Click Next
4. Choose the conservation features that will be part of your project
5. Select a cost surface (not currently implemented) and click Finish  

The project will now be created and opened and can be run immediately.  
#### Importing existing Marxan projects
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
#### Duplicating a project
Duplicating a project copies all of the project information to a new project with the same project name but with a '\_copy' suffix. The project can then be opened, edited and run. This provides a mechanism for iterating and improving projects until they are fit-for-purpose.
#### Deleting a project
To delete a project, select a project and click on the delete button. Deleting a project will not delete any features or planning grids.
#### Controlling access to a project
By default projects are created as public which means that they can be viewed by any other Marxan user. In order to restrict access to the project, it can be flagged as private and it will then only be visible to the project author. To set a project as private, in the project tab select the check box marked private at the bottom of the window.  
#### Editing project metadata
To edit the name or description for a project, simply click on the name or description in the project tab and then edit it. When you are finished press ENTER.
### Managing features within a project
The features that are included in a project are shown in the features tab and for each feature there is a target icon (on the left), a status bar (underneath the feature name) and a context menu (on the right).  

The target icon shows the target that has been set for that particular species and its color reflects the status of the feature. If the project has been run and the target has been achieved for the feature then it is white. If the target has not been achieved it is shown in pink.  

The status bar shows a scale from 0 to 100% which shows the amount of the feature that needs to be protected (in grey) and the amount protected in the current run (in blue). If the amount protected in the current run does not reach the amount to be protected then the target icon is shown in pink.  

The context menu provides a set of functions that apply to the feature and the precise set of functions depends on whether the project was created using the New Project wizard or imported and also on whether the feature was uploaded to Mapbox (see the [Uploading spatial data to Mapbox](#uploading-spatial-data-to-mapbox) section).  

The following list is the full set of functions that are available in the context menu:  
- Properties - this opens the Feature Properties window - for more information see [Feature Properties window](#feature-properties-window).  
- Remove from project - this is a shortcut to remove that feature from the project.  
- Add to map - the features geometry will be added to the map as a polygon - currently only one feature at a time can be shown on the map.  
- Outline planning units where the feature occurs - this shows those planning units which intersect the features polygon. Only one feature can be shown at a time with its planning units.  
- Zoom to feature extent - zooms the map to the extent of the features geometry.  
- Preprocess - intersects the feature with the planning grid which is a prerequisite for a Marxan run. For more information see [Preprocessing features](#preprocessing-features).  

#### Adding and removing features  
To add or remove conservation features in a project click on the +/- button in the features tab and select which features you want to include in the project. Features that are included in the project will be listed in alphabetical order. Features can only be added or removed in projects that were created with the New Project Wizard and not for imported projects. For more information see [Why do imported projects have less functions available?](#why-do-imported-projects-have-less-functions-available)
#### Viewing feature metadata  
In the context menu click Properties to view all of the feature metadata. For more information see [Feature Properties window](#feature-properties-window).  

#### Changing feature targets  
Feature targets can be changed in one of two ways:  
- In the features tab, double click on the target icon of the feature whos target you want to change, type the new target percent and press ENTER
- In the Feature Properties window, enter a new value in the Target Percent field and click OK  

#### Changing feature penalty factor  
In the Feature Properties window, enter a new value in the Species Penalty Factor field and click OK.  

### Running projects
#### An overview of running projects
When you run a project in Marxan Web there are a number of discrete steps that take place. These are described in the following paragraphs.  

If you are running the project for the first time or you have added new features since the last time you ran it, then all of those features need to be preprocesssed. For more information see [Preprocessing features](#preprocessing-features). This is done automatically as part of the Marxan run and the state of that preprocessing is shown in the Log tab.   

Once feature preprocessing has been completed, then the algorithms that compute the best combinations of planning units will be run. During this step, the algorithms produce a set of optimal solutions that protect the features (according to their stated targets) with the minimum cost. The number of these solutions that are produced is set in the Run Settings window (see [Run settings](#run-settings) and has a large bearing on how long the Marxan run will take. By default any new project will have 10 iterations. The run duration will also depend on how many features there are and how extensive and detailed the planning grid is. Runs can be stopped at any time using a number of methods. For more information see [Stopping runs](#stopping-runs).  

The state of the Marxan run is shown in the Log tab (although this is currently not supported on Windows) and the Run number shows the number of the iterations that have already been run. There is a lot of additional information in the Log window which shows the statistics that have been produced by the algorithms. The state of a Marxan run is also shown in the Run log window (admin users only). For more information see [the Run log](#the-run-log).

If the run completes succesfully, at the end of the run the results will be shown on the map and in the features tab. For more information see [Viewing and interpreting the results](#viewing-and-interpreting-the-results). If the run is stopped before it has finished then no results will be available and the results from the previous run (if available) will still be visible in the map and in the features tab.

#### Run settings
There are a large number of settings that can be changed for the Marxan run and these are edited in the Run Settings window which is accessed from the bottom of the main project window. A lot of these settings are for experienced Marxan users that understand how the different values can affect the results, but there are some commonly used settings that are described in the next sections: the number of runs and the degree of clumping. For more information on all of the Marxan Run settings consult the Marxan User Manual available in pdf from [here](https://github.com/andrewcottam/marxan-server/raw/master/marxan%20manual%201.8.10.pdf).  

To set a run parameter, click in the value column next to the corresponding parameter, enter a new value and click OK. The setting will be used the next time you run the project. The method to change the BLM parameter value is slightly different - for more information see [Clumping window](#clumping-window).  

##### Changing the number of runs
One of the most important of the run settings is the number of iterations that will be done. During the development of a Marxan project it will usually suffice if the number of runs is relatively low, e.g. 10-20 to get a rough idea of the impact of any changes in features, targets or costs. However, when these changes have been finalised it is important to run Marxan with a much greater number of iterations to get the best results. The number of iterations is set in the NUMITNS parameter. 

##### Clumping window
The degree to which the planning units are grouped or clumped together is controlled by the BLM setting and this value is set using the Clumping window. To access the Clumping window, click on the icon in the value column for the BLM setting.  

When the clumping window first opens for a project, Marxan Web has to produce the necessary information to determine the connectedness of the planning units and thus enable the clumping algorithm. The calculation of the connectedness (or boundary lengths) is done automatically in Marxan Web and the progress is shown in the Log tab. At the end of the process the clumping window will be enabled and can be used.  

This window provides an interactive way to set the degree of clumping by running the project 5 times using different clumping values and showing the results on 5 separate maps. To use a specific BLM value, click on the map that has the most promising distribution of planning units or enter its value directly in the Run settings window. The default values for the clumping window are: 0.001, 0.01, 0.1, 1 and 10. These may not necessarily be the best values for the current project and it may be necessary to experiment with different values to find the one that works the best. To change the range of BLM values in the clumping window, enter new values for the minimum and maximum and click the Refresh button. These values will be scaled over the 5 separate maps and a new set of results will be shown.  

To change the scale and position of all of the 5 separate maps, move or zoom the map in the main window.  

#### Stopping runs
Project runs can be stopped at any point using one of the following methods:
- By clicking on the Stop button in the main project window
- By opening the Run Log window (admin users only) and clicking on the running project and clicking the Stop button. For more information see [the Run Log](#the-run-log).

Marxan runs can also be stopped for other reasons - for more information see [the Run Log](#the-run-log).

#### Viewing and interpreting the results
Once a Marxan run has completed the results are shown on the map and in the Features tab. The map output will show either an individual solution or a summary of all solutions which are described in the following sections. The Features tab will show how much of each feature is protected in the individual solution and whether the feature has reached its target or not. This is described in [Viewing targets](#viewing-targets)

##### Understanding solutions
The outputs of a Marxan run are a set of individual solutions to the systematic conservation planning problem and a summary of those solutions. Each one of the individual solutions was created by the simulated annealing algorithm to maximise the overall protection for features while minimising the cost outlay. The number of solutions produced in the run is set as one of the run parameters - for more information see [Changing the number of runs](#changing-the-number-of-runs). Each individual solution shows a distribution of planning units that will protect the most features by using a process called complementarity, i.e. by looking at the overall complement of features within all the planning units rather than simply protecting those planning units with the most features in (which may have a similar set of features). This is a simple description of complementarity - for a more in depth discussion see, for example, [Marxan and Relatives: Software for Spatial Conservation Prioritization](https://www.researchgate.net/profile/Matthew_Watts/publication/43525654_Marxan_and_relatives_Software_for_spatial_conservation_prioritization/links/56ab3bcc08aeadd1bdcccc51.pdf).

##### Understanding the summary of solutions
The summary of all the solutions is the total, for each planning unit, of the number of solutions that contained that planning unit in its output. This is the default view in the map at the end of a Marxan run and effectively shows you the most important areas for protection. The mapping symbology for this layer can be changed by clicking on the Legend settings button. For more information see [Changing how the results are displayed](#changing-how-the-results-are-displayed).

##### Solutions tab
The individual solutions and the summary of solutions are presented in tabular form in the Solutions tab. By default, at the end of a Marxan run the summary of solutions is shown in the map and the sum row is selected in the table. Underneath the sum row, each one of the individual solutions are shown with information on the overall score, cost, number of planning units and the number, if any, of targets that have been missed. To show an individual solution on the map, click on the relevant solution in the table. The table data can be sorted (like all tables in Marxan Web) by clicking on the column header to sort in ascending or descending order. This allows you to rank the solutions in order of score etc.

##### Viewing targets
The Marxan run also produces information on how much of each feature is protected in each solution and whether or not it has met its target. Targets are set in the Features tab - for more information see [Changing feature targets](#changing-feature-targets). To view information on which features have met their targets for an individual solution, select that solution in the Solutions tab - the features are updated in the Features tab - for more information on understanding feature targets and how they are visualised see [Managing features within a project](#managing-features-within-a-project). By default, at the end of a Marxan run the solution with the best score is shown in the Features tab.  

#### The Log window
The purpose of the Log window is to provide realtime feedback on any processes that are running on the Marxan server. This is especially important for long-running processes (such as Marxan runs) where visual feedback is essential to know that something is still happening. The log window directly streams messages back from the Marxan server in realtime while the browser is connected. If the browser is closed or the connection is lost then the log will no longer update if the browser is reopened. In these cases processes on the server may still be running but there will be no realtime logging. To view the status of Marxan runs if you have disconnected you can use the Run log - for more information see [the Run log](#the-run-log).  

Whenever any preprocessing or Marxan runs are started, the log window is opened to show the progress and to show any errors, if they occur. This log can be copied to the clipboard (by clicking on the copy button at the bottom of the window) and cleared (by clicking on the erase button).  

#### The Run log
The Run log is used to view the status of any Marxan runs and to stop those runs where necessary. The table shows a list of all of the known Marxan runs and shows information on the process ID, user, project, start and end date, duration and the number of solutions completed and the number of solutions requested. The status is set according to the following values:  
- Running - the run is currently running. This can also appear under exceptional circumstances either if the server crashes or is turned off.  
- Stopped - the run was stopped by a user
- Killed - the run was killed by the operating system. This can happen if there are too many concurrent runs and the server runs out of memory.  

Projects that have started running will continue to run on the server until one of the following happens: they complete; they are explicitly stopped or if the server kills the process. If the browser window or tab is closed or the connection to the server is lost, the run will continue regardless. To check the progress of a run if you have lost the connection to the server, you can open the run log and click on the Refresh button to see whether it has completed or not. If it has completed and you want to view the results then you can open the project from the Projects window. Only the results from last successful run can be loaded, as each subsequent run overwrites the previous results in Marxan. If you want to save the results of previous runs then the best approach is to duplicate the project and then run it with a different name.  

Bear in mind that admin users have access to all of the runs that are currently running (for any user) and can stop runs using the Run Log window. To avoid this happening you can restrict access to particular projects by setting them as private. See [Controlling access to a project](#controlling-access-to-a-project).   

## Features
### Understanding features
Features in Marxan Web are those things that need to be protected and can range from biodiversity features, for example species or habitats, to ecosystem services, for example scenic areas or natural capital. All projects must contain one or more features and for each feature a target must be specified for the amount of that feature that must be protected (based on the geographic extent). For example, if a feature within a project is 'sea grass beds' and it has a total geographic area of 32Km2 within the planning grid and a target of 10%, then the total area of sea grass beds that must be protected is 3.2Km2.  

All features within the project initially carry the same weight - that is, all of them are considered equally in the Marxan run. This can be changed by changing the Species Penalty Factor. For more information see [Changing feature penalty factor](#changing-feature-penalty-factor).  

The source for these features can come from a range of different sources including local spatial data, global data providers or digitising them on the screen. One of the benefits of using Marxan Web is that any features that have been captured by the community can be shared between projects (if users have permissions).  

### The features window
The features window is used to show all of the features that are available on the server and it allows the user to manage those features. The list of features shows information on the name of the feature, a description and the date that it was created on. Features can be sorted either in ascending or descending order by clicking the column in the table. Hovering over the feature name will show the full unique system identifier for the feature and hovering over the description will show the full description if it cannot be read in the table.  

### Managing features
#### Creating new features
All users can create new features using a number of different methods which are described below. In each case the process ends with the feature being uploaded to Mapbox so that it can be visualised in the map. For more information see [Uploading spatial data to Mapbox](#uploading-spatial-data-to-mapbox).  

##### Importing existing features
To upload existing spatial data from the local machine onto the server as a new feature, click on the Import button. This opens the Import wizard, which requires a zipped shapefile and the name and description of the new feature. If the feature with the name specified already exists, then an error message will be shown at the bottom of the screen and the feature name will have to be updated.  
The only prerequisite for importing an existing feature is that the feature must have the necessary projection information file present - for more information see [Requirements for importing spatial data](#requirements-for-importing-spatial-data).

##### Drawing features on screen
Another way to capture new features within Marxan Web is to digitise them directly on the map using the mouse. To do this:
1. In the Features window click on New and Draw on screen   
2. Draw the new feature on the map by clicking and drawing a polygon
3. When you are finished double click to finish the polygon
4. Enter the name and description in the dialog box and click OK  

##### Adding features from the Global Biodiversity Information Facility (GBIF)
The ability to add new features from GBIF will be made available in future versions of Marxan Web, but the workflow will be to present the user with a list of species names that they can select and then data for those species will be added into the project.  The user would be able to control how that data is represented in the project, for example whether to use squares that represent the species occurrence data at the correct resolution or whether to draw a convex hull around the points - or some other representation.  

##### Adding features from the IUCN Red List of Threatened Species
Adding features from the IUCN Red List will also be made available in future versions of Marxan Web and the workflow will be similar to that for GBIF data.  

#### Deleting features
Deleting features is only possible as an admin user and should be done with great caution as those features may be in use in any number of projects on that server. If they are deleted then the projects that reference them will no longer work correctly and it may not be possible to repair them.

### Preprocessing features
In order for the features to be able to be used in Marxan, they have to be preprocessed by intersecting them with all of the planning units in the planning grid. This is necessary so that the algorithms know which features occur in which planning units. This process is done automatically in Marxan Web when a project is run for the first time, or if new features are added to a project. Once the preprocessing has started it cannot be stopped and once is has finished it does not need to be done again.  

### Feature properties window
The Feature properties window shows information about the feature including its metadata, its spatial statistics and its protection in the currently selected solution (if no individual solution is selected then the statistics will relate to the best solution by default). To show the feature properties window, click on Properties in the features context menu. For more information see [Managing features within a project](#managing-features-within-a-project). 

The information that is shown for a feature is summarised below. Note that not all of this information is shown for features in an imported Marxan project. For more information see [Why do imported projects have less functions available?](#why-do-imported-projects-have-less-functions-available).
- ID - an internal unique identifer for the feature.  
- Alias - the user-friendly name for the feature and the one that will be shown in the features window and features tab
- Feature class name - the unique system-provided name for the feature. This identifer is unique across all server databases and is the same identifier used in the Mapbox ID.  
- Description - the description the user provided for the feature.
- Creation date - the date that the feature was created in Marxan Web (not the date that the shapefile was created in the case of an imported shapefile)
- Mapbox ID - a unique identifier for the feature in Mapbox.
- Total area - the total area of the feature in square kilometers.
- Target percent - the target percentage for the feature for the Marxan run.
- Species penalty factor - the weighting given to the feature.
- Preprocessed - a flag to indicate if the feature has already been preprocessed (i.e. intersected with the planning grid). If the feature has already been preprocessed then there will be statistics for the  planning unit count and area.
- Planning unit count - the total number of planning units which intersect the feature.
- Planning unit area - the total area of the feature in the planning grid (in square kilometers). 
- Target area - the area that needs to be protected to meet the target percentage for the feature (in square kilometers).
- Area protected - the total area of the feature protected in the current solution (in square kilometers). This is only available after a run has completed. If the area protected is less than the target area then this figure will be shown in red. In some cases the area protected may appear to be the same as the target area and yet the figure is shown in red. This is because of rounding issues in showing the figure in the table and if you hover over the area protected you will see the actual un-rounded area of the feature.  

### Showing features on the map
For new projects that have been created in Marxan Web, the features can be shown on the map as polygons.  Imported projects do not support showing feature polygons on the map - for more information see [Why do imported projects have less functions available?](#why-do-imported-projects-have-less-functions-available) To show a feature on a map, click on the link in the features context menu. Only one feature can be shown in the map at any time.  

For all projects, the extent of the feature can also be mapped by clicking 'Outline planning units where the feature occurs' in the context menu - this shows those planning units which intersect the features polygon. Only one feature can be shown at a time with its planning units.  

## Planning grids
### Understanding planning grids
Planning grids provide the geographic framework for the systematic conservation planning process. They define the geographic extent and the resolution of the individual planning units that make up the grid and it is this grid which forms the basis of the Marxan analysis. Within Marxan Web there are various tools for creating and managing planning grids and the size and type of planning grid used has an important bearing on the analysis and also on the real-world implementation of the new reserve system. 

### The planning grids window
The planning grids window provides information on the planning grids that are available on the server. The table shows the following information:

- Name - the user-friendly name of the planning grid. If you hover over the name you will also see the internal unique identifier for the planning grid. This is also the unique identifier for the dataset on Mapbox.
- Description - a brief description of the planning grid. Hover over the description to see the full text.
- Country - The country that the planning grid covers (not available for imported planning grids).
- Domain - Whether the planning grid relates to marine or terrestrial areas (not available for imported planning grids).
- Area - The area of the planing units that make up the planning grid (in square kilometers).  

At the bottom of the planning grids window is a toolbar that allows you to manage planning grids. These tools are described in the following sections.  

### Managing planning grids
Planning grids can be created, imported and deleted using the tools in the planning grids window. Not all tools are available for all roles. For more information see [Roles](#roles).  

#### Creating planning grids
There are two basic types of planning grid: ones created in Marxan Web and ones created externally and imported from the local machine. Both of these can be used in projects and the only difference is that creating planning grids externally provides more flexibility in defining the geographic extent and characteristics of the planning units. For example, you may want to conduct a project over a province or state rather that a whole country and in this case you would have to create the planning grid using an external tool and import it.  

Whatever type of planning grid that you create, at the end of the creation process the planning grid will be uploaded to Mapbox - for more information see [Uploading spatial data to Mapbox](#uploading-spatial-data-to-mapbox).   

##### Creating new planning grids using Marxan Web 
To create a new planning grid in Marxan Web, click on the New button in the planning grids window. This opens the New Planning Grid window where you will need to select the necessary information to create the planning grid. For the area of interest, in future versions of Marxan Web you will be able to upload an area of interest which will define the geographic extent for the planning grid.  

#### Importing existing planning grids
To import an existing planning grid into Marxan Web, click on the Import button in the planning grids window. This opens the Import Planning Grid window where you will need to provide a name for the planning grid and a zipped shapefile containing the spatial data. The shapefile must have a field called 'puid' (lowercase) and have a projection file associated with it - for more information see [Requirements for importing spatial data](#requirements-for-importing-spatial-data).  

#### Deleting planning grids
Deleting planning grids can only be done by admin users and should be done with great caution as those grids may be in use in any number of projects on that server. If they are deleted then the projects that reference them will no longer work correctly and it may not be possible to repair them.  

### The Planning Units tab
When a planning grid is used within a project, by default all of the planning units within the grid are used in the analysis. If you want to change how these planning units are used, this is done through the Planning Units tab. This tab allows you to either manually include or exclude individual planning units, or to include all planning units which contain existing protected areas. These are described in the sections below.  

#### Including/excluding individual planning units
Manually including or excluding individual planning units is useful where a real-world issue affects where new protected areas can be designated. For example, if you know that a particular planning unit contains a restricted military area and cannot be designated, then you could manually exclude that planning unit from the project.  

If you want to manually include or exclude individual planning units from the project, then click on the lock icon. The planning units are now in edit mode, where you can change the status of any of the units to be one of the following: 

- initially included (i.e. the planning unit is initially in the reserve system but is not guaranteed to be in the results). 
- locked in the reserve system, i.e. the planning unit will be present in every solution.
- locked out of the reserve system, i.e. the planning unit will be absent in every solution.

To change the status of a planning unit, click on the map. The status will cycle between the three states. If you want to reset the status to the default then right click on the planning unit. If you want to reset all of your manual edits, click on the eraser button.  

When you have finished editing the planning units, click on the lock icon again and the statuses will be saved. You can now run the project with these updated statuses. It is important to note that these changes to the planning units only appy to the current project and not to the planning grid itself. Creating a new project with the same planning grid will not show any of the manual changes that have been made.  

#### Including existing protected areas
Another method of changing the status of planning units, is to include all existing protected areas in the project. By including protected areas in the project you are ensuring that the existing protected areas network is part of your overall reserve design. See [Protected Areas information](#protected-areas-information) for information on the source of the protected areas data.  

To include existing protected areas in your project, select the appropriate IUCN protected areas category from the list. For more information on IUCN categories, see [Protected Area Categories](https://www.iucn.org/theme/protected-areas/about/protected-area-categories). The map will update to show the protected areas within that particular IUCN category - terrestrial protected areas are shown in green and marine protected areas are shown in blue.  

If this is the first time that the protected areas have been selected, then preprocessing will need to be done on those protected area boundaries. For more information see [Preprocessing protected areas](#preprocessing-protected-areas).  

If you have already made some manual edits to the planning units and these overlap with the planning units that contain protected areas, then the manual edit will take precedence.  

#### Protected Areas information
Marxan Web uses protected areas information from the World Database of Protected Areas (WDPA) and the citation and version of the WDPA that is used is indicated in the Help | About window and at the bottom of the map (see also [Acknowledgements](#acknowledgements)). Future versions of Marxan Web will allow users to upload their own protected areas information if they want to be able to include protected areas that are not part of the WDPA, e.g. Other Effective Area-Based Conservation Measures such as Locally Managed Marine Areas.  

#### Preprocessing protected areas
Preprocessing of protected areas is necessary to see how they intersect with the planning units. This only needs to be done once and at the end of the process the planning units which intersect with the protected areas are shown with a blue border in the map. This indicates that they will be locked into the reserve network. The progress of this preprocessing can be seen in the Log tab.  

## Users
### Understanding users
The Marxan Web tool is designed to support the design of new reserve systems and protected area networks that can be shared amongst a user community and some of that information may be sensitive or confidential. Therefore controlling access to that data and who can do what with it is a fundamental requirement of the tool.  

Marxan Web provides controlled access to resources through the use of Roles and every registered user belongs to a particular role. By default all new registered users belong to the 'user' role. Role management is done by users with an admin role through the Users window.  

Every user has access to their own profile and settings through the User menu which allows you to change overall settings for Marxan Web, change your personal information and your password. For more information see [The User menu](#the-user-menu).  

### The Users window (admin users only)
The Users window provides information on the users that are registered on the server and is available from the Admin menu. The table shows the following information: the username, the users full name and email and their current role. At the bottom of the Users window is a toolbar that allows you to manage Users. These tools are described in the following sections.  

### Managing users
#### New User Registration
New users are registered with the New User Registration window accessible from the Login form and new users must provide their username, password, full name and an email address. If the username already exists on that server then they will receive an error message and will have to choose a different username. This user information can be changed at any time using the User menu. For more information see [The User menu](#the-user-menu).  

Currently registration is done automatically and users can immediately login with their credentials in the Login form.  

#### Deleting users (admin users only)
Users can be deleted from the Users window by admin users. To delete a user, select the user and click on the Delete button. This should be done with great caution as all of the associated projects for that user on that server will also be deleted.  

#### Enabling Guest Users (admin users only)
By default all servers provide read-only access to all projects through the Guest user. For more information see [Guest users](#guest-users). To enable/disable the Guest user tick/untick the checkbox at the bottom of the Users window.  

### Roles
This section describes the access that specific roles have to Marxan Web and the underlying data.  

#### Guest users
Guest users are users that have read-only access to all projects on the server (with the exception of projects which have been flagged as private, which they will not be able to see - for more information see [Controlling access to a project](#controlling-access-to-a-project)). As a read-only user they can view projects, features and grids but they will not be able to change any of them. For projects, they will be restricted to viewing the results of projects and changing how they are displayed on the map - no other settings can be changed for a project and they will not be able to run them either.  

The Guest user is enabled by default on servers so that you can view projects on other servers as a read-only user. This can be changed in the Users window. For more information see [Enabling Guest Users](#enabling-guest-users-admin-users-only). If the Guest user is disabled on a server then login attempts will fail.  

#### Users
The role 'User' is the default role for new registered users in Marxan Web. This role can create and manage projects, features and planning grids with some restrictions (they have no delete rights for any of these resources). In addition, the Projects window will only show projects belonging to that user (to make it easier for them to find their own projects on a server with lots of other users and projects). If a user wants to see all of the other projects on the server, regardless of user, then they can log in as the Guest user (with read-only access).  

#### Admin users
Admin users have the most privilages in Marxan Web and have full access to all features including managing users. Each server will have at least one admin user and this role is responsible for managing access for all of the other registered users. Administration of Marxan Web is covered in more detail in the [Administrator Documentation](https://andrewcottam.github.io/marxan-web/documentation/docs_admin.html).  

### The User menu
The User menu allows you to view and update information on the currently logged on user and to set general settings for Marxan Web. Hovering over the User menu will show you the username of the currently logged on user and their role. The items in the menu below are described in the following sections.  

#### Settings 
The Settings window provides access to general settings for the Marxan Web tool and these settings are saved between sessions.  

The Mapbox basemap style setting allows users to select their default basemap from a list including vector basemaps and imagery basemaps. For more information see [Changing the basemap](#changing-the-basemap).  

The Show planning unit popup is used to control the visibility of the popup with information about each of the planning units. With this emabled whenever the user hovers over a planning unit, a window is shown with information about that planinng unit including the number of times it is included in the summed solutions. For more information see [Understanding the summary of solutions](#understanding-the-summary-of-solutions).  

#### Profile
The Profile window allows users to update their profile information.  

#### Change password
The Change password window allows users to update their password. Users will have to use this new password the next time they log into Marxan Web.  

#### Logout
Logs a user out of the system.  

## Mapping
### Understanding mapping
One of the main aims in the design of Marxan Web has been to be able to view the results of any analyses quickly and easily on a map. In the DOS version of Marxan there was no mapping interface built in and users had to use a variety of tools to be able to visualise the results. The most advanced tool for visualising Marxan results is the CLUZ tool which is a plugin for the QGIS desktop GIS software - for more information see the [CLUZ website](https://anotherbobsmith.wordpress.com/software/cluz/). Marxan Web builds on the mapping features of CLUZ but from within a web browser where results can be accessed and shared without any additional software requirements.  

The main features of the mapping components in Marxan web are:
- High performance visualising of hundreds of thousands of planning units  
- On-the-fly changes to the symbols and rendering  
- A range of different basemaps available all with Open Street Map content  
- Rotation and tilting of the map (including rotating labels)
- Low bandwith for the data

In order to meet these requirements a technology called MapboxGL has been used and Marxan Web benefits from in-kind contributions from Mapbox - for more information see [Acknowledgements](#acknowledgements). These include access to a number of global Open Stree Map basemaps - for more information see [Changing the basemap](#changing-the-basemap).  

The main mapping features are described in the following sections.  

### Interacting with the map
The interactive map supports all of the usual web map features such as panning, zooming and navigating but it also supports rotating and tilting the map view as well. To rotate or tilt the map view, right-click on the map and move the mouse up/down to tilt or left/right to rotate the map. To reset the rotation, click the compass icon in the bottom right of the map window. 

When the results of a Marxan run are shown in the map, users can click on planning units to see a list of all of the features that occur in that particular planning unit. 

### Changing how the results are displayed
The display of the analysis results in the map can be configured using the Legend Settings window, accessible from the bottom left corner of the Legend tab. This window allows you to set the classification method that is used to color the various planning units in the results. At the top of the classification window is a frequency histogram which shows the distribution of the summed solutions and their frequency. For more information about the summed solutions see [Understanding the summary of solutions](#understanding-the-summary-of-solutions). To change how the planning units are symbolised, change any of the parameters in the Legend Settings window to immediately see the results. Once you are satisfied with the symbols click OK. These settings are saved with the project and will be reloaded when the project is reloaded.  

To change the transparency of the results layer in the map, click on the slider underneath the legend and move it to the right (more opaque) or the left (more transparent). This also applies to the protected areas layer which is shown when a set of protected areas is selected in the Planning Units tab. For more information see [Including existing protected areas](#including-existing-protected-areas).  
### Changing the basemap
The basemaps that are used in Marxan Web include both traditional vector cartography and high resolution imagery. The vector data is provided by Open Street Map (OSM) which is a community-driven public dataset of the worlds geographic features. In many parts of the world it offers unrivalled detail on a whole range of geographic features which are updated on a rolling basis (including down to the street and house level). For more information see [OpenStreetMap](https://www.openstreetmap.org/). The imagery data comes from a variety of commercial providers, as well as open data from NASA, USGS, and others. For more information see [Mapbox Sources](https://www.mapbox.com/about/maps/#data-sources).  

To change the basemap, select one from the list in the User Menu. For more information see [The User menu](#the-user-menu).  

### Requirements for importing spatial data  
Any spatial data imported into Marxan Web must have the necessary projection information file present (a *.prj file in a shapefile) so that the feature can be projected internally to an equal area projection. This internal reprojection is necessary so that spatial operations can be done (e.g. intersection) and so that Marxan can run using the data.  

### Uploading spatial data to Mapbox
Any spatial data that is imported into Marxan Web is stored in a database on the server and it is also uploaded to Mapbox to make the high performance visualisation possible. This process is done when the data are first uploaded and once this has finished it does not need to be done again. The process should not take more than 1-2 minutes and you can continue using Marxan Web while the process is ongoing.  

## Reports and outputs
Future versions of Marxan Web will have features to produce a downloadable report which presents information on the project, features, targets and shows the map results.  

GIS users can directly connect to the database of a local installation of Marxan Web and produce their own maps and reports by combining this Marxan data with their own local data layers. For more information see the [Developer Documentation](https://andrewcottam.github.io/marxan-web/documentation/docs_dev.html).  

## Help menu
The Help menu provides simple information on the server, a link to the documentation and an About box. These are described in the following sections.  

### Server details
The Server details show the information about the server that the user is currently connected to, including the server name, description, host, operating system and the version of the marxan-server (and the marxan-client, if it is installed).  

### Documentation
This provides a link to the main page for the Marxan Web documentation.  

### About window
The About window provides information on the versions of software that are being used including the underlying DOS version of Marxan. It also provides information on data providers and funding and in-kind contributions. 

## Providing Feedback
Please provide any feature requests or bug reports to the [GitHub repo](https://github.com/andrewcottam/marxan-web) by logging in and clicking on: Issues | New Issue and attaching a label of Bug (for a bug) or Enhancement (for a feature request).  

![Image of Yaktocat](https://octodex.github.com/images/yaktocat.png)

For general feedback, please email andrew.cottam@ec.europa.eu.

## Acknowledgements
### Data providers:  

Uses data from the World Database of Protected Areas. IUCN and UNEP-WCMC (2017), The World Database on Protected Areas (WDPA) August 2017, Cambridge, UK: UNEP-WCMC. Available at: www.protectedplanet.net  

### Funding and in-kind contributions:  
Marxan Web funded by the BIOPAMA project of the European Commission. With in-kind contributions from Mapbox.  

Marxan funded by a range of donors - see [here](http://marxan.org/credits.html).

## FAQ
### Why do imported projects have less functions available?
Projects that have been imported from the DOS version of Marxan only contain text files with data in. These files were taken directly from the Marxan project input and output folders and do not contain the original spatial data that was used to create all of the necessary tabular input files. Therefore, because there is no spatial data available for any of the features, they cannot be shown on the map pr added/removed from projects in the same way that new projects created with Marxan Web can be.   

