Flasky
====== 


"flasky" is a simple flask application from the instructions in Miguel Grinberg (2018), [Flask Web Development](http://www.flaskbook.com). 
Once working, it will get refactored into the more complex application, "alchemy".


## Virtual Environment

Activate the virtual environment in PowerShell by running: 

```
cd flasky

flasky\Scripts\Activate.ps1
```

To succeed, this may first require a change to execution policies in Power Shell: 

```
Set-ExecutionPolicy Unrestricted -Scope Process
``` 

Success is visible when the path begins with (flasky) 


# Requirements 

Requirements can be updated at any time by running: 
```
pip freeze >requirements.txt
```


# Web Server 

In VS Code powershell: 
```
$env:FLASK_APP = "hello.py"
$env:FLASK_DEBUG = "1"
```
then: 
```
python -m flask run
```

the flask web server can be found at: http://localhost:5000/
