class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __str__(self):
        return f"{self.x, self.y, self.width, self.height}"


class Square():

    def __init__(self, x, y, width):
        self.x = x
        self.y = y
        self.width = width

    def __str__(self):
        return f"{self.x, self.y, self.width}"


class Circle():

    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def __str__(self):
        return f"{self.x, self.y, self.r}"
