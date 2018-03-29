import os
rotate = 0
rotate = int(input("please input display_rotate value:"))
if rotate == 1:
    addstr = 'Option \"CalibrationMatrix\" \"0 1 0 -1 0 1 0 0 1\n        '
elif rotate == 2:
    addstr = 'Option \"CalibrationMatrix\" \"-1 0 1 0 -1 1 0 0 1\n        '
elif rotate == 3:
    addstr = 'Option \"CalibrationMatrix\" \"0 -1 1 1 0 0 0 0 1\n        '
else:
    addstr = ''
p = os.path.isfile(os.path.join('/usr/share/X11/xorg.conf.d/','40-libinput.conf'))
if p != True:
    os.system("sudo apt-get install xserver-xorg-input-libinput")
p = os.path.isfile(os.path.join('/etc/X11/','xorg.conf.d'))
if p != True:
    os.system("sudo cp /usr/share/X11/xorg.conf.d/40-libinput.conf /etc/X11/xorg.conf.d/")
getok = False
with open('/etc/X11/xorg.conf.d/40-libinput.conf','r') as f:
    lines=f.readlines()
with open('/etc/X11/xorg.conf.d/40-libinput.conf','w') as f_w:
    for line in lines:
        if getok == False:
            if "touchscreen" in line:
                getok = True
        else:
            if "CalibrationMatrix" in line:
                getok = False
                continue
            else:
                getok = False
        f_w.write(line)
    f.close()
    f_w.close()
f = open("/etc/X11/xorg.conf.d/40-libinput.conf","r")
content = f.read()
keyword = '\"libinput touchscreen catchall\"'
post = content.find('touchscreen')
if post != -1:
    content = content[:post+len(keyword)-1]+addstr+content[post+len(keyword)-1:]
    f = open('/etc/X11/xorg.conf.d/40-libinput.conf','w')
    f.write(content)
f.close()
os.system("sudo reboot")

