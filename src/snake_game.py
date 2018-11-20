"""
from LeetCode

Design a Snake game that is played on a device with screen size = width x height. Play the game online if you are
not familiar with the game. The snake is initially positioned at the top left corner (0,0) with length = 1 unit. You
are given a list of food's positions in row-column order. When a snake eats the food, its length and the game's score
both increase by 1. Each food appears one by one on the screen. For example, the second food will not appear until
the first food was eaten by the snake.
When a food does appear on the screen, it is guaranteed that it will not appear on a block occupied by the snake.
"""
from tabulate import tabulate


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class QueueWithPeek:
    def __init__(self):
        self.head = None
        self.tail = None
        self.__size = 0

    def size(self):
        return self.__size

    def put(self, val):
        if self.__size == 0:
            n = Node(val)
            self.head = n
            self.tail = n
            self.__size = 1
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next
            self.__size += 1

    def peek(self):
        if not self.__size == 0:
            val = self.head.val
            return val

    def get(self):
        if not self.__size == 0:
            val = self.head.val
            self.head = self.head.next
            self.__size -= 1
            return val

    def __repr__(self):
        if self.__size == 0:
            return '{}'
        else:
            rpr = '{'
            cur = self.head
            while cur is not None:
                rpr += str(cur.val) + ', '
                cur = cur.next
            return rpr + '}'


class SnakeGame:

    def __init__(self, width, height, food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        self.food = [(i, j) for [i, j] in food]
        self.food_ind = 0
        self.width = width
        self.height = height
        self.score = 0
        self.queue = QueueWithPeek()
        self.queue.put((0, 0))
        self.set = set()
        self.set.add((0, 0))
        self.head = 0, 0

    def move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down
        @return The game's score after the move. Return -1 if game over.
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """

        # compute where the snake would be after the move
        row, col = self.head
        if direction == 'U':
            new_head = row - 1, col
        elif direction == 'R':
            new_head = row, col + 1
        elif direction == 'D':
            new_head = row + 1, col
        elif direction == 'L':
            new_head = row, col - 1
        else:
            raise Exception('invalid direction')

        # check if the snake hits itself after the move
        tail = self.queue.peek()
        if new_head != tail and new_head in self.set:
            return -1  # dead

        # check if the snake hits a wall after the move
        r, c = new_head
        if r < 0 or c < 0 or r >= self.height or c >= self.width:
            return -1

        # check if snake eats food after move
        eat_food = False
        if self.food_ind < len(self.food):
            if new_head == self.food[self.food_ind]:
                eat_food = True
                self.food_ind += 1
                self.score += 1

        # move the snake
        if not eat_food:
            tail = self.queue.get()
            self.set.remove(tail)
        self.queue.put(new_head)
        self.set.add(new_head)
        self.head = new_head

        return self.score

    def __repr__(self):
        rpr = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                if (i, j) in self.set:
                    row.append('S')
                elif self.food_ind < len(self.food):
                    if (i, j) == self.food[self.food_ind]:
                        row.append('F')
                    else:
                        row.append(' ')
                else:
                    row.append(' ')
            rpr.append(row)
        return tabulate(rpr, tablefmt='grid')

    def __str__(self):
        return self.__repr__()
