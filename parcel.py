# Mark Murphy, 001223523

import math


# Trucks' routes are assigned based on time restraints and distance, in that order
import graph


# Packages are prioritized first by time and then by distance. All priority noodes' eulerian circuit
# is calculated separately from non-priority nodes and then the resulting paths are merged
# O(n^m) where n is the amount of nodes and m is the amount of packages
def prioritizeByTime(g, truck, packageHash):
    priorityNodes = {}
    distanceMatrix = g.getDistanceMatrix()

    # Get the minimum minimum delivery time of a node by checking the delivery requirements of packakges being
    # delivered to that node.
    for node in truck.nodes:
        if node not in priorityNodes and node != 0:
            priorityNodes[node] = 100
        for package in truck.packages:
            packagePriority = packageHash.search(package).priority
            if packageHash.search(package).address == node:
                if packagePriority < priorityNodes[node]:
                    priorityNodes[node] = packagePriority

    sortedNodes = sorted(priorityNodes.items(), key=lambda x: (x[1], x[0]))
    prioritySet = sorted(list(set([x[1] for x in sortedNodes])))
    nodeGroups = [None] * len(prioritySet)

    # Nodes are grouped together by priority
    groupNumber = 0
    for p in prioritySet:
        nodeGroups[groupNumber] = [x[0] for x in sortedNodes if x[1] == p]
        groupNumber += 1

    if 0 not in nodeGroups[0]:
        nodeGroups[0].append(0)
        for n in nodeGroups[1:]:
            if 0 in n:
                n.remove(0)

    finalNodes = graph.tsp(g, nodeGroups[0])[1]
    finalNodes = finalNodes[finalNodes.index(0):] + finalNodes[:finalNodes.index(0)]

    for n in nodeGroups[1:]:
        prevNode = finalNodes[-1]
        newNode = n[0]
        minDistance = distanceMatrix[prevNode][newNode]
        for node in n:
            if distanceMatrix[prevNode][node] < minDistance:
                newNode = node
                minDistance = distanceMatrix[prevNode][node]
        n = graph.tsp(g, n)[1]
        n = n[n.index(newNode):] + n[:n.index(newNode)]
        finalNodes += n

    truck.nodes = finalNodes


# Returns the next node which a truck will want to travel to given their current load of packages
# O(n)
def getNextNode(currentNode, remainingPackages, packageHash, distanceMatrix):
    minimumTime = timeClock(17, 0)

    # Determine the next delivery time by finding the closest node to the previous node (greedy)
    # Determine the next delivery time by finding the package with the lowest priority and then
    # creating a list of packages with that priority.
    for package in packageHash.hashTable:
        if package.deadline < minimumTime and package.idNumber in remainingPackages:
            minimumTime = package.deadline

    nodesToChooseFrom = list(set(
        [p.address for p in packageHash.hashTable if p.deadline == minimumTime and p.idNumber in remainingPackages]))

    if len(nodesToChooseFrom) == 1:
        newNode = nodesToChooseFrom[0]
    elif len(nodesToChooseFrom) == 0:
        return None
    else:
        newNode = nodesToChooseFrom[0]
        minDistance = distanceMatrix[currentNode][newNode]
        for node in nodesToChooseFrom:
            if distanceMatrix[currentNode][node] < minDistance:
                newNode = node
                minDistance = distanceMatrix[currentNode][node]

    return newNode


# Bread and butter of the package, this is where packages are delivered
# O(n^2)
def deliverPackages(g, truck, packageHash, time, printed=None, displayTime=None, displayPackage=None):
    totalDistance = 0
    current = truck.nodes[0]
    hasPrinted = False

    # If displayTime is less than the time at which the method is called, no display should occur
    if displayTime and displayTime < time:
        displayTime = None
        print()
        print("_______________________________")
        print("               TIME: ", time)
        print("_______________________________")
        printPackages(packageHash, printed, packages=displayPackage)

    for i in truck.nodes[1:]:
        packageDistance = g.edgeWeights[(g.indexes[i], g.indexes[current])]
        packageTime = packageDistance * (60 / 18)

        if displayTime and displayPackage:
            if time > displayTime and not hasPrinted:
                if truck.name != "T3":  # Banner should not print a second time when T3 is sent out
                    print()
                    print("_______________________________")
                    print("               TIME: ", time)
                    print("_______________________________")
                printPackages(packageHash, printed, packages=displayPackage)
                hasPrinted = True

        time += packageTime

        for p in range(packageHash.size):

            if packageHash.search(p).address == i and packageHash.search(p).idNumber in truck.packages:
                if packageHash.search(p).deliveryTime == timeClock(0, 0):

                    packageHash.search(p).deliveryTime.setTime(time.hours, time.minutes)
                    packageHash.search(p).deliveryTruck = truck.name

                    if packageHash.search(p).deadline > time:
                        packageHash.search(p).status = "Delivered"
                    else:
                        packageHash.search(p).status = "Late"
                        totalDistance += 100

        totalDistance += packageDistance
        current = i

    return totalDistance


