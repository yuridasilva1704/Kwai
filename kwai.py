import pyautogui

while(True):

    #Assiste ao video, curte e seleciona para comentar
    pyautogui.moveTo(840,470)
    pyautogui.click(840,470, duration=25)
    pyautogui.click(840,520) # Clica para comentar

    #Comentário
    pyautogui.moveTo(600,650)
    pyautogui.moveTo(600,650,duration=2)
    pyautogui.doubleClick(600,650)
    pyautogui.moveTo(600,650,duration=2)
    pyautogui.typewrite("o/",interval=0.5)
    pyautogui.moveTo(830,650)
    pyautogui.moveTo(830,650,duration=3)
    pyautogui.click(830,650)
    pyautogui.click(830,650)
    pyautogui.click(650,170)


    # Barra de rolagem
    pyautogui.moveTo(700,190)
    pyautogui.moveTo(700,190,duration=2)
    pyautogui.click(700,200)
    pyautogui.scroll(-20)

    print("FEITO")
