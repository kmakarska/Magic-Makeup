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
    def __init__(self, color, prevMousePositions, lines, dragging, mouseReleased, lineWidth, 
                 sliderDragged, sliderOffset, eyelinerMode, borderColor):
        self.color = color
        self.prevMousePositions = prevMousePositions
        self.lines = lines
        self.dragging = dragging
        self.mouseReleased = mouseReleased
        self.lineWidth = lineWidth
        self.sliderDragged = sliderDragged
        self.sliderOffset = sliderOffset
        self.eyelinerMode = eyelinerMode
        self.borderColor = borderColor

    def eyelinerPressed(self, mouseX, mouseY):
        if (mouseX >= 650 and mouseX <= 875 and mouseY >= 700 and mouseY <= 925):
            self.eyelinerMode = True
            # self.borderColor = 'black'
            return True
        else:
            # self.borderColor = None
            return False

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
    
class Lipstick:
    def __init__(self, color, prevMousePositions, lines, dragging, mouseReleased,
                  lineWidth, sliderDragged, sliderOffset, lipstickMode, borderColor):
        self.color = color
        self.prevMousePositions = prevMousePositions
        self.lines = lines
        self.dragging = dragging
        self.mouseReleased = mouseReleased
        self.lineWidth = lineWidth
        self.sliderDragged = sliderDragged
        self.sliderOffset = sliderOffset
        self.lipstickMode = lipstickMode
        self.borderColor = borderColor

    def lipstickPressed(self, mouseX, mouseY):
        if (mouseX > 1025 and mouseX < 1255 and mouseY > 700 and mouseY < 900):
            self.lipstickMode = True
            # self.borderColor = 'black'
            return True
        else:
            # self.borderColor = None
            return False

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
        
class Blush:
    def __init__(self, color, prevMousePositions, lines, dragging, mouseReleased,
                  lineWidth, sliderDragged, sliderOffset, blushMode, borderColor):
        self.color = color
        self.prevMousePositions = prevMousePositions
        self.lines = lines
        self.dragging = dragging
        self.mouseReleased = mouseReleased
        self.lineWidth = lineWidth
        self.sliderDragged = sliderDragged
        self.sliderOffset = sliderOffset
        self.blushMode = blushMode
        self.borderColor = borderColor

    def blushPressed(self, mouseX, mouseY):
        if (mouseX > 270 and mouseX < 420 and mouseY > 720 and mouseY < 870):
            self.blushMode = True
            # self.borderColor = 'black'
            return True
        else:
            # self.borderColor = None
            return False


    def drawLines(self):
        for line in self.lines:
            for i in range(len(line) - 1):
                x0, y0 = line[i]
                x1, y1 = line[i+1]
                drawLine(x0, y0, x1, y1, lineWidth=self.lineWidth, fill=self.color, opacity=2)
        for i in range(len(self.prevMousePositions) - 1):
            x0, y0 = self.prevMousePositions[i]
            x1, y1 = self.prevMousePositions[i+1]
            drawLine(x0, y0, x1, y1, lineWidth=self.lineWidth, fill=self.color, opacity=2)
    
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
        
class LipstickColorButton:
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
        
class BlushColorButton:
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

class replayButton:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        
    def draw(self):
        drawRect(1225, 575, 150, 70, fill='hotPink', border='mediumVioletRed') 
        drawLabel("Replay", 1300, 610, size=30, fill='mediumVioletRed')

    def checkForPress(self, app, mouseX, mouseY):
        if (mouseX > self.x and mouseX < self.x + self.w and mouseY > self.y and mouseY < self.y + self.h):
            setActiveScreen('start')
            init(app)
          

def game_openImage(fileName):
    #line below taken from lecture notes
    return Image.open(os.path.join(pathlib.Path(__file__).parent,fileName))

def game_onAppStart(app):
    init(app) 
    colorInit(app)
    openingImages(app)
    resizeFaceImages(app)
    resizeOtherImages(app)
    convertImgType(app)

def end_onAppStart(app):
    openingImages(app)
    resizeFaceImages(app)
    convertImgType(app)
   

def init(app):
    app.eyeliner = Eyeliner('black', [], [], False, True, 1, False, 0, False, None)
    app.lipstick = Lipstick('pink', [], [], False, True, 1, False, 0, False, None)
    app.blush = Blush('pink', [], [], False, True, 1, False, 0, False, None)
    app.doneButton = doneButton(1225, 550, 200, 100)
    app.replayButton = replayButton(1225, 550, 150, 70)
    app.input = ''

