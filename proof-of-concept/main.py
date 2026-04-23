#import necessary modules
import time as t
import tkinter
import random as r
import threading
import playsound
import os, sys
import audioread #for determining audio file length

#necessary global variables -> need to be accessible by all functions
days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
month = 1 #each month has 28 days (4 weeks) for the sake of simplicity. this is only a proof of concept.
week = 1
day = 0
daysElapsed = 0 #two different variables needed here. "day" is to count days of the week/month and "daysElapsed" is for counting time differences needed for policy/government change
phrases = ["I need a new hobby...","How many more days of this again?","Another day, another policy."]

#tooltips for buttons
class ToolTip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip_window = None

        # Bind hover events
        widget.bind("<Enter>", self.show_tooltip)
        widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event):
        # Create a tooltip window
        x = self.widget.winfo_rootx() + 20
        y = self.widget.winfo_rooty() + 20
        self.tooltip_window = tw = tkinter.Toplevel(self.widget)
        tw.wm_overrideredirect(True) # Remove window decorations
        tw.geometry(f"+{x}+{y}")

        label = tkinter.Label(tw, text=self.text, background="darkgray", fg="white")
        label.pack()

    def hide_tooltip(self, event):
        if self.tooltip_window:
            self.tooltip_window.destroy()
            self.tooltip_window = None

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

#music player. in future, this will be changeable depending on political system
def playMusic():
    while True:
        with audioread.audio_open(f"Republic 1.mp3") as f:
            duration = f.duration
        song = resource_path(f"Republic 1.mp3")
        playsound.playsound(song)
        t.sleep(duration)

def playSound(target):
    playsound.playsound(resource_path(target))



#GAME LOGIC -> Below are all of the functions that the game runs on top of.
def next_day():
    global day, days, month, week, phrases, daysElapsed, soundthread
    soundthread = threading.Thread(target=playSound, kwargs={"target":"eventSound.mp3"} ,daemon= True)
    day+=1
    daysElapsed+=1
    if day>6:
        day = 0
        week+=1
    if daysElapsed>=28:
        month+=1
        week=1
        daysElapsed=0
    mainText.config(text=f"{days[day]}, Week {week}, Month {month}\n-----------------------\n{phrases[r.randint(0,2)]}")
    mainWindow.update_idletasks()

    #Create randomly-ocurring events
    if r.randint(0,7)==7:
        soundthread.start()
        t.sleep(0.2)
        event = tkinter.Toplevel()
        event.geometry("200x200")
        event.title("Event!")
        event.config(background="black")
        desc = tkinter.Label(event, text=f"EVENT!\n\nA thing has happened!\n\n",bg = "black",fg="white")
        opt=[
            tkinter.Button(event,text="Do This",bg="gold"),
            tkinter.Button(event,text="Do That",bg="gold"),
            tkinter.Button(event,text="Do Something Else",bg = "gold"),
            tkinter.Button(event,text="Ignore",bg="gold")
        ]
        desc.pack()
        for i in opt:
            i.pack()
        optTip = [
            ToolTip(opt[0],"This will be good for the economy!"),
            ToolTip(opt[1],"This will be good for our popularity!"),
            ToolTip(opt[2],"This will give us a new policy!"),
            ToolTip(opt[3],"This will give us new focuses!")
            ]

#POLICIES!
#Policies can be taken either after completing focuses or making decisions based on affairs that people bring you. They only last for a certain duration of time, but some can be renewed. This has not been implemented yet.
#The idea is also that, in future, things like military, healthcare and education spending can be changed here (depending on ideology).
#Particular areas of scientific interest can also be policies (for example, "Modern Fighter Jets" or "Improved Cancer Research" can be policies.)
#The buttons would, in an ideal world, be clickable to view policy information. This has not been implemented.
def POLICIES():
    polWindow = tkinter.Toplevel()
    polWindow.geometry("200x200")
    polWindow.config(background="black")
    policy = tkinter.Label(polWindow, text=f"Our current policies are:",bg = "black",fg="white")
    policies=[
        tkinter.Button(polWindow,text="Military Reforms",bg="gold"),
        tkinter.Button(polWindow,text="Heightened Internationalism",bg="gold"),
        tkinter.Button(polWindow,text="Trading Co-operation",bg = "gold"),
        tkinter.Button(polWindow,text="Fostering Economic Growth",bg="gold"),
        tkinter.Button(polWindow,text="Intercontinental Ballistic Missiles",bg="gold"),
        tkinter.Button(polWindow,text="The Space Program",bg = "gold")
        
    ]
    policy.pack()
    for i in policies:
        i.pack()

