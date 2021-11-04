# Django template

<!-- TOC -->
1. [Overview](#overview)
2. [Running locally](#running-locally)
    1. [Running with Docker](#running-with-docker)
        1. [Build the Docker image](#build-the-docker-image)
        2. [Launch the Docker container](#launch-the-docker-container)
    2. [Running without Docker](#running-without-docker)
3. [Deploying to AWS ECS](#deploying-to-aws-ecs)
4. [Setting up Continuous Delivery (CD)](#setting-up-continuous-delivery-cd)
<!-- /TOC -->

## Overview

A Pyclops template for running a Django project on ECS. 

**Features:**

* All infrastructure is mastered in CloudFormation
* Working Dockerfile for production and development
* Continuous delivery with Code Pipelines
* Authentication with JWT

## Running locally

### Running with Docker

#### Build the Docker image

Before the Docker container can be run, the Docker image must be built. From the root of the repo, execute the following command:

```
./docker/build.sh
```

For a production-like build, set the `STAGE` environment variable to `production`:

```
STAGE=production ./docker/build.sh
```

#### Launch the Docker container

Once the image has been built, a Docker container can be launched with the following:

```
./docker/run.sh
```

For a production-like run, once again, set the `STAGE` environment variable to `production`:

```
STAGE=production ./docker/run.sh
```

### Running without Docker

*Note: you probably want to run the below commands within a [Python virtual environment](https://github.com/pyenv/pyenv)*

To run without Docker, change into the `app/` directory and run the following:

```
cd app
pip install -r requirements.txt
./run.sh python ./manage.py runserver
```


To run with gunicorn, set the `STAGE` environment variable to `production`:

```
STAGE=production ./run.sh
```

## Deploying to AWS ECS

The following instructions depend on the pyclops CLI. Install pyclops with:
```
pip install pyclops
```

To deploy to AWS, first create an ECR docker repository:
```
pyclops aws ecr create-repo --repo-name pyclops/orchards-nutrition
```

If successful, the above command would have printed out the URI for the newly created repository. The URI would look something like `{accountId}.dkr.ecr.{region}.amazonaws.com/pyclops/orchards-nutrition`. Before moving forward, set the `ecr_repo` variable in your `params.py` file (located at the root of your generated project) to the printed out URI.

Now that we have a repository for our Docker image, we need to build the image and push it up to the repository.
```
pyclops aws ecr build --dockerfile docker/Dockerfile.prod --repository pyclops/orchards-nutrition --tag latest
pyclops aws ecr push --repository pyclops/orchards-nutrition --tag latest
```

You are now all set to build and deploy the project to AWS (ensure you have copied the ECR repo ARN into your `params.py` file as instructed above). In the base directry of your project, run the following commands:
```
pyclops aws cloudformation build --templates-dir cfn/service --params-file params.py --stage staging
pyclops aws cloudformation deploy --stack-name orchards-nutrition --template-file build/cfn/cfn.template.yml --template-config build/cfn/service.config.json --capabilities CAPABILITY_IAM
```

##  Setting up Continuous Delivery (CD)

*Coming soon*