def colorInit(app):
    #eyeliner
    app.blackE = EyelinerColorButton(1225, 120, 70, 70, 'black', None, 0, '')
    app.brownE = EyelinerColorButton(1310, 120, 70, 70, 'saddleBrown', None, 0, '')
    app.pinkE = EyelinerColorButton(1225, 200, 70, 70, 'deepPink', None, 0, '')
    app.purpleE = EyelinerColorButton(1310, 200, 70, 70, 'darkViolet', None, 0, '')
    app.greenE = EyelinerColorButton(1225, 280, 70, 70, 'limeGreen', None, 0, '')
    app.blueE = EyelinerColorButton(1310, 280, 70, 70, 'royalBlue', None, 0, '')
    app.eraserE = EyelinerColorButton(145, 550, 150, 70, 'hotPink', 'mediumVioletRed', 2, 'Clear')
    #lipstick
    app.hotPinkL = LipstickColorButton(1225, 120, 70, 70, 'hotPink', None, 0, '')
    app.crimsonL = LipstickColorButton(1310, 120, 70, 70, 'crimson', None, 0, '')
    app.deepPinkL = LipstickColorButton(1225, 200, 70, 70, 'deepPink', None, 0, '')
    app.darkRedL = LipstickColorButton(1310, 200, 70, 70, 'darkRed', None, 0, '')
    app.magentaL = LipstickColorButton(1225, 280, 70, 70, 'magenta', None, 0, '')
    app.darkMagentaL = LipstickColorButton(1310, 280, 70, 70, 'darkMagenta', None, 0, '')
    app.eraserL = LipstickColorButton(145, 550, 150, 70, 'hotPink', 'mediumVioletRed', 2, 'Clear')
    #blush
    app.hotPinkB = BlushColorButton(1225, 120, 70, 70, 'hotPink', None, 0, '')
    app.crimsonB = BlushColorButton(1310, 120, 70, 70, 'crimson', None, 0, '')
    app.deepPinkB = BlushColorButton(1225, 200, 70, 70, 'deepPink', None, 0, '')
    app.darkRedB = BlushColorButton(1310, 200, 70, 70, 'darkRed', None, 0, '')
    app.magentaB = BlushColorButton(1225, 280, 70, 70, 'magenta', None, 0, '')
    app.darkMagentaB = BlushColorButton(1310, 280, 70, 70, 'darkMagenta', None, 0, '')
    app.eraserB = BlushColorButton(145, 550, 150, 70, 'hotPink', 'mediumVioletRed', 2, 'Clear')

def openingImages(app):
    #default face (and other faces) found on https://barbie-makeup.goldhairgames.com/barbie-makeup/1382-barbie-loves-capybaras
    app.defaultFace = Image.open('images/defaultFace.png')
    #eyeliner icon found on https://pngtree.com/free-png-vectors/eyeliner-clipart
    app.eyelinerImg = Image.open('images/eyeliner.png')
    app.eyelinerFace = Image.open('images/eyelinerFace.jpg')
    #lipstick icon found on https://pngtree.com/freepng/a-lipstick-makeup-illustration_4562723.html
    app.lipstickImg = Image.open('images/lipstick.png')
    app.lipstickFace = Image.open('images/lipstickFace.jpg')
    #blush icon found on https://favpng.com/png_view/cosmetics-rouge-compact-face-powder-clip-art-png/CiDXsDzS 
    app.blushImg = Image.open('images/blush.png')
    app.blushFace = Image.open('images/blushFace.jpg')
    #bg image found on https://www.shutterstock.com/search/pink-purple-glitter
    app.bgImg = Image.open('images/bg.png')
    #fairy image found on https://www.pngwing.com/en/free-png-svqht
    app.fairyImg = Image.open('images/fairy.png')


def resizeFaceImages(app):
    newsizeE = (700, 700)
    newsizeL = (700, 695)
    newsizeB = (700, 685)
    app.defaultFace = app.defaultFace.resize(newsizeE)
    app.eyelinerFace = app.eyelinerFace.resize(newsizeE)
    app.lipstickFace = app.lipstickFace.resize(newsizeL)
    app.blushFace = app.blushFace.resize(newsizeB)

def resizeOtherImages(app):
    newsize2 = (200, 200)
    app.lipstickImg = app.lipstickImg.resize(newsize2)
    newsize3 = (150, 150)
    app.blushImg = app.blushImg.resize(newsize3)

