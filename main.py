import tkinter as tk

#TODO: 
#   - XY Validation in Create Menu
#   - Split main into smaller files (e.g. paint.py, erase.py etc.)

def getX():
    input = int(inputX.get())
    return input

def getY():
    input = int(inputY.get())
    return input

def getR():
    input = int(scaleR.get())
    return input

def getG():
    input = int(scaleG.get())
    return input

def getB():
    input = int(scaleB.get())
    return input

def RGBtoHEX():
    return '#%02x%02x%02x' % (getR(), getG(), getB())

def changeBrushSize(num):
    global brushSize
    match num:
        case 1:
            brushSize = 2
        case 2:
            brushSize = 6
        case 3:
            brushSize = 12
        case 4:
            brushSize = 24

def starting_point_brush(event):
    newCanvas.old_x = event.x
    newCanvas.old_y = event.y
    newCanvas.create_oval(newCanvas.old_x, newCanvas.old_y, event.x, event.y, width=brushSize, fill=paintingColour, outline=paintingColour)

def starting_point_shape(event):
    newCanvas.old_x = event.x
    newCanvas.old_y = event.y
    
    global startingX
    global startingY
    startingX = newCanvas.old_x
    startingY = newCanvas.old_y

def paint(event):
    newCanvas.create_oval(newCanvas.old_x, newCanvas.old_y, event.x, event.y, width=brushSize, fill=paintingColour, outline=paintingColour)
    newCanvas.old_x = event.x 
    newCanvas.old_y = event.y

def erase(event):
    newCanvas.create_oval(newCanvas.old_x, newCanvas.old_y, event.x, event.y, width=brushSize, fill=RGBtoHEX(), outline=RGBtoHEX())
    newCanvas.old_x = event.x 
    newCanvas.old_y = event.y

def rectangle(event):
    newCanvas.create_rectangle(startingX, startingY, event.x, event.y, width=brushSize, outline=paintingColour)

def circle(event):
    newCanvas.create_oval(startingX, startingY, event.x, event.y, width=brushSize, outline=paintingColour)

def arc(event):
    newCanvas.create_arc(startingX, startingY, event.x, event.y, width=brushSize, outline=paintingColour)

def isosceles(event):
    newCanvas.create_line(((event.x+startingX)/2), startingY, event.x, event.y, width=brushSize)
    newCanvas.create_line(event.x, event.y, startingX, event.y, width=brushSize)
    newCanvas.create_line(startingX, event.y, ((event.x+startingX)/2), startingY, width=brushSize)

def raTriangle(event):
    newCanvas.create_line(startingX, startingY, event.x, event.y, width=brushSize)
    newCanvas.create_line(event.x, event.y, startingX, event.y,  width=brushSize)
    newCanvas.create_line(startingX, event.y, startingX, startingY, width=brushSize)

def arrow(event):
    newCanvas.create_line(event.x, (event.y+startingY)/2, startingX, startingY, width=brushSize)
    newCanvas.create_line(event.x, (event.y+startingY)/2, startingX, event.y, width=brushSize)

    newCanvas.create_line(startingX, startingY, (startingX+event.x)/2, (startingY+event.y)/2, width=brushSize) # (startingX+event.x)/3 on var3 make a cool shape
    newCanvas.create_line(startingX, event.y, (startingX+event.x)/2, (startingY+event.y)/2, width=brushSize) # (startingX+event.x)/3 on var3 make a cool shape

def star(event):
    print("star")

def hexagon(event):
    print("hexagon")


def changeColour(num):
    global paintingColour
    match num:
        case 1:
            paintingColour = "red"
            #selectRed.config(relief="sunken")
        case 2:
            paintingColour = "green"
        case 3:
            paintingColour = "blue"
        case 4:
            paintingColour = "yellow"
        case 5:
            paintingColour = "pink"
        case 0:
            paintingColour = "black"

