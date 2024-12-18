#!/bin/bash

# Build the Docker image
docker build -t ai-project-backend ./backend

# Deploy the image (replace with your deployment command)
docker run -d -p 5000:5000 ai-project-backend

# (Optional) Deploy the frontend to a web server or static hosting service