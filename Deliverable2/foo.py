# winsoundDemo.py
#
# beep

from Tkinter import *
import winsound

def playSound(canvas, synchronous):
    if (synchronous):
        flags = winsound.SND_FILENAME
    else:
        # asynchronous
        flags = winsound.SND_FILENAME | winsound.SND_ASYNC
    canvas.data["soundCounter"] += 1
    sounds = ["sound1.wav", "sound2.wav", "sound3.wav" ]
    sound = sounds[canvas.data["soundCounter"] % len(sounds)]
    winsound.PlaySound(sound, flags)

def startSoundLoop():
    flags = winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP
    winsound.PlaySound("sound1.wav", flags)

def stopSoundLoop():
    flags = winsound.SND_FILENAME
    winsound.PlaySound(None, flags)

def keyPressed(event):
    canvas = event.widget.canvas
    if (event.char == "p"):
        playSound(canvas, True) # synchronous
    elif (event.char == "a"):
        playSound(canvas, False) # asynchronous
    elif (event.char == "l"):
        startSoundLoop()
    elif (event.char == "s"):
        stopSoundLoop()
    else:
        # quick short high beep
        hertz = 1760
        milliseconds = 64
        winsound.Beep(hertz, milliseconds)
    redrawAll(canvas)

def redrawAll(canvas):
    canvas.delete(ALL)
    font = ("Arial", 24, "bold")
    # Draw the event info
    msg = "Press p to play synchronous sound"
    canvas.create_text(300, 100, text=msg, font=font)
    msg = "Press a to play asynchronous sound"
    canvas.create_text(300, 200, text=msg, font=font)
    msg = "Press l to start loop"
    canvas.create_text(300, 300, text=msg, font=font)
    msg = "Press s to stop loop"
    canvas.create_text(300, 400, text=msg, font=font)

def init(canvas):
    canvas.data["soundCounter"] = 0
    redrawAll(canvas)

########### copy-paste below here ###########

def run():
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=600, height=500)
    canvas.pack()
    # Store canvas in root and in canvas itself for callbacks
    root.canvas = canvas.canvas = canvas
    # Set up canvas data and call init
    canvas.data = { }
    init(canvas)
    # set up events
    root.bind("<Key>", keyPressed)
    # timerFired(canvas)
    # and launch the app
    root.mainloop()  # This call BLOCKS (so your program waits until you close the window!)

run()
