import tkinter as tkinter


class UserInterface:

    def __init__(self):
        pass

    # Need to do real OOP with this and move the ui stuff in here. Also a selectable list of target ip's
    scene = tkinter.Tk()

    # Basic UI elements, need to redo this shit
    scene.title("Slow Loris Tool 4416")

    scene.geometry("500x500")

    attack = tkinter.Button(text="Start Attack", width=10, height=3, bg="snow4", fg="grey1")

    targetText = tkinter.Label(text="Target Address")

    attackStatusContainer = tkinter.Frame(scene, width=499, highlightbackground="grey1", highlightthickness=3, bg="grey1", height=150)

    liveFeed = tkinter.Text(attackStatusContainer, width=100, bg="grey1", fg="green", height=150)

    liveFeed.config(state="disabled")


    attackStatus = tkinter.Label(text="Attack Status")

    target = tkinter.Entry(fg="grey1", bg="snow4", width=50)


    attack.place(x=215, y=200)

    target.place(x=100, y=190)

    targetText.place(x=100, y=170)

    attackStatus.place(x=215, y=275)

    attackStatusContainer.place(x=1, y=300)

    liveFeed.pack()



    scene.iconbitmap("AppIcon.ico")

    # Init method
    def init(self):
        self.scene.mainloop()


test = UserInterface()
test.init()
