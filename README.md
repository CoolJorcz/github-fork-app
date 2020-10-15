## Github Fork App

#### Description 
This is a small toy app to utilize a Github OAuth Application to interact with the Github API's POST /repos/{owner}/{repo}/forks endpoint

### Requirements

#### For development
Python 3.7.5
Pipenv

#### For deployment
heroku


### Setup


#### Github
1. Settings -> Developer Settings
2. OAuth Apps
3. New OAuth App
4. Create the name of your application, Homepage URL, description, and callback url (the resulting deployed application url + /github-callback)
5. Set GITHUB_CLIENT_ID and GITHUB_CLIENT_SECRET in your .env file


