#The last UI was terrible, let's try this instead
import asyncio
import tkinter as tkinter
from  AttackManager import AttackManager

class Application():
    def __init__(self):
        # Need to do real OOP with this and move the ui stuff in here. Also a selectable list of target ip's
        self.scene = tkinter.Tk()

        # Basic UI elements, need to redo this shit
        self.scene.title("Slow Loris Tool 4416")
        # Screen Size
        self.scene.geometry("400x300")

        # Menu
        self.lorisMenu = tkinter.Menu(self.scene)



        self.helpButton = tkinter.Button(text="Open Readme", width=10, height=3, bg="snow4", fg="grey1",command= lambda : self.openHelp())

        # Attack Button
        self.attack = tkinter.Button(text="Start Attack", width=10, height=3, bg="snow4", fg="grey1",command= lambda : self.beginAttack())

        self.targetText = tkinter.Label(text="Target Address")
        # Frame to contain info that happens during attack
        #self.attackStatusContainer = tkinter.Frame(self.scene, width=50, highlightbackground="grey1", highlightthickness=1,
              #                                bg="grey4", height=50)
        # The live feed of the attack
       # self.liveFeed = tkinter.Text(self.attackStatusContainer, width=50, bg="grey1", fg="green", height=50)

        #self.liveFeed.config(state="disabled")

       # self.attackStatus = tkinter.Label(text="Attack Status")
        # An entry field for getting the target of the attack
        self.target = tkinter.Entry(fg="grey1", bg="snow4", width=50)

        self.socketCount = tkinter.Entry(fg="grey1", bg="snow4", width=5)

        self.attack.place(x=165, y=100)

        self.target.place(x=50, y=90)

        self.socketCount.place(x=50, y=140)

        self.targetText.place(x=165, y=70)

        #self.attackStatus.place(x=160, y=175)

       # self.attackStatusContainer.place(x=1, y=200)

       #self.liveFeed.pack()

        # scene.config(menu=helpMenu)

        self.helpButton.pack()

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
