from tkinter import *
import LEDlib
import re


mainwin = Tk(className = " LED Simulator")
mainwin.geometry("1200x880")
canvas1 = Canvas(mainwin,width = 1200, height = 880, bg = "black")
canvas1.place(x=-1,y=-1)

psize = 12

charPacmanBlinky = [(0,6,"#FF0000"), (0,7,"#FF0000"), (0,8,"#FF0000"), (0,9,"#FF0000"), (0,10,"#FF0000"), (0,11,"#FF0000"), (0,12,"#FF0000"), (0,13,"#FF0000"), (0,14,"#FF0000"), (1,3,"#FF0000"), (1,4,"#FFFFFF"), (1,5,"#0000FF"), (1,6,"#0000FF"), (1,7,"#FF0000"), (1,8,"#FF0000"), (1,9,"#FF0000"), (1,10,"#FF0000"), (1,11,"#FF0000"), (1,12,"#FF0000"), (1,13,"#FF0000"), (2,2,"#FF0000"), (2,3,"#FFFFFF"), (2,4,"#FFFFFF"), (2,5,"#0000FF"), (2,6,"#0000FF"), (2,7,"#FFFFFF"), (2,8,"#FF0000"), (2,9,"#FF0000"), (2,10,"#FF0000"), (2,11,"#FF0000"), (2,12,"#FF0000"), (3,1,"#FF0000"), (3,2,"#FF0000"), (3,3,"#FFFFFF"), (3,4,"#FFFFFF"), (3,5,"#FFFFFF"), (3,6,"#FFFFFF"), (3,7,"#FFFFFF"), (3,8,"#FF0000"), (3,9,"#FF0000"), (3,10,"#FF0000"), (3,11,"#FF0000"), (3,12,"#FF0000"), (3,13,"#FF0000"), (4,1,"#FF0000"), (4,2,"#FF0000"), (4,3,"#FF0000"), (4,4,"#FFFFFF"), (4,5,"#FFFFFF"), (4,6,"#FFFFFF"), (4,7,"#FF0000"), (4,8,"#FF0000"), (4,9,"#FF0000"), (4,10,"#FF0000"), (4,11,"#FF0000"), (4,12,"#FF0000"), (4,13,"#FF0000"), (4,14,"#FF0000"), (5,0,"#FF0000"), (5,1,"#FF0000"), (5,2,"#FF0000"), (5,3,"#FF0000"), (5,4,"#FF0000"), (5,5,"#FF0000"), (5,6,"#FF0000"), (5,7,"#FF0000"), (5,8,"#FF0000"), (5,9,"#FF0000"), (5,10,"#FF0000"), (5,11,"#FF0000"), (5,12,"#FF0000"), (5,13,"#FF0000"), (5,14,"#FF0000"), (6,0,"#FF0000"), (6,1,"#FF0000"), (6,2,"#FF0000"), (6,3,"#FF0000"), (6,4,"#FF0000"), (6,5,"#FF0000"), (6,6,"#FF0000"), (6,7,"#FF0000"), (6,8,"#FF0000"), (6,9,"#FF0000"), (6,10,"#FF0000"), (6,11,"#FF0000"), (6,12,"#FF0000"), (7,0,"#FF0000"), (7,1,"#FF0000"), (7,2,"#FF0000"), (7,3,"#FF0000"), (7,4,"#FFFFFF"), (7,5,"#0000FF"), (7,6,"#0000FF"), (7,7,"#FF0000"), (7,8,"#FF0000"), (7,9,"#FF0000"), (7,10,"#FF0000"), (7,11,"#FF0000"), (7,12,"#FF0000"), (8,0,"#FF0000"), (8,1,"#FF0000"), (8,2,"#FF0000"), (8,3,"#FFFFFF"), (8,4,"#FFFFFF"), (8,5,"#0000FF"), (8,6,"#0000FF"), (8,7,"#FFFFFF"), (8,8,"#FF0000"), (8,9,"#FF0000"), (8,10,"#FF0000"), (8,11,"#FF0000"), (8,12,"#FF0000"), (8,13,"#FF0000"), (8,14,"#FF0000"), (9,1,"#FF0000"), (9,2,"#FF0000"), (9,3,"#FFFFFF"), (9,4,"#FFFFFF"), (9,5,"#FFFFFF"), (9,6,"#FFFFFF"), (9,7,"#FFFFFF"), (9,8,"#FF0000"), (9,9,"#FF0000"), (9,10,"#FF0000"), (9,11,"#FF0000"), (9,12,"#FF0000"), (9,13,"#FF0000"), (9,14,"#FF0000"), (10,1,"#FF0000"), (10,2,"#FF0000"), (10,3,"#FF0000"), (10,4,"#FFFFFF"), (10,5,"#FFFFFF"), (10,6,"#FFFFFF"), (10,7,"#FF0000"), (10,8,"#FF0000"), (10,9,"#FF0000"), (10,10,"#FF0000"), (10,11,"#FF0000"), (10,12,"#FF0000"), (10,13,"#FF0000"), (11,2,"#FF0000"), (11,3,"#FF0000"), (11,4,"#FF0000"), (11,5,"#FF0000"), (11,6,"#FF0000"), (11,7,"#FF0000"), (11,8,"#FF0000"), (11,9,"#FF0000"), (11,10,"#FF0000"), (11,11,"#FF0000"), (11,12,"#FF0000"), (12,3,"#FF0000"), (12,4,"#FF0000"), (12,5,"#FF0000"), (12,6,"#FF0000"), (12,7,"#FF0000"), (12,8,"#FF0000"), (12,9,"#FF0000"), (12,10,"#FF0000"), (12,11,"#FF0000"), (12,12,"#FF0000"), (12,13,"#FF0000"), (13,4,"#FF0000"), (13,5,"#FF0000"), (13,6,"#FF0000"), (13,7,"#FF0000"), (13,8,"#FF0000"), (13,9,"#FF0000"), (13,10,"#FF0000"), (13,11,"#FF0000"), (13,12,"#FF0000"), (13,13,"#FF0000"), (13,14,"#FF0000")]
LEDpoints = []

