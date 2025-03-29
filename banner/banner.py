from colored import fg
import random 
import time 
import os 


class Banner():
    colors = ['red', 'green', 'blue', 'yellow', 'pink', 'MAGENTA','CYAN']

    def banner1(self):
        banner = fg(random.randrange(0,6)) + r'''
+--------------------------------------------------------------+
|           _             _                                    |
|          | |           | |                                   |
|__      __| |__    __ _ | |_  ___   __ _  _ __   _ __         |
|\ \ /\ / /| '_ \  / _` || __|/ __| / _` || '_ \ | '_ \        |
| \ V  V / | | | || (_| || |_ \__ \| (_| || |_) || |_) |       |
|  \_/\_/  |_| |_| \__,_| \__||___/ \__,_|| .__/ | .__/        |
|              | |                        | || | | |           |
|  __ _  _   _ | |_   ___   _ __ ___    __|_|| |_|_|___   _ __ |
| / _` || | | || __| / _ \ | '_ ` _ \  / _` || __| / _ \ | '__||
|| (_| || |_| || |_ | (_) || | | | | || (_| || |_ | (_) || |   |
| \__,_| \__,_| \__| \___/ |_| |_| |_| \__,_| \__| \___/ |_|   |
|                                                              |
|Github : @Pankajkr2699                 Code by : Pankaj Kumar |
+--------------------------------------------------------------+
'''
        print(banner)


# Loading Animation 
    def loadingAnimation(self):
        symbols = ['⣾', '⣷', '⣯', '⣟', '⡿', '⢿', '⣻', '⣽']
        breakTheCode = 0 
        i = 0 
        while True: 
            i = (i + 1) % len(symbols)
            print('\r\033[K%s loading...' % symbols[i], flush=True, end='')
            time.sleep(0.1)
            breakTheCode +=1 
            if breakTheCode == 20:
                break 
        os.system('cls')
    




