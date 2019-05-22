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
Marxan Web is based on the DOS version of Marxan and therefore it includes all of the features of the DOS version but adds a whole new set of features to make it easier to do systematic conservation planning. Many of the workflows that are associated with the DOS version are no longer necessary and indeed the whole planning process can be achieved with Marxan Web from beginning to end without any software installations (if using the hosted version). For more information see [Which do I choose? Hosted or a local installation](#which-do-i-choose-hosted-or-a-local-installation).  

### Where are all the .dat files?
All of the *.dat files are still present in Marxan Web, but you don't need to manage them or even know where they are. All of the information within those files is managed from the Marxan Web interface. To understand where that information is, see the individual files below.  

#### input.dat file
A project in Marxan Web is defined by the input.dat file and this includes the project metadata, the run settings, the location of the other *.dat files and a few other items. Run settings are accessed from the Run settings window at the bottom of the project tab. Project metadata is accessed directly from the project tab and can be edited in place. For more information see the [User Guide - Run settings](docs_user.md#run-settings).  

#### pu.dat file
The planning unit file is managed from the Planning Unit tab where the status of each planning unit can be directly edited using the map. Planning units can be locked in, locked out or in the initial reserve system.  For more information see 

#### puvspr.dat file
#### spec.dat file
#### bounds.dat file


### No more external tools
### Built in mapping interface
### Share resources online
Projects, features and planning grids
Marxan Registry
### Scalable
### Iterate with stakeholders
## Migrating to Marxan Web
### Which do I choose? Hosted or a local installation
### Importing existing Marxan projects
#### Preparation
Planning grids need to be in WGS84 geographic coordinates and there must be a field named 'puid' (lowercase).
#### Issues
## FAQ
### Can I just copy all my existing Marxan projects over to Marxan Web?