colourRed   = "#FF0000"
colourWhite = "#FFFFFF"
colourBlack = "#000000"
colourBlue  = "#0000FF"
colourBlueLight = "#B5B3F5"
colourGrey  = "#AAAAAA"
colourPink  = "#F498EC"
colourGreen = "#279627"
colourGreenLight = "#90EE90"
colourOrange = "#FF5900"
colourOrangeLight = "#FFA07A"
colourYellow = "#FFFF00"
colourBrown = "#8B4513"
colourBrownLight = "#C19153"
colourBrownDark = "#4C3A23"
colourAqua = "#00FFFF"
colourPurple = "#BE1CBE"

selectedColour = colourWhite



def CopyText():
   textOutput.tag_add('sel','1.0','end')
   selected_text = textOutput.get(SEL_FIRST, SEL_LAST)
   mainwin.clipboard_clear()
   mainwin.clipboard_append(selected_text)

btnCopyText = Button(mainwin,text="Copy the above pixel text to clipboard", bg="black", fg="white", command = CopyText)
btnCopyText.place(x=700,y=840)


def chooseBrownDark():
   global selectedColour
   selectedColour = colourBrownDark

btnBrownDark = Button(mainwin,text="Dark Brown", bg="black", fg="white", command = chooseBrownDark)
btnBrownDark.place(x=20,y=300)

def chooseGreenLight():
   global selectedColour
   selectedColour = colourGreenLight

btnGreenLight = Button(mainwin,text="LIGHT GREEN", bg="black", fg="white", command = chooseGreenLight)
btnGreenLight.place(x=100,y=400)

def chooseOrangeLight():
   global selectedColour
   selectedColour = colourOrangeLight

btnOrangeLight = Button(mainwin,text="LIGHT ORANGE", bg="black", fg="white", command = chooseOrangeLight)
btnOrangeLight.place(x=100,y=425)

def chooseBrownLight():
   global selectedColour
   selectedColour = colourBrownLight

btnBrownLight = Button(mainwin,text="LIGHT BROWN", bg="black", fg="white", command = chooseBrownLight)
btnBrownLight.place(x=100,y=325)

def chooseAqua():
   global selectedColour
   selectedColour = colourAqua

btnAqua = Button(mainwin,text="AQUA", bg="black", fg="white", command = chooseAqua)
btnAqua.place(x=100,y=350)

def choosePurple():
   global selectedColour
   selectedColour = colourPurple

btnPurple = Button(mainwin,text="PURPLE", bg="black", fg="white", command = choosePurple)
btnPurple.place(x=100,y=375)

def chooseBrown():
   global selectedColour
   selectedColour = colourBrown

btnBrown = Button(mainwin,text="BROWN", bg="black", fg="white", command = chooseBrown)
btnBrown.place(x=100,y=300)

def chooseYellow():
   global selectedColour
   selectedColour = colourYellow

btnYellow = Button(mainwin,text="YELLOW", bg="black", fg="white", command = chooseYellow)
btnYellow.place(x=100,y=275)

def chooseGrey():
   global selectedColour
   selectedColour = colourGrey

btnGrey = Button(mainwin,text="GREY", bg="black", fg="white", command = chooseGrey)
btnGrey.place(x=100,y=250)

def choosePink():
   global selectedColour
   selectedColour = colourPink

