# Container image that runs your code
FROM python:3.10

# WORKDIR
WORKDIR /app

# Copies your code file from your action repository to the filesystem path `/` of the container
COPY . /app

RUN pip install -r requirements.txt

# Code file to execute when the docker container starts up (`entrypoint.sh`)
ENTRYPOINT ["python", "./hello_world.py"]

