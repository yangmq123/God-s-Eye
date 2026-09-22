from tkinter import *
from tkinter.ttk import *
class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        self.tk_canvas_muaz74cc = self.__tk_canvas_muaz74cc(self)
        self.tk_button_muaza337 = self.__tk_button_muaza337(self)
        self.tk_button_mub0ibok = self.__tk_button_mub0ibok(self)
        self.tk_button_mub0qdg8 = self.__tk_button_mub0qdg8(self)
    def __win(self):
        self.title("God's Eyes")
    
        width = 641
        height = 513
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        
        self.resizable(width=False, height=False)
        
    def scrollbar_autohide(self,vbar, hbar, widget):
        
        def show():
            if vbar: vbar.lift(widget)
            if hbar: hbar.lift(widget)
        def hide():
            if vbar: vbar.lower(widget)
            if hbar: hbar.lower(widget)
        hide()
        widget.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Leave>", lambda e: hide())
        if hbar: hbar.bind("<Enter>", lambda e: show())
        if hbar: hbar.bind("<Leave>", lambda e: hide())
        widget.bind("<Leave>", lambda e: hide())
    
    def v_scrollbar(self,vbar, widget, x, y, w, h, pw, ph):
        widget.configure(yscrollcommand=vbar.set)
        vbar.config(command=widget.yview)
        vbar.place(relx=(w + x) / pw, rely=y / ph, relheight=h / ph, anchor='ne')
    def h_scrollbar(self,hbar, widget, x, y, w, h, pw, ph):
        widget.configure(xscrollcommand=hbar.set)
        hbar.config(command=widget.xview)
        hbar.place(relx=x / pw, rely=(y + h) / ph, relwidth=w / pw, anchor='sw')
    def create_bar(self,master, widget,is_vbar,is_hbar, x, y, w, h, pw, ph):
        vbar, hbar = None, None
        if is_vbar:
            vbar = Scrollbar(master)
            self.v_scrollbar(vbar, widget, x, y, w, h, pw, ph)
        if is_hbar:
            hbar = Scrollbar(master, orient="horizontal")
            self.h_scrollbar(hbar, widget, x, y, w, h, pw, ph)
        self.scrollbar_autohide(vbar, hbar, widget)
    def __tk_canvas_muaz74cc(self,parent):
        canvas = Canvas(parent,bg="#aaa")
        canvas.place(x=0, y=0, width=640, height=360)
        return canvas
    def __tk_button_muaza337(self,parent):
        btn = Button(parent, text="Get an Image", takefocus=False,)
        btn.place(x=45, y=414, width=135, height=36)
        return btn
    def __tk_button_mub0ibok(self,parent):
        btn = Button(parent, text="Watch Living", takefocus=False,)
        btn.place(x=461, y=414, width=135, height=36)
        return btn
    def __tk_button_mub0qdg8(self,parent):
        btn = Button(parent, text="Stop Living", takefocus=False,)
        btn.place(x=253, y=415, width=135, height=36)
        return btn
class Win(WinGUI):
    def __init__(self, controller):
        self.ctl = controller
        super().__init__()
        self.__event_bind()
        self.__style_config()
        self.ctl.init(self)
    def __event_bind(self):
        self.tk_button_muaza337.bind('<Button-1>',self.ctl.create_image)
        self.tk_button_mub0ibok.bind('<Button-1>',self.ctl.live_start)
        self.tk_button_mub0qdg8.bind('<Button-1>',self.ctl.stop_live)
        pass
    def __style_config(self):
        pass
if __name__ == "__main__":
    win = WinGUI()
    win.mainloop()