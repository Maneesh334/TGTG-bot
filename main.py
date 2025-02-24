import pyautogui
import pytesseract
import pygetwindow as gw
import time


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  


while True:
    try:
        tgtg_window = gw.getWindowsWithTitle('Too Good To Go')[0]

        tgtg_window.activate()

        left, top, width, height = tgtg_window.left, tgtg_window.top, tgtg_window.width, tgtg_window.height
        screenshot = pyautogui.screenshot(region=(left, top, width, height))
        print(left, top, width, height)

        text = pytesseract.image_to_string(screenshot)
        print(text)

        if "left" in text:
            pyautogui.click(left + 100, top + 200)
            time.sleep(0.8)
            pyautogui.click(left + 150, top + height - 50)
            time.sleep(0.6)
            pyautogui.click(left + 150, top + height - 140)
            time.sleep(0.7)
            pyautogui.click(left + 300, top + height - 260)
            time.sleep(0.5)
            pyautogui.click(left + 300, top + height - 380)
            time.sleep(0.5)
            pyautogui.click(left + 300, top + height - 260)
            time.sleep(0.7)
            pyautogui.typewrite("129")
            time.sleep(0.1)
            pyautogui.click(left + 150, top + height - 100)
            #pyautogui.click(left + 150, top + height - 50)

        print(text)
        pyautogui.click(left + 150, top + height - 50)
        pyautogui.click(left + 400, top + height - 50)
        time.sleep(1.3)


    except IndexError:
        print(IndexError)
        continue
    except Exception as e:
        print(e)
        continue



