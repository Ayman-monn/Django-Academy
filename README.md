
# Online-Academy

## Description
Welcome to our project! This is a Online Academy App made in Python and the Django framework. It allow student to subscribe in various programming languages courses with stripe payment method. With this app student can comment their error and teachers can help to find the proper solutions , All users can write aritcles and comment in the blog. 

## Contributing
We welcome any and all contributions! Here are some ways you can get started:
1. Report bugs: If you encounter any bugs, please let us know. Open up an issue and let us know the problem.
2. Contribute code: If you are a developer and want to contribute, follow the instructions below to get started!
3. Suggestions: If you don't want to code but have some awesome ideas, open up an issue explaining some updates or imporvements you would like to see!
4. Documentation: If you see the need for some additional documentation, feel free to add some!


## Running App 
1. first clone the repository: 
>` git clone https://github.com/Ayman-monn/django_academy.git` 
2. change your dirctory to the App. 
3. make sure you installed pipenv if not 
>` pip install pipenv ` 
4. install requirements.txt file
>` pipenv install -r path/to/requirements.txt ` 
5. wait till all requirements installed. 
6. active env with
>`pipenv shell`. 
7. make migrations .
>python manage.py makemigrations
8. make migrate
>python manage.py migrate
9. create super user .
>python manage.py createsuperuser
10. now you can use the app by going to your localserver  