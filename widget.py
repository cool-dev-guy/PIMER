from globals import *
from panes import ToolsPane,CanvasPane,LayersPane

class MainPanedWindow(tk.PanedWindow):
    def __init__(self, master):
        super().__init__(master)
        self.configure(self,bg="#333", orient=tk.HORIZONTAL,bd=0,borderwidth=0)

        self.CanvasPaneWidget = CanvasPane(self)
        self.add(self.CanvasPaneWidget)
        self.paneconfigure(self.CanvasPaneWidget, minsize=800)

        self.LayersPaneWidget = LayersPane(self)
        self.add(self.LayersPaneWidget)
class SubWidget(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(bg='#222', relief=tk.FLAT)
        self.ToolsPaneWidget = ToolsPane(self)
        self.ToolsPaneWidget.pack(fill=tk.BOTH,expand=True)
class TopWidget(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(bg='#333', relief=tk.FLAT,height=40)

#Main widget
class widget(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(bg='#222', bd=1, relief=tk.FLAT)
        self.columnconfigure(0,weight=0)
        self.columnconfigure(1,weight=1)
        self.rowconfigure(0,weight=0)
        self.rowconfigure(1,weight=1)

        self.TopWidgetGroup = TopWidget(self)
        self.TopWidgetGroup.grid(row=0,column=0,columnspan=2,sticky=tk.NSEW)

        self.SubWidgetGroup = SubWidget(self)
        self.SubWidgetGroup.grid(row=1,column=0,sticky=tk.NSEW)

        self.MainPanedWindowWidgetGroup = MainPanedWindow(self)
        self.MainPanedWindowWidgetGroup.grid(row=1,column=1,sticky=tk.NSEW)