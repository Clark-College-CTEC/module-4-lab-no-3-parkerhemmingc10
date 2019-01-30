# Lab No. 3
# CTEC 121
# Parker Hemming

from graphics import *

def snowman():
    # create the graphics window
    win = GraphWin('Lab 3 - Snowman',800,800)
    win.setCoords(0,0,4,4)
    
    # your code to draw the snowman goes here
    # draw three circles for the body
    # name the three circles circle1, circle2 and circle3
    circle1 = Circle(Point(2,1),.8)
    circle1.draw(win)
    circle2 = Circle(Point(2,2.3),.5)
    circle2.draw(win)
    circle3 = Circle(Point(2,3.1),.3)
    circle3.draw(win)





    # draw two eyes on the top circle
    # name the two eyes using variables eye1 and eye2
    eye1 = Circle(Point(1.9,3.15),.05)
    eye1.draw(win)
    eye2 = Circle(Point(2.1,3.15),.05)
    eye2.draw(win)





    # draw a nose using the polygon method and make it orange
    # name the nose using the variable nose
    nose = Polygon(Point(1.97,3.1),Point(2.03,3.1),Point(2.1, 3))
    nose.setFill("orange")
    nose.draw(win)


    # draw a hat using a rectangle and fill it with black
    # name the hat using the variable hat
    hat = Rectangle(Point(1.8,3.7),Point(2.2,3.33))
    hat.setFill("black")
    hat.draw(win)




    # draw a line to represent the rim of the hat using a line
    # name the line using the variable hatline
    hatLine = Line(Point(1.5,3.33),Point(2.5,3.33))
    hatLine.draw(win)

    # arms
    arm1 = Line(Point(1.5,2.3),Point(1,2.6))
    arm1.draw(win)
    arm2 = Line(Point(2.5,2.3),Point(3,2.6))
    arm2.draw(win)

    # buttons
    button1 = Circle(Point(2,2.1),.05)
    button1.setFill("black")
    button1.draw(win)
    button2 = button1.clone()
    button2.move(0,.2)
    button2.draw(win)
    button3 = button2.clone()
    button3.move(0,.2)
    button3.draw(win)



    # close the program
    input('Press enter to quit the program ')
    # close the graphics window
    win.close()


# Call the snowman() function to start the program
snowman()