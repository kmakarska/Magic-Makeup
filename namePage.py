from cmu_graphics import *
from PIL import Image
import os, pathlib

def openImage(fileName):
    return Image.open(os.path.join(pathlib.Path(__file__).parent,fileName))

def onAppStart(app):  
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

def redrawAll(app):
    drawImage(app.bgImg, 0, 0)
    drawImage(app.fairyImg, 1200, 100)
    drawOval(950, 150, 400, 200, fill='lavenderBlush')
    drawRegularPolygon(1120, 200, 25, 3, fill='lavenderBlush')
    drawLabel("I'm Pixie, I will be", 960, 130, size=35, fill='mediumVioletRed')
    drawLabel("your teacher!", 950, 180, size=35, fill='mediumVioletRed')
    drawRect(350, 300, 800, 550, fill='pink', border='hotPink', borderWidth=5)   
    inputFieldDraw(app)
    drawRect(650, 650, 200, 100, fill='hotPink', border='mediumVioletRed') 
    drawLabel("GO", 750, 700, size=50, fill='mediumVioletRed')

def inputFieldDraw(app):
    drawLabel("Enter your name:", 750, 425, size=50, fill='mediumVioletRed')
    drawRect(550, 500, 400, 100, fill='lavenderBlush')
    drawLabel(app.input, 750, 550, size=40)
    if app.boxPressed:
        drawRect(550, 500, 400, 100, fill=None, border='hotPink')

def onMousePress(app, mouseX, mouseY):
    if mouseX > 550 and mouseX < 950 and mouseY > 500 and mouseY < 600:
        app.boxPressed = True

def onKeyPress(app, key):
    if (app.boxPressed):
        if key.isalpha() and key != 'enter' and key != 'tab' and len(app.input) != 10:
            app.input += key
        if key == 'backspace':
            app.input = app.input[:-10]
        if key == 'space':
            app.input = app.input[:-5] + ' '


def main():
    runApp(width=2000, height=1000)

if __name__ == '__main__':
    main()