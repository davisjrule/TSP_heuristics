import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation


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
        self.max_x = 0
        self.max_y = 0
        self.tour = [0, 1, 2, 0]
        self.distance = 0.0
        self.fig = plt.figure()
        self.axes = self.fig.subplots()

    def get_vertices(self):
        # redirect input from test-n.txt files
        max_range = input().split()
        self.max_x = int(max_range[0])
        self.max_y = int(max_range[1])
        self.axes.set_xlim(-self.max_x, self.max_x)
        self.axes.set_ylim(-self.max_y, self.max_y)

        self.num_vertices = int(input())
        for i in range(self.num_vertices):
            split_in = input().split()
            self.vertices.append(Vertex(i, int(split_in[0]), int(split_in[1])))
            plt.plot(self.vertices[i].x, self.vertices[i].y, marker="o", markersize=5)

    def display_vertices(self):
        for v in self.vertices:
            print(str(v.num) + " " + str(v.x) + " " + str(v.y))

    def arbitrary_tsp(self):
        # loop through remaining vertices
        for i in range(3, self.num_vertices):
            next_v = self.vertices[i]
            best_candidate = math.inf
            best_ind = 0
            for v in range(1, len(self.tour) - 1):
                temp_candidate = find_distance(self.vertices[v], next_v) \
                                 + find_distance(self.vertices[v + 1], next_v)
                if temp_candidate < best_candidate:
                    best_candidate = temp_candidate
                    best_ind = v
            self.tour.insert(best_ind, next_v.num)

    def two_opt(self):
        for i in range(len(self.tour) - 4):
            a_b = find_distance(self.vertices[self.tour[i]], self.vertices[self.tour[i + 1]])
            for j in range(i+1, len(self.tour) - 1):
                c_d = find_distance(self.vertices[self.tour[j]], self.vertices[self.tour[j + 1]])

                a_c = find_distance(self.vertices[self.tour[i]], self.vertices[self.tour[j]])
                b_d = find_distance(self.vertices[self.tour[i+1]], self.vertices[self.tour[j+1]])

                if(a_c + b_d) < (a_b + c_d):
                    self.tour[i+1], self.tour[j] = self.tour[j], self.tour[i+1]

    def tour_distance(self, tour):
        distance = 0.0
        for i in range(0, len(tour) - 1):
            distance += find_distance(self.vertices[tour[i]],
                                      self.vertices[tour[i + 1]])
        return distance

    def draw_tour(self):
        for i in range(0, len(self.tour) - 1):
            plt.plot([self.vertices[self.tour[i]].x, self.vertices[self.tour[i + 1]].x],
                     [self.vertices[self.tour[i]].y, self.vertices[self.tour[i + 1]].y],
                     color="black", linewidth=0.3)

    def display_tour(self):
        self.distance = self.tour_distance(self.tour)
        print("distance: " + str(self.distance))
        print(self.tour)
        self.draw_tour()
        plt.title("distance: " + str(self.distance))
        plt.show()


def main():
    tsp = TSP()
    tsp.get_vertices()
    tsp.arbitrary_tsp()
    tsp.two_opt()
    tsp.display_tour()


if __name__ == "__main__":
    main()
