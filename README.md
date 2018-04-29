# Project Panelist
## Web and API backend

### Dependencies

* Python 3.5+
* pip
* virtualenv

For installation instructions, see [Installing Python](https://github.com/outfrost/panelist-potato/wiki/Installing-Python).

### Environment setup

First, clone repository and checkout the appropriate branch, e.g.

```sh
$ git clone https://github.com/outfrost/panelist-potato.git
$ cd panelist-potato/
$ git checkout <branch_name>
```

#### With PyCharm

1. Open the working directory in PyCharm
1. Open any `.py` file in the editor, e.g. `manage.py`
1. At the top of the editor you should see a message saying "No python interpreter configured for the project" - click "Configure Python interpreter"
1. In Project Interpreter settings, to the right of the Project Interpreter dropdown (probably showing "<No interpreter>"), click the gearbox icon and choose "Show all..."
1. Click the plus icon to add a new interpreter
1. If you've only just cloned the repository, you should have "New environment" selected, with a path to `python3` or `python3.x` as the base interpreter. If you've already initialised a virtual environment, you should have "Existing environment" selected, with a path to a Python executable within the project's `venv` directory. Accept these settings by clicking "OK"
1. In "Project Interpreters" select the newly created Python instance (probably labelled "Python 3.x (panelist-potato)" or alike) and click the pencil icon to edit
1. Change its name to `python-panelist` (make sure it's exactly that to avoid Git conflicts) and hit "OK"
1. Accept changes by clicking "OK" to leave "Project Interpreters" and then "OK" to leave the settings window
1. After PyCharm processes the new settings, you should see another message at the top of the editor, saying "Package requirements ..." - click "Install requirements", make sure all checkboxes are checked and hit "Install"
1. PyCharm will now take some time to install project dependencies and index the files, allow it to finish and you're good to go.

#### Via terminal

1. `cd` into the working directory
1. Create a new Python 3 virtual environment
	```sh
	$ virtualenv -p python3 venv
	```
	For Windows:
	```
	virtualenv venv
	```
1. Enter the virtual environment
	```sh
	$ source venv/bin/activate
	```
	For Windows:
	```
	venv\Scripts\activate.bat
	```
1. Install project requirements in the environment
	```sh
	$ pip3 install -r requirements.txt
	```
	That should be it, you're ready to work.

To leave the virtual environment after you're done, use
```sh
$ deactivate
```
... or exit the shell.

If you're planning to use PyCharm for development, follow the instructions above in the "Environment setup: With PyCharm" to set it up.

### Running Django

#### With PyCharm

1. Open the "Run Configuration" dropdown on the main toolbar and select "Edit Configurations..."
1. In the top left corner of "Run/Debug Configuration" click the plus icon to add a new configuration and select "Django server" from the dropdown menu
1. Name the configuration as you please (e.g. `Panelist`), leave all other settings at their default values and click "OK"
1. Start the server using the play icon to the right of the run configurations dropdown
1. Open http://localhost:8000 in your Web browser; you should see a welcome page saying "The install worked successfully! Congratulations!"
<!-- TODO Change if hello world page is configured -->

#### Via terminal

1. `cd` into the working directory and enter the virtual environment if you haven't already
	```sh
	$ source venv/bin/activate
	```
	For Windows:
	```
	venv\Scripts\activate.bat
	```
1. Start the Django server
	```sh
	$ python3 manage.py runserver
	```
	For Windows:
	```
	python manage.py runserver
	```
1. Open http://localhost:8000 in your Web browser; you should see a welcome page saying "The install worked successfully! Congratulations!"

To stop the server, interrupt it by sending `Ctrl`+`C` through the terminal, or closing the terminal window.
