#!/usr/bin/python3
from ftplib import FTP
import time
import threading
import random
import sys


threadLock = threading.Lock()
g_count = 0


def ftpconnect(host, username, password):
    ftp = FTP()
    ftp.set_debuglevel(2)
    ftp.connect(host, 2008)
    ftp.login(username, password)
    return ftp


def downloadfile(ftp, remotepath, localpath):
    bufsize = 1024
    fp = open(localpath, 'wb')
    ftp.retrbinary('RETR ' + remotepath, fp.write, bufsize)
    ftp.set_debuglevel(0)
    fp.close()


def uploadfile(ftp, localpath, remotepath):
    bufsize = 1024
    fp = open(localpath, 'rb')
    ftp.storbinary('STOR ' + remotepath, fp, bufsize)
    ftp.set_debuglevel(0)
    fp.close()

def testuploadfile(threadName):
    global threadLock
    global g_count
    ftp = ftpconnect("10.1.1.61", "admin", "admin")
    start_tick = time.time()
    count = 0
    while True:
        pic_name = '51010000491320000001/' + threadName + '_' + str(count) + '.jpg'
        uploadfile(ftp, "/img_xzrs/Face_01.jpg", pic_name)
        end_tick = time.time()
        count = count + 1
        if (end_tick - start_tick) > 1.0:
            break
    ftp.quit()
    print(threadName+': count='+str(count))
    threadLock.acquire()
    g_count = g_count + count
    threadLock.release()

def virtualUploadFile():
    global threadLock
    global g_count
    start_tick = time.time()
    count = 0
    while True:
        num = random.random()
        time.sleep(num)
        end_tick = time.time()
        count = count + 1
        if (end_tick - start_tick) > 1.0:
            break
    threadLock.acquire()
    g_count = g_count + count
    threadLock.release()


class MyThread(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

    def run(self):
        print("start:"+self.name)
        testuploadfile(self.name)
        # virtualUploadFile()
        print("end:"+self.name)

if __name__ == "__main__":
    threadList = []
    for i in range(0,int(sys.argv[1])):
    #for i in range(0,500):	
        thread = MyThread(i, "Thread_" + str(i))
        thread.start()
        threadList.append(thread)
    for t in threadList:
        t.join()
    print(sys.argv)
    print("main exit...")
    print('g_count='+str(g_count))
