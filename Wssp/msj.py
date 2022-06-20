import pyautogui, webbrowser
import time

number = '+51940709267'
msj = 'txt'

webbrowser.open('https://web.whatsapp.com/send?/phone='+number)


time.sleep(15)

for i in range(5):
    pyautogui.typewrite(msj)
    pyautogui.press('enter')

