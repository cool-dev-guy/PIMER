from globals import *
from widget import widget
class window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(APPDATA['name'])
        self.geometry(APPDATA['geometry'])
        self.protocol("WM_DELETE_WINDOW", self._exit_)
        self.__initUI__()
    def __initUI__(self):

        self.MainWidget = widget(self)
        self.MainWidget.pack(fill=tk.BOTH, expand=True)
        self.CANVAS = self.MainWidget.MainPanedWindowWidgetGroup.CanvasPaneWidget.AREA.CANVAS
        self.CANVAS.AppON = True
    def __initCanvas__(self):
        self.update()
        self.CANVAS.__initCanvas__()
    def _exit_(self):
        self.CANVAS.AppON = False
        print(self.CANVAS.AppON)
        self.destroy()
