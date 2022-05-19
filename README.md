# E2E_Final_project
This is the Final project task for the course: 22SM1 End-to-end Sample ML project
## Information about source data and some statistics (maybe plots, tables, images)
We have data from Yandex.Realty classified https://realty.yandex.ru containing real estate listings for apartments in St. Petersburg and Leningrad Oblast from 2016 till the middle of August 2018. Accurate price prediction can help to find fraudsters automatically and help Yandex.Realty users to make better decisions when buying and selling real estate. The data was cleaned and processed.
## Information about your model, choosen framework, hyperparams) 
For this project I've created two models. The first one is minimalistic and contains only parameters with the highest correlation to the price. While the second one is a bit more complex. Also, the model types are the ones demonstrating the best performance (MAE, MSE and RMSE)
Since the database is the same the models have some similiarities, here is the description:

**Model_1** - Decision Tree:
 - Rooms -- integer
 - Area -- float
 - Renovation -- integer
 
**Model_2** - Random Forest:
 - Open_plan -- integer
 - Rooms -- integer
 - Area -- float
 - Renovation -- integer
 - Time_gap -- integer
## How to install instructions and run your app with virtual environment
- You need to create A Virtual Machine based on Ubuntu OS
- Install Python 3
- Install libraries (Flask, Numpy...check Requirements.txt)
- Initialise Git and pull files from the repository
- Run App.py
## Information about Dockerfile and describe it’s content
The Dockerfile is a container with the whole app. It can help you to both run or transfer this app to other devices.
However, the same as GitHub it needs to be installed and activated:
[install docker on ubuntu](https://docs.docker.com/engine/install/ubuntu/) //
[tune the docker on ubuntu](https://docs.docker.com/engine/install/linux-postinstall/)
## How to open the port in your remote VM
First, you have to run the app by any means you prefer. Then make requests using the port:5444 (built in the app)

Request should contain all the parameters or else it will return an Error.

Example: > http://x.x.x.x:5444/predict_price?model=2&open_plan=1&rooms=3&area=25&renovation=1&time_gap=240

x.x.x.x - your VM public IP address

Also, the model should be either 1 - Decision Tree or 2 - Random Forest
## How to run app using docker and which port it uses
  First step is to install docker and use a command to pull the image:

    docker pull melikianstudent/final_project:v.1.6

Then just use **docker run**, it's easy!

    docker run --network host -d melikianstudent/final_project:v.1.6
    OR
    docker run --network host -it melikianstudent/final_project:v.1.6 /bin/bash
    Then: Python3 App.py

    
Now everything is ready and you can make your queries)
