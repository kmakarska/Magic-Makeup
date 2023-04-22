from cmu_graphics import *
from PIL import Image
import os, pathlib

#button class idea inspired by lecture demo on buttons
class Button:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        
    def draw(self):
        drawRect(800, 450, 200, 100, fill='hotPink', border='mediumVioletRed') 
        drawLabel("Next", 900, 500, size=50, fill='mediumVioletRed')

    def checkForPress(self, app, mouseX, mouseY):
        if (mouseX > self.x and mouseX < self.x + self.w and mouseY > self.y and mouseY < self.y + self.h):
            setActiveScreen('name')


def start_openImage(fileName):
    return Image.open(os.path.join(pathlib.Path(__file__).parent,fileName))

def start_onAppStart(app):  
    app.fairyImg = Image.open('images/fairy.png')
    app.bgImg = Image.open('images/bg.png')
    #changing size of image
    newsize = (300, 400)
    app.fairyImg = app.fairyImg.resize(newsize)
    #converting to CMU image type
    app.fairyImg = CMUImage(app.fairyImg)
    app.bgImg = CMUImage(app.bgImg)
    #creating button
    app.myButton = Button(800, 450, 200, 100)

def start_redrawAll(app):
    drawImage(app.bgImg, 0, 0)
    drawImage(app.fairyImg, 80, 300)
    drawOval(900, 400, 900, 600, fill='pink')
    drawRegularPolygon(460, 440, 50, 3, fill='pink')
    drawLabel("Welcome To", 900, 250, size=50, fill='mediumVioletRed')
    drawLabel("MAGIC MAKEUP", 900, 350, size=90, fill='mediumVioletRed', bold=True)
    app.myButton.draw()

def start_onMousePress(app, mouseX, mouseY):
    #button pressing
    app.myButton.checkForPress(app, mouseX, mouseY)


def name_openImage(fileName):
    return Image.open(os.path.join(pathlib.Path(__file__).parent,fileName))

def name_onAppStart(app):  
    app.fairyImg = Image.open('images/fairy2.png')
    app.bgImg = Image.open('images/bg.png')
    #changing size of image
    newsize = (225, 300)
    app.fairyImg = app.fairyImg.resize(newsize)
    #converting to CMU image type
    app.fairyImg = CMUImage(app.fairyImg)
    app.bgImg = CMUImage(app.bgImg)
    app.input = ''
    app.boxPressed = False

def name_redrawAll(app):
    drawImage(app.bgImg, 0, 0)
    drawImage(app.fairyImg, 1200, 100)
    drawOval(950, 150, 400, 200, fill='lavenderBlush')
    drawRegularPolygon(1120, 200, 25, 3, fill='lavenderBlush')
    drawLabel("I'm Pixie, I will be", 960, 130, size=35, fill='mediumVioletRed')
    drawLabel("your teacher!", 950, 180, size=35, fill='mediumVioletRed')
    drawRect(350, 300, 800, 550, fill='pink', border='hotPink', borderWidth=5)   
    name_inputFieldDraw(app)
    drawRect(650, 650, 200, 100, fill='hotPink', border='mediumVioletRed') 
    drawLabel("GO", 750, 700, size=50, fill='mediumVioletRed')

def name_inputFieldDraw(app):
    drawLabel("Enter your name:", 750, 425, size=50, fill='mediumVioletRed')
    drawRect(550, 500, 400, 100, fill='lavenderBlush')
    drawLabel(app.input, 750, 550, size=40)
    if app.boxPressed:
        drawRect(550, 500, 400, 100, fill=None, border='hotPink')

def name_onMousePress(app, mouseX, mouseY):
    #input box
    if mouseX > 550 and mouseX < 950 and mouseY > 500 and mouseY < 600:
        app.boxPressed = True


def name_onKeyPress(app, key):
    if (app.boxPressed):
        if key.isalpha() and key != 'enter' and key != 'tab' and len(app.input) != 15:
            app.input += key
        if key == 'backspace':
            app.input = app.input[:-10]
        if key == 'space':
            app.input = app.input[:-5] + ' '


def main():
    runAppWithScreens(initialScreen='start')
    runApp(width=2000, height=1000)


if __name__ == '__main__':
    main()
