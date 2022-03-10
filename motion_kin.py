import time
import math
#Kinematic Motion Calculator by IntraConnect Corporation (C) All rights reserved.
print("Welcome to Motive by IntraConnect.")
time.sleep(1)
print("//////////////////////////////////////////////////////////////////////\nThis program will calculate the motion of a point in a straight line.\n//////////////////////////////////////////////////////////////////////\n")
time.sleep(1.5)
print("Loading System Info...")
time.sleep(2)
print("Loading Python Modules...")
time.sleep(1)
print("Readying up...")
time.sleep(3)
print("Ready")

#defining key funcs
def specRound(n):
    decim = 2
    mltplr = 10 ** decim
    return int(n * mltplr) / mltplr
def checkRealCond(x):
    z = x >= 0
    print("[["+ x + "]]")
    if z is False:
        print("====Error: Please enter positive numbers only.====")
        return False
    else:
        return True
def speed():
    t = float(input("Insert time value (s): "))
    s = float(input("Insert distance value (m): "))
    if checkRealCond(t):
        v = s / t
        print("The speed is: ~ " + str(specRound(v)) + " m/s")
    else: 
        print("\nError: Please enter positive numbers only.")
def distance():
    v = float(input("Insert speed value (m/s): "))
    t = float(input("Insert time value (s): "))
    if checkRealCond(t):
        s = v * t
        print("The distance traveled is: ~ " + str(specRound(s)) + " m")
    else: 
        print("\nError: Please enter positive numbers only.")
def time():
    s = float(input("Insert distance value (m): "))
    v = float(input("Insert speed value (m/s): "))
    if s >= 0 and v >= 0 or s < 0 and v < 0:
        t = s / v
        print("The time passed is: ~ " + str(specRound(t)) + " s")
    else: 
        print("time must be positive decimal")
     
def Rspeed():
    s1 = float(input("Insert first distance value (m): "))
    sf = float(input("Insert final distance value (m): "))
    t1 = float(input("Insert corresponding(s) first time value (s): "))
    tf = float(input("Insert corresponding(s) final time value (s): "))
    cond = tf - t1
    if checkRealCond(cond):
        v = (sf - s1) / (tf - t1)
        print("The speed is: ~ " + str(specRound(v)) + " m/s")
def Rdistance():
    v1 = float(input("Insert first distance value (m): "))
    vf = float(input("Insert final distance value (m): "))
    t1 = float(input("Insert corresponding(s) first time value (s): "))
    tf = float(input("Insert corresponding(s) final time value (s): "))
    if checkRealCond(v1, vf) and checkRealCond(t1, tf):
        s = (vf - v1) * (tf - t1)
        print("The distance traveled is: ~ " + str(specRound(s)) + " m")
def Rtime():
    s1 = float(input("Insert first distance value (m): "))
    sf = float(input("Insert final distance value (m): "))
    v1 = float(input("Insert corresponding(s) first speed value (m/s): "))
    vf = float(input("Insert corresponding(s) final speed value (m/s): "))
    if checkRealCond(s1, sf) and checkRealCond(v1, vf):
        t = (sf - s1) / (vf - v1)
        print("The time passed is: ~ " + str(specRound(t)) + " s")

#start
while True: 
    slt = int(input("Select:\n[1] Range of values\n[2] Single values\n> "))
    if slt == 1:
        print("\nSelect:\n[1] Speed\n[2] Distance\n[3] Time")
        slt = int(input("> "))
        if slt == 1:
            Rspeed()
        elif slt == 2:
            Rdistance()
        elif slt == 3:
            Rtime()
        else:
            print("\nError: Please enter a valid number.")

    elif slt == 2:
        slt = int(input("Select operation:\n[1] Calc. SPEED (V)\n[2] Calc. TIME (t)\n[3] Calc. DISTANCE (s)\n> "))
        if slt == 1:
            speed()
        elif slt == 2:
            time()
        elif slt == 3:
            distance()
        else:
            print("Invalid input.")
    else:
        print("Invalid selection.")
        exit()