#THE ECONOMY!
#The economy is partially influenced by random trade factors, but also by world events, government policies, focuses, ideology, etc.
def ECONOMY():
    ecWindow = tkinter.Toplevel()
    ecWindow.geometry("200x200")
    ecWindow.config(background="black")
    ecLabel = tkinter.Label(ecWindow, text="Business is boooming!\n\nThe National Stock Index is UP.",bg = "black",fg="white")
    ecLabel.pack()

#WORLD AFFAIRS!
#World affairs are the news and also events that reach the government. They allow you to take policies, change ideologies, influence the economy or the army, and more.
def AFFAIRS():
    affWindow = tkinter.Toplevel()
    affWindow.geometry("300x200")
    affWindow.config(background="black")
    affLabel = tkinter.Label(affWindow, text="BROADCASTING COMPANY:\n\nNothing to report from the Broadcasting Station.\n\n\nEMERGENCY ALERT SYSTEM:\n\nAll quiet from here.\n\n\nCABINET AND ADVISORS:\n\nNo news or issues to report.",bg = "black",fg="white")
    affLabel.pack()

#IDEOLOGY!
#The ideology of the government affects things like focuses, policies and events/affairs. It can also have impacts on the economy, open up new positions in cabinet or bring in new affairs, policies or events.
def IDEOLOGY():
    idWindow = tkinter.Toplevel()
    idWindow.geometry("300x200")
    idWindow.config(background="black")
    idLabel = tkinter.Label(idWindow, text="CURRENT IDEOLOGY:\n\nOur current ideology is SOCIAL LIBERALISM.\n\nSUPPORT:\n\nWe have 84% support for this ideology.\n\nAn ideology change is\nNOT ADVISED\nat this time.",bg = "black",fg="white")
    idLabel.pack()

#THE CABINET!
#The cabinet is where party support and tension can be viewed, as well as the potential threat of defectors and also the chance of new members. Here, critical roles like "Secretary of state" or "Commissar for war" (Communism exclusive) can be assigned, too.
def CABINET():
    cabWindow = tkinter.Toplevel()
    cabWindow.geometry("300x200")
    cabWindow.config(background="black")
    cabLabel = tkinter.Label(cabWindow, text="CABINET SUPPORT:\n\nWe have the support of 97% of our cabinet.\n\nDEFECTORS:\n\nWe have a 1% chance of a defector in the next month.\n\nHIGH-RANK POSITIONS:\n\nThere is no current demand for high-ranking positions.",bg = "black",fg="white")
    cabLabel.pack()

#FOCUSES!
#The focuses are semi-permanent "upgrades" to your government or nation (some are only permanent as long as your ideology stays the same). These will have benefits (and drawbacks!) on your nation and government, and can also unlock cabinet positions, policies or affairs.
def FOCUSES():
    focusWindow = tkinter.Toplevel()
    focusWindow.geometry("300x200")
    focusWindow.config(background="black")
    focusLabel = tkinter.Label(focusWindow, text="CURRENT FOCUS:\n\nOur current focus is CIVIL LIBERTIES\n\nThis focus is compatible with 4 other ideologies\n\n.",bg = "black",fg="white")
    focusLabel.pack()
    change = tkinter.Button(focusWindow,text="Change Focus",bg="gold",fg="black")
    change.pack()

if __name__ == "__main__":
    #set up main window
    mainWindow = tkinter.Tk()
    mainWindow.geometry("600x100")
    mainWindow.title("The President's Office")
    mainWindow.config(background="black")
    mainText = tkinter.Label(mainWindow, text=f"{days[day]}, Week {week}, Month {month}\n-----------------------\n{phrases[r.randint(0,2)]}",fg="white",bg="black")
    mainText.configure(anchor="center")
    mainText.pack()

    #menu buttons
    mainButtons = [
        tkinter.Button(mainWindow,text="POLICIES",bg="gold",command=POLICIES),
        tkinter.Button(mainWindow,text="ECONOMY",bg = "red",command=ECONOMY),
        tkinter.Button(mainWindow,text="AFFAIRS",bg="blue",command=AFFAIRS),
        tkinter.Button(mainWindow,text="IDEOLOGY",bg = "green",command=IDEOLOGY),
        tkinter.Button(mainWindow,text="CABINET",bg = "purple",command = CABINET),
        tkinter.Button(mainWindow,text="FOCUSES",bg = "orange",command=FOCUSES),
        tkinter.Button(mainWindow,text="NEXT DAY",bg = "white",command=next_day)
    ]

    #arrange buttons
    x = 0
    for i in range(len(mainButtons)):
        mainButtons[i].place(x=x,y=70)
        x +=89

    #start music thread
    musicThread = threading.Thread(target=playMusic, daemon=True)
    musicThread.start()


    #start game
    mainWindow.mainloop()
