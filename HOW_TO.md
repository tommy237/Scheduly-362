HOW TO CREATE A WEBSITE
-----------------------
```
python3 -m venv [VENV NAME]
cd ./[VENV NAME]
source ./bin/activate
```

If the indicated errors pop up within the terminal, requested Ubuntu or WSL, proceed with the following commands:
> apt install python3.12-venv (ERROR: )
> pip install django==3.2     (ERROR: Couldn't import Django.)
> pip install setuptools      (ERROR: No module named 'distutils')

```
django-admin startproject [PROJECT NAME]
cd ./[PROJECT NAME]
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```

HOW TO RUN THE WEBSITE
----------------------
(tentative section, working in progress)
```
source ./[VENV DIRECTORY]/bin/activate
python3 manage.py runserver
```
