Alchemy 
=======

A flask project exploring SQL Alchemy. Initial structure from: 

Miguel Grinberg (2018). Flask Web Development: Developing Web Applications with Python. O'Reilly. 


# Requirements

The application includes a _requirements.txt_ file containing the package dependencies. The initial commit just used the latest version available. 
The dependencies can be loaded in a virtual environment with: 

```
pip install -r requirements.txt 
``` 

The package versioning can be added or updated with: 

```
pip freeze >requirements.txt 
``` 

# Virtual Environment 

The virtual environment is setup in powershell using: 

```
python -m venv venv
```

Activate the virtual environment in PowerShell by running: 

```
venv\Scripts\Activate.ps1
```

To succeed, this may first require a change to execution policies in Power Shell: 

```
Set-ExecutionPolicy Unrestricted -Scope Process
``` 

Success is visible when the path begins with(venv) 



# Configuration 

Configuration options are useful for things like using different databases in dev and test environments, for example. 

A hierarchy of configuration classes is used. 
The config base class holds common settings. The subclasses hold specific settings for different configurations. 

Most settings can be imported from environmental variables for flexibility and security. Defaults are generally provided in case they are not defined by environmental variables. These are suitable for development environments only. 

The SQLALCHEMY_DATABASE_URI, required by Flask, receives different values under each of these configurations, so that the application uses a different database in each environment. Each configuration tries to import the database URL from an environment variable, and when that is not available it sets a default one based on SQLite. The testing configuration defaults to an in-memory database as there is no need to store data outside of a test run. 

The development and production configurations have mail server configuration options. The Config class and subclasses can define an init_app() class method that takes the application instance as an argument. The base Config class has an empty init_app() method at first, but this may change later. 

The different configurations are registered in a config dictionary towards the end of the configuration script. The development configuration is registered as the default. 

