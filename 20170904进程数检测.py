#!/usr/bin/python3

import psutil
import types
import datetime

try:
    PID = int(input("Please input PID:"))
except Exception as e:
    print(e)
else:
    # 获取pid对应的应用名
    p = psutil.Process(PID)
    print('Process name:%s' % p.name())

    # 获取进程bin路径
    print('Process bin path:%s' % p.exe())

    # 获取pid对应的路径
    # print('Process path:%s' % p.cwd())

    # 获取进程状态
    print('Process staus:%s' % p.status())

    # 进程运行时间
    print('Process creation time:%s' % datetime.datetime.fromtimestamp(p.create_time()).strftime("%Y-%m-%d %H:%M:%S"))

    # CPU使用情况
    print(p.cpu_times())

    # 内存使用情况
    print('Memory usage : %s%%' % p.memory_percent())

    # 硬盘读取信息
    # print(p.io_counters())

    # 打开进程socket的namedutples列表
    # print(p.connections())

    # 此进程的线程数
    print('Process number of threads : %s' % p.num_threads())
