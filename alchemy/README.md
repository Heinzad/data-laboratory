Alchemy 
=======

A data laboratory experiment exploring Flask and SQL Alchemy. 


# Overview 

In chapter 7 of _Flask Web Development: Developing Web Applications with Python_, Miguel Grinberg (2018) sets out a way to organise a large application in packages and modules. 

The structure has several top-level folders or packages: 
* _app_ package -- holds the Alchemy application 
* _migrations_ package -- holds database migration scripts
* _tests_ package -- holds unit tests
* _venv_ package -- contains the python virtual environment

There are also several files in the top layer: 
* _requirements.txt_ -- lists the package dependences used when generating a virtual environment
* _config.py_ -- holds the configuration settings
* _alchemy.py_ -- defines the Flask application instance, and other tasks for managing the application

The following sections describe the setup in further detail. 


# Requirements File 

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



# Configuration Package

Configuration options are useful for things like using different databases in dev and test environments, for example. 

A hierarchy of configuration classes is used. 
The config base class holds common settings. The subclasses hold specific settings for different configurations. 

Most settings can be imported from environmental variables for flexibility and security. Defaults are generally provided in case they are not defined by environmental variables. These are suitable for development environments only. 

The SQLALCHEMY_DATABASE_URI, required by Flask, receives different values under each of these configurations, so that the application uses a different database in each environment. Each configuration tries to import the database URL from an environment variable, and when that is not available it sets a default one based on SQLite. The testing configuration defaults to an in-memory database as there is no need to store data outside of a test run. 

The development and production configurations have mail server configuration options. The `Config` class and subclasses can define an `init_app()` class method that takes the application instance as an argument. The base `Config` class has an empty `init_app()` method at first, but this may change later. 

The different configurations are registered in a config dictionary towards the end of the configuration script. The development configuration is registered as the default. 


# Application Package

The application package or _app_ folder contains the application code. Its modules include: Templates, static files, database models and email support files. 

## Application Package Constructor

A factory function is invoked from a script to create the application. This gives the ability to create multiple application instances, such as for multiple environments. 

The application factory function is defined in the application package constructor _app/__init__.py_  

This constructor imports most of the Flask extensions currently in use, but passes no arguments to their constructors when creating them so they are uninitialised.  
* The `create_app()` function is the application factory, utilising a given configuration name for the application.  
* The `from_object()` imports configuration settings directly into the app from a given configuration class. 
* The `init_app()` completes their initialisation when called. 

The application intialisation is performed in this factory function, using the `from_object()` method from the Flask configuration object, taking as an argument one of the configuration classes in _config.py_. The `init_app()` method of the selected configuration is also invoked, to enable more complex initalisation procedures. 

The factory function returns the created application instance. The necessary routes and custom error page handlers are discussed in the next section. 


## Application Blueprint

A Flask _blueprint_ defines routes and error handlers that are registered with the application, and defined in the global scope.
The blueprints are created in a subpackage of the application package: _app/main__init__.py_

Blueprints are created by instantiating an object of class `Blueprint`. The two required arguments are the blueprint name and the module in which the blueprint is located. 

The routes of the application are stored in _app/main/views.py_ module and error handlers in _app/main/errors.py_. They are associated with the blueprint when imported. The import sits at the end of _app/main/__init__.py_ to prevent circular dependency errors. 

The blueprint is registered with the application inside the `create_app()` factory function in _app/__init__.py_

_Error Handlers:_ The `main.app_errorhandler` decorator is used to install application-wide error handling via a blueprint. 

_Route:_ The route of the application to be updated. The route decorator comes from `main.route`.  
With blueprints, Flask applies a namespace to all the endpoints defined in a blueprint, so that multiple blueprints can define view functions with the same endpoint names without collisions.  
The namespace is the name of the blueprint (the first argument to the `Blueprint` constructor) and is separated from the endpoint name with a dot. The `index()` view function is registered with the endpoint name `main.index` and its URL is obtained by `url_for('main.index')`.  
Redirects within a blueprint can use the short form of `url_for('.index')`. 

Form objects are stored inside the blueprint in _app/main/forms.py_ module. 

## Application Script

The _flaks.py_ module defines the application instance. It sits in the top-level directory.  
The script begins by creating an application. If given, the configuration is taken from the environmental variable `FLASK_CONFIG`; if not, the default is used.  

Within the virtual environment, the `FLASK_APP` environment variable needs to be set so that the flask command can locate the application instance. It also helps to set `FLASK_DEBUG=1`.  

In VS Code powershell: 
```
$env:FLASK_APP = "alchemy.py"
```
then: 
```
python -m flask run
```

the flask web server can be found at: http://localhost:5000/


# Unit Tests 

The tests are written with the `unittest` package from the Python library. The `setUp()` and `tearDown()` methods run before and after each test. any methods that have a name that begins with `test_` are executed as tests. 

The `setUp()` method tries to create an environment for the test that is close to that of a running application. It: 
* Creates an application configured for testing and activates its context, so that tests access `current_app` like regular requests. 
* Creates a new database for the tests using Flask-SQLAlchemy's `create_all()` method. 

The first test verifies the application instance exists. The second test verifies the application is running under the testing configuration.

The `tearDown()` method removes the database and application context. 

An empty _tests/__init__.py_ module makes the test folder a proper package

A custom command to run the unit tests is added to _alchemy.py_ script. 

The unit tests can be executed in the virtual environment by: 

```
flask test 
```


# References 

Miguel Grinberg (2018). Flask Web Development: Developing Web Applications with Python. O'Reilly.  



© Adam Heinz 

9 December 2023 
