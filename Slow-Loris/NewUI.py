
import tkinter as tkinter
from  AttackManager import AttackManager

class Application():
    def __init__(self):

        self.scene = tkinter.Tk()

        self.scene.title("Slow Loris Tool 4416")
        # Screen Size
        self.scene.geometry("400x300")

        # Menu
        self.lorisMenu = tkinter.Menu(self.scene)

        self.helpButton = tkinter.Button(text="Open Readme", width=10, height=3, bg="snow4", fg="grey1",command= lambda : self.openHelp())

        # Attack Button
        self.attack = tkinter.Button(text="Start Attack", width=10, height=3, bg="snow4", fg="grey1",command= lambda : self.beginAttack())

        self.targetText = tkinter.Label(text="Target Address")

        self.socketsToUse = tkinter.Label(text="Socket Count")

        # An entry field for getting the target of the attack
        self.target = tkinter.Entry(fg="grey1", bg="snow4", width=50)

        self.socketCount = tkinter.Entry(fg="grey1", bg="snow4", width=5)

        self.attack.place(x=165, y=100)

        self.target.place(x=50, y=90)

        self.socketCount.place(x=50, y=140)

        self.targetText.place(x=165, y=70)

        self.socketsToUse.place(x=50, y=120)

        self.helpButton.place(x=165, y=200)

    # Open a help window
    def openHelp(self):
        helpWindow = tkinter.Toplevel()

        helpWindow.title("Help")

        helpWindow.geometry("800x400")

        helpText = tkinter.Text(helpWindow)

        contents = open("readme.txt","r")

        helpText.insert("1.0", contents.read())

        contents.close()

        helpText.config(state="disabled")

        helpText.pack()

    def beginAttack(self):
        lorisManager = AttackManager(self.target.get(),int(self.socketCount.get()))

        lorisManager.attack()

    def start(self):
        self.scene.mainloop()
test = Application()
test.start()

