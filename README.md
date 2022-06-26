#### HELLO YOU

This repository contains a project in which the goal is to analyse a dataset about books and their features,and at the end to build a machine learning model to predict the rating of a book

# Requirement

## The jupyter notebook 
The contains all the installation and result of this work so you just need to have jupyter installed or ananconda to open it.
Make sure the file Books.csv and and the notebook is in the same directory.

## Docker application

The project comes with a docker application writen in flask, the only operational endpoint at this time is /training​/train​/model​/predic endPoint which 
makes prediction base of features of a book i have chosen.(number of pages, author, number of review, publisher, number of rating).

To use the API install ``docker desktop` in your machine clone this project with the command git clone https://github.com/WarrenLata/Python_Lab.
You will need to have git install and terminal (WSL2 for example)

next:`cd Python_Lab`
and run the command `docker-compose up -d`

This command will build the application and after the build is done you can access the api in http://localhost:8002/ on your machine.

Don't hesitate to write me at latawarren@gmail.com if you have any remark of suggestion on this work.

Good bye




