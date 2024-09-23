# Chatbot with Chainlit, OpenAI, and Traefik

## Overview

This project sets up a Python chatbot application using Chainlit and OpenAI. Traefik is used as a reverse proxy to route traffic to the chatbot. The project can be started easily with Docker Compose, and the chatbot can be accessed via `http://chatbot.localhost`.

## Note

I was unable to configure **path-based routing** (i.e., `http://localhost:8080/chatbot`). Instead, I configured routing through a **hostname** (`http://chatbot.localhost`). This setup works successfully and allows access to the chatbot, but the path-based route could not be achieved. Details on limitations can be seen below.

## Technologies Used
- **Docker Compose**: For managing the services.
- **Traefik**: As a reverse proxy for routing traffic to the chatbot.
- **Chainlit**: The framework for the chatbot's UI.
- **Python**: For the chatbot application, utilizing Python 3.11.
- **OpenAI**: For natural language processing.

## Project Setup and Running

### 1. Prerequisites
- Installation of **Docker** in my local machine.
- An **OpenAI API Key** generation

### 2. Set Up Environment Variables

Created a `.env` file in the root directory of the project and added the following:

```bash
OPENAI_API_KEY=<your-openai-api-key>
```

This key is used by the Python application to interact with the OpenAI API.

### 3. Running the Project

Once I finished setting up the environment variables, I built and ran the project using Docker Compose. I ran the following commands in my terminal

```bash
docker-compose up --build -d
```

This will:
- Build the chatbot application.
- Start the Traefik reverse proxy.
- Set up the routing to access the chatbot.

### 4. Accessing the Application

The chatbot can be accessed by navigating to:

```bash
http://chatbot.localhost
```


## Limitations

During the development of this project, I encountered an issue while trying to set up **path-based routing** (i.e., accessing the chatbot via `http://localhost:8080/chatbot`). 

Despite various attempts and reviewing Traefik's documentation, I was unable to get the chatbot to work with the desired path-based routing. However, I was successful in configuring the hostname-based routing using `chatbot.localhost`, which is working correctly and allows access to the chatbot.

Port 8080 Conflict: On my system, Docker and WSL (Windows Subsystem for Linux) were using port 8080 locally, which was causing conflicts when attempting to run the application on the same port. 



### What I Tried:
- **PathPrefix Rule**: Attempted to configure routing via the path using Traefik’s `PathPrefix('/chatbot')` rule, but could not get it to work.

- **Shut down conflicting services**: Attempted to stop the services, but the whole container stopped working.

Despite these efforts, the application currently only works via the hostname `chatbot.localhost`.

## Conclusion

The chatbot is fully functional and accessible via `http://chatbot.localhost`. While path-based routing could not be achieved, the project successfully uses Traefik as a reverse proxy, and the setup can easily be expanded or modified in the future.

