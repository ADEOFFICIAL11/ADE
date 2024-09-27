import os,platform
os.system('git pull --quiet 2>/dev/null')
os.system("clear")
print('\033[97;1m [•] Join Whatsapp Group')
#os.system('xdg-open https://chat.whatsapp.com/Gj0Sev9DEWtIudpJXsTvCo')
King=platform.architecture()[0]
if King=="32bit":
    #__import__("ADE")
    os.system("clear")
    exit('\033[91;1m [•] Sorry Bro 32 Bit Devices Not Supported')
elif King=="64bit":
    __import__("ADE")
