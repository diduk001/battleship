"""
0 - empty               +
1 - empty around ship   +
2 - horizontal body     +
3 - vertical body       +
4 - empty after shot    +
5 - ship after shot     +
6 - up end              +
7 - down end            +
8 - left end            +-
9 - right end           +-
10 - ship size 1        +
"""


class Ship:
    def __init__(self, field, size: int, x: int, y: int, direction: int):
        self.field = field
        self.x = x
        self.y = y
        self.direction = direction
        self.status = {}
        self.hp = size
        self.ceils_around = []
        if direction == 1:
            self.place_up(size, x, y)
        if direction == 2:
            self.place_down(size, x, y)
        if direction == 3:
            self.place_left(size, x, y)
        if direction == 4:
            self.place_right(size, x, y)

    def shot(self, x: int, y: int) -> None:
        if self.status[(x, y)]:
            self.status[(x, y)] = 0
            self.hp -= 1
            self.field.field_view[x][y] = 5
        if not self.hp:
            self.drowned()

    def drowned(self) -> None:
        for x, y in self.ceils_around:
            self.field.field_view[x][y] = 4

    def place_up(self, size: int, x: int, y: int) -> None:
        for i in range(-1, size + 1):
            for j in range(-1, 2):
                p = (x - i, y + j)
                if 0 <= x - i < 10 and 0 <= y + j < 10:
                    self.ceils_around.append(p)
                    self.field.field_view[x - i][y + j] = 1
                    if p in self.field.free_spots:
                        self.field.free_spots.remove(p)
                if j == 0 and 0 <= i < size:
                    self.field.field_view[x - i][y + j] = 3
                    self.status[p] = 1
                    self.ceils_around.remove(p)
                    self.field.field_ships[x - i][y + j] = self
        if size != 1:
            self.field.field_view[x][y] = 7
            self.field.field_view[x - size + 1][y] = 6
        else:
            self.field.field_view[x][y] = 10

    def place_down(self, size: int, x: int, y: int) -> None:
        for i in range(-1, size + 1):
            for j in range(-1, 2):
                p = x + i, y + j
                if 0 <= x + i < 10 and 0 <= y + j < 10:
                    self.ceils_around.append(p)
                    self.field.field_view[x + i][y + j] = 1
                    if p in self.field.free_spots:
                        self.field.free_spots.remove(p)
                if j == 0 and 0 <= i < size:
                    self.field.field_view[x + i][y + j] = 3
                    self.status[p] = 1
                    self.ceils_around.remove(p)
                    self.field.field_ships[x + i][y + j] = self
        if size != 1:
            self.field.field_view[x][y] = 6
            self.field.field_view[x + size - 1][y] = 7
        else:
            self.field.field_view[x][y] = 10

    def place_left(self, size: int, x: int, y: int) -> None:
        for i in range(-1, 2):
            for j in range(-1, size + 1):
                p = (x + i, y - j)
                if 0 <= x + i < 10 and 0 <= y - j < 10:
                    self.ceils_around.append(p)
                    self.field.field_view[x + i][y - j] = 1
                    if p in self.field.free_spots:
                        self.field.free_spots.remove(p)
                if i == 0 and 0 <= j < size:
                    self.field.field_view[x + i][y - j] = 2
                    self.status[p] = 1
                    self.ceils_around.remove(p)
                    self.field.field_ships[x + i][y - j] = self
        if size != 1:
            self.field.field_view[x][y] = 9
            self.field.field_view[x][y - size + 1] = 8
        else:
            self.field.field_view[x][y] = 10

    def place_right(self, size: int, x: int, y: int) -> None:
        for i in range(-1, 2):
            for j in range(-1, size + 1):
                p = x + i, y + j
                if 0 <= x + i < 10 and 0 <= y + j < 10:
                    self.ceils_around.append(p)
                    self.field.field_view[x + i][y + j] = 1
                    if p in self.field.free_spots:
                        self.field.free_spots.remove(p)
                if i == 0 and 0 <= j < size:
                    self.field.field_view[x + i][y + j] = 2
                    self.status[p] = 1
                    self.ceils_around.remove(p)
                    self.field.field_ships[x + i][y + j] = self
        if size != 1:
            self.field.field_view[x][y] = 8
            self.field.field_view[x][y + size - 1] = 9
        else:
            self.field.field_view[x][y] = 10
