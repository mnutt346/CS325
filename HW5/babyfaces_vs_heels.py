import sys
import queue


class Wrestler:
    def __init__(self, name):
        self.name = name
        self.identifier = 0
        self.type = "NA"
        self.distance = 9999
        self.adjacent_wrestlers = list()

    def add_adjacent_wrestlers(self, vertex):
        if vertex not in self.adjacent_wrestlers:
            self.adjacent_wrestlers.append(vertex)
            self.adjacent_wrestlers.sort()


class Graph:
    def __init__(self):
        self.wrestlers = {}
        self.is_possible = True
        self.first_wrestler = None
        self.count = 0
        self.previous = None

    def add_wrestler(self, wrestler):
        if isinstance(wrestler, Wrestler):
            if self.count == 0:
                wrestler.type = "babyface"
                self.first_wrestler = wrestler
                self.count += 1
            if wrestler.name not in self.wrestlers:
                self.wrestlers[wrestler.name] = wrestler

    def add_rival(self, current, rival):
        self.wrestlers[current].add_adjacent_wrestlers(rival)
        self.wrestlers[rival].add_adjacent_wrestlers(current)

    def get_wrestler(self, wrestler_name):
        return self.wrestlers[wrestler_name]

    def BFS(self, curr_wrestler):
        wrestlers_queue = queue.Queue()
        curr_wrestler.identifier = 1
        curr_wrestler.distance = 0
        wrestlers_queue.put(self.first_wrestler)

        while not wrestlers_queue.empty():
            current = wrestlers_queue.get()
            rivals_length = len(current.adjacent_wrestlers)

            for i in range(0, rivals_length):
                rival_name = current.adjacent_wrestlers[i]
                rival = self.wrestlers[rival_name]
                if rival.identifier == 0:
                    rival.identifier = 1
                    if rival.distance > current.distance + 1:
                        rival.distance = current.distance + 1
                    if rival.distance % 2 == 0:
                        rival.type = "babyface"
                    elif rival.distance % 2 != 0:
                        rival.type = "heel"
                    rival.previous = current
                    wrestlers_queue.put(rival)
                elif rival.identifier == 1:
                    if rival.type == 'babyface':
                        if current.type != 'heel':
                            self.is_possible = False
                    elif rival.type == 'heel':
                        if current.type != 'babyface':
                            self.is_possible = False
                current.identifier = 2

                if current.identifier == 2 and current.type == "NA":
                    current.type = "babyface"

            if wrestlers_queue.empty():
                for wrestler in self.wrestlers:
                    remaining = self.wrestlers[wrestler]
                    if remaining.identifier == 0 or remaining.identifier == "NA":
                        wrestlers_queue.put(remaining)

    def print_babyfaces(self):
        babyface_string = "Babyfaces: "
        for wrestler in self.wrestlers:
            if self.wrestlers[wrestler].type == 'babyface':
                babyface_string += self.wrestlers[wrestler].name + " "
        print(babyface_string)

    def print_heels(self):
        heel_string ="Heels: "
        for wrestler in self.wrestlers:
            if self.wrestlers[wrestler].type == 'heel':
                heel_string += self.wrestlers[wrestler].name + " "
        print(heel_string)


def main():

    wrestler_graph = Graph()
    rivalries = []

    input_file = open("data.txt", "r")
    input_lines = input_file.read().splitlines()
    input_file.close()
    wrestler_number = map(int, input_lines[0])
    wrestler_count = ''.join(map(str, wrestler_number))
    wrestler_count = int(wrestler_count)

    for i in range(1, wrestler_count + 1):
        wrestler_graph.add_wrestler(Wrestler(input_lines[i]))

    rival_number = map(int, input_lines[wrestler_count + 1])
    rival_count = ''.join(map(str, rival_number))
    rival_count = int(rival_count)

    for j in range(wrestler_count + 2, len(input_lines)):
        rivalries.append(input_lines[j])

    for rivalry in rivalries:
        rival_tuple = rivalry.split()
        wrestler_graph.add_rival(rival_tuple[0], rival_tuple[1])

    wrestler_graph.BFS(wrestler_graph.first_wrestler)

    # If it is possible, print yes, otherwise print no
    if wrestler_graph.is_possible:
        print("Yes Possible")
        wrestler_graph.print_babyfaces()
        wrestler_graph.print_heels()
    else:
        print("Not Possible")


main()