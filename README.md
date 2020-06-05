# Discovbeat
## What is it?
Discovbeat is a new way to share the music you love with your friends. For too long Spotify social features have been lacking. Discovbeat is here to change that by our new way to share playlists to your friends with your own personal touch! Our mission is to allow more people to discover new music through sharing!

## Instalation instructions
1. Create your virtual environment using your preferred way with the python version 3.8.1
    
2.  Activate your virtual environment
    
3.  Clone the repository using the command into your desired folder  `git clone https://github.com/RobertNimmo26/discovbeat.git` 
    
4.  Open the discovbeat folder in your command prompt  `cd discovbeat`
    
5.  Install the required packages  `pip install –r requirements.txt`

6. Open the  discovbeat_project folder with the command `cd discovbeat_project`

7. Open `settings.py` file
    
8.  Set up the .env file with the instructions below
    
9.  Set up the database using the commands  `python manage.py makemigrations discovbeat`  and  `python manage.py migrate`
    
10.  Run the web app using the command  `python manage.py runserver`
    
11.  In your preferred browser, access the web app using the URL  `http://localhost:8000/`

## Database
You can use any Database provider you wish. Currently there is two options with default code already provide, SQLite and mySQL.

Open `settings.py` and set up your prefered database provider. If you are planning to use SQLite or mySQL then you can uncomment the default code and set the parameters to reach your own database. Make sure you delete any unused databases code in `settings.py`.

If you are planning to use another database, such as postgreSQL, you will have to set this up on your own. Instructions can be found here [https://docs.djangoproject.com/en/3.0/ref/databases/](https://docs.djangoproject.com/en/3.0/ref/databases/)

You may wish to add the database login parameters to your enviromental variables

## Setting up .env file
There are 6 seperate environmental vairables to set up. 

Create a new file in this directory (it should be in the same directory as `settings.py`) called `.env`

###  Spotify api env vairables
Create a new app on [https://developer.spotify.com/dashboard](https://developer.spotify.com/dashboard) 

With the generated ClientId and ClientSecret set the env vairables to:

	SOCIALAUTHSPOTIFYKEY = <Your ClientId>
	SOCIALAUTHSPOTIFYSECRET = <Your ClientSecret>
	
	- There should be no < > in the env vairables

### Contact Us form email vairables
Using your prefered Email Provider set the env vaiarbles below.

	EMAIL = <Email address>
	EMAILPASSWORD = <Password for your Email Account>
	HOST = <Email Host>
	PORT = <Email Port>
	
	- There should be no < > in the env vairables

## External Sources

-   Bootstrap
    -   Nothing is required to be done to set up
-   jQuery
    -   Nothing is required to be done to set up
-   Spotify API
    -   Instructions provided above on how to set up

## Contributors

- Robert Nimmo
