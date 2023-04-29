from globals import *
from editor import editor
class ToolsPane(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(bg='#222', bd=0,highlightthickness=0,relief=tk.FLAT)

        self.spacer = tk.Frame(self,bg='#222', bd=0,highlightthickness=0,relief=tk.FLAT,height=26)
        self.spacer.pack(padx=0,pady=0)
        self.label = tk.Button(self,bg="#333",bd=0,fg="#DDD",highlightthickness=0, text="=",width=1,height=1,relief=tk.FLAT)
        self.label.pack(padx=0,pady=0)
class CanvasPane(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(bg='#111', bd=0,highlightthickness=0, relief=tk.FLAT)

        self.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=0)
        self.rowconfigure(1,weight=1)

        self.TAB = CanvasTabPane(self)
        self.TAB.grid(row=0,column=0,sticky=tk.NSEW)

        self.AREA = CanvasAreaPane(self)
        self.AREA.grid(row=1,column=0,sticky=tk.NSEW)
class CanvasTabPane(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(bg='#444', bd=0,highlightthickness=0,relief=tk.FLAT,height=30)

        self.tab1 = TabBtn(self)
        self.tab1.pack(padx=0,pady=0,side=tk.LEFT)
        self.tab2 = TabBtn(self)
        self.tab2.pack(padx=0,pady=0,side=tk.LEFT)
class TabBtn(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(bg='#111', bd=0,highlightthickness=0,relief=tk.FLAT,height=40)
        self.tab = tk.Button(self,bg="#111",bd=0,fg="#AAA",highlightthickness=0, text="wonderfool.jpg",height=0,relief=tk.FLAT,font=("Arial", 10))
        self.close = tk.Button(self,bg="#111",bd=0,fg="#AAA",highlightthickness=0, text="x",width=1,height=0,relief=tk.FLAT, font=("Arial", 10))
        self.tab.pack(side=tk.LEFT)
        self.close.pack(side=tk.RIGHT)

class CanvasAreaPane(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(bg='#111', bd=0,highlightthickness=0,relief=tk.FLAT)
        self.CANVAS = editor(self)
        self.CANVAS.pack(fill=tk.BOTH,expand=True)
class LayersPane(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(bg='#222', bd=0,highlightthickness=0, relief=tk.FLAT)

        self.label = tk.Label(self, text="Hello, World!")
        self.label.pack()