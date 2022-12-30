# Hairdresser webpage for make believe hairdresser called Betakrøll

Group project with me and three others. Group assigment the whole semester. Using an agile approach. Project planning, collaboration, software design, demo, retrospectives. Test driven development. My main task was login/regitstration functionality (that also had to be customized mid project), a few tests and the design of the page.

Parts of the code has been removed due to privacy reasons.

## Lessons learned

Programming language used: Python
Tools and framework: Django, GitLab (repository and planning), agile development, Bootstrap

This project's main goal is learning agile development practices. The product that we were tasked with 
was creating a webapp that is based on the Django framework. We chose therefore to work with a hair 
salon which handles booking and controls hairdressing appointments. In order to learn the agile 
development process four students would work together in a team.

<img
  src="/logged_in_menu.jpg"
  alt="Picture of the webpage when logged in"
  title="Logged in menu"
  style="display: inline-block; margin: 2px auto; max-width: 300px">


<img
  src="/register.jpg"
  alt="Picture of the register new user screen"
  title="Register new user"
  style="display: inline-block; margin: 2px auto; max-width: 300px">

## The original readme info

Hair salon application.

To run the application: 

- Make sure to have all the files in the zip folder in the same directory when you run the program.
- Navigate to the folder containing `manage.py`.
- Type in `python3 manage.py runserver`
- Once the server is running, you can view the site by navigating to `http://127.0.0.1:8000/` in your local web browser. 

To run the tests:
- Make sure to have all the files in the zip folder in the same directory when you run the program.
- Navigate to the folder containing `manage.py`
- Type in `python3 manage.py test`

To add data to the user database and bookings:
- Make sure to have all the files in the zip folder in the same directory when you run the program.
- Navigate to the folder containing `manage.py`.
- Type in `python3 manage.py runserver`
- Go to `Min side` and `Registrer bruker`
- Register your user there. 
- Log in to the site.
- Go to `Min side` and `Book en time`
- Add a booking.
- Make sure to run `python3 manage.py makemigrations` and `python3 manage.py migrate`

OR use the admin page:
- Add your superuser by typing `python3 manage.py createsuperuser`
- Type in `python3 manage.py runserver`
- Once the server is running, you can view the site by navigating to `http://127.0.0.1:8000/admin` in your local web browser. 
- Log in with your super user credentials 
- Add users or bookings in Djangos administration site.
