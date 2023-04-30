pyinstaller main.py --hidden-import='PIL._tkinter_finder'
cd dist
p7zip main
