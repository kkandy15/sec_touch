#! /usr/bin/python2.7

import schedule
import os
import random


def job():
    print("11")
	os.system("rm Cen*")
    os.system("do somethin")
	

if __name__ == '__main__':
    i=random.randint(15,38)
    schedule.every(i).minutes.do(job)
    while True:
        schedule.run_pending()