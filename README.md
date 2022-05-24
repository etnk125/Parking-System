# Parking System with PI LineNoti dialogflow+chatbot MEVN

## problem

- waste to many time to find car parking place
- don't know how many car parking place left
- forget how long you have parked
- forget your parking spot
 
## feature

- check empty parking place
- notify
- reserve


## author
 part of embedded class
 - this is [demo vdo](https://www.youtube.com/watch?v=iik25wqIuFo)

## raspi

using 
- ir sensor
- led 
- lcd or 7segment

## frontend
using vite/vue - bs5 to build 

- Login page 
- register page
- reservation page

this is parking reservation system , You can reserve via this website

### register

input `email`,`password`,`lineToken`

### login

using `email`,`password`

### reservation

after login press button to reserve and checkout
display remaining slot and your parking number

## backend

using node express and using mongo database
this is [doclink](https://documenter.getpostman.com/view/19700615/UyxbrAUg)


## line notify

- reservation  
- checkout
- routine

## chatbot,web for free parking

- run with flask
- ngrok hosting public ip
- detect intent with dialogflow


# Free Parking System
- access by web app 
- access by line chatbot
  
# VIP Parking System
- access by web app
- notify by line notify