def convertImgType(app):
    app.bgImg = CMUImage(app.bgImg)
    app.defaultFace = CMUImage(app.defaultFace)
    app.eyelinerImg = CMUImage(app.eyelinerImg)
    app.eyelinerFace = CMUImage(app.eyelinerFace)
    app.lipstickImg = CMUImage(app.lipstickImg)
    app.lipstickFace = CMUImage(app.lipstickFace)
    app.blushImg = CMUImage(app.blushImg)
    app.blushFace = CMUImage(app.blushFace)
    app.fairyImg = CMUImage(app.fairyImg)
    
def game_redrawAll(app):
    drawImage(app.bgImg, 0, 0)
    drawImage(app.fairyImg, 70, 100)
    drawImage(app.defaultFace, 400, -5)
    drawRect(0, 680, 2000, 300, fill='violet')
    app.doneButton.draw()
    eyelinerDrawing(app)
    lipstickDrawing(app)
    blushDrawing(app)
    savingDrawings(app)
    drawProducts(app)

def end_redrawAll(app):
    drawImage(app.bgImg, 0, 0)
    drawImage(app.fairyImg, 70, 100)
    drawImage(app.defaultFace, 400, -5)
    savingDrawings(app)
    app.replayButton.draw()
    drawRect(0, 680, 2000, 300, fill='violet')
    if app.input == '':
        drawLabel(f'Great Job! Play again!', app.width/2, 780, size=50, fill='mediumVioletRed')
    else:
        drawLabel(f'Great Job, {app.input}! Play again!', app.width/2, 780, size=50, fill='mediumVioletRed')

def drawProducts(app):
    drawImage(app.eyelinerImg, 650, 700)
    drawImage(app.lipstickImg, 1050, 710)
    drawImage(app.blushImg, 270, 720)
    
def eyelinerDrawing(app):
    if app.eyeliner.eyelinerMode:
        drawImage(app.eyelinerFace, 400, 0)
        drawRect(0, 680, 2000, 300, fill='violet')
        #pixie hints
        drawOval(550, 125, 400, 200, fill='lavenderBlush')
        drawRegularPolygon(360, 150, 25, 3, fill='lavenderBlush')
        drawLabel("Place eyeliner on", 550, 80, size=30, fill='mediumVioletRed')
        drawLabel("the upper lash line to", 550, 120, size=30, fill='mediumVioletRed')
        drawLabel("accentuate the eyes!", 550, 160, size=30, fill='mediumVioletRed')
        app.eyeliner.drawSlider()
        drawLabel("Brush Size", 1300, 420, size=30, fill='mediumVioletRed')
        drawLabel("small <=======> large", 1300, 505, size=17, fill='mediumVioletRed')
        eyelinerColors(app)
    
def lipstickDrawing(app):
    if app.lipstick.lipstickMode:
        drawImage(app.lipstickFace, 400, 0)
        drawRect(0, 680, 2000, 300, fill='violet')
        #pixie hints
        drawOval(550, 125, 400, 200, fill='lavenderBlush')
        drawRegularPolygon(360, 150, 25, 3, fill='lavenderBlush')
        drawLabel("Place lipstick on", 550, 80, size=30, fill='mediumVioletRed')
        drawLabel("lips to brighten", 550, 120, size=30, fill='mediumVioletRed')
        drawLabel("the smile!", 550, 160, size=30, fill='mediumVioletRed')    
        app.lipstick.drawSlider()
        drawLabel("Brush Size", 1300, 420, size=30, fill='mediumVioletRed')
        drawLabel("small <=======> large", 1300, 505, size=17, fill='mediumVioletRed')
        lipstickColors(app)

def blushDrawing(app):
    if app.blush.blushMode:
        drawImage(app.blushFace, 400, 0)
        drawRect(0, 680, 2000, 300, fill='violet')
        #pixie hints
        drawOval(550, 125, 400, 200, fill='lavenderBlush')
        drawRegularPolygon(360, 150, 25, 3, fill='lavenderBlush')
        drawLabel("Place blush on", 550, 80, size=30, fill='mediumVioletRed')
        drawLabel("apples of the cheeks", 550, 120, size=30, fill='mediumVioletRed')
        drawLabel("to create glow!", 550, 160, size=30, fill='mediumVioletRed')     
        app.blush.drawSlider()
        drawLabel("Brush Size", 1300, 420, size=30, fill='mediumVioletRed')
        drawLabel("small <=======> large", 1300, 505, size=17, fill='mediumVioletRed')
        blushColors(app)

def savingDrawings(app):
    app.setMaxShapeCount(10000)
    app.eyeliner.drawLines()
    app.lipstick.drawLines()
    app.blush.drawLines()


        
