# Project Overview
This project demonstrate how to write restful crud api that persist data, for demo sqllite is used.
CI\CD demonstration - build(Docker) and deploy(k8s) capabilites in to cloud enviornments.

## app
[app]
1. app.py - This file contains the complete app logic but in prod setting this would be splitted into a well defined structure, like model, resources and app creation.
2. config.py - Here all the configurable variable are stored.
3. requirements.py - this file contains all python dependecies.
4.wsgi.py - this module is consumed by guincorn to start the app

[data]
1. only for demo , this file contains sqllite DB.

[tests]
this folder contains all the pytest files to demonstrat testing capabilities.
contains, functional and unit tesing.  

[DockerFile]
This file contains declarative statments to build container.

## env_vars
This file contains all the env variables that should be supplied during deployment.

## k8s
This folder contains files to deploy container and to create service and ingress controller.

## .gitignore
this file contains patterns to be matched while committing file to git repo.

## jenkinsfile
This file contains declarative statments to run jenkins CI\CD pipeline.

## Improvement Areas
1. app restructuring like seggregating logic , models and resources to be in seprate modules.
2. Proper Exception handling needs to be added int he code.
3. Token based authentication needs to be added in all api endpoints calls.
4. Comprehensive test cases needs to be added for both functional and unit test cases
5. In pipeline follwoing steps needs to be added,
    - add, code linting steps (sonarqube project is preferred)
    - add, testing steps to run all functional and unit test cases.
6. Dockerfile can be enhanced further to add more env variables to control build creation.
