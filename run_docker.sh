#! /bin/bash

## Complete the following steps to get Docker running locally

# Set version tag
version="v6"

# Step 1:
# Build image and add a descriptive tag with version
docker build -t dogbreedspotter:$version .

# Step 2:
# List docker images
docker image ls

# Step 3:
# Run flask app with version tag
docker run -it -p 8080:8080 dogbreedspotter:$version