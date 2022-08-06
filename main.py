import pyautogui
from typing import NoReturn
from time import sleep


# get the RBG value of the pixel at the mouse position
def getRGBFromMouse():
    x, y = pyautogui.position()
    return pyautogui.screenshot().getpixel((x, y))


def getHexFromRGB(r: int, g: int, b: int) -> str:
    return f"0x{r:02x}{g:02x}{b:02x}"


def main() -> NoReturn:
    while 1:
        rgb = getRGBFromMouse()
        print(f"{rgb[0]}, {rgb[1]}, {rgb[2]} [{getHexFromRGB(*rgb)}]")
        sleep(1)


if __name__ == "__main__":
    main()