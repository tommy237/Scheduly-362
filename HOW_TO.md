------
# _<ins>**I<sub>NFORMATION</sub>**</ins>_
This guide shows users on how to run this website project _Scheduly_, and other general inquries about website hosting. Once you've cloned this repository within a folder of your choice, begin the process below. Keep in mind that knowing basic terminal commands from Linux, and Ubuntu WSL installation is recommended.

------
# _<ins>**C<sub>reating a website</sub>**</ins>_

Start from here and follow from top to bottom adding commands into Ubuntu WSL terminal:
```Linux Kernel Module
python3 -m venv [VENV NAME]
cd ./[VENV NAME]
source ./bin/activate
```

If the indicated errors pop up within the terminal, requested Ubuntu or WSL, proceed with the following commands:
```
apt install python3.12-venv (ERROR: ...ensurepip is not available.)
pip install django==3.2     (ERROR: Couldn't import Django.)
pip install setuptools      (ERROR: No module named 'distutils')
```

If those commands are done, proceed to execute:
```
django-admin startproject [PROJECT NAME]
cd ./[PROJECT NAME]
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```

------
# _<ins>**R<sub>unning the website</sub>**</ins>_

```
source ./[VENV DIRECTORY]/bin/activate
python3 ./[PROJECT DIRECTORY]/manage.py runserver
```

------
### _<ins>**N<sub>otes to cover</sub>**</ins>_
* ``cd ./[FOLDER NAME]`` focuses to the next folder from the current folder the terminal is on.
* ``cd /[FOLDER NAME]`` focuses to the next folder from the very beginning of the directory.

* ``pip install [PACK NAME]==[VERSION #]`` requests the package installation to be exactly the version needed.
* ``./[#### DIRECTORY]`` refers to the path from the current folder to the destination file.

------