# Packages are loaded based on the trucks' original list of packages
# If a truck is delivering packages to a location, other packages sharing the location are added to the truck's
# cache as well.
# O(n^2). There is a brief segment of 3 nested loops, but the outer loop is almost certain to be very small
def greedyTruck(g, trucks, remainingPackages, lowPriority, packageHash):
    distanceMatrix = g.getDistanceMatrix()
    current = [0] * len(trucks)
    full = [False] * len(trucks)
    n = 0

    for truck in trucks:
        for node in truck.nodes:
            for i in packageHash.hashTable:
                if i.address == node and len(truck.packages) < 16:
                    if i.idNumber in remainingPackages:
                        truck.packages.append(i.idNumber)
                        remainingPackages.remove(i.idNumber)

    while len(remainingPackages) > 0:
        if len(trucks[n % len(trucks)].packages) < 16:
            nextNode = getNextNode(current[n % len(current)], remainingPackages, packageHash, distanceMatrix)
            if nextNode:
                if nextNode not in trucks[n % len(trucks)].nodes:
                    trucks[n % len(trucks)].nodes.append(nextNode)
            else:
                break
            for i in packageHash.hashTable:
                if i.address == nextNode and len(trucks[n % len(trucks)].packages) < 16:
                    if i.idNumber in remainingPackages:
                        trucks[n % len(trucks)].packages.append(i.idNumber)
                        remainingPackages.remove(i.idNumber)
                        i.deliveryTruck = trucks[n % len(trucks)].name

            current[n % len(current)] = nextNode

        else:
            full[n % len(full)] = True
            if False not in full:
                break

        n += 1

    for truck in trucks:
        for node in truck.nodes:
            for i in packageHash.hashTable:
                if i.address == node and len(truck.packages) < 16:
                    if i.idNumber in lowPriority:
                        truck.packages.append(i.idNumber)
                        lowPriority.remove(i.idNumber)

    for truck in trucks:
        truck.assignNodes()


# Returns a list of all nodes which belong to a given list of packages
# O(n)
def getNodes(packageList, packageHash):
    nodes = []

    for i in packageHash.hashTable:
        if i.idNumber in packageList and i.address not in nodes:
            nodes.append(i.address)

    return nodes


# Low prioirity packages are assigned to the trucks.
# Packages are assigned to a truck until the truck is full.
# O(n^2)
def linkLowPriority(g, trucks, remainingPackages, remainingNodes, packageHash):
    distanceMatrix = g.getDistanceMatrix()
    current = [0] * len(trucks)
    nextNode = [0] * len(trucks)
    full = [False] * len(trucks)
    n = 0

    for i in range(len(trucks)):
        try:
            current[i] = trucks[i].nodes[-1]
            minDistance = 100
            for node in remainingNodes:
                if minDistance > distanceMatrix[current[i]][node] > 0:
                    newNode = node
                    minDistance = distanceMatrix[current[i]][node]
            nextNode[i] = newNode
        except:
            current[i] = 0
            minDistance = 100
            for node in remainingNodes:
                if minDistance > distanceMatrix[current[i]][node] > 0:
                    newNode = node
                    minDistance = distanceMatrix[current[i]][node]
            nextNode[i] = newNode

    while len(remainingPackages) > 0:
        k = n % len(trucks)
        if len(trucks[k].packages) < 16:

            if nextNode[k] not in trucks[k].nodes:
                trucks[k].nodes.append(nextNode[k])
            for i in packageHash.hashTable:
                if i.address == nextNode[k]:

                    if i.idNumber in remainingPackages and len(trucks[k].packages) < 16:
                        trucks[k].packages.append(i.idNumber)
                        remainingPackages.remove(i.idNumber)
                        i.deliveryTruck = trucks[k].name

            current[k] = nextNode[k]
            nodeIndex = remainingNodes.index(current[k])

            if nodeIndex < len(remainingNodes) - 1:
                nextNode[k] = remainingNodes[nodeIndex + 1]
            elif len(remainingNodes) == 0:
                break
            else:
                nextNode[k] = remainingNodes[0]

        else:
            full[k] = True
            if False not in full:
                break

        if len(trucks[k].packages) >= 16:
            n += 1


