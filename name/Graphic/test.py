import tkinter

import draw_object

sprite = draw_object.Sprite()

tk = tkinter.Tk()
canvas = tkinter.Canvas(tk)
canvas.pack()

photoimage = sprite.image()

canvas.create_image((0, 0),
                    image=photoimage,
                    anchor='nw',
                    )

tk.mainloop()
