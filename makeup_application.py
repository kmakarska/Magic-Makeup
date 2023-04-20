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
    resizeOtherImages(app)
    convertImgType(app)

def init(app):
    app.prevMousePositionsE = []
    app.prevMousePositionsL = []
    app.eyelinerPressed = False
    app.lipstickPressed = False
    app.eyelinerColor = 'black'
    app.lipstickColor = 'pink'

def colorInit(app):
    #eyeliner
    app.blackE = False
    app.brownE = False
    app.pinkE = False
    app.purpleE = False
    app.greenE = False
    app.blueE = False
    #lipstick
    app.hotPinkL = False
    app.crimsonL = False
    app.deepPinkL = False
    app.darkRedL = False
    app.magentaL = False
    app.darkMagentaL = False

def openingImages(app):
    #default face (and other faces) found on https://barbie-makeup.goldhairgames.com/barbie-makeup/1382-barbie-loves-capybaras
    app.defaultFace = Image.open('images/defaultFace.png')
    #eyeliner icon found on https://pngtree.com/free-png-vectors/eyeliner-clipart
    app.eyeliner = Image.open('images/eyeliner.png')
    app.eyelinerFace = Image.open('images/eyelinerFace.jpg')
    #lipstick icon found on https://pngtree.com/freepng/a-lipstick-makeup-illustration_4562723.html
    app.lipstick = Image.open('images/lipstick.png')
    app.lipstickFace = Image.open('images/lipstickFace.jpg')
    #bg image found on https://www.shutterstock.com/search/pink-purple-glitter
    app.bgImg = Image.open('images/bg.png')
    #fairy image found on https://www.pngwing.com/en/free-png-svqht
    app.fairyImg = Image.open('images/fairy.png')

def resizeFaceImages(app):
    newsize = (700, 700)
    app.defaultFace = app.defaultFace.resize(newsize)
    app.eyelinerFace = app.eyelinerFace.resize(newsize)
    app.lipstickFace = app.lipstickFace.resize(newsize)

def resizeOtherImages(app):
    newsize2 = (200, 200)
    app.lipstick = app.lipstick.resize(newsize2)

def convertImgType(app):
    app.bgImg = CMUImage(app.bgImg)
    app.defaultFace = CMUImage(app.defaultFace)
    app.eyeliner = CMUImage(app.eyeliner)
    app.eyelinerFace = CMUImage(app.eyelinerFace)
    app.lipstick = CMUImage(app.lipstick)
    app.lipstickFace = CMUImage(app.lipstickFace)
    app.fairyImg = CMUImage(app.fairyImg)
    
def redrawAll(app):
    drawImage(app.bgImg, 0, 0)
    drawImage(app.fairyImg, 70, 100)
    drawImage(app.defaultFace, 400, -5)
    drawRect(0, 680, 2000, 300, fill='violet')
    drawRect(1200, 550, 200, 100, fill='hotPink', border='mediumVioletRed') 
    drawLabel("Done", 1300, 600, size=50, fill='mediumVioletRed')
    eyelinerPressed(app)
    lipstickPressed(app)
    drawProducts(app)

def drawProducts(app):
    drawImage(app.eyeliner, 650, 700)
    drawImage(app.lipstick, 1050, 710)
    
def eyelinerPressed(app):
    if (app.eyelinerPressed):
        drawImage(app.eyelinerFace, 400, 0)
        drawRect(0, 680, 2000, 300, fill='violet')
        #pixie hints
        drawOval(550, 125, 400, 200, fill='lavenderBlush')
        drawRegularPolygon(360, 150, 25, 3, fill='lavenderBlush')
        drawLabel("Place eyeliner on", 550, 80, size=30, fill='mediumVioletRed')
        drawLabel("the upper lash line to", 550, 120, size=30, fill='mediumVioletRed')
        drawLabel("accentuate the eyes!", 550, 160, size=30, fill='mediumVioletRed')
        drawImage(app.eyeliner, 650, 700)
        drawRect(650, 700, 230, 200, fill=None, border='black')
        eyelinerColors(app)
    print("eyeliner entered")
    
