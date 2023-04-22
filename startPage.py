# from cmu_graphics import *
# from PIL import Image
# import os, pathlib

def openImage(fileName):
    return Image.open(os.path.join(pathlib.Path(__file__).parent,fileName))

def onAppStart(app):  
    app.fairyImg = Image.open('images/fairy.png')
    app.bgImg = Image.open('images/bg.png')
    #changing size of image
    newsize = (300, 400)
    app.fairyImg = app.fairyImg.resize(newsize)
    #converting to CMU image type
    app.fairyImg = CMUImage(app.fairyImg)
    app.bgImg = CMUImage(app.bgImg)

def redrawAll(app):
    drawImage(app.bgImg, 0, 0)
    drawImage(app.fairyImg, 80, 300)
    drawOval(900, 400, 900, 600, fill='pink')
    drawRegularPolygon(460, 440, 50, 3, fill='pink')
    drawLabel("Welcome To", 900, 250, size=50, fill='mediumVioletRed')
    drawLabel("MAGIC MAKEUP", 900, 350, size=90, fill='mediumVioletRed', bold=True)
    drawRect(800, 450, 200, 100, fill='hotPink', border='mediumVioletRed') 
    drawLabel("Next", 900, 500, size=50, fill='mediumVioletRed')

def main():
    runApp(width=2000, height=1000)

if __name__ == '__main__':
    main()