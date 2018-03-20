import os
import erase
erase.run()
os.system("dfu-util.exe -d 0483:df11 -a 0 -D Touch1.dfu")
input()