def eyelinerColors(app):
    if(app.eyeliner.eyelinerMode):
        drawLabel("Colors", 1300, 80, size=30, fill='mediumVioletRed')
        app.blackE.draw()
        app.brownE.draw()
        app.pinkE.draw()
        app.purpleE.draw()
        app.greenE.draw()
        app.blueE.draw()
        app.eraserE.draw()

def lipstickColors(app):
    if(app.lipstick.lipstickMode):
        drawLabel("Colors", 1300, 80, size=30, fill='mediumVioletRed')
        app.hotPinkL.draw()
        app.crimsonL.draw()
        app.deepPinkL.draw()
        app.darkRedL.draw()
        app.magentaL.draw()
        app.darkMagentaL.draw()
        app.eraserL.draw()

def blushColors(app):
    if(app.blush.blushMode):
        drawLabel("Colors", 1300, 80, size=30, fill='mediumVioletRed')
        app.hotPinkB.draw()
        app.crimsonB.draw()
        app.deepPinkB.draw()
        app.darkRedB.draw()
        app.magentaB.draw()
        app.darkMagentaB.draw()
        app.eraserB.draw()
    
      
def game_onMouseDrag(app, mouseX, mouseY):
    eyelinerOnMouseDrag(app, mouseX, mouseY)
    lipstickOnMouseDrag(app, mouseX, mouseY)
    blushOnMouseDrag(app, mouseX, mouseY)
   
def eyelinerOnMouseDrag(app, mouseX, mouseY):
    if app.eyeliner.eyelinerMode:
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
        

def lipstickOnMouseDrag(app, mouseX, mouseY):
    if app.lipstick.lipstickMode:
        if not app.lipstick.dragging:
            app.lipstick.lines.append(app.lipstick.prevMousePositions)
            app.lipstick.prevMousePositions = [(mouseX, mouseY)]
            app.lipstick.dragging = True
        elif app.lipstick.dragging:
            app.lipstick.prevMousePositions.append((mouseX, mouseY))
        #creating bounds for slider
        if app.lipstick.pressedInSlider(mouseX, mouseY):
            sliderPos = min(1400, max(1225, mouseX - app.lipstick.sliderOffset))
            app.lipstick.lineWidth = (sliderPos - 1225) // 20 + 1

def blushOnMouseDrag(app, mouseX, mouseY):
    if app.blush.blushMode:
        if not app.blush.dragging:
            app.blush.lines.append(app.blush.prevMousePositions)
            app.blush.prevMousePositions = [(mouseX, mouseY)]
            app.blush.dragging = True
        elif app.blush.dragging:
            app.blush.prevMousePositions.append((mouseX, mouseY))
        #creating bounds for slider
        if app.blush.pressedInSlider(mouseX, mouseY):
            sliderPos = min(1400, max(1225, mouseX - app.blush.sliderOffset))
            app.blush.lineWidth = (sliderPos - 1225) // 20 + 1


def game_onMouseRelease(app, mouseX, mouseY):
    eyelinerOnMouseRelease(app, mouseX, mouseY)
    lipstickOnMouseRelease(app, mouseX, mouseY)
    blushOnMouseRelease(app, mouseX, mouseY)
    
def eyelinerOnMouseRelease(app, mouseX, mouseY):
    app.eyeliner.dragging = False
    app.eyeliner.mouseReleased = True
    app.eyeliner.lines.append(app.eyeliner.prevMousePositions)
    app.eyeliner.sliderDragged = True

def lipstickOnMouseRelease(app, mouseX, mouseY):
    app.lipstick.dragging = False
    app.lipstick.mouseReleased = True
    app.lipstick.lines.append(app.lipstick.prevMousePositions)
    app.lipstick.sliderDragged = True

def blushOnMouseRelease(app, mouseX, mouseY):
    app.blush.dragging = False
    app.blush.mouseReleased = True
    app.blush.lines.append(app.blush.prevMousePositions)
    app.blush.sliderDragged = True



def game_onMousePress(app, mouseX, mouseY):
    eyelinerOnMousePress(app, mouseX, mouseY)
    lipstickOnMousePress(app, mouseX, mouseY)
    blushOnMousePress(app, mouseX, mouseY)
    app.doneButton.checkForPress(app, mouseX, mouseY)

def end_onMousePress(app, mouseX, mouseY):
    app.replayButton.checkForPress(app, mouseX, mouseY)
   
