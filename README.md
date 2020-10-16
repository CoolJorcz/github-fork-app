## Github Fork App

#### Description 
This is a small toy app to utilize a Github OAuth Application to interact with the Github API's POST /repos/{owner}/{repo}/forks endpoint

Sample application lives at https://fork-that-app.herokuapp.com/

###Requirements


#### For development
Python 3.7.5
Pipenv

#### For deployment
heroku


###Setup
1. Create a virtual shell: `$ pipenv shell`
2. Copy over .env file: `$ cp .env.example .env`
3. Install dependencies `$ pipenv install -r requirements.txt`
4. Launch a server: `$ gunicorn wsgi:app` 



#### Github
1. Settings -> Developer Settings
2. OAuth Apps
3. New OAuth App
4. Create the name of your application, Homepage URL, description, and callback url (the resulting deployed application url + /github-callback)
5. Set GITHUB_CLIENT_ID and GITHUB_CLIENT_SECRET in your .env file


###Deploy instructions (For Heroku)
1. Create a new heroku app: `$ heroku create`
2. In Heroku console, add postgres add on (alternatively, from command line: `$ heroku addons:create heroku-postgresql:hobby-dev --app app_name`
3. Push your latest to heroku `$ git push heroku main`
4. To set env vars, run `$ python heroku-config.py`. This will copy your .env file and set individual one-line env vars to heroku.
5. Update individual local dev values for production/staging values using `$ heroku config:set ENV_VAR:VALUE`
6. Set up database by running:
```
heroku run python
(in Python shell)
from app.main import Base

Base.metadata.create_all(bind=engine)
exit()
```
7. Reload application, ensuring that all values are set properly for GITHUB_ID, GITHUB_SECRET, SECRET_KEY, and correct callback and homepage urls for the OAuth application in Github.
8. Login and fork the repo!

###Updates coming
1. Current feature/clean-up branch has some code reorganization, with tests and make tasks to come(such as for the DB creation setup above, and initial application setup)