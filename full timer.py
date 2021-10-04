#typed by : @l_f_f_6_6_6
import time
import os
import colorama
import random



while True:
            
    def bunner():
    a ='''
      
      wWw W  W    wWw        oo_    wWw    c  c  wWw  wWw()_()wW  Ww(o)__(o)wWw  wWw       c  cwWw  wWw___   wWw()_()  
      (O)(O)(O)   (O)_      /  _)-< (O)_   (OO)  (O)  (O)(O o)(O)(O)(__  __)(O)  (O)       (OO)(O)  (O|___)__(O)(O o)  
      / __)||     / __)     \__ `.  / __),'.--.) / )  ( \ |^_\ (..)   (  )  ( \  / )     ,'.--.| \  / |O)(O) / __)^_\  
     / (   | \   / (           `. |/ (  / //_|_\/ /    \ \|(_)) ||     )(    \ \/ /     / //_|_\\ \/ //  _\ / (  |(_)) 
    (  _)  |  `.(  _)          _| (  _) | \___  | \____/ ||  / _||_   (  )    \o /      | \___   \o / | |_)|  _) |  /  
     \ \_ (.-.__) /         ,-'   |\ \_ '.    ) '. `--' .`)|\\(_/\_)   )/    _/ /       '.    ) _/ /  | |_))\ \_ )|\\  
      \__) `-'  )/         (_..--'  \__)  `-.'    `-..-' (/  \)       (     (_.'          `-.' (_.'   (.'-'  \__|/  \      
         
         
         ''' 
    i = random.randint(1,10)

        if i == 1:
            print(colorama.Fore.GREEN+a)
        if i == 2: 
            print(colorama.Fore.RED+colorama.Cursor.BACK()+a)
        if i ==3 :
            print(colorama.Fore.BLUE+colorama.Style.DIM+a)    
        if i == 4:
            print(colorama.Fore.CYAN+colorama.Cursor.BACK(a))
        if i == 5:
            print(colorama.Fore.YELLOW+a)
        if i == 6:
            print(colorama.Fore.LIGHTWHITE_EX+colorama.Style.DIM+colorama.Cursor.BACK(a))
        if i == 7:
            print(colorama.Fore.MAGENTA+a)
        if i == 8:
            print(colorama.Fore.LIGHTCYAN_EX+a)    
        if i == 9:
            print(colorama.Fore.CYAN+colorama.Style.DIM+a)
        if i ==10:
            print(colorama.Fore.LIGHTBLACK_EX+colorama.Style.DIM+a)
    bunner()    
    a = time.localtime()
    c = time.strftime(colorama.Fore.CYAN+colorama.Style.BRIGHT+'\t"year is":"%Y\n\t\t"mon is":"%m\n\t\t\t"day is":"%d"\n\t\t"yaer day":"%j"\n\t"monts":"%b"\n\n\n"%Z"\n\n\n\n\t\t\t}' , a)
    b = time.strftime(colorama.Fore.CYAN+colorama.Style.BRIGHT+'{ \n\n"time is":"%H:%M:%S"\n' , a )
    print(g)
    print(b , c)
    time.sleep(1)
    if os.name == 'nt':
          os.system('cls')
    else:
          os.system('clear')

    
    
