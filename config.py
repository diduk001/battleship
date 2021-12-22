class Config:
    SCREEN_WIDTH = 602
    SCREEN_HEIGHT = 602

    FIELD_WIDTH = 10
    FIELD_HEIGHT = 10

    BORDER_WEIGHT = 2
    BORDER_COLOR = (0, 0, 0)
    CEIL_COLOR_BY_TYPE = {0: (255, 0, 0),
                          1: (255, 127, 0),
                          2: (255, 255, 0),
                          3: (0, 255, 0),
                          4: (0, 0, 255),
                          5: (75, 0, 130),
                          6: (148, 0, 211)}

    assert (SCREEN_WIDTH - ((FIELD_WIDTH + 1) * BORDER_WEIGHT)) % FIELD_WIDTH == 0, "Width is not properly divisible"
    CEIL_WIDTH = (SCREEN_WIDTH - ((FIELD_WIDTH + 1) * BORDER_WEIGHT)) // FIELD_WIDTH

    assert (SCREEN_HEIGHT - (
            (FIELD_HEIGHT + 1) * BORDER_WEIGHT)) % FIELD_HEIGHT == 0, "Height is not properly divisible"
    CEIL_HEIGHT = (SCREEN_HEIGHT - ((FIELD_HEIGHT + 1) * BORDER_WEIGHT)) // FIELD_HEIGHT
