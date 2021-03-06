"""
RASPBERRY PI SUB PROGRAM CONTAINING THE INTERLOCKING LOGIC
NEEDED FOR ASSISTING THE OPERATOR OF THE ROV TO CONTROL THE
ROV IN TIGHT SPACES.
"""

class InterlockingSystem:
    def __init__(self):
        print("Interlocking system initalized")
        self.lockedZones = [False] * 8
        self.zoneLockedAngles = [None] * 8

    # Resets all interloked zones
    def resetAllZones(self):
        print("Operator-forced reset of all interlocked zones")
        self.lockedZones = [False] * 8

    # By taking in the currently scanned angle, finds which zone the angle
    # is a part of, and return this zone
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

    # Function taking in the echo strengths from sonar, and finds if these
    # values within close proximity is above a certain treshold, and determines
    # if an object was located
    def findObject (self, dataPoints):

        # Constants for object detection, can be adjusted for range and sensitivity
        numOfValues = 100
        thresholdObjDetect = 40

        # Slicing list to appropiate values, changing this means changing what range are scanned for objects
        objectData = dataPoints[numOfValues:2*numOfValues]
        avrObj = sum(objectData)/numOfValues
        # print("Average echo strength (0-255): ", avrObj)

        # If average of datapoints is above threshold return true (object is detected)
        if avrObj > thresholdObjDetect:
            return True
        else:
            return False

    # Takes in zone and angle and interlocks that zone for no movement in that direction
    # Additionally the angle which the object was located at is saved, for later resetting
    # of zone during normal operation
    def setInterlockZone (self, zone, angle):
        if zone == 0:
            self.lockedZones[0] = True
            self.zoneLockedAngles[0] = angle
        elif zone == 1:
            self.lockedZones[1] = True
            self.zoneLockedAngles[1] = angle
        elif zone == 2:
            self.lockedZones[2] = True
            self.zoneLockedAngles[2] = angle
        elif zone == 3:
            self.lockedZones[3] = True
            self.zoneLockedAngles[3] = angle
        elif zone == 4:
            self.lockedZones[4] = True
            self.zoneLockedAngles[4] = angle
        elif zone == 5:
            self.lockedZones[5] = True
            self.zoneLockedAngles[5] = angle
        elif zone == 6:
            self.lockedZones[6] = True
            self.zoneLockedAngles[6] = angle
        elif zone == 7:
            self.lockedZones[7] = True
            self.zoneLockedAngles[7] = angle
        else:
            print("Invalid set zone given")

    # Checks if the scanned angle has been interlocked last revolution
    # and if no object was found this reviolution, reset the zone
    def checkIfResetPermitted (self, angle):
        for i in range(len(self.zoneLockedAngles)):
            if (self.zoneLockedAngles[i] == angle):
                self.resetInterlockZone(self.findZone(angle))

    # Takes in an angle, and resets the zone containing that angle
    def resetInterlockZone (self, zone):
        if zone == 0:
            self.lockedZones[0] = False
        elif zone == 1:
            self.lockedZones[1] = False
        elif zone == 2:
            self.lockedZones[2] = False
        elif zone == 3:
            self.lockedZones[3] = False
        elif zone == 4:
            self.lockedZones[4] = False
        elif zone == 5:
            self.lockedZones[5] = False
        elif zone == 6:
            self.lockedZones[6] = False
        elif zone == 7:
            self.lockedZones[7] = False
        else:
            print("Invalid reset zone given")