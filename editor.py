from globals import *
import canvas
class editor(tk.Canvas):
	def __init__(self, master):
		super().__init__(master)
		self.configure(bg='#111',bd=0,highlightthickness=0)
		self.bind('<Motion>', self.RulerPointer)
		self.bind('<Configure>', self.PaintOnConfig)

		self.canvasState = False
		self.RulerMarkerX = []
		self.RulerMarkerY = []
		self.RulerText = []
		const = 20
		self.const = const

		
	def PaintOnConfig(self,event):
		# self.delete("all")


		self.DrawRulers()
	def DrawRulersOnInit(self):
		const = 20
		self.const = const
		self.create_line(20, 0, 20, self.winfo_height(), width=1,fill='#444')
		self.create_line(0, 20, self.winfo_width(), 20, width=1,fill='#444')

		for i in range(0, self.winfo_width(), 10):
			if i % 50 == 0:
					self.RulerMarkerX.append(self.create_line(i+const,20, i+const,10, width=1,fill='#444'))
					self.RulerText.append(self.create_text(i+const, 10, text=str(i), font=("Arial", 7),anchor=tk.SW,fill='#555'))
			else:
				self.RulerMarkerX.append(self.create_line(i+const, 20, i+const, 15, width=1,fill='#444'))

		for i in range(0, self.winfo_height(), 10):
			if i % 50 == 0:
					# if i == 0:continue;
				self.RulerMarkerY.append(self.create_line(20, i+const, 10, i+const, width=1,fill='#444'))
				self.RulerText.append(self.create_text(0, i+const, text=str(i), font=("Arial", 7),anchor=tk.SW,fill='#555'))
			else:
				self.RulerMarkerY.append(self.create_line(20, i+const, 15, i+const, width=1,fill='#444'))
		print(self.RulerMarkerX)
	def DrawRulers(self):
		if self.canvasState:
			print(int(self.winfo_width()/10),len(self.RulerMarkerX))
			if not(int(self.winfo_width()/10)<=len(self.RulerMarkerX) or int(self.winfo_height()/10)<=len(self.RulerMarkerY)):

				print(int(self.winfo_width()/10),len(self.RulerMarkerX),"jjjj")
				# pass
			else:
				
				self.AddXlist = int(self.winfo_width()/10)-len(self.RulerMarkerX)
				self.RulerMarkerX = self.RulerMarkerX + [None] * self.AddXlist

				self.AddYlist = int(self.winfo_height()/10)-len(self.RulerMarkerY)
				self.RulerMarkerY = self.RulerMarkerY + [None] * self.AddYlist
				const = 20
				print(self.AddXlist,self.AddYlist,len(self.RulerMarkerX),len(self.RulerMarkerY))
				self.const = const
				self.create_line(20, 0, 20, self.winfo_height(), width=1,fill='#444')
				self.create_line(0, 20, self.winfo_width(), 20, width=1,fill='#444')

				for i,j in zip(range(0, self.winfo_width(), 10),range(len(self.RulerMarkerX))):
					if self.RulerMarkerX[j] == None:
						if i % 50 == 0:

								self.RulerMarkerX[j] = self.create_line(i+const,20, i+const,10, width=1,fill='#444')
								self.RulerText.append(self.create_text(i+const, 10, text=str(i), font=("Arial", 7),anchor=tk.SW,fill='#555'))
						else:
							self.RulerMarkerX[j] = self.create_line(i+const, 20, i+const, 15, width=1,fill='#444')
					else:
						continue
				for i,j in zip(range(0, self.winfo_height(), 10),range(len(self.RulerMarkerY))):
					if self.RulerMarkerY[j] ==None:
						if i % 50 == 0:
								# if i == 0:continue;
							self.RulerMarkerY[j] = self.create_line(20, i+const, 10, i+const, width=1,fill='#444')
							self.RulerText.append(self.create_text(0, i+const, text=str(i), font=("Arial", 7),anchor=tk.SW,fill='#555'))
						else:
							self.RulerMarkerY[j] = self.create_line(20, i+const, 15, i+const, width=1,fill='#444')
					else:
						continue
				print(self.RulerMarkerX,self.RulerMarkerY)
		else:
			pass
	def __initCanvas__(self):
		self.RulerPointerTriangleCordsX = [15, 15, 20, 20, 25, 15]
		self.RulerPointerTriangleCordsY = [15, 15, 20, 20, 15, 25]
		self.RulerPointerTriangleX = self.create_polygon(self.RulerPointerTriangleCordsX, fill='red')

		self.RulerPointerTriangleY = self.create_polygon(self.RulerPointerTriangleCordsY, fill='red')
		self.canvasState = True
		self.DrawRulersOnInit()

		self.canvasContext = canvas.createCanvas(self,900,600)
		self.canvasContext.Render()
		# self.RulerPointer('j')
	def removePreviusCache(self):
		self.delete(self.self.photo_image)
		del self.self.photo_image
	def renderCanvas(self,Render):
		print('h')
		# self.delete(self.self.photo_image)
		# del self.self.photo_image
		# self.create_image(20, 20, anchor=tk.NW, image=Render)
		#global self.photo_image
		self.photo_image.config(data=Render)
		print(self.photo_image)
		# print(self.self.photo_image)
		self.itemconfig(self.canvas_img, image=self.photo_image)
		# self.update()

	def RulerPointer(self,event):
		self.RulerPointerTriangleCordsX = [15+event.x-self.const, 15, 20+event.x-self.const, 20, 25+event.x-self.const, 15]
		self.RulerPointerTriangleCordsY = [15, 15+event.y-self.const, 20, 20+event.y-self.const, 15, 25+event.y-self.const]
		self.coords(self.RulerPointerTriangleX, self.RulerPointerTriangleCordsX)
		self.coords(self.RulerPointerTriangleY, self.RulerPointerTriangleCordsY)
	def initMainCanvas(self,Data):
		print('g')
		#global self.photo_image
		self.photo_image = tk.PhotoImage(data=Data)
		self.canvas_img = self.create_image(20, 20, anchor=tk.NW, image=self.photo_image)
		self.update()