def changeTool(num):
    newCanvas.unbind("<Button-1>")
    newCanvas.unbind("<B1-Motion>")
    newCanvas.unbind("<ButtonRelease-1>")
    match num:
        case 1:
            newCanvas.config(cursor="pencil")
            newCanvas.bind("<Button-1>", starting_point_brush)
            newCanvas.bind("<B1-Motion>", paint)
        case 2:
            newCanvas.config(cursor="X_cursor")
            newCanvas.bind("<Button-1>", starting_point_brush)
            newCanvas.bind("<B1-Motion>", erase)
        case 3:
            newCanvas.create_rectangle(0,0,getX(),getY(), fill=RGBtoHEX())    
        case 4:
            newCanvas.config(cursor="heart")
            newCanvas.bind("<Button-1>", starting_point_shape)
            newCanvas.bind("<ButtonRelease-1>", rectangle)
        case 5:
            newCanvas.config(cursor="heart")
            newCanvas.bind("<Button-1>", starting_point_shape)
            newCanvas.bind("<ButtonRelease-1>", circle)
        case 6:
            newCanvas.config(cursor="heart")
            newCanvas.bind("<Button-1>", starting_point_shape)
            newCanvas.bind("<ButtonRelease-1>", arc)
        case 7:
            newCanvas.config(cursor="pirate")
            newCanvas.bind("<Button-1>", starting_point_shape)
            newCanvas.bind("<ButtonRelease-1>", isosceles)
        case 8:
            newCanvas.config(cursor="pirate")
            newCanvas.bind("<Button-1>", starting_point_shape)
            newCanvas.bind("<ButtonRelease-1>", raTriangle)
        case 9:
            newCanvas.config(cursor="X_cursor")
            newCanvas.bind("<Button-1>", starting_point_shape)
            newCanvas.bind("<ButtonRelease-1>", arrow)
        case 10:
            newCanvas.config(cursor="X_cursor")
            newCanvas.bind("<Button-1>", starting_point_shape)
            newCanvas.bind("<ButtonRelease-1>", star)
        case 11:
            newCanvas.config(cursor="X_cursor")
            newCanvas.bind("<Button-1>", starting_point_shape)
            newCanvas.bind("<ButtonRelease-1>", hexagon)
    