def lipstickPressed(app):
    if (app.lipstickPressed):
        drawImage(app.lipstickFace, 400, 0)
        drawRect(0, 680, 2000, 300, fill='violet')
        drawRect(1025, 700, 230, 200, fill=None, border='black')
        lipstickColors(app)
        drawOval(550, 125, 400, 200, fill='lavenderBlush')
        drawRegularPolygon(360, 150, 25, 3, fill='lavenderBlush')
        drawLabel("Place lipstick on", 550, 80, size=30, fill='mediumVioletRed')
        drawLabel("lips to brighten", 550, 120, size=30, fill='mediumVioletRed')
        drawLabel("the smile!", 550, 160, size=30, fill='mediumVioletRed')
        drawImage(app.lipstick, 1050, 710)
    print("lipstick entered")
    for pos in app.prevMousePositionsL:
        drawCircle(pos[0], pos[1], 3, fill=app.lipstickColor)
    print(len(app.prevMousePositionsL))
    for pos in app.prevMousePositionsE:
        drawCircle(pos[0], pos[1], 3, fill=app.eyelinerColor)
    print(len(app.prevMousePositionsE))

        
def eyelinerColors(app):
    if(app.eyelinerPressed):
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

def lipstickColors(app):
    if app.lipstickPressed:
        drawLabel("Colors", 1300, 80, size=30)
        #hot pink
        drawRect(1225, 120, 70, 70, fill='hotPink')
        if app.hotPinkL:
            drawRect(1220, 115, 80, 80, fill=None, border='yellow', borderWidth=5)
        #crimson
        drawRect(1310, 120, 70, 70, fill='crimson')
        if app.crimsonL:
            drawRect(1305, 115, 80, 80, fill=None, border='yellow', borderWidth=5)
        #deepPink
        drawRect(1225, 200, 70, 70, fill='deepPink')
        if app.deepPinkL:
            drawRect(1220, 195, 80, 80, fill=None, border='yellow', borderWidth=5)
        #darkRed
        drawRect(1310, 200, 70, 70, fill='darkRed')
        if app.darkRedL:
            drawRect(1305, 195, 80, 80, fill=None, border='yellow', borderWidth=5)
        #magenta
        drawRect(1225, 280, 70, 70, fill='magenta')
        if app.magentaL:
            drawRect(1220, 275, 80, 80, fill=None, border='yellow', borderWidth=5)
        #darkMagenta
        drawRect(1310, 280, 70, 70, fill='darkMagenta')
        if app.darkMagentaL:
            drawRect(1305, 275, 80, 80, fill=None, border='yellow', borderWidth=5)

      
def onMouseDrag(app, mouseX, mouseY):
    if app.eyelinerPressed:
        app.prevMousePositionsE.append((mouseX, mouseY))
    elif app.lipstickPressed:
        app.prevMousePositionsL.append((mouseX, mouseY))

def onMousePress(app, mouseX, mouseY):
    eyelinerOnMousePress(app, mouseX, mouseY)
    lipstickOnMousePress(app, mouseX, mouseY)
   
