# Use an official Nginx image as a base
FROM nginx:stable-alpine3.20

# Set the working directory to /usr/share/nginx/html
WORKDIR /usr/share/nginx/html

# Copy the index.html file into the container
COPY . .

# Expose port 80 for Nginx
EXPOSE 80

# Run Nginx when the container starts
CMD ["nginx", "-g", "daemon off;"]