def createCanvas():        
    canvasWindow = tk.Tk()
    canvasWindow.title("Canvas")

    canvasContainer = tk.Frame(canvasWindow, height=getY()+100, width=getX()+100, background='#ffffff')
    canvasContainer.grid()

    labelTools = tk.Label(canvasContainer, text="Tools")
    labelTools.grid(row=0, column=0)

    # I'm not sure why but the commands automatically activate unless I use lambda 
    # Tools Row
    selectPencil = tk.Button(canvasContainer, text="Pencil", command=lambda: changeTool(1) )  
    selectPencil.grid(row=0, column=1)

    selectEraser = tk.Button(canvasContainer, text="Eraser", command=lambda: changeTool(2) )
    selectEraser.grid(row=0, column=2)

    selectClear = tk.Button(canvasContainer, text="Clear", command=lambda: changeTool(3) ) 
    selectClear.grid(row=0, column=3)

    # Brush size row
    labelBrushSize = tk.Label(canvasContainer, text="Brush Size")
    labelBrushSize.grid(row=1, column=0)

    selectSmall = tk.Button(canvasContainer, text="Small", command=lambda: changeBrushSize(1) )  
    selectSmall.grid(row=1, column=1)

    selectMedium = tk.Button(canvasContainer, text="Medium", command=lambda: changeBrushSize(2) )
    selectMedium.grid(row=1, column=2)

    selectLarge = tk.Button(canvasContainer, text="Large", command=lambda: changeBrushSize(3) ) 
    selectLarge.grid(row=1, column=3)

    selectXL = tk.Button(canvasContainer, text="XL", command=lambda: changeBrushSize(4) )
    selectXL.grid(row=1, column=4)

    # Colours Row
    labelColours = tk.Label(canvasContainer, text="Colours")
    labelColours.grid(row=2, column=0)

    #global selectRed
    selectRed = tk.Button(canvasContainer, text="Red", command=lambda: changeColour(1) )
    selectRed.grid(row=2, column=1)

    selectGreen = tk.Button(canvasContainer, text="Green", command=lambda: changeColour(2) )
    selectGreen.grid(row=2, column=2)

    selectBlue = tk.Button(canvasContainer, text="Blue", command=lambda: changeColour(3) )
    selectBlue.grid(row=2, column=3)

    selectYellow = tk.Button(canvasContainer, text="Yellow", command=lambda: changeColour(4) )
    selectYellow.grid(row=2, column=4)

    selectPink = tk.Button(canvasContainer, text="Pink", command=lambda: changeColour(5) )
    selectPink.grid(row=2, column=5)

    selectBlack = tk.Button(canvasContainer, text="Black", command=lambda: changeColour(0) )
    selectBlack.grid(row=2, column=6)

    # Shapes Row
    labelShapes = tk.Label(canvasContainer, text="Shapes")
    labelShapes.grid(row=3, column=0)

    selectSquare = tk.Button(canvasContainer, text="Square", command=lambda: changeTool(4) )
    selectSquare.grid(row=3, column=1)

    selectCircle = tk.Button(canvasContainer, text="Circle", command=lambda: changeTool(5) )
    selectCircle.grid(row=3, column=2)

    selectArc = tk.Button(canvasContainer, text="Arc", command=lambda: changeTool(6) )
    selectArc.grid(row=3, column=3)

    selectIsosceles = tk.Button(canvasContainer, text="Isosceles", command=lambda: changeTool(7) )
    selectIsosceles.grid(row=3, column=4)

    selectTriangle = tk.Button(canvasContainer, text="RA-Triangle", command=lambda: changeTool(8) )
    selectTriangle.grid(row=3, column=5)

    selectArrow = tk.Button(canvasContainer, text="Arrow Head", command=lambda: changeTool(9) )
    selectArrow.grid(row=3, column=6)

    selectStar = tk.Button(canvasContainer, text="Star", command=lambda: changeTool(10) )
    selectStar.grid(row=3, column=7)

    selectHexagon = tk.Button(canvasContainer, text="Hexagon", command=lambda: changeTool(11) )
    selectHexagon.grid(row=3, column=8)

    global newCanvas
    newCanvas = tk.Canvas(canvasContainer, height=getY(), width=getX(), background=RGBtoHEX(), cursor="pencil")
    newCanvas.grid(row=4, column=0, columnspan=12)

    newCanvas.bind("<Button-1>", starting_point_brush)
    newCanvas.bind("<B1-Motion>", paint)
    
    changeColour(0)
    changeBrushSize(1)

    canvasWindow.mainloop()


def intValidation(P):
    if str.isdigit(P) or P == "":
        return True
    else:
        return False

#
#   GUI 
#

window = tk.Tk()
window.title("Create")

frame = tk.Frame(window)
frame.pack()

# X/Y Values
labelX = tk.Label(frame, text="X: ")
labelX.grid(row=0, column=0)
inputX = tk.Entry(frame, width=10)
inputX.grid(row=0, column=1)
inputX.insert(0, 600)

labelY = tk.Label(frame, text="Y: ")
labelY.grid(row=0, column=3)
inputY = tk.Entry(frame, width=10)
inputY.grid(row=0, column=4)
inputY.insert(0, 600)

labelXYError = tk.Label(frame, text="")
labelXYError.grid(row=1,column=0)

# RGB Values
labelR = tk.Label(frame, text="R: ")
labelR.grid(row=2, column=0)
scaleR = tk.Scale(frame, variable=int, from_= 0, to = 255, orient= "horizontal")
scaleR.grid(row=2, column=1, columnspan=3)
scaleR.set(255)

labelG = tk.Label(frame, text="G: ")
labelG.grid(row=3, column=0)
scaleG = tk.Scale(frame, variable=int, from_= 0, to = 255, orient= "horizontal")
scaleG.grid(row=3, column=1, columnspan=3)
scaleG.set(123)

labelB = tk.Label(frame, text="B: ")
labelB.grid(row=4, column=0)
scaleB = tk.Scale(frame, variable=int, from_= 0, to = 255, orient= "horizontal")
scaleB.grid(row=4, column=1, columnspan=3)
scaleB.set(123)

buttonCreate = tk.Button(window, text="Create", command=createCanvas)
buttonCreate.pack()

window.resizable(False, False)
window.mainloop()