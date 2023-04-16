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

def colorInit(app):
    app.blackE = False
    app.brownE = False

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
    if (app.eyelinerPressed):
        drawImage(app.eyelinerFace, 400, 0)
        drawRect(0, 680, 2000, 300, fill='violet')
        drawRect(650, 700, 230, 200, fill=None, border='black')
    drawImage(app.eyeliner, 650, 700)
    for pos in app.prevMousePositions:
        drawCircle(pos[0], pos[1], 3, fill='pink')
      
def onMouseDrag(app, mouseX, mouseY):
    app.prevMousePositions.append((mouseX, mouseY))

def onMousePress(app, mouseX, mouseY):
    if (mouseX >= 650 and mouseX <= 850 and mouseY >= 700 and mouseY <= 900):
        app.eyelinerPressed = True

def main():
    runApp(width=2000, height=1000)

if __name__ == '__main__':
    main()