def eyelinerOnMousePress(app, mouseX, mouseY):
    #eyeliner pressed
    if (mouseX >= 650 and mouseX <= 850 and mouseY >= 700 and mouseY <= 900):
        app.eyelinerPressed = True
        app.lipstickPressed = False
    #blackE pressed
    if (mouseX > 1225 and mouseX < 1295 and mouseY > 120 and mouseY < 190):
        app.blackE = True
        app.brownE = False
        app.pinkE = False
        app.purpleE = False
        app.greenE = False
        app.blueE = False
        app.eyelinerColor = 'black'
    #brownE pressed
    if (mouseX > 1310 and mouseX < 1380 and mouseY > 120 and mouseY < 190):
        app.brownE = True
        app.blackE = False
        app.pinkE = False
        app.purpleE = False
        app.greenE = False
        app.blueE = False
        app.eyelinerColor = 'saddleBrown'
    #pinkE pressed
    if (mouseX > 1225 and mouseX < 1295 and mouseY > 200 and mouseY < 270):
        app.pinkE = True
        app.brownE = False
        app.blackE = False
        app.purpleE = False
        app.greenE = False
        app.blueE = False
        app.eyelinerColor = 'deepPink'
    #purpleE pressed
    if (mouseX > 1310 and mouseX < 1380 and mouseY > 200 and mouseY < 270):
        app.purpleE = True
        app.pinkE = False
        app.brownE = False
        app.blackE = False
        app.greenE = False
        app.blueE = False
        app.eyelinerColor = 'darkViolet'
    #greenE pressed
    if (mouseX > 1225 and mouseX < 1295 and mouseY > 280 and mouseY < 350):
        app.greenE = True
        app.pinkE = False
        app.brownE = False
        app.blackE = False
        app.purpleE = False
        app.blueE = False
        app.eyelinerColor = 'limeGreen'
    #blueE pressed
    if (mouseX > 1310 and mouseX < 1380 and mouseY > 280 and mouseY < 350):
        app.blueE = True
        app.greenE = False
        app.pinkE = False
        app.brownE = False
        app.blackE = False
        app.purpleE = False
        app.eyelinerColor = 'royalBlue'

def lipstickOnMousePress(app, mouseX, mouseY):
    #lipstick pressed
    if (mouseX >= 1050 and mouseX <= 1250 and mouseY >= 700 and mouseY <= 900):
        app.lipstickPressed = True
        app.eyelinerPressed = False
    #hotPinkL pressed
    if (mouseX > 1225 and mouseX < 1295 and mouseY > 120 and mouseY < 190):
        app.hotPinkL = True
        app.crimsonL = False
        app.deepPinkL = False
        app.darkRed = False
        app.magentaL = False
        app.darkMagentaL = False
        app.lipstickColor = 'hotPink'
    #crimsonL pressed
    if (mouseX > 1310 and mouseX < 1380 and mouseY > 120 and mouseY < 190):
        app.crimsonL = True
        app.hotPinkL = False
        app.deepPinkL = False
        app.darkRed = False
        app.magentaL = False
        app.darkMagentaL = False
        app.lipstickColor = 'crimson'
    #deepPinkL pressed
    if (mouseX > 1225 and mouseX < 1295 and mouseY > 200 and mouseY < 270):
        app.deepPinkL = True
        app.crimsonL = False
        app.hotPinkL = False 
        app.darkRed = False       
        app.magentaL = False
        app.darkMagentaL = False
        app.lipstickColor = 'deepPink'
    #darkRedL pressed
    if (mouseX > 1310 and mouseX < 1380 and mouseY > 200 and mouseY < 270):
        app.darkRed = True
        app.deepPinkL = False
        app.crimsonL = False
        app.hotPinkL = False  
        app.magentaL = False
        app.darkMagentaL = False
        app.lipstickColor = 'darkRed'
    #magentaL pressed
    if (mouseX > 1225 and mouseX < 1295 and mouseY > 280 and mouseY < 350):
        app.magentaL = True
        app.darkRed = False
        app.deepPinkL = False
        app.crimsonL = False
        app.hotPinkL = False  
        app.darkMagentaL = False
        app.lipstickColor = 'magenta'
    #darkMagentaL pressed
    if (mouseX > 1310 and mouseX < 1380 and mouseY > 280 and mouseY < 350):
        app.darkMagentaL = True
        app.magentaL = False
        app.darkRed = False
        app.deepPinkL = False
        app.crimsonL = False
        app.hotPinkL = False  
        app.lipstickColor = 'darkMagenta'

def main():
    runApp(width=2000, height=1000)

if __name__ == '__main__':
    main()