import  os.path
class Config:
    SCREEN_WIDTH = 602
    SCREEN_HEIGHT = 602

    FIELD_PIX_WIDTH = 602
    FIELD_PIX_HEIGHT = 602

    FIELD_WIDTH = 10
    FIELD_HEIGHT = 10

    BORDER_WEIGHT = 2
    BORDER_COLOR = (0, 0, 0)

    CEIL_SPRITES_FILENAMES = ["empty.png",
                 "empty.png",
                 "body_v.png",
                 "body_h.png",
                 "empty_with_bomb.png",
                 "ship_shotted.png",
                 "left_end.png",
                 "right_end.png",
                 "up_end.png",
                 "down_end.png",
                 "size_one.png"]
    """
    0 - empty               +
    1 - empty around ship   +
    2 - vertical body       +
    3 - horizontal body     +
    4 - empty after shot    +
    5 - ship after shot     +
    6 - left end            +
    7 - right end           +
    8 - up end              +
    9 - down end            +
    10 - ship size 1        +
    """

    SHIPS_SIZES = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]

    assert (FIELD_PIX_WIDTH - ((FIELD_WIDTH + 1) * BORDER_WEIGHT)) % FIELD_WIDTH == 0, "Width is not properly divisible"
    CEIL_WIDTH = (FIELD_PIX_WIDTH - ((FIELD_WIDTH + 1) * BORDER_WEIGHT)) // FIELD_WIDTH

    assert (FIELD_PIX_HEIGHT - (
            (FIELD_HEIGHT + 1) * BORDER_WEIGHT)) % FIELD_HEIGHT == 0, "Height is not properly divisible"
    CEIL_HEIGHT = (FIELD_PIX_HEIGHT - ((FIELD_HEIGHT + 1) * BORDER_WEIGHT)) // FIELD_HEIGHT
