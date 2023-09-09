# DogBreedSpotter

## Description

**DogBreedSpotter** is a Python-based image classification project designed to identify and classify dog breeds in images. This project utilizes deep learning models, including convolutional neural networks (CNNs) such as VGG, AlexNet, and ResNet, to accurately detect whether an image contains a dog and, if so, determine the breed.

## Key Features

- Image classification to identify dogs
- Accurate breed classification for dog images
- Utilizes pre-trained deep learning models
- Measures algorithm accuracy and runtime performance
- Supports various dog breeds recognition

## Objective

The primary goal of **DogBreedSpotter** is to provide a reliable tool for dog breed identification, making it useful for various applications, including dog shows, pet registration, and more.

## Usage

1. Clone the repository.
2. Install the required dependencies.
3. Run the project and provide an image for breed identification.
4. Explore the results and accuracy of different deep learning models.

## How to deploy your DogBreedSpotter Flask API?

In order to deploy your Flask API to the cloud, here are the steps that you need to follow:

## 1. Build your Flask application

Obviously, the first step is to create your web application.

Then, when your Flask app is implemented, you can launch it locally using the following command:

```
flask run
```

### NOTE

This is a development server, you cannot use it in a production deployment. In production


## 2. Create VM Instance

![classifier-vm](/static/docs/1.png)

### NOTE

Boot disk size should be at least **30GB**

## 3. Remote SSH config in VS Code

### 1. install Remote - SSH Extension in VS Code

![SSH Extension in VS Code](/static/docs/8.png)

### 2. Click [Ctrl+Shift+p] and search for [Remote-SSH: Open SSH Configuration File...]

![Remote-SSH: Open SSH Configuration File...](/static/docs/9.png)

### 3. Open the configuration file

![Open the configuration file](/static/docs/10.png)

### 4. Edit the configuration file

![Edit the configuration file](/static/docs/11.png)

### NOTE

* **Host**: Your VM name (from GCP Console)
* **HostName**: Your VM External IP Address (from GCP Console)
* **User**: The username you want to use to SSH to this VM
* **IdentityFile**: The path to your IdentityFile

### 5. IdentityFile (How to make it)

```
mkdir google_compute_engine
```

```
cd google_compute_engine
```

```
ssh-keygen -t rsa -f remote-ssh-demo -C omarkhalil -b 2048
```

### 6. Add the path to the IdentityFile to your Configuration File then

```
cd google_compute_engine
```

```
cat remote-ssh-demo.pub
```

### 7. Add it to your VM on GCP

* Copy the content of [remote-ssh-demo.pub]
* Open GCP Console
* Go to Compute Engine Instances
* Click on your instance (in our case **classifier-vm**)
* Click on **Edit**
* Scroll down **to SSH Keys**
* Click on **ADD ITEM**
* Paste the content you copied from **remote-ssh-demo.pub** into **SSH Key 1**
  
### 8. Connect to your VM Instance

![Connect to your VM Instance](/static/docs/9.png)

* Click [Ctrl+Shift+p]
* Click on Connect to Host
* Choose classifier-vm

![Choose classifier-vm](/static/docs/12.png)

### Wait Until conniction is stablished.

## 2. Clone the repository

```
git clone https://github.com/OmarKhalil10/DogBreedSpotter.git
```

## 3. Update the system

It is always a good idea to update before trying to install a new package. Run the commands below:

```
sudo apt-get update
```

Upgrade the dependencies using the command:

```
sudo apt upgrade
```

## 4. Install pip3

If Python 3 has already been installed on the system, execute the command below to install pip3:

```
sudo apt-get -y install python3-pip
```

Verification (Verify your installation)
 
To verify the installation, run the following command to cross check the version number:

```
pip3 --version
```

## 5. Install virtualenv

```
pip install --upgrade pip virtualenv
```

Then make virtualvenv

```
python -m virtualenv venv
```

Then you will need to activate the virtaual env

```
source venv/bin/activate  
```

After that you should install dependencies using the command

```
pip install -r requirements.txt
```

## 6. Run your Flask App

```
set FLASK_APP='app.py'
flask run --reload
```

Ensure that it works correctly and close it

## 7. Set up GCP account, project, etc.

```
export MY_EMAIL_ADDRESS=omar@bamboogeeks.com
export MY_PROJECT_ID=landmark-classifier
```

## 8. Set up GCP account, project, etc.

```
gcloud config set account $MY_EMAIL_ADDRESS
gcloud auth login $MY_EMAIL_ADDRESS
gcloud config set project $MY_PROJECT_ID
```

