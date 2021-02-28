# DeskFocus
![](https://github.com/intuition2021/DeskFocus/blob/gh-pages/images/DeskFocus.gif)

An application to help students focus during study sessions while studying remotely

This application is tested to work with MacO. 

The Website Blocker feature for Windows version requires a minor change in the host path for it to work. 

After downloading the application, run

`sudo python main.py`

Next, enter the same password you use to log into your computer. 
(This step is nessassary as the app needs to gain permission from the computer to block websites.)

:film_strip: Check out our project video [here](https://www.youtube.com/watch?v=Ky1dltMkWzU&feature=emb_title)!

:information_source:  [Devpost Link](https://devpost.com/software/desktranslate) 

## Inspiration
During the circuit breaker period many of us found ourselves stuck at home with lots of work to do but no motivation to do it. We often find ourselves distracted with social media, unable to sit down and work for long periods. DeskFocus can help improve productivity with the tried and tested Pomodoro method, as well as a few other features to keep you off the internet and on task.

## What it does
* DeskFocus allows students to increase their productivity and get more work done. This multipurpose app is designed to build long-term and sustainable motivation. 
* It includes features such as a Pomodoro Timer, a built-in dictionary and a web blocker.
* What makes our application so special is that many applications in the market are specifically built with only one of these functions and cannot be used in other ways, meaning you’d have to find multiple different applications solely to get more productive. Some would argue that this is inherently counterproductive because of that time wasted. This one app allows you those functions right on the spot, with absolute ease.  

## How we built it
It was built in python using Pyqt5 to develop the graphical user interface (GUI). PyDictionary was used to gather the definitions offline. 

## Challenges we ran into
* Time constraints since this hackathon takes place in the exam period. Not much time for ideation prior to the hackathon
* Unfamiliarity with python threading resulted in a lot of time wasted trying to make it work
* Teammate had less experience with the code, more time was needed to try and guide them 

## Accomplishments that we're proud of
* Despite the lack of sleep and the rush for time we were able to at least produce a working finished product, and managed to remove some of the more serious bugs with the program
* Creating a decent looking logo

## What we learned
* Having a clearer concept and a more refined target group would have been more important for creating a meaningful product. Nonetheless it was a good coding exercise implementing the various features of the application.
* It is also important to discuss and prioritize certain features that would be more value added given the time crunch, and to focus on polishing existing features rather than adding new ones

## What's next for DeskFocus
* Simple to do list implementation to help the user keep track of tasks, and a function of users to share their task lists with each other to keep each other accountable add some friendly competition to keep them motivated
* Peer to peer study sessions with a chat function between peers that restricts the messages sent to only work related messages so that the users can encourage / peer pressure each other to stay focused despite safe distancing

# Credits
Website blocker code was adapted from Sajag Chauhan:
https://github.com/sajag1999/Website-Blocker-Project
