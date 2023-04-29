import tkinter as tk
from tkinter import ttk

#canvas imports
import skia
import pygame
from numpy import *
from pygame.locals import *
from contextlib import contextmanager
from PIL import Image, ImageTk

photo_image = None
APPDATA={
	"version":"0.0.1",
	"name":"Piraside",
	"geometry":"1080x700"
}
CANVASX = 0
CANVASY = 0
global App
App = ''