## 9. Build a Docker image of the Flask application

Create the Dockerfile

```
# Use Python37
FROM python:3.7

## Step 1:
# Create a working directory
WORKDIR /app

## Step 2:
# Copy source code to working directory
COPY app.py requirements.txt /app/
COPY templates /app/templates/
COPY static /app/static/
COPY uploads /app/uploads/
COPY ./imagenet-dictionary /app/imagenet-dictionary/

## Step 3:
# Install packages from requirements.txt
RUN pip install -r requirements.txt && \
    rm /app/requirements.txt

## Step 4:
# Expose port 8080
EXPOSE 8080

# Run app.py at container launch
CMD ["python", "app.py"]
```

## 10. Install Docker on your new Google Compute Engine Machine:
# Login as super user

```
sudo -s
```

Run the following command to install docker

```
sudo apt-get install docker.io
```

When Docker is ready! Test docker

```
docker ps
```

### NOTE:

We shall build the Docker image and push it to Container Registry on GCP. The service name is defined as dogbreedspotter with tag v1

```
docker login
```

```
sudo bash run_docker.sh
```

If you face a problem with the size of the disk **no space left**
Check **Disk Usage**:

Use the df -h command to check the current disk usage on your instance. This command will show you the disk space usage for each mounted filesystem.

```
df -h
```

Identify the filesystem with limited space, and take appropriate action to free up space on that filesystem.

### Resize the Disk

If you've determined that you need more disk space for your Compute Engine instance, you can resize the root disk. Here are the general steps:


### Stop the Compute Engine instance:

```
sudo poweroff 
```

### NOTE 

If you are logged out you could srart the instance again from the console after increasing the disk space


* In the Google Cloud Console, navigate to "Compute Engine" > "Disks."
* Select the disk attached to your instance.
* Click "Edit" and increase the size of the disk as needed.
* Start the Compute Engine instance:

If You want to start the Compute Engine instance from your terminal

```
sudo poweron
```

## 11. Build Docker on your local machine

```
docker build -t gcr.io/$MY_PROJECT_ID/dogbreedspotter:v6 -f Dockerfile .
```

## 12. Push the Docker image to Container Registry 

```
docker push gcr.io/$MY_PROJECT_ID/dogbreedspotter:v6
```

### Container Registry Repository

![Container Registry Repository](/static/docs/3.png)

### Docker image

![Docker image](/static/docs/4.png)

### Docker image details

![Docker image details](/static/docs/5.png)

## 13. Deploy a Docker image on Cloud Run

```
gcloud run deploy dog-breed-spotter \
 --image gcr.io/$MY_PROJECT_ID/dogbreedspotter:v6 \
 --region europe-west6 \
 --platform managed \
 --memory 8Gi \
 --cpu 2 \
 --max-instances 25
```

### Cloud Run revision for dogbreedspotter

![Cloud Run](/static/docs/6.png)


## 14. Use the gcloud run revisions list command to list all revisions of your Cloud Run service. Replace <SERVICE_NAME> with the name of your service.

```
gcloud run revisions list --platform managed --region europe-west6 --service dog-breed-spotter --format="value(name)" | sort
```

## 15. Use the gcloud run revisions delete command to delete each of the old revisions. Replace <REVISION_NAME> with the name of each revision you want to delete. [If Any!]

```
gcloud run revisions delete <REVISION_NAME> --platform managed --region europe-west6 --quiet
```

### NOTE
You can run this command for each old revision you copied in the previos step

## 16. Show the description of a specific revision in Google Cloud Run

```
gcloud run revisions describe dog-breed-spotter-00019-5s2 \
  --platform managed \
  --region europe-west6 \
```

## 17. Check the Flask application on Cloud Run

```
https://dog-breed-spotter-t6mbhrffxa-oa.a.run.app
```

Or you send HTTPS requests to the Cloud Run instance for testing

```
python request_main_v6.py
```

## The response can be found from the log on dog-breed-spotter-00019-5s2 instance on Cloud Run.

![dog-breed-spotter-00019-5s2 logs](/static/docs/7.png)

## Contributions

Contributions and enhancements to **DogBreedSpotter** are welcome! Feel free to fork the repository, make improvements, and submit pull requests.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/OmarKhalil10/DogBreedSpotter/blob/main/LICENSE) file for details.

## Authors

- [Omar Khalil]

## Contact

If you have any questions or suggestions, please feel free to [contact me](mailto:omar.khalil498@gmail.com).
