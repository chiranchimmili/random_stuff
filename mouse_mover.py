import ctypes, pyautogui, random, time

prevx, prevy = pyautogui.position()
while True:
    # move if idle for 5 mins
    time.sleep(300)
    currx, curry = pyautogui.position()
    if prevx == currx and prevy == curry:
        x, y = random.randint(300, 500), random.randint(300, 500)
        ctypes.windll.user32.SetCursorPos(x, y)
        # pyautogui.moveTo(x, y, 0.5)
        prevx, prevy = x, y
    else:
        prevx, prevy = currx, curry





    