# How to Run
To start this web streamlt application, first you will have to git clone this github repository into your local computer.

## clone repository
To achieve this you will have to either download it using the `git clone` command below:
```
    git clone https://github.com/TechTeam-inf2021/data_analysis_dev_app.git
```
or can download it manually here:

![image](https://github.com/TechTeam-inf2021/data_analysis_dev_app/assets/166173503/5f746267-8e2d-4b94-9b9c-b142dc71029e)


## Run the streamlit app using docker:
### Install Docker Desktop:
#### Windows 10/11 and macOS
If you haven't installed Docker Desktop, you can download it from the [Docker website](https://docs.docker.com/desktop/install/windows-install/).

##### Start Docker Desktop app
First you will need to open the Docker Desktop app and ensure it runs. 

#### Linux
##### Start Docker Daemon:
Open a terminal and run:
```
    sudo systemctl start docker
```
##### Enable Docker to Start at Boot (Optional):

To ensure Docker starts on boot, run:
```
    sudo systemctl enable docker
```
##### Verify Docker Daemon it runs
You can verify it runs by typing in your terminal:
```
docker info
```
if its not running you will get an error.

### Build docker image container
To build the docker image container you will have to be inside your app folder and then type on the terminal:
```
docker build -t data_analysis_dev_app .
```
and Wait for it to build.

### run the Docker Container
To run the docker container you will have to enter the following command on the terminal:
```
docker run -p 8501:8501 data_analysis_dev_app
```

### Open your app in your browser
To run your app in your browser will have to enter the following URL:
```
127.0.0.1:8501
```
and NOT the Network - External URL that the docker is showing.


## Run the streamlit app using a python virtual environment (instead of docker)

### Verify Python installation
First, you would need to have installed python3+ version into your system and can check your python version with the command below:
```
    python -V
```
After you successfully installed python you would need to create and activate a virtual environment to run the streamlit application.

### Create venv
To create a new virtual environment you will have to run the command below into your command prompt or terminal:
```
    python -m venv virtual_environment_name
```
### Activate venv
The python virtual environment activation command is different for every system: 
#### Ubuntu debian command
For linux / debian terminal:
```
    source ./virtual_environment_name/bin/activate
```
#### Windows 10/11 command
For windows command prompt:
```
    .\virtual_environment_name\Scipts\activate
```
