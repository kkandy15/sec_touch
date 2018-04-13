import pyautogui
import time
import sys
"""
this code for the 
"""

def click_4sec(gTime):
    #print("now is %d", time.time())
    while True:
        now=time.time()
        if(now>gTime):
           # print("knock now...")
            knock_screen()
           # print("knock end...")


def knock_screen():
    """
    knock 4 second till time out

    """
    for i in range(0,4000):

        #time.sleep(2)
        pyautogui.click()
        time.sleep(1*0.001)
    sys.exit()

def conv_time():
    tmlist = [2018, 4, 17, 9, 59, 58, 0, 0, 0]
    return time.mktime(tmlist)


if __name__ == '__main__':
    click_4sec(conv_time())
