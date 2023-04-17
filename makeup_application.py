from cmu_graphics import *
from PIL import Image
import os, pathlib

def openImage(fileName):
    return Image.open(os.path.join(pathlib.Path(__file__).parent,fileName))

def onAppStart(app):
    init(app) 
    colorInit(app)
    openingImages(app)  
    resizeFaceImages(app)
    convertImgType(app)

def init(app):
    app.prevMousePositions = []
    app.eyelinerPressed = False
    app.eyelinerColor = 'black'

def colorInit(app):
    app.blackE = False
    app.brownE = False
    app.pinkE = False
    app.purpleE = False
    app.greenE = False
    app.blueE = False

def openingImages(app):
    app.defaultFace = Image.open('images/defaultFace.png')
    app.eyeliner = Image.open('images/eyeliner.png')
    app.eyelinerFace = Image.open('images/eyelinerFace.jpg')

def resizeFaceImages(app):
    newsize = (700, 700)
    app.defaultFace = app.defaultFace.resize(newsize)
    app.eyelinerFace = app.eyelinerFace.resize(newsize)

def convertImgType(app):
    app.defaultFace = CMUImage(app.defaultFace)
    app.eyeliner = CMUImage(app.eyeliner)
    app.eyelinerFace = CMUImage(app.eyelinerFace)

def redrawAll(app):
    drawImage(app.defaultFace, 400, -5)
    drawRect(0, 680, 2000, 300, fill='violet')
    eyelinerPressed(app)
    
def eyelinerPressed(app):
    if (app.eyelinerPressed):
        drawImage(app.eyelinerFace, 400, 0)
        drawRect(0, 680, 2000, 300, fill='violet')
        drawRect(650, 700, 230, 200, fill=None, border='black')
        eyelinerColors(app)
    drawImage(app.eyeliner, 650, 700)
    for pos in app.prevMousePositions:
        drawCircle(pos[0], pos[1], 3, fill=app.eyelinerColor)

def eyelinerColors(app):
    drawLabel("Colors", 1300, 80, size=30)
    #black
    drawRect(1225, 120, 70, 70, fill='black')
    if app.blackE:
        drawRect(1220, 115, 80, 80, fill=None, border='yellow', borderWidth=5)
    #brown
    drawRect(1310, 120, 70, 70, fill='saddleBrown')
    if app.brownE:
        drawRect(1305, 115, 80, 80, fill=None, border='yellow', borderWidth=5)
    #pink
    drawRect(1225, 200, 70, 70, fill='deepPink')
    if app.pinkE:
        drawRect(1220, 195, 80, 80, fill=None, border='yellow', borderWidth=5)
    #purple
    drawRect(1310, 200, 70, 70, fill='darkViolet')
    if app.purpleE:
        drawRect(1305, 195, 80, 80, fill=None, border='yellow', borderWidth=5)
    #green
    drawRect(1225, 280, 70, 70, fill='limeGreen')
    if app.greenE:
        drawRect(1220, 275, 80, 80, fill=None, border='yellow', borderWidth=5)
    #blue
    drawRect(1310, 280, 70, 70, fill='royalBlue')
    if app.blueE:
        drawRect(1305, 275, 80, 80, fill=None, border='yellow', borderWidth=5)


      
def onMouseDrag(app, mouseX, mouseY):
    app.prevMousePositions.append((mouseX, mouseY))

def onMousePress(app, mouseX, mouseY):
    #eyeliner pressed
    if (mouseX >= 650 and mouseX <= 850 and mouseY >= 700 and mouseY <= 900):
        app.eyelinerPressed = True
    #black pressed
    if (mouseX > 1225 and mouseX < 1295 and mouseY > 120 and mouseY < 190):
        app.blackE = True
        app.brownE = False
        app.pinkE = False
        app.purpleE = False
        app.greenE = False
        app.blueE = False
        app.eyelinerColor = 'black'
    #brown pressed
    if (mouseX > 1310 and mouseX < 1380 and mouseY > 120 and mouseY < 190):
        app.brownE = True
        app.blackE = False
        app.pinkE = False
        app.purpleE = False
        app.greenE = False
        app.blueE = False
        app.eyelinerColor = 'saddleBrown'
    #pink pressed
    if (mouseX > 1225 and mouseX < 1295 and mouseY > 200 and mouseY < 270):
        app.pinkE = True
        app.brownE = False
        app.blackE = False
        app.purpleE = False
        app.greenE = False
        app.blueE = False
        app.eyelinerColor = 'deepPink'
    #purple pressed
    if (mouseX > 1310 and mouseX < 1380 and mouseY > 200 and mouseY < 270):
        app.purpleE = True
        app.pinkE = False
        app.brownE = False
        app.blackE = False
        app.greenE = False
        app.blueE = False
        app.eyelinerColor = 'darkViolet'
    #green pressed
    if (mouseX > 1225 and mouseX < 1295 and mouseY > 280 and mouseY < 350):
        app.greenE = True
        app.pinkE = False
        app.brownE = False
        app.blackE = False
        app.purpleE = False
        app.blueE = False
        app.eyelinerColor = 'limeGreen'
    #blue pressed
    if (mouseX > 1310 and mouseX < 1380 and mouseY > 280 and mouseY < 350):
        app.blueE = True
        app.greenE = False
        app.pinkE = False
        app.brownE = False
        app.blackE = False
        app.purpleE = False
        app.eyelinerColor = 'royalBlue'

def main():
    runApp(width=2000, height=1000)

if __name__ == '__main__':
    main()