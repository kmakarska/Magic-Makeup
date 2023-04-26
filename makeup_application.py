from cmu_graphics import *
from PIL import Image
import os, pathlib

#button class idea inspired by lecture demo on buttons
class nextButton:
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

class goButton:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        
    def draw(self):
        drawRect(650, 650, 200, 100, fill='hotPink', border='mediumVioletRed') 
        drawLabel("GO", 750, 700, size=50, fill='mediumVioletRed')

    def checkForPress(self, app, mouseX, mouseY):
        if (mouseX > self.x and mouseX < self.x + self.w and mouseY > self.y and mouseY < self.y + self.h):
            setActiveScreen('game')

def start_openImage(fileName):
    #line directly below taken from image lecture notes
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
    app.nextButton = nextButton(800, 450, 200, 100)


def start_redrawAll(app):
    drawImage(app.bgImg, 0, 0)
    drawImage(app.fairyImg, 80, 300)
    drawOval(900, 400, 900, 600, fill='pink')
    drawRegularPolygon(460, 440, 50, 3, fill='pink')
    drawLabel("Welcome To", 900, 250, size=50, fill='mediumVioletRed')
    drawLabel("MAGIC MAKEUP", 900, 350, size=90, fill='mediumVioletRed', bold=True)
    app.nextButton.draw()
   

def start_onMousePress(app, mouseX, mouseY):
    #button pressing
    app.nextButton.checkForPress(app, mouseX, mouseY)

def name_openImage(fileName):
    #line directly below taken from image lecture notes
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
    app.goButton = goButton(650, 650, 200, 100)

def name_redrawAll(app):
    drawImage(app.bgImg, 0, 0)
    drawImage(app.fairyImg, 1200, 100)
    drawOval(950, 150, 400, 200, fill='lavenderBlush')
    drawRegularPolygon(1120, 200, 25, 3, fill='lavenderBlush')
    drawLabel("I'm Pixie, I will be", 960, 130, size=35, fill='mediumVioletRed')
    drawLabel("your teacher!", 950, 180, size=35, fill='mediumVioletRed')
    drawRect(350, 300, 800, 550, fill='pink', border='hotPink', borderWidth=5)   
    name_inputFieldDraw(app)
    app.goButton.draw()
    

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
    app.goButton.checkForPress(app, mouseX, mouseY)


def name_onKeyPress(app, key):
    if (app.boxPressed):
        if key.isalpha() and key != 'enter' and key != 'tab' and key != 'escape' and len(app.input) != 15:
            app.input += key
        if key == 'backspace':
            app.input = app.input[:-10]
        if key == 'space':
            app.input = app.input[:-5] + ' '


class Eyeliner:
    def __init__(self, color, prevMousePositions, lines, dragging, mouseReleased, lineWidth, sliderDragged, sliderOffset):
        self.color = color
        self.prevMousePositions = prevMousePositions
        self.lines = lines
        self.dragging = dragging
        self.mouseReleased = mouseReleased
        self.lineWidth = lineWidth
        self.sliderDragged = sliderDragged
        self.sliderOffset = sliderOffset

    def drawLines(self):
        for line in self.lines:
            for i in range(len(line) - 1):
                x0, y0 = line[i]
                x1, y1 = line[i+1]
                drawLine(x0, y0, x1, y1, lineWidth=self.lineWidth, fill=self.color)
        for i in range(len(self.prevMousePositions) - 1):
            x0, y0 = self.prevMousePositions[i]
            x1, y1 = self.prevMousePositions[i+1]
            drawLine(x0, y0, x1, y1, lineWidth=self.lineWidth, fill=self.color)
    
    def drawSlider(self):
        drawRect(1200, 450, 200, 40, fill='pink', border='mediumVioletRed')
        sliderPos = 1200 + (self.lineWidth - 1) * 20
        drawRect(sliderPos, 450, 40, 40, fill='hotPink', border='mediumVioletRed')

    def pressedInSlider(self, mouseX, mouseY):
        if mouseX > 1200 and mouseX < 1400 and mouseY > 450 and mouseY < 490:
            return True
    



class EyelinerColorButton:
    def __init__(self, x, y, width, height, color, borderColor, borderWidth, label):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.isClicked = False
        self.borderColor = borderColor
        self.borderWidth = borderWidth
        self.label = label

    def draw(self):
        drawRect(self.x, self.y, self.width, self.height, fill=self.color, border=self.borderColor, borderWidth=self.borderWidth)
        drawLabel(self.label, self.x + self.width/2, self.y + self.height/2, fill='mediumVioletRed', size=30)

    def clickedInside(self, mouseX, mouseY):
        if mouseX > self.x and mouseX < self.x + self.width and mouseY > self.y and mouseY < self.y + self.height:
            self.isClicked = True
            return True
        

