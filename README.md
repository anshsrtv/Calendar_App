# Django Personal Event Calender

## How To Setup in Ubuntu
1. Clone This Project `git clone https://github.com/anshsrtv/Calendar_App.git`
2. Go to Project Directory `cd Calendar_App/`
3. Install Python `sudo apt install python3`
4. Install virtualenv `sudo apt-get install python3-venv`
4. Create a Virtual Environment `python3 -m venv env`
5. Activate Virtual Environment `source env/bin/activate`
6. Install Rest Framework by Django `pip install djangorestframework`
6. Install Requirements Package `pip install -r requirements.txt`
7. Create Migration `python manage.py makemigrations`
8. Migrate Database `python manage.py migrate`
9. Create Super User `python manage.py createsuperuser`
10. Finally Run The Project `python manage.py runserver`
