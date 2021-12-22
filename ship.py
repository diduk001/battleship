class Ship:
    def __init__(self, field, size, x, y, direction):
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

    def shot(self, x, y):
        if self.status[(x, y)]:
            self.status[(x, y)] = 0
            self.hp -= 1
        if not self.hp:
            self.drowned()

    def drowned(self):
        for x, y in self.ceils_around:
            self.field.field_view[x][y] = 4

    def place_up(self, size, x, y):
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

    def place_down(self, size, x, y):
        for i in range(-1, size + 1):
            for j in range(-1, 2):
                p = (x + i, y + j)
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

    def place_left(self, size, x, y):
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

    def place_right(self, size, x, y):
        for i in range(-1, 2):
            for j in range(-1, size + 1):
                p = (x + i, y + j)
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
