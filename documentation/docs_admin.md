# Administrator Documentation
This documentation is aimed at IT staff within organisations who wish to host and use Marxan Web within their organisation. It covers the architecture, installation, configuration and security and maintenance. If you just want to use Marxan Web without hosting it yourself, then you can simply use a hosted service which requires no installation. For more information see [Migration Guide - Which should I choose? A hosted service or hosted within my organisation](/docs_migration.md#which-should-i-choose-a-hosted-service-or-hosted-within-my-organisation).  

## Architecture
The Marxan Web software comprises a set of discrete components that work together in a network to provide the tools to do systematic conservation planning. This section outlines how these components work together and what the options are for deploying and using Marxan Web in your organisation.  

### Client/server
Marxan Web comprises software running on a server ([marxan-server](https://github.com/andrewcottam/marxan-server)) and software running on the client ([marxan-client](https://github.com/andrewcottam/marxan-client)). These two separate bits of software work together in a loosely-coupled way through web services with the marxan-server providing the data storage and processing layer and marxan-client providing the user interface to that content (running in a browser). For more information on the architecture for each of these bits of software, see the relevant GitHub repos.  

These two separate components can be installed on a local, network or cloud-based machine, either on the same machine or on different machines. These different options are shown in the following sections.  

#### Single machine installation
In a single machine installation, both marxan-server and marxan-client are installed on the same physical machine. Marxan Web is cross-platform and this is typical of a Windows installation on a desktop computer or a Unix installation on a network machine. For more information on installing on Windows, see [Windows](#windows). For more information on installing on Unix, see [Unix](#unix).  

#### Separate machine installation
The marxan-server and marxan-client software can also be installed on separate machines, although this is less common and requires some additional configuration. The main advantage is that the client can then link to other installations of marxan-server.  

### Marxan Servers and the Marxan Registry
Wherever Marxan Web is installed, when it is run the login screen shows a list of marxan-servers that are available and that you can connect to. These have been registered in the Marxan Registry and these are essentially instances of marxan-server that organisations are hosting and want to make public and share. Any organisation can register their own instance of marxan-server and can control whether it is read-only or read-write and from which domains. For more information see [CORS restrictions](#cors-restrictions) and [ENABLE_GUEST_USER](#enable_guest_user).  To register your organisation in the Marxan Registry contact: andrew.cottam@ec.europa.eu.  

## Installation
Marxan Web is cross-platform which means that it will install and run on any operating system (although there may be some slight differences in the support on different platforms). Instructions for installing on different operating systems are given below.  

### Windows
A Windows installer is available for installing Marxan Web on Windows. For more information, see the [Windows Releases](https://github.com/andrewcottam/marxan-web/releases) page.  

### Unix
marxan-server and marxan-client have to be installed separately on Unix operating systems. For more information on installing these, see the relevant GitHub repos: [marxan-server](https://github.com/andrewcottam/marxan-server) and[marxan-client](https://github.com/andrewcottam/marxan-client).  

### Mac
The installation of Marxan Web on Mac operating systems has not been done yet as there are some issues with installing PostGIS which is a prerequisite of marxan-server.  

## Configuration

### Configuration files
#### server.dat
##### ENABLE_GUEST_USER 
#### user.dat
#### runlog.dat
### Securing access
#### Using SSL
#### Cookie authentication
#### CORS restrictions
#### Disabling security
### Database configuration
## Maintenance
### Updates 
To software just pull
### Routines tasks
#### Removing clumping projects
## FAQ
## Providing Feedback
