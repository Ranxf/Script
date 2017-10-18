from ftplib import FTP
import time
import threading

num = 0
count = 0


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

if __name__ == "__main__":
    ftp = ftpconnect("192.168.2.200", "admin", "admin")
    start_tick = time.time()

    threads = []
    t1 = threading.Thread(target=uploadfile,)
    threads.append(t1)
    t2 = threading.Thread()
    threads.append(t2)

    # for n in range(11):
    while True:
        file_name = '51010000491320000001/' + str(num) + '.jpg'
        num = num + 1
        uploadfile(ftp, "/home/rxf/other/PlatServerTest/2.jpg", file_name)
        end_tick = time.time()
        count = count + 1
        if (end_tick - start_tick) > 1.0:
            break
    print('count=', count)
    ftp.quit()