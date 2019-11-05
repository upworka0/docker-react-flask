Constant Contact Oauth2 Demo
============================


Configuration
-------------
	- Change the api/.env_sample to .env and set the api credentials in .env file
        CLIENT_ID=XXXXXXXXXXX
        REDIRECT_URI=http://localhost:8888/oauth/redirect
        SECRET=XXXXXXXXXXX


### Important commands

Build and run :: `docker-compose up --build`

Build and run in the background and view logs for all the instances ::
`docker-compose up --build -d && docker-compose logs --tail=all -f`

Stop instances :: docker-compose down

Stop and Delete all containers :: `docker container stop $(docker container ls -aq) && docker container rm $(docker container ls -aq)`

_Cheers!_