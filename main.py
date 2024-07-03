import tkinter as tk

#TODO: 
#   - XY Validation
#   - Split main into smaller files (e.g. paint.py, erase.py etc.)
#   - Fix bug mentioned @ ln 31~

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

# BUG: it only starts painting once you move the mouse, you can't just press M1 to create a small dot. 
def starting_point(event):
    newCanvas.old_x = event.x
    newCanvas.old_y = event.y

def paint(event):
    newCanvas.create_line(newCanvas.old_x, newCanvas.old_y, event.x, event.y, width=2, fill=paintingColour)
    newCanvas.old_x = event.x 
    newCanvas.old_y = event.y

def erase(event):
    newCanvas.create_line(newCanvas.old_x, newCanvas.old_y, event.x, event.y, width=20, fill=RGBtoHEX())
    newCanvas.old_x = event.x 
    newCanvas.old_y = event.y    

def changeTool(num):
    match num:
        case 1:
            newCanvas.config(cursor="pencil")
            newCanvas.bind("<Button-1>", starting_point)
            newCanvas.bind("<B1-Motion>", paint)
        case 2:
            newCanvas.config(cursor="X_cursor")
            newCanvas.bind("<Button-1>", starting_point)
            newCanvas.bind("<B1-Motion>", erase)
        case 3:
            newCanvas.create_rectangle(0,0,getX(),getY(), fill=RGBtoHEX())    
        case 4:
            newCanvas.config(cursor="heart")

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

    selectTemp2 = tk.Button(canvasContainer, text="Temp2", command=lambda: changeTool(4) )
    selectTemp2.grid(row=0, column=4)

    labelColours = tk.Label(canvasContainer, text="Colours")
    labelColours.grid(row=1, column=0)

    # Colours Row
    #global selectRed
    selectRed = tk.Button(canvasContainer, text="Red", command=lambda: changeColour(1) )
    selectRed.grid(row=1, column=1)

    selectGreen = tk.Button(canvasContainer, text="Green", command=lambda: changeColour(2) )
    selectGreen.grid(row=1, column=2)

    selectBlue = tk.Button(canvasContainer, text="Blue", command=lambda: changeColour(3) )
    selectBlue.grid(row=1, column=3)

    selectYellow = tk.Button(canvasContainer, text="Yellow", command=lambda: changeColour(4) )
    selectYellow.grid(row=1, column=4)

    selectPink = tk.Button(canvasContainer, text="Pink", command=lambda: changeColour(5) )
    selectPink.grid(row=1, column=5)

    selectBlack = tk.Button(canvasContainer, text="Black", command=lambda: changeColour(0) )
    selectBlack.grid(row=1, column=6)

    global newCanvas
    newCanvas = tk.Canvas(canvasContainer, height=getY(), width=getX(), background=RGBtoHEX(), cursor="pencil")
    newCanvas.grid(row=2, column=0, columnspan=12)

    newCanvas.bind("<Button-1>", starting_point)
    newCanvas.bind("<B1-Motion>", paint)
    changeColour(0)

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
scaleR.grid(row=2, column=1)
scaleR.set(255)

labelG = tk.Label(frame, text="G: ")
labelG.grid(row=3, column=0)
scaleG = tk.Scale(frame, variable=int, from_= 0, to = 255, orient= "horizontal")
scaleG.grid(row=3, column=1)
scaleG.set(123)

labelB = tk.Label(frame, text="B: ")
labelB.grid(row=4, column=0)
scaleB = tk.Scale(frame, variable=int, from_= 0, to = 255, orient= "horizontal")
scaleB.grid(row=4, column=1)
scaleB.set(123)

buttonCreate = tk.Button(window, text="Create", command=createCanvas)
buttonCreate.pack()

window.resizable(False, False)
window.mainloop()