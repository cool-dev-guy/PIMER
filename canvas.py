from globals import *
import time
import threading
from OpenGL import GL
import cv2
import numpy as np
import base64
WIDTH, HEIGHT = 900, 600
@contextmanager
def opengl_context(width, height):
	pygame.init()
	context = pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL | HIDDEN)
	yield context
	pygame.quit()
@contextmanager
def skia_surface(window):
	context = skia.GrDirectContext.MakeGL()
	(fb_width, fb_height) = pygame.display.get_surface().get_size()
	backend_render_target = skia.GrBackendRenderTarget(
		fb_width,
		fb_height,
		0,  # sampleCnt
		0,  # stencilBits
		skia.GrGLFramebufferInfo(0, GL.GL_RGBA8))
	surface = skia.Surface.MakeFromBackendRenderTarget(
		context, backend_render_target, skia.kBottomLeft_GrSurfaceOrigin,
		skia.kRGBA_8888_ColorType, skia.ColorSpace.MakeSRGB())
	assert surface is not None
	yield surface
	context.abandonContext()
def createCanvas(canvasSurf,width,height):
	PIMPcanvas = Canvas(canvasSurf,width,height)
	return PIMPcanvas
def create_circle(canvas):
	radius = random.randint(10, 50)
	x = random.randint(radius, WIDTH - radius)
	y = random.randint(radius, HEIGHT - radius)
	color = skia.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 255)
	canvas.drawCircle(x, y, radius, skia.Paint(Color=color))


class Canvas:
	def __init__(self, canvasSurf, width, height):
		self.canvasSurf = canvasSurf
		self.width = width
		self.height = height
		self.font = skia.Font(skia.Typeface('Arial'), 24)
		self.text = 'Type something'
		self.text_color = skia.ColorWHITE
		self.text_position = skia.Point(100, 100)
		# self.MakeContext('')

		# self.action = {
		# 	'AddText':self.AddText()
		# }

	def AddText(self):

		self.canvas.clear(skia.ColorWHITE)
		self.canvas.drawImage(self.image, 0, 0)
		paint = skia.Paint(self.text_color)
		self.canvas.drawString(self.text, self.text_position.x(), self.text_position.y(), self.font, paint)
	def AddCircle(self):
		pass
	# def updateCanvas(self,data):
	# 	# print(data)
	# 	data = data.reshape(-1)
	# 	data = tuple(data)
	# 	# print(data)
	# 	self.pil_image.putdata(data)
	# 	return self.pil_image
	def MakeContext(self):
		with opengl_context(self.width,self.height) as window:
			GL.glClear(GL.GL_COLOR_BUFFER_BIT)
			with skia_surface(window) as surface:
				with surface as canvas:
					canvas.clear(skia.ColorWHITE)
				self.image = surface.makeImageSnapshot()
				self.data = self.image.toarray()
				self.pil_image = Image.fromarray(self.data)
				cv2_image = cv2.cvtColor(np.array(self.pil_image), cv2.COLOR_RGB2BGR)
				retval, buffer = cv2.imencode(".png", cv2_image)
				image_data_base64_encoded_string = base64.b64encode(buffer).decode("utf-8")
				# cv2.imshow('image', cv2_image)

				# # Wait for a key press and then close the window
				# cv2.waitKey(0)
				# cv2.destroyAllWindows()
				# self.pil_image = Image.frombuffer("RGBA", (self.width, self.height), self.data, "raw", "RGBA", 0, 1)
				surface.flushAndSubmit()
				pygame.display.flip()
				#print(len(self.data),self.data.shape[1])
				self.canvasSurf.initMainCanvas(image_data_base64_encoded_string)
				while self.canvasSurf.AppON:
					create_circle(canvas)
					surface.flushAndSubmit()
					pygame.display.flip()
					#self.image = surface.makeImageSnapshot()
					assert self.image is not None
					self.image = surface.makeImageSnapshot()
					self.data = self.image.toarray()
					self.pil_image = Image.fromarray(self.data)
					cv2_image = cv2.cvtColor(np.array(self.pil_image), cv2.COLOR_RGB2BGR)
					retval, buffer = cv2.imencode(".png", cv2_image)
					image_data_base64_encoded_string = base64.b64encode(buffer).decode("utf-8")
					# self.data = self.image.toarray()
					#img = cv2.cvtColor(self.data, cv2.COLOR_RGB2BGR)
					# self.pil_image.putdata([tuple(pixel) for row in self.data for pixel in row])
					# print(self.pil_image)
					#self.pil_image = Image.frombuffer("RGBA", (self.width, self.height), self.data, "raw", "RGBA", 0, 1)
					# self.photo_image = ImageTk.PhotoImage(self.pil_image)
					# print(self.photo_image,self.pil_image,self.canvasSurf.AppON)
					self.canvasSurf.renderCanvas(image_data_base64_encoded_string)
					time.sleep(1) # wait for one second before creating the next circle
	def Render(self):
		# self.MakeContext(action)
		self.thread = threading.Thread(target=self.MakeContext)
		self.thread.start()
		# self.thread.join()



