.. title: Docker
.. slug: docker
.. date: 2018-08-26 15:42:22 UTC
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Illarion Khlestov


Based on `this tutorial <https://docs.docker.com/engine/userguide/containers/dockerizing/>`__

.. code-block:: bash

    # list running images
    $ docker ps
    # list all containers
    $ docker ps -a
    # stop the container
    $ docker stop CONTAINER_ID 
    # remove a container
    $ docker rm CONTAINER_ID 
    # list all images
    $ docker images
    # remove image
    $ docker rmi IMAGE_ID 
    
    # create a build from Dockerfile
    $ docker build -t ikhlestov/thenotes-docker .
    # run image and enter to it
    $ docker run -t -i ouruser/sinatra:v2 /bin/bash
    # enter inside running container
    $ docker exec -it CONTAINER_NAME bash
    # attach to already running container
    $ docker start -ai container_name
    
    # run detached image with name
    $ docker run -d -P --name web training/webapp python app.py
    # mount some folder inside docker container on the start
    $ docker run -it -v /path/from:/path/to /bin/bash
    # run again an image
    $ docker run -itd --name=networktest ubuntu
    # run some web image
    # remove the container and its image after exit
    $ docker run -it -d some.uri.amazonaws.com/mxnet:gpu /bin/bash
    $ docker run --rm CONTAINER_NAME
    
    # login to docker on the AWS EC2 service
    $ $(aws ecr get-login --region us-west-2)
    # check the state of container by name
    $ docker inspect web
    # list all networks drivers
    $ docker network ls
    # inspect current sate of network
    $ docker network inspect bridge
    # disconnect a container
    $ docker network disconnect bridge networktest

**Docker compose**

.. code-block:: bash

    $ docker-compose build web
    $ docker-compose up --no-deps -d web
    # run with additional settings file in background(detached)
    $ docker-compose -f docker-compose.yml -f production.yml up -d
    # enter to compose container
    $ docker-compose run CONTAINER_NAME bash
    
**Bash scripts**

.. code-block:: bash

    # stop first running docker instance
    # all runing| second line| container name    | stop container by name
    $ docker ps | sed -n 2p  | awk '{print $NF}' | xargs docker stop
    # stop all running containers
    $ docker ps | awk '{print $NF}' | tail -n +2 | xargs docker stop

