from queue import PriorityQueue

parks = []
roads = {}

class Park:
    def __init__(self, name, b_wait, t_wait):
        self.name = name
        self.b_wait = b_wait / 60
        self.t_wait = t_wait / 60


class Road:
    def __init__(self, dist, trans, b_name=None, v_bus=None, v_taxi=None):
        self.distance = dist
        self.transport = trans
        if self.transport:
            self.b_name = b_name
            self.v_bus = v_bus
            self.v_taxi = v_taxi
            
class Node:
    def __init__(self, park_id, energy, money, time, trans_type=-1, parent=None):
        self.park_id = park_id
        self.energy = energy
        self.time = time
        self.money = money
        self.transport_type = trans_type
        self.parent = parent

    def printDetails(self):
        print("\n\nPark Name:", parks[self.park_id].name, end=', ')
        print("Energy:", self.energy, end=', ')
        print("Money:", self.money, end=', ')
        print("Time (mintues):", round(self.time * 60), end=', ')
        if self.transport_type == 1:
            print("Transport Type: Bus", end='')
        elif self.transport_type == 2:
            print("Transport Type: Taxi", end='')
        elif self.transport_type == 3:
            print("Transport Type: Foot", end='')

    def isFinal(self):
        if self.park_id == len(parks) - 1:
            return True
        return False

    def canMove(self, road, trans_type):
        d = road.distance
        if trans_type == 1: # Bus
            v_bus = road.v_bus
            money = self.money - 400
            energy = self.energy - 5 * d
            time = self.time + parks[self.park_id].b_wait + d/v_bus
        elif trans_type == 2: # Taxi
            v_taxi = road.v_taxi
            money = self.money - d * 1000
            energy = self.energy + 5 * d
            time = self.time + parks[self.park_id].t_wait + d/v_taxi
        else: # Foot
            money = self.money
            energy = self.energy - 10 * d
            time = self.time + d/5.5

        if energy > 0 and money >= 0:
            return True, energy, money, time
        else:
            return False, None, None, None

    def move(self, park_id, energy, money, time, trans_type):
        return Node(park_id, energy, money, time, trans_type, self)

    def nextNodes(self):
        nodes = []
        for i in range(len(parks)):
            key = (self.park_id, i)
            if key in roads.keys():
                road = roads[key]
                if road.transport:
                    # Bus
                    ok, energy, money, time = self.canMove(road, 1)
                    if ok:
                        node = self.move(i, energy, money, time, 1)
                        nodes.append(node)
                    # Taxi
                    ok, energy, money, time = self.canMove(road, 2)
                    if ok:
                        node = self.move(i, energy, money, time, 2)
                        nodes.append(node)
                # Foot
                ok, energy, money, time = self.canMove(road, 3)
                if ok:
                    node = self.move(i, energy, money, time, 3)
                    nodes.append(node)
                
        return nodes



def firstHoristic(node):
    return -1 * node.money

def secondHoristic(node):
    return -1 * node.energy

def thirdHoristic(node):
    return node.time

def firstAStar(node):

    visited = []
    index = 0
    best_cost = 1000
    best_node = None

    pq = PriorityQueue()
    pq.put((0, -1, node))

    while not pq.empty():

        fromQ = pq.get()
        cost = fromQ[0]
        element = fromQ[2]

        visited.append((element.park_id, element.transport_type))

        if (element.isFinal()):
            if cost < best_cost:
                best_cost = cost
                best_node = element

        nodes = element.nextNodes()
        for el in nodes:
            if (el.park_id, el.transport_type) not in visited:
                pq.put((firstHoristic(el), index, el))
            index += 1

    return best_node, len(visited)

def secondAStar(node):

    visited = []
    index = 0
    best_cost = 1000
    best_node = None

    pq = PriorityQueue()
    pq.put((0, -1, node))

    while not pq.empty():

        fromQ = pq.get()
        cost = fromQ[0]
        element = fromQ[2]

        visited.append((element.park_id, element.transport_type))

        if (element.isFinal()):
            if cost < best_cost:
                best_cost = cost
                best_node = element

        nodes = element.nextNodes()
        for el in nodes:
            if (el.park_id, el.transport_type) not in visited:
                pq.put((secondHoristic(el), index, el))
            index += 1

    return best_node, len(visited)

def thirdAStar(node):

    visited = []
    index = 0
    best_cost = 1000
    best_node = None

    pq = PriorityQueue()
    pq.put((0, -1, node))

    while not pq.empty():

        fromQ = pq.get()
        cost = fromQ[0]
        element = fromQ[2]

        visited.append((element.park_id, element.transport_type))

        if (element.isFinal()):
            if cost < best_cost:
                best_cost = cost
                best_node = element

        nodes = element.nextNodes()
        for el in nodes:
            if (el.park_id, el.transport_type) not in visited:
                pq.put((thirdHoristic(el), index, el))
            index += 1

    return best_node, len(visited)

def play(node, func=1):
    
    if func == 1:
        result, nodes = firstAStar(node)
    elif func == 2:
        result, nodes = secondAStar(node)
    elif func == 3:
        result, nodes = thirdAStar(node)

    if result != None:
        getRoute(result)
        print("\n\n\t\tThe Number Of Visited Nodes: ", nodes)
    else:
        print("\n\t\tThere Are No Road To Final Park")

def getRoute (node):
    if(node is None):
        return
    getRoute(node.parent)
    node.printDetails()


############### Main ###############


energy = 200

num_parks = int(input("What's The Number Of Parks: "))
for i in range(num_parks):
    if i < num_parks-1:
        print(f"Park {i+1}")
        name = input("Park's Name: ")
        bus_wait = int(input("Bus Wait (mintues): "))
        taxi_wait = int(input("Taxi Wait(mintues): "))
        parks.append(Park(name, bus_wait, taxi_wait))
    else:
        print(f"Final Park")
        name = input("Park's Name: ")
        parks.append(Park(name, 0, 0))


for i, park1 in enumerate(parks):
    for j, park2 in enumerate(parks):
        if i >= j:
            continue
        isRoad = input(f"\nIs There An Road Between {park1.name} And {park2.name} (y, n): ")
        if isRoad.lower() == 'y':
            dist = int(input("The Distance Between Them: "))
            transport = input("Can Buses And Taxis pass Between Them (y, n): ")
            if transport.lower() == 'y':
                bus_name = input("Bus Name: ")
                v_bus = int(input("Bus Speed: "))
                v_taxi = int(input("Taxi Speed: "))
                roads[(i, j)] = Road(dist, True, bus_name, v_bus, v_taxi)
                roads[(j, i)] = Road(dist, True, bus_name, v_bus, v_taxi)
            else:
                roads[(i, j)] = Road(dist, False)
                roads[(j, i)] = Road(dist, False)
money = int(input("\nHow much Do You Have? "))


node = Node(0, energy, money, 0)
play(node,1)
