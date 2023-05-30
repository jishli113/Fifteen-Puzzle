# author: Joshua Li
# date: Dec 4, 2022
# file: fifteen.py a Python program that implements the fifteen puzzle base code containing all functionality
# input: for the base code: nothing. for the print game: a user typed input
# output: base code: nothing. print game: the updated board printed out
import numpy as np
import random
from graph import Vertex, Graph


class Fifteen:

    # create a vector (ndarray) of tiles and the layout of tiles positions (a graph)
    # tiles are numbered 1-15, the last tile is 0 (an empty space)
    def __init__(self, size=4):
        self.tiles = Graph()
        for i in range(1, 17):
            if i == 16:
                self.tiles.vertList[16] = Vertex(0)
            else:
                self.tiles.addVertex(i)
        retvert = self.tiles.getDict()
        for i in range(1, 17):
            baseline = int((i - 1) / 4)
            if i - 1 >= 1 and int((i - 1) / 4) == baseline and (i - 1) % 4 != 0:
                retvert[i].addNeighbor(Vertex(retvert[i - 1].getId()))
            if i + 1 <= 16 and (int((i + 1) / 4) == baseline or (i + 1) % 4 == 0):
                retvert[i].addNeighbor(Vertex(retvert[i + 1].getId()))
            if i + 4 <= 16:
                retvert[i].addNeighbor(Vertex(retvert[i + 4].getId()))
            if i - 4 >= 1:
                retvert[i].addNeighbor(Vertex(retvert[i - 4].getId()))

    # draw the layout with tiles:
    # +---+---+---+---+
    # | 1 | 2 | 3 | 4 |
    # +---+---+---+---+
    # | 5 | 6 | 7 | 8 |
    # +---+---+---+---+
    # | 9 |10 |11 |12 |
    # +---+---+---+---+
    # |13 |14 |15 |   |
    # +---+---+---+---+
    def draw(self):
        print("")
        count = 0
        for i in self.tiles.getDict().keys():
            if count == 0:
                print("+---+---+---+---+\n|", end="")
            if self.tiles.getDict()[i].getId() >= 10:
                print(f"{self.tiles.getDict()[i].getId()} |", end="")
            else:
                print(f" {self.tiles.getDict()[i].getId()} |", end="")
            count = count + 1
            if count == 4:
                count = 0
                print()
        print("+---+---+---+---+")

    # return a string representation of the vector of tiles as a 2d array
    # 1  2  3  4
    # 5  6  7  8
    # 9 10 11 12
    # 13 14 15
    def __str__(self):
        ret = ""
        count = 0
        for i in self.tiles.getDict().keys():
            count = count + 1
            if count == 4:
                if self.tiles.getDict()[i].getId() == 0:
                    ret = ret + "  " + " \n"
                elif self.tiles.getDict()[i].getId() >= 10:
                    ret = ret + str(self.tiles.getDict()[i].getId()) + " \n"
                else:
                    ret = ret + " " + str(self.tiles.getDict()[i].getId()) + " \n"
                count = 0
            else:
                if self.tiles.getDict()[i].getId() == 0:
                    ret = ret + "   "
                elif self.tiles.getDict()[i].getId() >= 10:
                    ret = ret + str(self.tiles.getDict()[i].getId()) + " "
                else:
                    ret = ret + " " + str(self.tiles.getDict()[i].getId()) + " "
                    # print(ret)
        return ret

    # exchange i-tile with j-tile
    # tiles are numbered 1-15, the last tile is 0 (empty space)
    # the exchange can be done using a dot product (not required)
    # can return the dot product (not required)
    def transpose(self, i, j):
        self.tiles.swapVertices(i, j)

    # checks if the move is valid: one of the tiles is 0 and another tile is its neighbor
    def is_valid_move(self, move):
        vertex = None
        for i in self.tiles.getDict().keys():
            if self.tiles.getDict()[i].getId() == move:
                vertex = self.tiles.getDict()[i]
                break
        for i in vertex.getConnections():
            if 0 == i.getId():
                return True
        return False

    # update the vector of tiles
    # if the move is valid assign the vector to the return of transpose() or call transpose
    def update(self, move):
        if self.is_valid_move(move):
            one = 0
            for i in self.tiles.getDict().keys():
                if self.tiles.getDict()[i].getId() == move:
                    one = i
                    break
            store = -1
            for i in range(1, 17):
                if self.tiles.getDict()[i].getId() == 0:
                    store = i
                    break
            self.transpose(one, store)
            retvert = self.tiles.getDict()
            for i in range(1, 17):
                retvert[i].replaceConnections(connections={})
            for i in range(1, 17):
                baseline = int((i - 1) / 4)
                if i - 1 >= 1 and int((i - 1) / 4) == baseline and (i - 1) % 4 != 0:
                    retvert[i].addNeighbor(Vertex(retvert[i - 1].getId()))
                if i + 1 <= 16 and (int((i + 1) / 4) == baseline or (i + 1) % 4 == 0):
                    retvert[i].addNeighbor(Vertex(retvert[i + 1].getId()))
                if i + 4 <= 16:
                    retvert[i].addNeighbor(Vertex(retvert[i + 4].getId()))
                if i - 4 >= 1:
                    retvert[i].addNeighbor(Vertex(retvert[i - 4].getId()))
            return True
        return False

    # shuffle tiles
    def shuffle(self, moves=100):
        retvert = {}
        vertices = []
        while True:
            solvabletest = []
            for i in self.tiles.getDict().keys():
                vertices.append(self.tiles.getDict()[i])
            for i in range(1, 17):
                a = int(len(vertices) * random.random())
                p = vertices[a].getId()
                vertices.pop(a)
                solvabletest.append(p)
                retvert[i] = Vertex(p)
            if self.is_solvable(solvabletest):
                break
        for i in range(1, 17):
            baseline = int((i - 1) / 4)
            if i - 1 >= 1 and int((i - 1) / 4) == baseline and (i - 1) % 4 != 0:
                retvert[i].addNeighbor(Vertex(retvert[i - 1].getId()))
            if i + 1 <= 16 and (int((i + 1) / 4) == baseline or (i + 1) % 4 == 0):
                retvert[i].addNeighbor(Vertex(retvert[i + 1].getId()))
            if i + 4 <= 16:
                retvert[i].addNeighbor(Vertex(retvert[i + 4].getId()))
            if i - 4 >= 1:
                retvert[i].addNeighbor(Vertex(retvert[i - 4].getId()))
        # for i in range(16):
        #     print(retvert[i].getId())
        self.tiles.replaceVertices(retvert)

    # verify if the puzzle is solved
    def is_solved(self):
        list = self.tiles.getDict()
        for i in list.keys():
            if list[i].getId() != i:
                if i != 16:
                    return False
        return True

    # verify if the puzzle is solvable (optional)
    def is_solvable(self, vals):
        count = 0
        for i in range(len(vals) - 1):
            for j in range(i + 1, len(vals)):
                if vals[i] > vals[j]:
                    count = count + 1
        if count % 2 == 0:
            return True
        else:
            return False

    # solve the puzzle (optional)
    def solve(self):
        current = []
        pos = 0
        for i in self.tiles.vertList.keys():
            current.append(self.tiles.vertList[i].getId())
            if self.tiles.vertList[i].getId() == 0:
                pos = i
        self.tiles.breadth_first_search(current, pos - 1, None, [])


if __name__ == '__main__':
    game = Fifteen()
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_valid_move(15) == True
    assert game.is_valid_move(12) == True
    assert game.is_valid_move(14) == False
    assert game.is_valid_move(1) == False
    game.update(15)
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14    15 \n'
    game.update(15)
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_solved() == True
    game.shuffle()
    assert str(game) != ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_solved() == False

    game = Fifteen()
    game.shuffle()
    game.draw()
    while True:
        move = input('Enter your move or q to quit: ')
        if move == 'q':
            break
        elif not move.isdigit():
            continue
        game.update(int(move))
        game.draw()
        if game.is_solved():
            break
    print('Game over!')

