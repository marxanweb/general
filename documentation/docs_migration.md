# Migration Guide
This guide is aimed at existing users of the DOS version of Marxan (together with the various tools that support it) who are considering migrating to Marxan Web. It describes when it may be useful to migrate and how to do it.

## Should I migrate to Marxan Web?
Marxan Web offers a number of advantages and features that were not available in the DOS version of Marxan. However, there are some cases in which it may be better to stick with what you know rather than moving to Marxan Web. Below are some of the questions that may help in making the decision.  

### Do you have an internet connection?  
It may be obvious, bu Marxan Web depends on an internet connection and although it will work over low bandwidth connections it will not work without an internet connection. This also applies to the local installation of Marxan Web running on Windows as it uses live spatial data from Open Street Map and Mapbox. CLUZ (Conservation Land-Use Zoning software) is an alternative tool for working with Marxan that has no dependency on the internet, so if you need to work offline then this is a better option that migrating to Marxan Web. For more information see [CLUZ](https://anotherbobsmith.wordpress.com/software/cluz/).  

### Do you need to share resources?
Another question to ask is whether or not you need to share various Marxan resources with anyone else, e.g. scenarios, features, spatial data, planning grids or indeed the results. If the answer to all of these is no, then you may be better to continue with your existing Marxan tools and setup. However, if you want to share at least some data then Marxan Web makes it very easy.  

### Do you have many existing Marxan projects?
If you have a lot of existing Marxan projects it is actually very easy to import them into Marxan Web and indeed, managing them will be much easier once they have been brought into the tool. Existing Marxan projects can co-exist side-by-side with their imported versions as they do not share the same files or information, so you can continue to work with the projects in both tools if necessary.  

### Does Marxan Web offer the same set of features as the DOS version of Marxan?
Yes, it offers more features but with one caveat. None of the features that are available in Marxan with Zones are currently available, although this is planned for a future release. If you currently use Marxan with Zones then you are better off sticking with that until a future version of Marxan Web offers the same set of features.

## What's different?
Marxan Web is based on the DOS version of Marxan and therefore it includes all of the features of the DOS version but adds a whole new set of features to make it easier to do systematic conservation planning. Many of the workflows that are associated with the DOS version are no longer necessary and indeed the whole planning process can be achieved with Marxan Web from beginning to end without any software installations (if using the hosted version). For more information see [Which should I choose? A hosted service or hosted within my organisation](#which-do-i-choose-a-hosted-service-or-hosted-within-my-organisation).  

### Where are all the .dat files?
All of the *.dat files are still present in Marxan Web, but you don't need to manage them or even know where they are. All of the information within those files is managed from the Marxan Web interface. To understand where that information is, see the individual files below.  

#### input.dat file
A project in Marxan Web is defined by the input.dat file and this includes the project metadata, the run settings, the location of the other *.dat files and a few other items. Run settings are accessed from the Run settings window at the bottom of the project tab. Project metadata is accessed directly from the project tab and can be edited in place. For more information see the [User Guide - Run settings](docs_user.md#run-settings).  

#### pu.dat file
The planning unit file is managed from the Planning Unit tab where the status of each planning unit can be directly edited using the map. Planning units can be locked in, locked out or in the initial reserve system.  For more information see [User Guide - The Planning Units tab](docs_user.md#the-planning-units-tab).  

#### puvspr.dat file
The puvsrp.dat file is created automatically whenever a project is run by intersecting the features with the planning units. The progress of this preprocessing is shown in the Log window. If features are removed from a project, then the relevant records are also removed from the puvspr.dat file. For more information see [User Guide - Preprocessing features](docs_user.md#preprocessing-features).  

#### spec.dat file
The species file managed using the Features tab and when species are added/removed or their targets of spf values are changed then the underlying spec.dat file is updated. For more information see [User Guide - Managing features within a project](docs_user.md#managing-features-within-a-project).  

#### bounds.dat file
The boundary length file is created automatically when the Clumping window is opened for the first time in a project. For more information see [User Guide - Clumping window](docs_user.md#clumping-window).  

### No more external tools
The architecture of Marxan Web includes the open-source spatial database called PostGIS which provides all of the spatial functionality required for the tool, including doing all of the preprocessing to produce the various *.dat files that had to be produced by external tools in the DOS version of Marxan. In addition, because PostGIS is feature rich, in future versions of Marxan Web new functionality can be easily integrated without having to bring in any additional software. 

### Built in mapping interface
Marxan Web includes a powerful mapping component which is able to render hundreds of thousands of planning units and detailed data from OpenStreetMap. There is no longer any need for import/export routines to GIS tools to visualise the results. For more information see [User Guide - Mapping](docs_user.md#mapping).  

### Share resources online
One of the main differences between the DOS version of Marxan and Marxan Web is that Marxan Web allows you to quickly and easily share results with stakeholders and the conservation community, all in a controlled way. Projects, features and planning grids can all be shared online making it easy for other users to re-use spatial data and thematic datasets. If your organisation wants to share your resources, you can be added to the Marxan Registry which is the list of servers that are shown to users when they login to Marxan Web. 

### Scalable
The Marxan Web software can be used online (hosted option), installed on a network server within an organisation or installed on desktop machines. If you are planning on running big projects with lots of features and large planning grids then it may be appropriate to run these on your organisations infrastructure rather than online, where you will be sharing resources with other users.  

### Iterate with stakeholders
One of the major advantages of Marxan Web is that because it can be run online, iterations with stakeholders can be done very quickly and easily. In the process of designing reserve networks, those proposed networks can be changed in real time and the results can be viewed instantly. This significantly reduces the time required for iterating new projected area networks with decision making bodies.  

## Migrating to Marxan Web
If you have decided to migrate to Marxan Web, then this section describes what decisions you need to take and then how to get started.  

### Which should I choose? A hosted service or hosted within my organisation  
The Marxan Web software can be used from a hosted servive or hosted within your own organisation. Which one you choose depends mainly on the scale of your projects, whether you have any sensitive information and on whether you want to use existing data from other Marxan servers. The advantages and disadvantages of each option are described below.  

A hosted service of Marxan Web presents the easiest and fastest way to get going with Marxan Web. You are accessing the system online from an organisation that is hosting the software and they provide everything necessary. Once you have registered on that system you can use any of the existing content within your own projects and create your own data on that server. The disadvantages are that you are sharing that systems hardware with other users and so your projects may take longer to run than if they were installed within your own organisation on dedicated machines. Also, if you have any sensitive information (for example, sensitive species range data) then in the hosted version this data would be publically available and anyone could access it. In this case you would be better to host Marxan Web in your own organisation.  

Hosting Marxan Web in your own organisation requires you to install the software, either on a local, network or cloud-based machine. For more information about installing Marxan Web in your own organisation see the [Administrator Documentation](docs_admin.html). The advantages of this installation is that you can then share resources privately within your own organisation and performance is likely to be better as you are not sharing the processing with potentially many other users. The disadvantages are that you won't be able to access datasets that are available on hosted services of Marxan Web. If you have Marxan Web installed on a machine that is accessible over the internet, then you will still be able to share your results with others if you want to by registering in the Marxan Registry. For more information see [Share resources online](#share-resources-online).  

### Importing existing Marxan projects
Existing DOS based Marxan projects can easily be imported into Marxan Web. For more information see the [User Guide - Importing existing Marxan projects](docs_user.md#importing-existing-marxan-projects).  

## FAQ
### Can I just copy all my existing Marxan projects over to Marxan Web?
You cannot directly copy all of your existing projects over by simply copying the files as Marxan Web needs additional information that is not already included in those files. The best way to do this is to import each project one-by-one.