class doneButton:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        
    def draw(self):
        drawRect(1225, 550, 150, 70, fill='hotPink', border='mediumVioletRed') 
        drawLabel("Done", 1300, 585, size=30, fill='mediumVioletRed')

    def checkForPress(self, app, mouseX, mouseY):
        if (mouseX > self.x and mouseX < self.x + self.w and mouseY > self.y and mouseY < self.y + self.h):
            setActiveScreen('end')       
          
        
# class Lipstick:
#     def __init__(self, color):
#         self.color = color
#         self.prevMousePositions = []
#         self.lines = []

def game_openImage(fileName):
    #line below taken from lecture notes
    return Image.open(os.path.join(pathlib.Path(__file__).parent,fileName))

def game_onAppStart(app):
    init(app) 
    colorInit(app)
    openingImages(app)
    resizeFaceImages(app)
    # resizeOtherImages(app)
    convertImgType(app)

def end_onAppStart(app):
    openingImages(app)
    resizeFaceImages(app)
    # resizeOtherImages(app)
    convertImgType(app)
   

def init(app):
    app.eyeliner = Eyeliner('black', [], [], False, True, 1, False, 0)
    app.doneButton = doneButton(1225, 550, 200, 100)

    app.eyelinerPressed = False
    app.lipstickPressed = False


def colorInit(app):
    #eyeliner
    app.blackE = EyelinerColorButton(1225, 120, 70, 70, 'black', None, 0, '')
    app.brownE = EyelinerColorButton(1310, 120, 70, 70, 'saddleBrown', None, 0, '')
    app.pinkE = EyelinerColorButton(1225, 200, 70, 70, 'deepPink', None, 0, '')
    app.purpleE = EyelinerColorButton(1310, 200, 70, 70, 'darkViolet', None, 0, '')
    app.greenE = EyelinerColorButton(1225, 280, 70, 70, 'limeGreen', None, 0, '')
    app.blueE = EyelinerColorButton(1310, 280, 70, 70, 'royalBlue', None, 0, '')
    app.eraser = EyelinerColorButton(145, 550, 150, 70, 'hotPink', 'mediumVioletRed', 2, 'Clear')
    #lipstick
    # app.hotPinkL = False
    # app.crimsonL = False
    # app.deepPinkL = False
    # app.darkRedL = False
    # app.magentaL = False
    # app.darkMagentaL = False

def openingImages(app):
    #default face (and other faces) found on https://barbie-makeup.goldhairgames.com/barbie-makeup/1382-barbie-loves-capybaras
    app.defaultFace = Image.open('images/defaultFace.png')
    #eyeliner icon found on https://pngtree.com/free-png-vectors/eyeliner-clipart
    app.eyelinerImg = Image.open('images/eyeliner.png')
    app.eyelinerFace = Image.open('images/eyelinerFace.jpg')
    #lipstick icon found on https://pngtree.com/freepng/a-lipstick-makeup-illustration_4562723.html
    # app.lipstick = Image.open('images/lipstick.png')
    # app.lipstickFace = Image.open('images/lipstickFace.jpg')
    #bg image found on https://www.shutterstock.com/search/pink-purple-glitter
    app.bgImg = Image.open('images/bg.png')
    #fairy image found on https://www.pngwing.com/en/free-png-svqht
    app.fairyImg = Image.open('images/fairy.png')

def resizeFaceImages(app):
    newsize = (700, 700)
    app.defaultFace = app.defaultFace.resize(newsize)
    app.eyelinerFace = app.eyelinerFace.resize(newsize)
    # app.lipstickFace = app.lipstickFace.resize(newsize)

# def resizeOtherImages(app):
#     newsize2 = (200, 200)
#     app.lipstickImg = app.lipstickImg.resize(newsize2)

def convertImgType(app):
    app.bgImg = CMUImage(app.bgImg)
    app.defaultFace = CMUImage(app.defaultFace)
    app.eyelinerImg = CMUImage(app.eyelinerImg)
    app.eyelinerFace = CMUImage(app.eyelinerFace)
    # app.lipstickImg = CMUImage(app.lipstickImg)
    # app.lipstickFace = CMUImage(app.lipstickFace)
    app.fairyImg = CMUImage(app.fairyImg)
    