def eyelinerOnMousePress(app, mouseX, mouseY):
    if app.eyeliner.eyelinerPressed(mouseX, mouseY):
        if app.eyeliner.eyelinerMode:
            app.lipstick.lipstickMode = False
            app.blush.blushMode = False
    
        #drawing the line
        if not app.eyeliner.mouseReleased:
            app.eyeliner.dragging = True
            app.eyeliner.prevMousePositions = [(mouseX, mouseY)]
        app.eyeliner.mouseReleased = False

    if app.eyeliner.eyelinerMode: 
        #blackE pressed
        if (app.blackE.clickedInside(mouseX, mouseY)):
            app.eyeliner.color = 'black'
        #brownE pressed
        elif (app.brownE.clickedInside(mouseX, mouseY)):
            app.eyeliner.color = 'saddleBrown'
        #pinkE pressed
        elif (app.pinkE.clickedInside(mouseX, mouseY)):
            app.eyeliner.color = 'deepPink'
        #purpleE pressed
        elif (app.purpleE.clickedInside(mouseX, mouseY)):
            app.eyeliner.color = 'darkViolet'
        #greenE pressed
        elif (app.greenE.clickedInside(mouseX, mouseY)):
            app.eyeliner.color = 'limeGreen'
        #blueE pressed
        elif (app.blueE.clickedInside(mouseX, mouseY)):
            app.eyeliner.color = 'royalBlue'
        #clear eyeliner pressed
        elif (app.eraserE.clickedInside(mouseX, mouseY)):
            app.eyeliner.color = None
            app.eyeliner.prevMousePositions = []
            app.eyeliner.lines = []
    
def lipstickOnMousePress(app, mouseX, mouseY):
    if app.lipstick.lipstickPressed(mouseX, mouseY):
        if app.lipstick.lipstickMode:
            app.eyeliner.eyelinerMode = False
            app.blush.blushMode = False
    
        #drawing the line
        if not app.lipstick.mouseReleased:
            app.lipstick.dragging = True
            app.lipstick.prevMousePositions = [(mouseX, mouseY)]
        app.lipstick.mouseReleased = False

    if app.lipstick.lipstickMode:   
        #hotPinkL pressed
        if (app.hotPinkL.clickedInside(mouseX, mouseY)):
            app.lipstick.color = 'hotPink'
        #crimsonL pressed
        elif (app.crimsonL.clickedInside(mouseX, mouseY)):
            app.lipstick.color = 'crimson'
        #deepPinkL Pressed
        elif (app.deepPinkL.clickedInside(mouseX, mouseY)):
            app.lipstick.color = 'deepPink'
        #darkRedL
        elif (app.darkRedL.clickedInside(mouseX, mouseY)):
            app.lipstick.color = 'darkRed'
        #magentaL
        elif (app.magentaL.clickedInside(mouseX, mouseY)):
            app.lipstick.color = 'magenta'
        #darkMagentaL
        elif (app.darkMagentaL.clickedInside(mouseX, mouseY)):
            app.lipstick.color = 'darkMagenta'
        elif (app.eraserL.clickedInside(mouseX, mouseY)):
            app.lipstick.color = None
            app.lipstick.prevMousePositions = []
            app.lipstick.lines = []

def blushOnMousePress(app, mouseX, mouseY):
    if app.blush.blushPressed(mouseX, mouseY):
        if app.blush.blushMode:
            app.lipstick.lipstickMode = False
            app.eyeliner.eyelinerMode = False
        #drawing the line
        if not app.blush.mouseReleased:
            app.blush.dragging = True
            app.blush.prevMousePositions = [(mouseX, mouseY)]
        app.blush.mouseReleased = False

    if app.blush.blushMode:   
        #hotPinkL pressed
        if (app.hotPinkB.clickedInside(mouseX, mouseY)):
            app.blush.color = 'hotPink'
        #crimsonL pressed
        elif (app.crimsonB.clickedInside(mouseX, mouseY)):
            app.blush.color = 'crimson'
        #deepPinkL Pressed
        elif (app.deepPinkB.clickedInside(mouseX, mouseY)):
            app.blush.color = 'deepPink'
        #darkRedL
        elif (app.darkRedB.clickedInside(mouseX, mouseY)):
            app.blush.color = 'darkRed'
        #magentaL
        elif (app.magentaB.clickedInside(mouseX, mouseY)):
            app.blush.color = 'magenta'
        #darkMagentaL
        elif (app.darkMagentaB.clickedInside(mouseX, mouseY)):
            app.blush.color = 'darkMagenta'
        elif (app.eraserB.clickedInside(mouseX, mouseY)):
            app.blush.color = None
            app.blush.prevMousePositions = []
            app.blush.lines = []

def main():
    runAppWithScreens(initialScreen='start')
    runApp(width=2000, height=1000)

if __name__ == '__main__':
    main()