# Django automated Scrapper

## This application scrapes data automatically every minute from a news website and stores it in the database.
### The data is scraped with the help of CELERY and redis as the message broker. A CELERY flower dashboard on localhost:5555 with a very simple UI which helps track the completed and uncompleted tasks.
### CELERY beat acts as the scheduler whereas  CELERY worker acts as the task manager for our automated scrapper.
### For celery to run in a django application, a celery.py file has to be added in the project directory and a tasks.py file in the app directory as seen in the [celery-docker documentation](https://testdriven.io/courses/flask-celery/docker/)
### It is also a necessity to use docker to build up the containers of our application as seen in the above documentation.
 
