import time
import random
import pyautogui

massage = 'Kontol' , 'babi' , 'memek'

time.sleep(5)

for i in range(50):
    pyautogui.typewrite(random.choice(massage) + '\n')
