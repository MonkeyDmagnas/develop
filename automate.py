import subprocess
import os
import docker
import git

# Define the Docker image name and tag
image_name = "statiCI"
image_tag = "v1"

# Define the Docker Hub username
docker_hub_username = "monkeydmagnas007"

# Define the Dockerfile path
dockerfile_path = "./Dockerfile"

# Define the Git repository path
git_repo_path = "https://github.com/MonkeyDmagnas/develop.git"

# Load the Docker Hub password from a secret
def load_secret():
    try:
        with open("docker_hub_password.txt", "r") as f:
            docker_hub_password = f.read().strip()
        return docker_hub_password
    except FileNotFoundError:
        print("Error: Docker Hub password secret not found!")
        return None

# Build the Docker image
def build_image():
    try:
        print("Building Docker image...")
        subprocess.run(["docker", "build", "-t", f"{image_name}:{image_tag}", "."], check=True)
        print("Docker image built successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error building Docker image: {e}")

# Login to Docker Hub using a secret
def login_to_docker_hub(docker_hub_password):
    try:
        print("Logging in to Docker Hub...")
        client = docker.from_env()
        client.login(username=docker_hub_username, password=docker_hub_password)
        print("Logged in to Docker Hub successfully!")
    except docker.errors.ImageNotFound as e:
        print(f"Error logging in to Docker Hub: {e}")

# Push the Docker image to Docker Hub
def push_image():
    try:
        print("Pushing Docker image to Docker Hub...")
        subprocess.run(["docker", "tag", f"{image_name}:{image_tag}", f"{docker_hub_username}/{image_name}:{image_tag}"], check=True)
        subprocess.run(["docker", "push", f"{docker_hub_username}/{image_name}:{image_tag}"], check=True)
        print("Docker image pushed to Docker Hub successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error pushing Docker image to Docker Hub: {e}")

# Clone the Git repository
def clone_git_repo():
    try:
        print("Cloning Git repository...")
        subprocess.run(["git", "clone", git_repo_path], check=True)
        print("Git repository cloned successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error cloning Git repository: {e}")

# Pull the latest changes from the Git repository
def pull_latest_changes():
    try:
        print("Pulling latest changes from Git repository...")
        subprocess.run(["git", "pull", "origin", "main"], check=True)
        print("Latest changes pulled successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error pulling latest changes: {e}")

# Main function
def main():
    docker_hub_password = load_secret()
    if docker_hub_password:
        clone_git_repo()
        pull_latest_changes()
        build_image()
        login_to_docker_hub(docker_hub_password)
        push_image()

if __name__ == "__main__":
    main()
