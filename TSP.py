import math


class Vertex:
    def __init__(self, num, x, y):
        self.num = num
        self.x = x
        self.y = y


def find_distance(v1, v2):
    squared = float(((v2.x - v1.x) ** 2) + ((v2.y - v1.y) ** 2))
    return math.sqrt(squared)


class TSP:
    def __init__(self):
        self.vertices = []
        self.num_vertices = 0
        self.tour = [0, 1, 2, 0]
        self.distance = 0.0

    def get_vertices(self):
        # redirect input from test-n.txt files
        self.num_vertices = int(input())
        for i in range(self.num_vertices):
            read_in = input()
            split_in = read_in.split()
            self.vertices.append(Vertex(i, int(split_in[0]), int(split_in[1])))

    def display_vertices(self):
        for v in self.vertices:
            print(str(v.num) + " " + str(v.x) + " " + str(v.y))

    def display_tour(self):
        print("distance: " + str(self.distance))
        print(self.tour)

    def arbitrary_tsp(self):
        # loop through remaining vertices
        for i in range(3, self.num_vertices):
            next_v = self.vertices[i]
            best_candidate = math.inf
            best_ind = 0
            for v in range(0, len(self.tour) - 1):
                temp_candidate = find_distance(self.vertices[v], next_v) \
                                 + find_distance(self.vertices[v+1], next_v)
                if temp_candidate < best_candidate:
                    best_candidate = temp_candidate
                    best_ind = v
            self.tour.insert(best_ind, next_v.num)

    def find_distance(self):
        for i in range(0, len(self.tour) - 1):
            self.distance += find_distance(self.vertices[self.tour[i]],
                                           self.vertices[self.tour[i+1]])


def main():
    tsp = TSP()
    tsp.get_vertices()
    tsp.arbitrary_tsp()
    tsp.find_distance()
    tsp.display_tour()


if __name__ == "__main__":
    main()
