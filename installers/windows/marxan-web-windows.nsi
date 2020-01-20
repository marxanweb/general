;NSIS Modern User Interface
;Basic Example Script

;--------------------------------
;Include Modern UI

  !include "MUI2.nsh"

;--------------------------------
;Seeing if sections are selected
  !include "sections.nsh"

Function ConfigWrite
	!define ConfigWrite `!insertmacro ConfigWriteCall`
 
	!macro ConfigWriteCall _FILE _ENTRY _VALUE _RESULT
		Push `${_FILE}`
		Push `${_ENTRY}`
		Push `${_VALUE}`
		Call ConfigWrite
		Pop ${_RESULT}
	!macroend
 
	Exch $2
	Exch
	Exch $1
	Exch
	Exch 2
	Exch $0
	Exch 2
	Push $3
	Push $4
	Push $5
	Push $6
	ClearErrors
 
	IfFileExists $0 0 error
	FileOpen $3 $0 a
	IfErrors error
 
	StrLen $0 $1
	StrCmp $0 0 0 readnext
	StrCpy $0 ''
	goto close
 
	readnext:
	FileRead $3 $4
	IfErrors add
	StrCpy $5 $4 $0
	StrCmp $5 $1 0 readnext
 
	StrCpy $5 0
	IntOp $5 $5 - 1
	StrCpy $6 $4 1 $5
	StrCmp $6 '$\r' -2
	StrCmp $6 '$\n' -3
	StrCpy $6 $4
	StrCmp $5 -1 +3
	IntOp $5 $5 + 1
	StrCpy $6 $4 $5
 
	StrCmp $2 '' change
	StrCmp $6 '$1$2' 0 change
	StrCpy $0 SAME
	goto close
 
	change:
	FileSeek $3 0 CUR $5
	StrLen $4 $4
	IntOp $4 $5 - $4
	FileSeek $3 0 END $6
	IntOp $6 $6 - $5
 
	System::Alloc /NOUNLOAD $6
	Pop $0
	FileSeek $3 $5 SET
	System::Call /NOUNLOAD 'kernel32::ReadFile(i r3, i r0, i $6, t.,)'
	FileSeek $3 $4 SET
	StrCmp $2 '' +2
	FileWrite $3 '$1$2$\r$\n'
	System::Call /NOUNLOAD 'kernel32::WriteFile(i r3, i r0, i $6, t.,)'
	System::Call /NOUNLOAD 'kernel32::SetEndOfFile(i r3)'
	System::Free $0
	StrCmp $2 '' +3
	StrCpy $0 CHANGED
	goto close
	StrCpy $0 DELETED
	goto close
 
	add:
	StrCmp $2 '' 0 +3
	StrCpy $0 SAME
	goto close
	FileSeek $3 -1 END
	FileRead $3 $4
	IfErrors +4
	StrCmp $4 '$\r' +3
	StrCmp $4 '$\n' +2
	FileWrite $3 '$\r$\n'
	FileWrite $3 '$1$2$\r$\n'
	StrCpy $0 ADDED
 
	close:
	FileClose $3
	goto end
 
	error:
	SetErrors
	StrCpy $0 ''
 
	end:
	Pop $6
	Pop $5
	Pop $4
	Pop $3
	Pop $2
	Pop $1
	Exch $0
FunctionEnd

;--------------------------------
;General

  ;Name and file
  Name "Marxan Web"
  OutFile "marxan-web-v0.9.27.exe" ;TODO Update to correct version

  ;Default installation folder
  InstallDir "$LOCALAPPDATA\MarxanWeb"
  
  ;Get installation folder from registry if available
  InstallDirRegKey HKCU "Software\MarxanWeb" ""

  ;Request application privileges for Windows Vista and Windows 7 +
  RequestExecutionLevel admin
  
  ;Hide nullsoft install system
  BrandingText " "

;--------------------------------
;Interface Settings

  !define MUI_ABORTWARNING
  !define MUI_ICON "marxan.ico"	

;--------------------------------
;Pages

  !insertmacro MUI_PAGE_WELCOME
  !insertmacro MUI_PAGE_LICENSE "${NSISDIR}\Docs\Modern UI\License.txt"
  !insertmacro MUI_PAGE_COMPONENTS
  Page custom databaseDetails PgPageLeave
  !insertmacro MUI_PAGE_DIRECTORY
  !insertmacro MUI_PAGE_INSTFILES
  
  !insertmacro MUI_UNPAGE_CONFIRM
  !insertmacro MUI_UNPAGE_INSTFILES
  
