from ftplib import FTP
import threading
# import os

num = 0
def ftpconnect(host, username, password):
    ftp = FTP()
    ftp.set_debuglevel(2)
    ftp.connect(host, 21)
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
    ftp = ftpconnect("10.1.2.254", "download", "download")
    threads = []
    t1 = threading.Thread(target=uploadfile, args=(ftp, "/home/rxf/other/PlatServerTest/2.jpg", "D:/download/Ranxiangfei/1011_01.jpg"))
    threads.append(t1)
    t2 = threading.Thread(target=uploadfile, args=(ftp, "/home/rxf/other/PlatServerTest/2.jpg", "D:/download/Ranxiangfei/1011_02.jpg"))
    t2 = threads.append(t2)

    for t in threads:






    ftp.quit()