def game_redrawAll(app):
    drawImage(app.bgImg, 0, 0)
    drawImage(app.fairyImg, 70, 100)
    drawImage(app.defaultFace, 400, -5)
    drawRect(0, 680, 2000, 300, fill='violet')
    app.doneButton.draw()
    eyelinerDrawing(app)
    # lipstickPressed(app)
    drawProducts(app)

def end_redrawAll(app):
    drawImage(app.bgImg, 0, 0)
    drawImage(app.fairyImg, 70, 100)
    drawImage(app.defaultFace, 400, -5)
    app.eyeliner.drawLines()
    drawRect(0, 680, 2000, 300, fill='violet')



def drawProducts(app):
    drawImage(app.eyelinerImg, 650, 700)
    # drawImage(app.lipstick, 1050, 710)
    
def eyelinerDrawing(app):
    if (app.eyelinerPressed):
        drawImage(app.eyelinerFace, 400, 0)
        drawRect(0, 680, 2000, 300, fill='violet')
        #pixie hints
        drawOval(550, 125, 400, 200, fill='lavenderBlush')
        drawRegularPolygon(360, 150, 25, 3, fill='lavenderBlush')
        drawLabel("Place eyeliner on", 550, 80, size=30, fill='mediumVioletRed')
        drawLabel("the upper lash line to", 550, 120, size=30, fill='mediumVioletRed')
        drawLabel("accentuate the eyes!", 550, 160, size=30, fill='mediumVioletRed')
        drawImage(app.eyelinerImg, 650, 700)
        drawRect(650, 700, 230, 200, fill=None, border='black')
        app.eyeliner.drawLines()
        app.eyeliner.drawSlider()
        drawLabel("Brush Size", 1300, 400, size=30, fill='mediumVioletRed')
        eyelinerColors(app)
    
# def lipstickPressed(app):
#     if (app.lipstickPressed):
#         drawImage(app.lipstickFace, 400, 0)
#         drawRect(0, 680, 2000, 300, fill='violet')
#         drawRect(1025, 700, 230, 200, fill=None, border='black')
#         lipstickColors(app)
#         drawOval(550, 125, 400, 200, fill='lavenderBlush')
#         drawRegularPolygon(360, 150, 25, 3, fill='lavenderBlush')
#         drawLabel("Place lipstick on", 550, 80, size=30, fill='mediumVioletRed')
#         drawLabel("lips to brighten", 550, 120, size=30, fill='mediumVioletRed')
#         drawLabel("the smile!", 550, 160, size=30, fill='')
#         drawImage(app.lipstick, 1050, 710)

    

        
def eyelinerColors(app):
    if(app.eyelinerPressed):
        drawLabel("Colors", 1300, 80, size=30, fill='mediumVioletRed')
        app.blackE.draw()
        app.brownE.draw()
        app.pinkE.draw()
        app.purpleE.draw()
        app.greenE.draw()
        app.blueE.draw()
        app.eraser.draw()



        #black
        # drawRect(1225, 120, 70, 70, fill='black')
        # if app.blackE:
        #     drawRect(1220, 115, 80, 80, fill=None, border='yellow', borderWidth=5)
        # #brown
        # drawRect(1310, 120, 70, 70, fill='saddleBrown')
        # if app.brownE:
        #     drawRect(1305, 115, 80, 80, fill=None, border='yellow', borderWidth=5)
        # #pink
        # drawRect(1225, 200, 70, 70, fill='deepPink')
        # if app.pinkE:
        #     drawRect(1220, 195, 80, 80, fill=None, border='yellow', borderWidth=5)
        # #purple
        # drawRect(1310, 200, 70, 70, fill='darkViolet')
        # if app.purpleE:
        #     drawRect(1305, 195, 80, 80, fill=None, border='yellow', borderWidth=5)
        # #green
        # drawRect(1225, 280, 70, 70, fill='limeGreen')
        # if app.greenE:
        #     drawRect(1220, 275, 80, 80, fill=None, border='yellow', borderWidth=5)
        # #blue
        # drawRect(1310, 280, 70, 70, fill='royalBlue')
        # if app.blueE:
        #     drawRect(1305, 275, 80, 80, fill=None, border='yellow', borderWidth=5)

