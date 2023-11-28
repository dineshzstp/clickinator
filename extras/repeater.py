import pyautogui
import time
import keyboard




while True:
    if keyboard.is_pressed('c'):
        
        time.sleep(1)
        
        pyautogui.click(1266,347)
        time.sleep(1)

        pyautogui.hotkey('ctrl', 'a')
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)

        pyautogui.click(1402,421)
        time.sleep(1)
        pyautogui.click(1096,225)
        time.sleep(1)
        pyautogui.click(1327,122)
        time.sleep(1)  
        pyautogui.click(1370,122)
        time.sleep(1) 
        pyautogui.click(461,629)
        pyautogui.press('down')  
                                   
#
#    if keyboard.is_pressed('up arrow'):
#
#        print('up')
#        pyautogui.click(922,533)
#        time.sleep(1)
#
#    if keyboard.is_pressed('down arrow'):
#
#        print("down") 
#
#        pyautogui.click(411,506)
#        time.sleep(1)
#        pyautogui.click(227,235)
#        time.sleep(1)
#
#        pyautogui.doubleClick(509,481)
#        time.sleep(1)
#
#        pyautogui.click(182,232)
#        time.sleep(1)
#        pyautogui.click(412,536)
#        time.sleep(1)
#        pyautogui.click(228,234)
#        time.sleep(1)
#
#        pyautogui.doubleClick(498,484)
#        time.sleep(1)
#        pyautogui.click(195,229)
#        time.sleep(1)
#
#
#    if keyboard.is_pressed('right arrow'):
#
#        print("right") 
#
#        pyautogui.click(69,235)
#        time.sleep(1)
#        pyautogui.click(337,126)
#        time.sleep(1)
#
##saving the progress  
##    pdyautogui.hotkey('ctrl', 's')
##    tidme.sleep(20)
##   prindt("waiting for 20 seconds")d
#