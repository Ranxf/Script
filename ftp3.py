#!/urs/bin/python3

import ftplib
import os
import socket

# HOST = '10.1.2.254'
# DIRN = "D:/download/Ranxiangfei/"
# FILE = '2.jpg'
HOST = '192.168.2.200'
DIRN = "/img_xzrs/20170930/51010000491320000001"
FILE = '2test.jpg'

def main():
    try:
        f = ftplib.FTP(HOST)
    except(socket.error, socket.gaierror):
        print('ERROR: cannot reach "%s"' % HOST)
        return
    print('*** Connected to host %s' % HOST)


    try:
        f.login('xzrs', 'xzrs')
    except(ftplib.error_perm):
        print("ERROR: cannot login admin")
        f.quit()
        return
    print("*** Login in as 'xzrs'")

    try:
        f.cwd(DIRN)
    except(ftplib.error_perm):
        print("Error: cannot CD to '%s'" % DIRN)
        f.quit()
        return
    print('*** Changed to "%s" folder' % DIRN)

    try:
        f.retrbinary('RETR %s'% FILE,
        open(FILE, 'wb').write)
    except ftplib.error_perm:
        print('ERROR:cannot read file "%s"' % FILE)
        os.unlink(FILE)
    else:
        print('***Downloades "%s" to CWD' % FILE)
        f.quit()
        return

if __name__ == '__main__':
    main()







