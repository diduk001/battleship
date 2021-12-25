class Config:
    WINDOW_CAPTION = "Battleship"

    SCREEN_WIDTH = 1204
    SCREEN_HEIGHT = 602 + 60

    FIELD_PIX_WIDTH = 602
    FIELD_PIX_HEIGHT = 602

    FIELD_WIDTH = 10
    FIELD_HEIGHT = 10

    CEIL_BORDER_WEIGHT = 2
    CEIL_BORDER_COLOR = (0, 0, 0)

    # checks if we can fit field into width, height
    assert (FIELD_PIX_WIDTH - ((FIELD_WIDTH + 1) * CEIL_BORDER_WEIGHT)) % FIELD_WIDTH == 0, "Width is not properly " \
                                                                                            "divisible"
    CEIL_WIDTH = (FIELD_PIX_WIDTH - ((FIELD_WIDTH + 1) * CEIL_BORDER_WEIGHT)) // FIELD_WIDTH

    assert (FIELD_PIX_HEIGHT - (
            (FIELD_HEIGHT + 1) * CEIL_BORDER_WEIGHT)) % FIELD_HEIGHT == 0, "Height is not properly divisible"
    CEIL_HEIGHT = (FIELD_PIX_HEIGHT - ((FIELD_HEIGHT + 1) * CEIL_BORDER_WEIGHT)) // FIELD_HEIGHT

    PLAYERS_CNT = 2
    PLAYER_UI_WIDTH = FIELD_PIX_WIDTH
    PLAYER_UI_HEIGHT = FIELD_PIX_HEIGHT + 60
    PLAYER_UI_FONT_NAME = 'arial'
    PLAYER_UI_FONT_SIZE = 38
    PLAYER_BORDER_COLOR = (0, 0, 255)
    ACTIVE_PLAYER_BORDER_COLOR = (255, 0, 0)
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
    10 - ship ship size 1        +
    """

    CEIL_SPRITES_FILENAMES = ("empty.png",
                              "empty.png",
                              "body_v.png",
                              "body_h.png",
                              "empty_with_bomb.png",
                              "ship_shotten.png",
                              "left_end.png",
                              "right_end.png",
                              "up_end.png",
                              "down_end.png",
                              "size_one.png")

    TYPES_TO_MAKE_INVISIBLE = (2, 3, 6, 7, 8, 9, 10)

    SHIPS_SIZES = (4, 3, 3, 2, 2, 2, 1, 1, 1, 1)