;--------------------------------
;Languages
 
  !insertmacro MUI_LANGUAGE "English"

;--------------------------------
;Installer Sections

Var Dialog
Var Host
Var User
Var Password
Var Port
Var TextHost
Var TextUser
Var TextPass
Var TextPort
Var txt

Section "Marxan Server" SectionMarxanServer
  ;see if marxan web is already installed
  ;ReadRegStr $0 HKCU "Software\MarxanWeb" ""

  SectionIn 1 RO ;add RO to make it read only
  ;INSTALL MARXAN-SERVER 
  SetOutPath "$INSTDIR"
  File /r ..\..\..\marxan-server 
  #On windows we want to create a server.dat file from the default file - the user shouldnt have to configure it 
  File /oname=$INSTDIR\marxan-server\server.dat ..\..\..\marxan-server\server.dat.default

  ;CREATE WINDOWS SHORTCUTS
  SetOutPath "$INSTDIR"
  File "marxan.ico"
  File "run_marxan.bat"
  CreateDirectory "$SMPROGRAMS\MarxanWeb"
  CreateShortcut "$SMPROGRAMS\MarxanWeb\Launch Marxan Web.lnk" "C:\Windows\System32\cmd.exe" "/k $\"$INSTDIR\run_marxan.bat$\"" "$INSTDIR\marxan.ico" 0 SW_SHOWNORMAL ALT|M "Starts the marxan-server and opens Marxan Web"
  WriteINIStr "$SMPROGRAMS\MarxanWeb\Documentation.url" "InternetShortcut" "URL" "https://andrewcottam.github.io/marxan-web/documentation/docs_overview.html"

SectionEnd

Section "Marxan Client" SectionMarxanClient
  SectionIn 1 RO 
  ;INSTALL MARXAN-CLIENT
  SetOutPath "$INSTDIR"
  File /r ..\..\..\marxan-client 
  ;Store installation folder
  WriteRegStr HKCU "Software\MarxanWeb" "" $INSTDIR
  ;Create uninstaller
  WriteUninstaller "$INSTDIR\Uninstall.exe"
 
SectionEnd

Section "Marxan database" SectionMarxanDatabase
  SectionIn 1 RO 
  
SectionEnd

Section "Miniconda3" SectionMiniconda
  SectionIn 1 RO 
  ;INSTALL MINICONDA SILENTLY AND WHEN IT HAS FINISHED DELETE THE INSTALLER
  ;By default this installs Miniconda3 in the install directory just for the current user and does not register Python in the PATH environment variable
  SetOutPath "$INSTDIR"
  File "Miniconda3-latest-Windows-x86_64.exe"
  ExecWait '"$INSTDIR\Miniconda3-latest-Windows-x86_64.exe" /InstallationType=JustMe /S /D=$INSTDIR\Miniconda3'  
  Delete $INSTDIR\Miniconda3-latest-Windows-x86_64.exe
        
 SectionEnd

Section "Python packages" SectionPythonPackages
  SectionIn 1 RO 
  SetOutPath "$INSTDIR"
  File "python_prerequisites.bat"
  ;INITIALISE CONDA SO THAT IT CAN BE RUN FROM THE COMMAND LINE
  ExecWait '"$INSTDIR\Miniconda3\Scripts\conda" init cmd.exe'
  ;SET THE BASE ENVIRONMENT AND INSTALL PYTHON PREREQUISITES
  ExecWait '"$INSTDIR\python_prerequisites.bat"'
  Delete $INSTDIR\python_prerequisites.bat
  
SectionEnd

Section "PostGIS 2.5.1" SectionPostGIS
	SectionIn 1  
	;section to capture whether to install postgis or not - the flag is used in the next hidden section to either install full postgis or just the client tools
SectionEnd

