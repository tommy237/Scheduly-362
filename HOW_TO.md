------
# H<sub>OW TO CREATE A WEBSITE</sub>

Start from here and follow from top to bottom adding commands into Ubuntu WSL terminal:
```
python3 -m venv [VENV NAME]
cd ./[VENV NAME]
source ./bin/activate
```

If the indicated errors pop up within the terminal, requested Ubuntu or WSL, proceed with the following commands:
```
apt install python3.12-venv (ERROR: )
> pip install django==3.2     (ERROR: Couldn't import Django.)
> pip install setuptools      (ERROR: No module named 'distutils')
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
# H<sub>OW TO RUN THE WEBSITE</sub>

```
source ./[VENV DIRECTORY]/bin/activate
python3 ./[PROJECT_DIRECTORY]/manage.py runserver
```
