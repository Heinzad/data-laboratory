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

Success is visible when the path begins witth(venv) 