Section -"Database installation" 
	;default install location is: C:\Program Files\PostgreSQL\10 folder and sets the GDAL_DATA environment variable
	SetOutPath "$INSTDIR"
	File "postgresql-10.7-1-windows-x64.exe"
	File "dump.sql"
	${If} ${SectionIsSelected} ${SectionPostGIS}
		;install the full postgresql database on the local machine
		DetailPrint 'Installing the full postgresql database on the local machine'
		ExecWait '"$INSTDIR\postgresql-10.7-1-windows-x64.exe" --unattendedmodeui minimal --mode unattended'  

		;install the full postgis database on the local machine
	    File "postgis-bundle-pg10x64-setup-2.5.1-1.exe"
		DetailPrint 'Installing the full postgis database on the local machine'
	    ExecWait '"$INSTDIR\postgis-bundle-pg10x64-setup-2.5.1-1.exe" /S'  
	    Delete $INSTDIR\postgis-bundle-pg10x64-setup-2.5.1-1.exe

		;restore the database dump to the new local installation of postgresql/postgis connecting as the postgres superuser
		${If} ${SectionIsSelected} ${SectionMarxanDatabase}
			DetailPrint 'Restoring the database dump to the new local installation of postgresql/postgis'
			ExecWait '"$PROGRAMFILES64\PostgreSQL\10\bin\psql" -c "CREATE USER jrc WITH PASSWORD $\'thargal88$\' LOGIN NOSUPERUSER IN GROUP postgres;" --dbname postgresql://postgres:postgres@localhost:5432/'
			ExecWait '"$PROGRAMFILES64\PostgreSQL\10\bin\psql" -c "CREATE DATABASE marxanserver WITH TEMPLATE = template0 ENCODING=$\'UTF8$\'" --dbname postgresql://postgres:postgres@localhost:5432/'
			ExecWait '"$PROGRAMFILES64\PostgreSQL\10\bin\pg_restore" --dbname=postgresql://postgres:postgres@localhost:5432/marxanserver dump.sql'
			
		${EndIf}
		
	${Else}
		;Using an existing PostGIS instance - write the data to the marxan web server.dat file
		${ConfigWrite} "$INSTDIR\marxan-server\server.dat" "DATABASE_HOST " "$Host" $R0 
		;the DATABASE_NAME, DATABASE_USER and DATABASE_PASSWORD will be the same as a default install
		
		;install the client tools only so that the dump.sql can be restored to an existing database
		DetailPrint 'Installing the client tools only so that the dump.sql can be restored to an existing database'
		ExecWait '"$INSTDIR\postgresql-10.7-1-windows-x64.exe" --enable-components commandlinetools --disable-components server,pgAdmin,stackbuilder --unattendedmodeui minimal --mode unattended'
		
		;restore the database dump to the specified instance of postgis - here we run psql with the superuser user/password (or a user with CREATEROLE privileges)
		${If} ${SectionIsSelected} ${SectionMarxanDatabase}
			;create the JRC user
			DetailPrint 'Restoring the database dump to the specified instance of postgis'
			DetailPrint 'Creating the jrc user'
			StrCpy $1 '"$PROGRAMFILES64\PostgreSQL\10\bin\psql" -c "CREATE USER jrc WITH PASSWORD $\'thargal88$\' LOGIN NOSUPERUSER IN GROUP postgres;"'
			StrCpy $2 " --dbname=postgresql://"
			StrCpy $3 ":"
			StrCpy $4 "@"
			StrCpy $5 ":5432/"
			StrCpy $6 "$1$2$User$3$Password$4$Host$5"
			ExecWait $6 $0

			;check that the restore worked
			${If} $0 == 2
				;connection failed
				MessageBox MB_OK "The connection to the database failed. Check the connection settings and retry."
			${EndIf}

			DetailPrint 'Creating the marxanserver database'
			StrCpy $1 '"$PROGRAMFILES64\PostgreSQL\10\bin\psql" -c "CREATE DATABASE marxanserver WITH TEMPLATE = template0 ENCODING=$\'UTF8$\'"'
			StrCpy $6 "$1$2$User$3$Password$4$Host$5"
			ExecWait $6 $0
			
		    DetailPrint 'Restoring the database dump to the specified instance of postgis'
			StrCpy $1 "$PROGRAMFILES64\PostgreSQL\10\bin\pg_restore"
			StrCpy $7 "marxanserver"
			StrCpy $8 " dump.sql"
			StrCpy $6 "$1$2$User$3$Password$4$Host$5$7$8"
			ExecWait $6 $0

		${EndIf}
	${EndIf}
	Delete $INSTDIR\postgresql-10.7-1-windows-x64.exe		
	Delete "dump.sql"

SectionEnd

;--------------------------------
;Functions

