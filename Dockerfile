# Use the official Python 3.9 image from DockerHub
FROM python:3.10.12

# install essentials
RUN apt-get update && apt-get install -y -q --no-install-recommends \
        curl \
        git \
        wget \
        vim \
        nano

# Add user
ARG PUID=1000
ENV PUID ${PUID}
ARG PGID=1001
ENV PGID ${PGID}
ARG APP_USER=app_user
ENV APP_USER ${APP_USER}

RUN groupadd -g ${PGID} ${APP_USER} && \
    useradd -l -u ${PUID} -g ${APP_USER} -m ${APP_USER} && \
    usermod -p "*" ${APP_USER} -s /bin/bash

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install the dependencies
ENV PYHTONUNBUFFERED=1

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the content of the local directory to the working directory
COPY . .

# Expose the port Uvicorn will run on
EXPOSE 8030

# Command to run the application using Uvicorn when the docker is up
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8030"]