# def lipstickColors(app):
#     if app.lipstickPressed:
#         drawLabel("Colors", 1300, 80, size=30)
#         #hot pink
#         drawRect(1225, 120, 70, 70, fill='hotPink')
#         if app.hotPinkL:
#             drawRect(1220, 115, 80, 80, fill=None, border='yellow', borderWidth=5)
#         #crimson
#         drawRect(1310, 120, 70, 70, fill='crimson')
#         if app.crimsonL:
#             drawRect(1305, 115, 80, 80, fill=None, border='yellow', borderWidth=5)
#         #deepPink
#         drawRect(1225, 200, 70, 70, fill='deepPink')
#         if app.deepPinkL:
#             drawRect(1220, 195, 80, 80, fill=None, border='yellow', borderWidth=5)
#         #darkRed
#         drawRect(1310, 200, 70, 70, fill='darkRed')
#         if app.darkRedL:
#             drawRect(1305, 195, 80, 80, fill=None, border='yellow', borderWidth=5)
#         #magenta
#         drawRect(1225, 280, 70, 70, fill='magenta')
#         if app.magentaL:
#             drawRect(1220, 275, 80, 80, fill=None, border='yellow', borderWidth=5)
#         #darkMagenta
#         drawRect(1310, 280, 70, 70, fill='darkMagenta')
#         if app.darkMagentaL:
#             drawRect(1305, 275, 80, 80, fill=None, border='yellow', borderWidth=5)
    
      
def game_onMouseDrag(app, mouseX, mouseY):
    if not app.eyeliner.dragging:
        app.eyeliner.lines.append(app.eyeliner.prevMousePositions)
        app.eyeliner.prevMousePositions = [(mouseX, mouseY)]
        app.eyeliner.dragging = True
    elif app.eyeliner.dragging:
        app.eyeliner.prevMousePositions.append((mouseX, mouseY))
    #creating bounds for slider
    if app.eyeliner.pressedInSlider(mouseX, mouseY):
        sliderPos = min(1400, max(1225, mouseX - app.eyeliner.sliderOffset))
        app.eyeliner.lineWidth = (sliderPos - 1225) // 20 + 1

def game_onMouseRelease(app, mouseX, mouseY):
    app.eyeliner.dragging = False
    app.eyeliner.mouseReleased = True
    app.eyeliner.lines.append(app.eyeliner.prevMousePositions)
    app.eyeliner.sliderDragged = True

def game_onMousePress(app, mouseX, mouseY):
    # if mode is eyeliner, do this
    eyelinerOnMousePress(app, mouseX, mouseY)
    app.doneButton.checkForPress(app, mouseX, mouseY)

    # if app.lipstickPressed:
        # lipstickOnMousePress(app, mouseX, mouseY)
    
   