Function databaseDetails
	${If} ${SectionIsSelected} ${SectionPostGIS}
		Abort 
	${EndIf}
    !insertmacro MUI_HEADER_TEXT "PostGIS Server Settings" "Provide the existing PostGIS server details below. The user must have CREATEROLE privileges."
    nsDialogs::Create 1018
    Pop $Dialog
    ${If} $Dialog == error
        Abort
    ${EndIf}
    ${NSD_CreateGroupBox} 10% 10u 80% 76u "PostGIS Server Settings"
    Pop $0
        ${NSD_CreateLabel} 20% 26u 20% 10u "Host"
        Pop $0
        ${NSD_CreateText} 40% 24u 40% 12u "localhost"
        Pop $TextHost
        ${NSD_CreateLabel} 20% 40u 20% 10u "Port"
        Pop $0
        ${NSD_CreateText} 40% 38u 40% 12u "5432"
        Pop $TextPort
        ${NSD_CreateLabel} 20% 54u 20% 10u "User"
        Pop $0
        ${NSD_CreateText} 40% 52u 40% 12u "postgres"
        Pop $TextUser
        ${NSD_CreateLabel} 20% 68u 20% 10u "Password"
        Pop $0
        ${NSD_CreatePassword} 40% 66u 40% 12u "postgres"
        Pop $TextPass
    nsDialogs::Show
FunctionEnd

Function OnDirBrowse
    ${NSD_GetText} $TextPgDir $0
    nsDialogs::SelectFolderDialog "Select Postgres Directory" "$0" 
    Pop $0
    ${If} $0 != error
        ${NSD_SetText} $TextPgDir "$0"
    ${EndIf}
FunctionEnd

Function PgPageLeave
	;get the values for the dialog box components
    ${NSD_GetText} $TextHost $Host
    ${NSD_GetText} $TextPort $Port
    ${NSD_GetText} $TextUser $User
    ${NSD_GetText} $TextPass $Password
FunctionEnd

;--------------------------------
;Descriptions

  ;Language strings
  LangString DESC_SectionMiniconda ${LANG_ENGLISH} "Miniconda3 is a package manager for Python that contains Python version 3.7 and a minimal set of Python packages"
  LangString DESC_SectionPythonPackages ${LANG_ENGLISH} "Python packages required to run Marxan Web"
  LangString DESC_SectionPostgresql ${LANG_ENGLISH} "Open source SQL database"
  LangString DESC_SectionPostGIS ${LANG_ENGLISH} "PostgreSQL/PostGIS open-source spatial database. Unselect if you already have a PostGIS server that you want to use."
  LangString DESC_SectionPostGISDatabase ${LANG_ENGLISH} "Marxan database, tables, functions and test data"
  LangString DESC_SectionMarxanServer ${LANG_ENGLISH} "The Marxan Server provides the Tornado web server and application services for running Marxan Web"
  LangString DESC_SectionMarxanClient ${LANG_ENGLISH} "The Marxan Client is the web application that runs in a browser and interacts with the Marxan Server"

  ;Assign language strings to sections
  !insertmacro MUI_FUNCTION_DESCRIPTION_BEGIN
  !insertmacro MUI_DESCRIPTION_TEXT ${SectionMarxanServer} $(DESC_SectionMarxanServer)
  !insertmacro MUI_DESCRIPTION_TEXT ${SectionMarxanClient} $(DESC_SectionMarxanClient)
  !insertmacro MUI_DESCRIPTION_TEXT ${SectionMarxanDatabase} $(DESC_SectionPostGISDatabase)
  !insertmacro MUI_DESCRIPTION_TEXT ${SectionMiniconda} $(DESC_SectionMiniconda)
  !insertmacro MUI_DESCRIPTION_TEXT ${SectionPythonPackages} $(DESC_SectionPythonPackages)
  !insertmacro MUI_DESCRIPTION_TEXT ${SectionPostgresql} $(DESC_SectionPostgresql)
  !insertmacro MUI_DESCRIPTION_TEXT ${SectionPostGIS} $(DESC_SectionPostGIS)
  !insertmacro MUI_FUNCTION_DESCRIPTION_END

;--------------------------------
;Uninstaller Section

Section "Uninstall"
 
  ;marxan server and client files
  RMDir /r "$INSTDIR\marxan-client"
  RMDir /r "$INSTDIR\marxan-server"
  Delete "$INSTDIR\Uninstall.exe"
  
  ;anaconda3 and all packages
  ExecWait '"$INSTDIR\Miniconda3\Uninstall-Miniconda3.exe" /S' 
  RMDir -r "$INSTDIR\Miniconda3"
  
  ;postgis
  ;dont know how to do this silently
  
  ;remove windows shortcuts
  Delete "$INSTDIR\marxan.ico"
  Delete "$INSTDIR\run_marxan.bat"
  Delete "$INSTDIR\python_prerequisites.bat"
  RMDir /r "$SMPROGRAMS\MarxanWeb"
  RMDir "$SMPROGRAMS\MarxanWeb"
  
  ;delete registry keys
  DeleteRegKey HKCU "Software\MarxanWeb" 
SectionEnd
