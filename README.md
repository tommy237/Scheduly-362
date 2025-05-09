_**Note**: for the CPSC-362 Software Engineering course_
![image_logo_scheduly_new](https://github.com/user-attachments/assets/a556e767-b0b7-4b8b-a8dc-377578891126)

------
# |||:||||||||||||||||||||:||| _<ins>**B<sub>ACKGROUND</sub>**</ins>_ |||:||||||||||||||||||||:|||
_**Scheduly**_ is a social media platform that relies heavily on events, calendars, and (of course) schedules. It can allow users to add mututal friends, so that their profiles can display their busy schedules for the day, week, month, year, or later. This feature can help users organize their life and manage their time, since additional features enhance productivity among the social and online demographic.

Take calling your friends as a prime example; it's normal for them to not reciprocate, and reasons of that vary with work, sleep, school, or others. No one knows how active their friends are, currently, and there's also confusion as to why they're not active at that time. Rhethorical question, but how do people know when to connect with someone at the right time?

------
# |||:||||||||||||||||||||||||||:||| _<ins>**S<sub>ETUP</sub>**</ins>_ |||:||||||||||||||||||||||||||:|||
This guide shows users on how to run this website project _Scheduly_, and other general inquries about website hosting. Once you've cloned this repository within a folder of your choice, begin the process below. Keep in mind that knowing basic terminal commands from Linux, and Ubuntu WSL installation is recommended.

And also, read all the sections provided below.

## (i) — _<ins>**C<sub>reating a website</sub>**</ins>_

Create a virtual environment, where it utilizes the required packages needed for the program. Start from here and follow from top to bottom adding commands into Ubuntu WSL terminal:
```bash
python3 -m venv VENV_NAME     #creates a new virtual environment VENV_NAME
cd ./VENV_NAME                #accesses venv
source ./bin/activate         #you should see (VENV_NAME)
```

If the indicated errors pop up within the terminal, requested Ubuntu or WSL, proceed with the command:
```bash
apt install python3.12-venv    #(ERROR: ...ensurepip is not available.)
pip install django==3.2        #(ERROR: Couldn't import Django.)
pip install setuptools         #(ERROR: No module named 'distutils')
#OR (recommended)
pip install requirements.txt   #(to download all required packages)
```

If those commands are done, proceed to execute:
```bash
django-admin startproject PROJECT_NAME   #creates a django-based website template
cd ./PROJECT_NAME                        #accesses PROJECT_NAME
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```

## (ii) — _<ins>**R<sub>unning the website</sub>**</ins>_
This is the main section where a user should run the acquired website application locally, and consistently without issues. Follow these commands top to bottom.

```bash
source ./VENV_DIRECTORY/bin/activate              #you should see (VENV_NAME)
python3 ./PROJECT_DIRECTORY/manage.py migrate     #optional (for adding data models)
python3 ./PROJECT_DIRECTORY/manage.py runserver
```

### _<ins>**N<sub>otes to cover</sub>**</ins>_
* ``cd ./FOLDER_NAME`` focuses to the next folder from the current folder the terminal is on.
* ``cd /FOLDER_NAME`` focuses to the next folder from the very beginning of the directory.

* ``pip install PACK_NAME==VERSION_#`` requests the package installation to be exactly the version needed.
* ``./####_DIRECTORY`` refers to the path from the current folder to the destination file.

------
# |||:||||||||||||||||||||:||| _<ins>**I<sub>NFORMATION</sub>**</ins>_ |||:||||||||||||||||||||:|||
\*\* = yet to fully implement outside of CPSC-362

\* = extra credit

## (i) — **T<sub>EAM</sub> M<sub>EMBERS</sub>**
+ _<ins>**T<sub>OMMY</sub> N<sub>GUYEN</sub>**</ins>_ <sub>:: @tommy237</sub>
+ _<ins>**S<sub>EAN</sub> N<sub>GUYEN</sub>**</ins>_ <sub>:: @SNguyen267</sub>
+ _<ins>**S<sub>TEPHANY</sub> M<sub>URILLO</sub> M<sub>UNOZ</sub>**_ <sub>:: @stephanyyyyy</sub>

## (ii) — **F<sub>EATURES</sub>**
_**Scheduly**_ applies many features that benefit user experience.
+ <ins>**Transformable Events**</ins> are a good feature; helpful for rescheduling appointments when there are problems.
   - **Dragging** appointments to a different day on the calendar.
   - **Resizing** events vertically or horizontally, increasing/decreasing event duration.
+ <ins>**Status Update**</ins> is a base feature that allows the user's activity dependent on their current schedule. Yellow, green, red, or grey are moreso determined if the user is free, idle, currently busy, or offline. This feature was solely inspired from Discord's status options, and serves as a good basis for _Scheduly_.
   - 🟩 **Online** - If the user is currently free and is using the app/phone.
   - 🟨 **Idle** - If user is using the app/phone during an event/work/school/appointment.
   - ⬜ **Offline** - If the user is currently free but not using the app/phone.
   - 🟥 **Busy** - If the user is not using the app/phone during an event/work/school/appointment.
   - For text, the attending event name will hover over their profile. Formatted text depends on the type of event created (class/job/vacation/appointment/interview/sleeping).
+ <ins>**\* Timezone Recalibration**</ins> is a base feature to include; for mutual friends who currently have school, work, or events at a different state or country. Events for mutual friends using a different time zone will have appointment times recalibrated for the user's time zone.
  - > _**Example**: If a friend has an appointment at 2:00pm Tuesday under Japan Standard Time (JST), that appointment is then recalibrated to 9:00pm Monday under Pacific Standard Time (PST) for the user._
  - Daylight Savings Time is under consideration.
+ <ins>**\*\* Integration**</ins> is another feature that's helpful, especially LinkedIn for interviews and zoom meetings. Google Calendars will also have back-to-back connection, since _Scheduly_ and it can utilize and import calendars.

## (iii) — **G<sub>OALS</sub>**
_**Scheduly**_ aims to support effective time management and productivity through all users, including collaboration with other social media platforms so that features from _Scheduly_ are implemented within those applications. It should also be a recommended application to new users, as the features supply a simple process of setting appointments and events.

\*\* We yet to aim to integrate some existing platforms such as:
+ <ins>**Facebook**</ins>
  - shared updates from _Scheduly_
+ <ins>**Twitter/X**</ins>
  - same reason as Facebook
+ <ins>**Snapchat**</ins>
  - status updates
+ <ins>**LinkedIn**</ins>
  - professional faculty's office hours/busy hours
  - connections can view schedules
+ <ins>**Google Calendar**</ins>
  - tasks/event imports
+ <ins>**Instagram**</ins>
  - status updates
  - birthdays
  - mutuals can view schedules, etc.
+ <ins>**Indeed**</ins>
  - same reason as LinkedIn
+ and many more...

## (iv) — **M<sub>ETHODS</sub>**
+ Design an enticing application/website logo (besides the opening text)
+ Plan a design layout of the platform (UI design blueprint)
+ Research backend languages of famous social media platforms above
+ Mainly utilize Python/C++/JavaScript <sub>(Instagram, Facebook, Snapchat, etc.)</sub>
  - Perl & PHP most certainly additional <sub>(Snapchat & Facebook)</sub>
  - Erlang is possible <sub>(Facebook)</sub>

------
