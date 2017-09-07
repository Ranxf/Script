#!/usr/bin/python3
import os
def load_stat():
    loadavg = {}
    f = open("/proc/loadavg")
    con = f.read().split()
    f.close()
    loadavg['lavg_1'] = con[0]
    loadavg['lavg_5'] = con[1]
    loadavg['lavg_15'] = con[2]
    loadavg['nr'] = con[3]
    loadavg['last_pid'] = con[4]
    return loadavg
print("loadavg_15", load_stat()['lavg_15'])
print("loadavg_5", load_stat()['lavg_5'])
print("loadavg_1", load_stat()['lavg_1'])