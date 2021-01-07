:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

#  Platform Guy 
## CS 110 Final Project
###  Semester 1, 2020 
### [Assignment Description](https://drive.google.com/open?id=1HLIk-539N9KiAAG1224NWpFyEl4RsPVBwtBZ9KbjicE)

 [https://github.com/bucs110/final-project-fall20-team1.git](#) 

<< [link to demo presentation slides](#) >>

### Team:  Team 1 
#### Quentin Zayats, Emanuel Francisco, Mark Lanning

***

## Project Description
It is a basic side scrolling platorming, in which the character in controlled by the user and needs to avoid the enemies in order to get to the end of the level.

***    

## User Interface Design
* << A wireframe or drawing of the user interface concept along with a short description of the interface. You should have one for each screen in your program. >>
    * For example, if your program has a start screen, game screen, and game over screen, you should include a wireframe / screenshot / drawing of each one and a short description of the components

       * ![Start Screen](https://github.com/bucs110/final-project-fall20-team1/blob/master/assets/Start%20Screen.png)  
       
       **Start Screen** This is the screen you will see when you start the game
       * ![Game Screen](https://github.com/bucs110/final-project-fall20-team1/blob/master/assets/gamescreen.png) 
      
       **Game Screen** This is the screen you will see when you are playing the game
       * ![Game Over Screen](https://github.com/bucs110/final-project-fall20-team1/blob/master/assets/gameoverscreen.png)
       
       **Game Over Screen** This is the screen you will see when you lose and the game is over
       * ![Win Screen](https://github.com/bucs110/final-project-fall20-team1/blob/master/assets/winscreen.png)
       
       **Win Screen** This is the screen you will see if you beat the game
       
***        

## Program Design
* Non-Standard libraries
    * << You should have a list of any additional libraries or modules used (pygame, request) beyond non-standard python. >>
    * For each additional module you should include
        * url for the module documentation
        * a short description of the module
* Class Interface Design

  ![class diagram](https://github.com/bucs110/final-project-fall20-team1/blob/master/assets/ClassDiagram.jpg)
    
* Classes *
**menu()**
    -start() starts the game
    -quit() ends the game
    -pause() pauses the program
 
 **platform()**
   -position(x,y) keeps track of the position of platforms 
    -imagefilename() keeps track of image names and assets needed to use
 
 **window()**
    -position(x,y) keeps track or position of screen 
    -moveleft() moves left as character moves
    -moveright() moves right as character moves
 
 **maincharacter()**
    -imagefilename()  keeps track of image names and assets needed to use
    -position(x,y) keeps track of position of main character 
    -moveleft() moves main character to the left
    -moveright() moves main character to the right
    -jump() moves main character up
    -gravity() applies gravity mechanic
    -damage() applies damage mechanic to  maincharacter() 
 
 **enemies()**
    -imagefilename() keeps track of image names and assets needed to use
    -position(x,y) keeps track of position of enemies 
    -moveleft() movies enemies left 
    -moveright() moves enemies right
    -parametercheck() checks if they cross the boundaries at which point switches from moveleft() to moveright()
    -destroyed() enemy is taken out of game if maincharacter() interacts with enemies()

***

## Tasks and Responsibilities
* You must outline the team member roles and who was responsible for each class/method, both individual and collaborative.

### Software Lead - Mark Lanning

<< Worked as integration specialist by... >>

### Front End Specialist - Quentin Zayats

<< Front-end lead conducted significant research on... >>

### Back End Specialist - cEmanuel Francisco 

<< The back end specialist... >>

## Testing
* << Describe your testing strategy for your project. >>
    * << Example >>

* Your ATP

| Step                  | Procedure     | Expected Results  | Actual Results |
| ----------------------|:-------------:| -----------------:| -------------- |
|  1  | Run Counter Program  | GUI window appears with count = 0  |          |
|  2  | click count button  | display changes to count = 1 |                 |
etc...
