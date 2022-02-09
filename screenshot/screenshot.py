# Taking Screenshots using pyscreenshot in Python
'''
1)capture the image using grab()
2)display the image using show()
3)save the image using save()
'''

#from email.mime import image
import pyautogui

img=pyautogui.screenshot()
img.save(r"G:\python learning\Mini Projects\screenshot\screen1.png")