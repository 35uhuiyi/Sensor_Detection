import codecs
import numpy as np
import os
import datetime
import matplotlib.pyplot as plt
import math


def transData(A):
    for i in range(len(A)):
        try:
            A[i] = float(A[i])
        except:
            pass
    return A


def readData(filename, pos):
    time = []
    accX = []
    accY = []
    accZ = []
    palX = []
    palY = []
    palZ = []
    angX = []
    angY = []
    angZ = []
    f = codecs.open(filename, mode='r', encoding='utf-8')
    next(f)
    for line in f.readlines():
        currentNum = line.split()
        if currentNum[0] == pos:
            t = currentNum[3]
            nineData = transData(currentNum)[4:13]
            time.append(t)
            accX.append(nineData[0])
            accY.append(nineData[1])
            accZ.append(nineData[2])
            palX.append(nineData[3])
            palY.append(nineData[4])
            palZ.append(nineData[5])
            angX.append(nineData[6])
            angY.append(nineData[7])
            angZ.append(nineData[8])
    return [accX, accY, accZ, palX, palY, palZ, angX, angY, angZ, time]


def drawSingle(Data, startTime, endTime, pos):
    time = Data[-1]
    startTime = [startTime[0:2], startTime[3:5], startTime[6:8]]
    endTime = [endTime[0:2], endTime[3:5], endTime[6:8]]
    startFlag = 0
    endFlag = len(time) - 1
    for i in range(len(time)):
        [h, m, s] = [time[i][0:2], time[i][3:5], time[i][6:8]]
        if h == startTime[0] and m == startTime[1] and s >= startTime[2]:
            startFlag = i
            break
    for i in range(len(time)):
        [h, m, s] = [time[i][0:2], time[i][3:5], time[i][6:8]]
        if h == endTime[0] and m == endTime[1] and s >= endTime[2]:
            endFlag = i
            break
    accX, accY, accZ, palX, palY, palZ, angX, angY, angZ = Data[0:9]
    accX = accX[startFlag:endFlag]
    accY = accY[startFlag:endFlag]
    accZ = accZ[startFlag:endFlag]
    palX = palX[startFlag:endFlag]
    palY = palY[startFlag:endFlag]
    palZ = palZ[startFlag:endFlag]
    angX = angX[startFlag:endFlag]
    angY = angY[startFlag:endFlag]
    angZ = angZ[startFlag:endFlag]

    plt.figure(pos)
    plt.subplot(3, 3, 1)
    plt.title("accx")
    plt.plot(list(range(accX.__len__())), accX)
    plt.grid()

    plt.figure(pos)
    plt.subplot(3, 3, 2)
    plt.title("accy")
    plt.plot(list(range(accY.__len__())), accY)
    plt.grid()

    plt.figure(pos)
    plt.subplot(3, 3, 3)
    plt.title("accz")
    plt.plot(list(range(accZ.__len__())), accZ)
    plt.grid()

    plt.figure(pos)
    plt.subplot(3, 3, 4)
    plt.title("palx")
    plt.plot(list(range(palX.__len__())), palX)
    plt.grid()

    plt.figure(pos)
    plt.subplot(3, 3, 5)
    plt.title("paly")
    plt.plot(list(range(palY.__len__())), palY)
    plt.grid()

    plt.figure(pos)
    plt.subplot(3, 3, 6)
    plt.title("palz")
    plt.plot(list(range(palZ.__len__())), palZ)
    plt.grid()

    plt.figure(pos)
    plt.subplot(3, 3, 7)
    plt.title("angx")
    plt.plot(list(range(angX.__len__())), angX)
    plt.grid()

    plt.figure(pos)
    plt.subplot(3, 3, 8)
    plt.title("angy")
    plt.plot(list(range(angY.__len__())), angY)
    plt.grid()

    plt.figure(pos)
    plt.subplot(3, 3, 9)
    plt.title("angz")
    plt.plot(list(range(angZ.__len__())), angZ)
    plt.grid()


if __name__=='__main__':
    pos = ["WTarm1up", "WTarm2up", "WTarm1", "WTarm2", "WTleg1", "WTleg2"]
    fileName = "../oriData/20210709093248.txt"
    WTarm1up = readData(fileName, pos[0])  # 上臂
    WTarm2up = readData(fileName, pos[1])
    WTarm1 = readData(fileName, pos[2])
    WTarm2 = readData(fileName, pos[3])
    WTleg1 = readData(fileName, pos[4])
    WTleg2 = readData(fileName, pos[5])

    # 截取时间
    startTime = "09:32:53"
    endTime = "09:33:58"

    drawSingle(WTarm1up,startTime,endTime,1)
    drawSingle(WTarm2up,startTime,endTime,2)
    drawSingle(WTarm1,startTime,endTime,3)
    drawSingle(WTarm2,startTime,endTime,4)
    drawSingle(WTleg1,startTime,endTime,5)
    drawSingle(WTleg2,startTime,endTime,6)
    plt.show()





