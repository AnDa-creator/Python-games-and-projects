import tkinter #class functions are called methods
import math

# Modify the circle function so that it allows the
# colour of the circle to be specified and defaults to red if
# a colour is not given. You may want to review the previous
# lectures about named parameters and default values.


def parabola(page, size):
    for x in range(-size, size):
        y = x*x / size
        plot(page, x, y)


def circle(page , radius, g, h, color="red"):
    page.create_oval(g + radius, h + radius, g - radius,
                     h - radius, outline=color, width=2)
    # for x in range(g * 100, (g+radius) * 100):
    #     x /= 100
    #     y = h + (math.sqrt(radius ** 2 - ((x-g) ** 2)))
    #     plot(page, x, y)
    #     plot(page, x, 2*h - y)
    #     plot(page, 2 * g - x,y)
    #     plot(page, 2 * g - x, 2 * h - y)


def draw_axes(page):
    page.update()
    x_origin = page.winfo_width() / 2
    y_origin = page.winfo_height() / 2
    page.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    page.create_line(-x_origin, 0, x_origin, 0, fill="black")
    page.create_line(0, y_origin, 0, -y_origin, fill="black")
    print(locals())


def plot(canvas, x, y):
    canvas.create_line(x, -y, x + 1, -y+1, fill="red")


mainWindow = tkinter.Tk()

mainWindow.title("Parabola")
mainWindow.geometry("640x480")

canvas_1 = tkinter.Canvas(mainWindow, width=640, height=480)
canvas_1.grid(row=0, column=0)
draw_axes(canvas_1)

draw_axes(canvas_1)

# parabola(canvas_1, 100)
# parabola(canvas_1, 200)
circle(canvas_1, 100, 100 , 100, color="blue")
circle(canvas_1, 100, 50, 60, "yellow")


mainWindow.mainloop()