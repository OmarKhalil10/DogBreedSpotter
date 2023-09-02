Create VM Instance

Note: Boot disk size should be at least 30GB


Create key


Add key to instance


ssh to this instance



clone the repo



Step 1 - Update system
It is always a good idea to update before trying to install a new package. Run the command below:

sudo apt-get update

Upgrade the upgradable dependencies using the command:

sudo apt upgrade

Step 2 - Install pip3
If Python 3 has already been installed on the system, execute the command below to install pip3:

sudo apt-get -y install python3-pip
Step 3 - Verification
To verify the installation, run the following command to cross check the version number:

pip3 --version


install virtualenv
pip install --upgrade pip virtualenv

make virtualvenv
python -m virtualenv venv

activate the virtaual env
source venv/bin/activate  

install dependencies using the command
pip install -r requirements.txt

Run your flask app

set FLASK_APP='app.py'
flask run --reload

Ensure that it works correctly and close it

Set up GCP account, project, etc.

export MY_EMAIL_ADDRESS=omar@bamboogeeks.com
export MY_PROJECT_ID=landmark-classifier

gcloud config set account $MY_EMAIL_ADDRESS
gcloud auth login $MY_EMAIL_ADDRESS
gcloud config set project $MY_PROJECT_ID


Build a Docker image of the Flask application

Create the Dockerfile

# Install Docker on your new Google Compute Engine Machine:
# Login as super user

sudo -s
# Run the following command to install docker
sudo apt-get install docker.io
# When Docker is ready! Test docker
docker ps

Note: We shall build the Docker image and push it to Container Registry on GCP. The service name is defined as dogbreedspotter with tag v1

# Upload docker locally
docker login

sudo bash run_docker.sh

# If you face a problem with the size of the disk [no space left]
Check Disk Usage:

Use the df -h command to check the current disk usage on your instance. This command will show you the disk space usage for each mounted filesystem.
```
df -h
```
Identify the filesystem with limited space, and take appropriate action to free up space on that filesystem.
# Resize the Disk:

If you've determined that you need more disk space for your Compute Engine instance, you can resize the root disk. Here are the general steps:

a. Stop the Compute Engine instance:

```
sudo poweroff 
```

Note if you are logged out you could srart the instance again from the console after increasing the disk space

b. In the Google Cloud Console, navigate to "Compute Engine" > "Disks."

c. Select the disk attached to your instance.

d. Click "Edit" and increase the size of the disk as needed.

e. Start the Compute Engine instance:

```
sudo poweron
```

# Build Docker on your local machine
docker build -t gcr.io/$MY_PROJECT_ID/dogbreedspotter:v1 -f Dockerfile .
# Push the Docker image to Container Registry 
docker push gcr.io/$MY_PROJECT_ID/dogbreedspotter:v1
