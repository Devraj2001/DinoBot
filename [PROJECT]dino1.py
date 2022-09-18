import pyautogui  # pip install pyautogui
from PIL import Image, ImageGrab  # pip install pillow
# from numpy import asarray
import time


def hit(key):
    pyautogui.keyDown(key)


def isCollide(data):
    # Draw the rectangle for cACtus
    for i in range(205, 490):
        for j in range(470, 475):
            if data[i, j] < 100:
                return True
    return False
def isBird(data):
    for i in range(255, 265):
        for j in range(390, 400):
            if data[i, j] < 100:
                return True
    return False

if __name__ == "__main__":
    print("Hey.. Dino game about to start in 3 seconds")
    time.sleep(2)
    # image = ImageGrab.grab().convert('L')
    # data = image.load()
    # for i in range(245, 260):
    #     for j in range(390, 400):
    #         data[i, j] = 0
    # image.show()

    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        if isBird(data):
            hit('down')
        if isCollide(data):
            hit('up')


        # print(asarray(image))
    '''
    # Draw the rectangle for cactus
    for i in range(275, 325):
        for j in range(563, 650):
            data[i, j] = 0

    # Draw the rectangle for birds
    for i in range(250, 300):
        for j in range(410, 563):
            data[i, j] = 171

    image.show()
    break
    '''

