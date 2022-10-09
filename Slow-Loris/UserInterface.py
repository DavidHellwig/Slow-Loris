import tkinter as tkinter
import AttackManager


class UserInterface:

    def __init__(self):
        pass

    # Need to do real OOP with this and move the ui stuff in here. Also a selectable list of target ip's
    scene = tkinter.Tk()

    # Basic UI elements, need to redo this shit
    scene.title("Slow Loris Tool 4416")
    #Screen Size
    scene.geometry("1280x720")

    #Menu
    lorisMenu = tkinter.Menu(scene)


    helpMenu = tkinter.Menu(lorisMenu,tearoff=0)
    helpMenu.add_command(label="Help",command= 2*2)


    #Attack Button
    attack = tkinter.Button(text="Start Attack", width=10, height=3, bg="snow4", fg="grey1")

    targetText = tkinter.Label(text="Target Address")
    #Frame to contain info that happens during attack
    attackStatusContainer = tkinter.Frame(scene, width=50, highlightbackground="grey1", highlightthickness=1, bg="grey4", height=50)
    #The live feed of the attack
    liveFeed = tkinter.Text(attackStatusContainer, width=50, bg="grey1", fg="green", height=50)

    liveFeed.config(state="disabled")


    attackStatus = tkinter.Label(text="Attack Status")
    #An entry field for getting the target of the attack
    target = tkinter.Entry(fg="grey1", bg="snow4", width=50)


    attack.place(x=165, y=100)

    target.place(x=50, y=90)

    targetText.place(x=165, y=70)

    attackStatus.place(x=160, y=175)

    attackStatusContainer.place(x=1, y=200)

    liveFeed.pack()

    scene.config(menu=helpMenu)





    scene.iconbitmap("AppIcon.ico")

    # Init method
    def init(self):

        self.scene.mainloop()


test = UserInterface()
test.init()
