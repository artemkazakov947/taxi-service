 
![Logo of the project](https://www.pngall.com/wp-content/uploads/13/Taxi-Yellow.png)

# taxi-service
> Django project for managing drivers and cars in taxi-garage


## Installing / Getting started

You have to install Python 3!

```shell
git clone git@github.com:artemkazakov947/taxi-service.git
cd taxi-sevice
pip install virtualenv venv
venv\Scripts\activate
pip install -r requirementes.txt
python manage.py runserver 
```
- Use the following command to load prepared data from fixture to test and debug your code:
  `python manage.py loaddata taxi_service_db_data.json`.
- After loading data from fixture you can use following superuser (or create another one by yourself):
  - Login: `director`
  - Password: `taxi-service`


### Deploying / Publishing

[taxi-service project deployed to Heroku](LINK HERE)



## Features


* Managing cars and drivers directly on the website
* You can also leave your review about car or whatever
* Authentication functionality for Driver/User
* Strong Django admin panel for deep managing
