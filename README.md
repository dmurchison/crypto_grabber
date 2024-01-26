# Make API calls for crypto currency information

## This can be used as a tool for users to get a FastAPI backend built and actually start making some ASYNC API calls to get crypto currency information

* Clone repo
  * `$ git clone <repo>`

* Build docker image
  * `$ docker build -t app_name_dock:latest .`

* Build and run a docker container from the newly created image
  * `$ docker run --name app_name_cont -p 8080:8080 app_name_dock:latest`

* Visit the localhost server /docs and start making some requests!
  * `http://localhost:8080/docs`

## To stop the container

* This will stop the container but not remove it
  * `$ docker stop app_name_cont`
* This will remove the container
  * `$ docker rm app_name_cont`
* This will remove the image
  * `$ docker rmi app_name_dock:latest`
