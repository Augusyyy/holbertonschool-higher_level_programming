# Start with the Alpine base image
FROM alpine:latest

# Install curl package
RUN apk add --no-cache curl

# Create a directory for the app
RUN mkdir -p /app

# Copy the config.txt file to /app directory
COPY config.txt /app/config.txt

# Set the working directory
WORKDIR /app

# Specify the volume
VOLUME /data

# Specify the command to run when the container starts
CMD ["sh"]
