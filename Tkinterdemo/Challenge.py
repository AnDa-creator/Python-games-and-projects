# Write a GUI program to create a simple calculator
# layout that looks like the screenshot.
#
# Try to be as Pythonic as possible - it's ok if you
# end up writing repeated Button and Grid statements,
# but consider using lists and a for loop.
#
# There is no need to store the buttons in variables.
#
# As an optional extra, refer to the documentation to
# work out how to use minsize() to prevent your window
# from being shrunk so that the widgets vanish from view.
#
# Hint: You may want to use the widgets .winfo_height() and
# winfo_width() methods, in which case you should know that
# they will not return the correct results unless the window
# has been forced to draw the widgets by calling its .update()
# method first.
#
# If you are using Windows you will probably find that the
# width is already constrained and can't be resized too small.
# The height will still need to be constrained, though.


import tkinter
mainWindow = tkinter.Tk()
mainWindow.title("Calculator")
mainWindow.geometry("640x480")
mainWindow["padx"] = 10

mainWindow.rowconfigure( 0, weight=1)
mainWindow.rowconfigure( 1, weight=100)

# display widget
display = tkinter.Entry(mainWindow)
display.grid(row=0, column=0, sticky='nw')

#frame for buttons
buttonFrame = tkinter.Frame(mainWindow)
buttonFrame.grid(row=1, column=0, sticky='nw')

#Cancel buttons
Named_list = ['dummy', 'C', 'CE', '7', '8', '9', '+', '4', '5', '6', '-', '1', '2', '3', '*', '0', '=', '/']

for i in range(1,18):
        if Named_list[i] != '=':
            Button = tkinter.Button(buttonFrame, text=Named_list[i], width='3')
        else:
            Button = tkinter.Button(buttonFrame, text=Named_list[i], width='3')
        if i in range(1,3):
            Button.grid(row=0, column=i-1 ,sticky='nw')
        elif i in range(3, 7):
            Button.grid(row=1, column=i-3 , sticky='nw')
        elif i in range(7, 11):
            Button.grid(row=2, column=i-7, sticky='nw')
        elif i in range(11, 15):
            Button.grid(row=3, column=i-11, sticky='nw')
        elif i in range(15,18):
            Button.grid(row=4, column=i-15, sticky='nw')

mainWindow.update()
mainWindow.minsize(buttonFrame.winfo_width()
                   + 8, display.winfo_height()
                   + buttonFrame.winfo_height())
mainWindow.maxsize(buttonFrame.winfo_width()
                   + 50, display.winfo_height()+50
                   + buttonFrame.winfo_height())


mainWindow.mainloop()




