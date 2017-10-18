from ftplib import FTP
import time
import threading


class MyThread (threading.Thread):
    def __init__(self, threadID, name, count):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.count = count

    def run(self):
        print("开启线程： " + self.name)
        # 获取锁，用于线程同步
        threadLock.acquire()
        testuploadfile(self.name, self.count, count=threads)
        # 释放锁，开启下一个线程
        threadLock.release()


def ftpconnect(host, username, password):
    ftp = FTP()
    ftp.set_debuglevel(2)
    ftp.connect(host, 2008)
    ftp.login(username, password)
    return ftp


def downloadfile(ftp, remotepath, localpath):
    # 从ftp下载文件
    bufsize = 1024
    fp = open(localpath, 'wb')
    ftp.retrbinary('RETR ' + remotepath, fp.write, bufsize)
    ftp.set_debuglevel(0)
    fp.close()


def uploadfile(ftp, localpath, remotepath):
    # 从本地上传文件到ftp
    bufsize = 1024
    fp = open(localpath, 'rb')
    ftp.storbinary('STOR ' + remotepath, fp, bufsize)
    ftp.set_debuglevel(0)
    fp.close()


# def print_time(threadName, delay, counter):
#     while counter:
#         time.sleep(delay)
#         print("%s: %s" % (threadName, time.ctime(time.time())))
#         counter -= 1

def testuploadfile(threadName, delay, count):
    num = 0
    count = 0

    ftp = ftpconnect("192.168.2.200", "admin", "admin")
    start_tick = time.time()

    # for n in range(11):
    # # while True:
    while count:
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        count -=1

        pic_name = '51010000491320000001/' + str(num) + '.jpg'
        num = num + 1

        uploadfile(ftp, "/home/rxf/other/PlatServerTest/2.jpg", pic_name)
        end_tick = time.time()
        count = count + 1
        if (end_tick - start_tick) > 1.0:
            break

    print('count=', count)
    ftp.quit()

threadLock = threading.Lock()
threads = []

# 创建新线程
thread1 = MyThread(1, "Thread-1", 1)
thread2 = MyThread(2, "Thread-2", 2)

# 开启新线程
thread1.start()
thread2.start()

# 添加线程到线程列表
threads.append(thread1)
threads.append(thread2)

# 等待所有线程完成
for t in threads:
    t.join()
print("退出主线程")

if __name__ == "__main__":
    testuploadfile()
    MyThread.run()