btnPink = Button(mainwin,text="PINK", bg="black", fg="white", command = choosePink)
btnPink.place(x=100,y=225)

def chooseGreen():
   global selectedColour
   selectedColour = colourGreen

btnGreen = Button(mainwin,text="GREEN", bg="black", fg="white", command = chooseGreen)
btnGreen.place(x=100,y=200)

def chooseOrange():
   global selectedColour
   selectedColour = colourOrange

btnOrange = Button(mainwin,text="ORANGE", bg="black", fg="white", command = chooseOrange)
btnOrange.place(x=100,y=175)

def chooseRed():
   global selectedColour
   selectedColour = colourRed

btnRed = Button(mainwin,text="RED", bg="black", fg="white", command = chooseRed)
btnRed.place(x=100,y=150)   

def chooseBlue():
   global selectedColour
   selectedColour = colourBlue

btnBlue = Button(mainwin,text="BLUE", bg="black", fg="white", command = chooseBlue)
btnBlue.place(x=100,y=125) 

def chooseBlueLight():
   global selectedColour
   selectedColour = colourBlueLight

btnBlueLight = Button(mainwin,text="light blue", bg="black", fg="white", command = chooseBlueLight)
btnBlueLight.place(x=20,y=125) 

def chooseWhite():
   global selectedColour
   selectedColour = colourWhite

btnWhite = Button(mainwin,text="WHITE", bg="black", fg="white", command = chooseWhite)
btnWhite.place(x=100,y=100) 

def chooseBlack():
   global selectedColour
   selectedColour = colourBlack

btnBlack = Button(mainwin,text="BLACK", bg="black", fg="white", command = chooseBlack)
btnBlack.place(x=100,y=75) 

class ButtonManager:
    def __init__(self, button,x,y):
        self.button = button
        self.x = x
        self.y = y
        self.colour = colourBlack  # Track the button's color state
        self.button.config(command=self.toggle_color, activebackground="black")

    def toggle_color(self):
        global LEDpoints
        self.button.config(bg=selectedColour, activebackground=selectedColour)
        self.colour = selectedColour
        textOutput.delete("1.0","end-1c")
        whitebuttons = []
        whitebuttonsxy = []
        for b in buttons:
            if b.colour != colourBlack:
             whitebuttons.append(b)
            whitebuttonsxy.append((b.x,b.y,b.colour))
        for b in whitebuttons:
            textOutput.insert(INSERT,"("+str(b.x)+","+str(b.y)+",\""+str(b.colour)+"\")")
            if b != whitebuttons[-1]:
               textOutput.insert(INSERT,", ")
        LEDlib.Erasepoints(canvas1,LEDpoints)
        LEDpoints = []
        LEDlib.psize = 3
        LEDlib.createCharColour(canvas1,10, 10, whitebuttonsxy,LEDpoints)
        LEDlib.createCharColourSolid(canvas1,1100, 10, whitebuttonsxy,LEDpoints)
        LEDlib.psize = 2
        LEDlib.createCharColourSolid(canvas1,1100, 200, whitebuttonsxy,LEDpoints)
        LEDlib.psize = 1
        LEDlib.createCharColourSolid(canvas1,1100, 400, whitebuttonsxy,LEDpoints)



buttons = []
for i in range(24):
    for j in range(24):
      button = Button(mainwin, text=" ", bg="black", fg="white")
      button.place(x=i*35+200,y=20+j*30+10)
      buttons.append(ButtonManager(button,i,j))


textInput = Text(mainwin,width=80,height=6,bg="black",fg="yellow")
textInput.place(x=0,y=750)
textOutput = Text(mainwin,width=80,height=6,bg="black",fg="orange")
textOutput.place(x=600,y=750)

def cleargrid():
     for b in buttons:
       b.is_white = False
       b.button.config(bg="black") 

def ReadData():
    global selectedColour
    count = 0
    cleargrid()
    coordinate_string = textInput.get("1.0", END)
    # Regular expression to extract pairs of numbers
    matches = re.findall(r'\((\d+),(\d+),\"(#\w+)\"\)', coordinate_string)
    # Convert matches to a list of tuples
    coordinates = [(int(x),int(y),z) for x,y,z in matches]
    for x,y,z in coordinates:
       for b in buttons:
         if b.x == x and b.y == y:
          selectedColour = z
          count = count + 1
          b.colour = selectedColour
          b.toggle_color()
          print("reading ...", count)
       
btnRead = Button(mainwin,text="READ from this text", bg="black", fg="white", command = ReadData)
btnRead.place(x=50,y=720)

def Erase():
    LEDlib.Erasepoints(canvas1,LEDpoints)

btnErase = Button(mainwin,text="Erase", bg="black", fg="white", command = Erase)
btnErase.place(x=100,y=500)

mainwin.mainloop()