def eyelinerOnMousePress(app, mouseX, mouseY):
    #drawing the line
    if not app.eyeliner.mouseReleased:
        app.eyeliner.dragging = True
        app.eyeliner.prevMousePositions = [(mouseX, mouseY)]
    app.eyeliner.mouseReleased = False
    #eyeliner pressed
    if (mouseX >= 650 and mouseX <= 850 and mouseY >= 700 and mouseY <= 900):
        app.eyelinerPressed = True
        # app.lipstickPressed = False
    #blackE pressed
    if (app.blackE.clickedInside(mouseX, mouseY)):
        app.eyeliner.color = 'black'
    #brownE pressed
    elif (app.brownE.clickedInside(mouseX, mouseY)):
        app.eyeliner.color = 'saddleBrown'
    elif (app.pinkE.clickedInside(mouseX, mouseY)):
        app.eyeliner.color = 'deepPink'
    elif (app.purpleE.clickedInside(mouseX, mouseY)):
        app.eyeliner.color = 'darkViolet'
    elif (app.greenE.clickedInside(mouseX, mouseY)):
        app.eyeliner.color = 'limeGreen'
    elif (app.blueE.clickedInside(mouseX, mouseY)):
        app.eyeliner.color = 'royalBlue'
    elif (app.eraser.clickedInside(mouseX, mouseY)):
        app.eyeliner.color = None
        app.eyeliner.prevMousePositions = []
        app.eyeliner.lines = []
    
    # if (mouseX > 1225 and mouseX < 1295 and mouseY > 120 and mouseY < 190):
    #     app.blackE = True
    #     app.brownE = False
    #     app.pinkE = False
    #     app.purpleE = False
    #     app.greenE = False
    #     app.blueE = False
    #     app.eyelinerColor = 'black'
    # #brownE pressed
    # if (mouseX > 1310 and mouseX < 1380 and mouseY > 120 and mouseY < 190):
    #     app.brownE = True
    #     app.blackE = False
    #     app.pinkE = False
    #     app.purpleE = False
    #     app.greenE = False
    #     app.blueE = False
    #     app.eyelinerColor = 'saddleBrown'
    # #pinkE pressed
    # if (mouseX > 1225 and mouseX < 1295 and mouseY > 200 and mouseY < 270):
    #     app.pinkE = True
    #     app.brownE = False
    #     app.blackE = False
    #     app.purpleE = False
    #     app.greenE = False
    #     app.blueE = False
    #     app.eyelinerColor = 'deepPink'
    # #purpleE pressed
    # if (mouseX > 1310 and mouseX < 1380 and mouseY > 200 and mouseY < 270):
    #     app.purpleE = True
    #     app.pinkE = False
    #     app.brownE = False
    #     app.blackE = False
    #     app.greenE = False
    #     app.blueE = False
    #     app.eyelinerColor = 'darkViolet'
    # #greenE pressed
    # if (mouseX > 1225 and mouseX < 1295 and mouseY > 280 and mouseY < 350):
    #     app.greenE = True
    #     app.pinkE = False
    #     app.brownE = False
    #     app.blackE = False
    #     app.purpleE = False
    #     app.blueE = False
    #     app.eyelinerColor = 'limeGreen'
    # #blueE pressed
    # if (mouseX > 1310 and mouseX < 1380 and mouseY > 280 and mouseY < 350):
    #     app.blueE = True
    #     app.greenE = False
    #     app.pinkE = False
    #     app.brownE = False
    #     app.blackE = False
    #     app.purpleE = False
    #     app.eyelinerColor = 'royalBlue'

# def lipstickOnMousePress(app, mouseX, mouseY):
#     #lipstick pressed
#     if (mouseX >= 1050 and mouseX <= 1250 and mouseY >= 700 and mouseY <= 900):
#         app.lipstickPressed = True
#         app.eyelinerPressed = False
#     #hotPinkL pressed
#     if (mouseX > 1225 and mouseX < 1295 and mouseY > 120 and mouseY < 190):
#         app.hotPinkL = True
#         app.crimsonL = False
#         app.deepPinkL = False
#         app.darkRed = False
#         app.magentaL = False
#         app.darkMagentaL = False
#         app.lipstickColor = 'hotPink'
#     #crimsonL pressed
#     if (mouseX > 1310 and mouseX < 1380 and mouseY > 120 and mouseY < 190):
#         app.crimsonL = True
#         app.hotPinkL = False
#         app.deepPinkL = False
#         app.darkRed = False
#         app.magentaL = False
#         app.darkMagentaL = False
#         app.lipstickColor = 'crimson'
#     #deepPinkL pressed
#     if (mouseX > 1225 and mouseX < 1295 and mouseY > 200 and mouseY < 270):
#         app.deepPinkL = True
#         app.crimsonL = False
#         app.hotPinkL = False 
#         app.darkRed = False       
#         app.magentaL = False
#         app.darkMagentaL = False
#         app.lipstickColor = 'deepPink'
#     #darkRedL pressed
#     if (mouseX > 1310 and mouseX < 1380 and mouseY > 200 and mouseY < 270):
#         app.darkRed = True
#         app.deepPinkL = False
#         app.crimsonL = False
#         app.hotPinkL = False  
#         app.magentaL = False
#         app.darkMagentaL = False
#         app.lipstickColor = 'darkRed'
#     #magentaL pressed
#     if (mouseX > 1225 and mouseX < 1295 and mouseY > 280 and mouseY < 350):
#         app.magentaL = True
#         app.darkRed = False
#         app.deepPinkL = False
#         app.crimsonL = False
#         app.hotPinkL = False  
#         app.darkMagentaL = False
#         app.lipstickColor = 'magenta'
#     #darkMagentaL pressed
#     if (mouseX > 1310 and mouseX < 1380 and mouseY > 280 and mouseY < 350):
#         app.darkMagentaL = True
#         app.magentaL = False
#         app.darkRed = False
#         app.deepPinkL = False
#         app.crimsonL = False
#         app.hotPinkL = False  
#         app.lipstickColor = 'darkMagenta'

def main():
    runAppWithScreens(initialScreen='start')
    runApp(width=2000, height=1000)

if __name__ == '__main__':
    main()