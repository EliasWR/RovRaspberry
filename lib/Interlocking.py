


class InterlockingSystem:

    def __init__(self):
        print("Interlocking system initalized")
        self.zoneLock0 = False
        self.zoneLock1 = False
        self.zoneLock2 = False
        self.zoneLock3 = False
        self.zoneLock4 = False
        self.zoneLock5 = False
        self.zoneLock6 = False
        self.zoneLock7 = False

        # List with indexes corresponding to zone, and values it what angle that zone was last locked in
        self.zoneLockedAngles = [None] * 8

    def resetAllZones(self):
        print("Operator-forced reset of all interlocked zones")
        self.zoneLock0 = False
        self.zoneLock1 = False
        self.zoneLock2 = False
        self.zoneLock3 = False
        self.zoneLock4 = False
        self.zoneLock5 = False
        self.zoneLock6 = False
        self.zoneLock7 = False

    def findZone (self, angle):
        if 175 < angle <= 225:
            return 0
        elif 125 < angle <= 175:
            return 1
        elif 75 < angle <= 125:
            return 2
        elif 25 < angle <= 75:
            return 3
        elif 325 < angle <= 375:
            return 5
        elif 275 < angle <= 325:
            return 6
        elif 225 < angle <= 275:
            return 7
        else:
            return 4

    def findObject (self, dataPoints):
        # Constants for object detectin, can be adjusted for range and sensitivity
        numOfValues = 100
        thresholdObjDetect = 80

        # Slicing list to appropiate values,changing this means changing what range are scanned for objects
        objectData = dataPoints[numOfValues:2*numOfValues]
        avrObj = sum(objectData)/numOfValues
        print("Average echo strength (0-255): ", avrObj)


        # If average of datapoints is above threshold return true (object is detected)
        if avrObj > thresholdObjDetect:
            return True
        else:
            return False


    def setInterlockZone (self, zone, angle):
        if zone == 0:
            self.zoneLock0 = True
            self.zoneLockedAngles[0] = angle
        elif zone == 1:
            self.zoneLock1 = True
            self.zoneLockedAngles[1] = angle
        elif zone == 2:
            self.zoneLock2 = True
            self.zoneLockedAngles[2] = angle
        elif zone == 3:
            self.zoneLock3 = True
            self.zoneLockedAngles[3] = angle
        elif zone == 4:
            self.zoneLock4 = True
            self.zoneLockedAngles[4] = angle
        elif zone == 5:
            self.zoneLock5 = True
            self.zoneLockedAngles[5] = angle
        elif zone == 6:
            self.zoneLock6 = True
            self.zoneLockedAngles[6] = angle
        elif zone == 7:
            self.zoneLock7 = True
            self.zoneLockedAngles[7] = angle
        else:
            print("Invalid set zone given")


    def checkIfResetPermitted (self, angle):
        for i in range(len(self.zoneLockedAngles)):
            if (self.zoneLockedAngles[i] == angle):
                self.resetInterlockZone(self.findZone(angle))


    def resetInterlockZone (self, zone):
        if zone == 0:
            self.zoneLock0 = False
        elif zone == 1:
            self.zoneLock1 = False
        elif zone == 2:
            self.zoneLock2 = False
        elif zone == 3:
            self.zoneLock3 = False
        elif zone == 4:
            self.zoneLock4 = False
        elif zone == 5:
            self.zoneLock5 = False
        elif zone == 6:
            self.zoneLock6 = False
        elif zone == 7:
            self.zoneLock7 = False
        else:
            print("Invalid reset zone given")