# Because there is an element of randomness in Christofides algorithm, best path estimations are run several
# times and the best resulting paths are returned.
# O(n)
def getBestPath(g, trucks, packageHash):
    bestDistance = 1000

    for i in range(10):
        distance = 0
        for truck in trucks:
            prioritizeByTime(g, truck, packageHash)
            distance += deliverPackages(g, truck, packageHash, time=timeClock(8, 0))

        if distance < bestDistance:
            bestDistance = distance
            bestCombo = []
            for t in range(len(trucks)):
                bestCombo.append(trucks[t].packages)

    for t in range(len(trucks)):
        trucks[t].packages = bestCombo[t]


def printPackages(packageHash, printed, status="", packages=None):
    if packages is None:
        packages = []
    for p in range(packageHash.size):
        if packageHash.search(p).status == status or status == "":
            if packageHash.search(p).idNumber in packages or not packages:
                if packageHash.search(p).idNumber in printed:
                    printed.remove(packageHash.search(p).idNumber)
                    print(packageHash.search(p))
                    print()
                    print()


# Packages are simple objects, containing several properties and a method to return a string
class Parcel:

    def __init__(self, idNumber, address, deadline, city, zipCode, weight, status):
        self.idNumber = idNumber
        self.address = address
        dlHr, dlMin = deadline
        self.deadline = timeClock(dlHr, dlMin)
        self.city = str(city)
        self.zipCode = str(zipCode)
        self.weight = weight
        self.status = str(status)
        self.deliveryTime = timeClock(0, 0)
        self.priority = dlHr + (dlMin / 60)
        self.deliveryTruck = ""

    def __repr__(self):
        return "Package ID: " + str(self.idNumber) + "\nAddress: " + str(
            self.address) + "\nDeadline: " + str(self.deadline) + "\nDelivered: " + str(self.deliveryTime) + \
               "\nStatus: " + self.status + "\nTruck: " + self.deliveryTruck


# Trucks are basically buckets which hold a few properties
class Truck:

    def __init__(self, packages, packageHash, name):
        self.packages = packages
        self.nodes = [0]
        self.packageHash = packageHash
        self.zips = [None]
        self.cities = [None]
        self.name = name
        self.assignNodes()

    # Assures that all packages in the truck have a node associated with them
    def assignNodes(self):
        for package in self.packages:
            packageNode = self.packageHash.search(package).address
            packageZip = self.packageHash.search(package).zipCode
            packageCity = self.packageHash.search(package).city

            if packageNode not in self.nodes:
                self.nodes.append(packageNode)

            if packageZip not in self.zips:
                self.zips.append(packageZip)

            if packageCity not in self.cities:
                self.cities.append(packageCity)


# the timeClock class is used to track delivery times and deadlines
class timeClock(object):

    def __init__(self, hours, minutes):
        try:
            self.hours = hours
            self.minutes = minutes

            if self.hours > 24 or self.minutes > 60:
                raise ValueError("Invalid time")

        except ValueError:
            self.hours = 8
            self.minutes = 0

    def __add__(self, minutes):
        self.minutes += float(minutes)
        if self.minutes >= 60:
            self.hours += math.floor(self.minutes / 60)
            self.minutes = self.minutes % 60

        return self

    def __sub__(self, minutes):
        self.minutes -= minutes
        if self.minutes < 0:
            self.hours -= math.ceil(abs(self.minutes) / 60)
            self.minutes = 60 - abs(self.minutes % 60)

    def __lt__(self, other):
        if self.hours > other.hours:
            return False
        elif self.hours == other.hours and self.minutes > other.minutes:
            return False
        else:
            return True

    def __gt__(self, other):
        if self.hours > other.hours:
            return True
        elif self.hours == other.hours and self.minutes > other.minutes:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.hours == other.hours and self.minutes == other.minutes:
            return True
        return False

    def __repr__(self):
        repr_str = "{hours}:{minutes:02}"

        return repr_str.format(hours=self.hours, minutes=int(self.minutes))

    def getHours(self):
        return self.hours

    def getMinutes(self):
        return self.minutes

    def setTime(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes
