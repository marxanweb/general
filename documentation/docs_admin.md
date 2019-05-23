# Administrator Documentation
This documentation is aimed at IT staff within organisations who wish to deploy and use Marxan Web within their organisation. It covers the architecture, installation,configuration and security and maintenance.  

## Architecture
The Marxan Web software comprises a set of discrete components that work together in a network to provide the tools to do systematic conservation planning. This section outlines how these components work together and what the options are for deploying and using Marxan Web in your organisation.  

### marxan-server and marxan-client
Marxan Web comprises software running on a server (marxan-server) and software running on the client (marxan-client). These two separate bits of software work together in a loosely-coupled way through web services with the marxan-server providing the data storage and processing layer and marxan-client providing the user interface to that content. These two separate components can be installed on a single machine, a network machine or they can be accessed from a hosted Marxan Web installation (i.e. on the cloud). For more information about the advantages and disadvantages of each option, see [Migration Guide - Which do I choose - hosted or within my organisation?](/docs_migration.md#which-do-i-choose-hosted-or-within-my-organisation)
These different options are shown in the following sections. 

#### Single machine installation
In a single machine installation, both marxan-server and marxan-client are installed on the same physical machine.

<img src='images/admin_single_machine.png' title='Single machine installation' class='docsImage'>

This is typical of a Windows installation on a desktop computer or a Unix installation on a network machine. For more information on installing on Windows, see [Windows](#windows). For more information on installing on Unix, see [Unix](#unix).  



#### Separate machine installation


### Marxan Servers and the Marxan Registry

### Cross-platform
### 
## Installation
### Windows
### Unix
### Mac
## Configuration
### Configuration files
#### server.dat
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
