import tkinter as tk

#TODO: 
#   - XY Validation
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

def starting_point(event):
    newCanvas.old_x = event.x
    newCanvas.old_y = event.y

def paint(event):
    newCanvas.create_line(newCanvas.old_x, newCanvas.old_y, event.x, event.y, width=2)
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
            newCanvas.config(cursor="spider")
        case 4:
            newCanvas.config(cursor="pirate")
    

def createCanvas():        
    canvasWindow = tk.Tk()
    canvasWindow.title("Canvas")

    canvasContainer = tk.Frame(canvasWindow, height=getY()+100, width=getX()+100, background='#ffffff')
    canvasContainer.grid()

    labelTools = tk.Label(canvasContainer, text="Tools")
    labelTools.grid(row=0, column=0)

    # I'm not sure why but the commands automatically activate unless I use lambda 
    selectPencil = tk.Button(canvasContainer, text="Pencil", command=lambda: changeTool(1) )  
    selectPencil.grid(row=0, column=1)

    selectEraser = tk.Button(canvasContainer, text="Eraser", command=lambda: changeTool(2) )
    selectEraser.grid(row=0, column=2)

    selectTemp1 = tk.Button(canvasContainer, text="Temp", command=lambda: changeTool(3) ) 
    selectTemp1.grid(row=0, column=3)

    selectTemp2 = tk.Button(canvasContainer, text="Temp2", command=lambda: changeTool(4) )
    selectTemp2.grid(row=0, column=4)

    global newCanvas
    newCanvas = tk.Canvas(canvasContainer, height=getY(), width=getX(), background=RGBtoHEX(), cursor="pencil")
    newCanvas.grid(row=1, column=0, columnspan=5)

    newCanvas.bind("<Button-1>", starting_point)
    newCanvas.bind("<B1-Motion>", paint)

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