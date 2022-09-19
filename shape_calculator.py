class Rectangle:
    def __init__(self, width=None, height=None):
        self.width = width
        self.height = height

    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    # @classmethod
    def get_area(self):
        return self.width*self.height

    def get_perimeter(self):
        return 2*self.height + 2*self.width

    def get_diagonal(self):
        return (self.width**2 + self.height**2)**.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            horizontal_line = "*" * self.width
            area = ""
            for i in range(self.height):
                area += horizontal_line + "\n"
            return area

    def get_amount_inside(self, shape):
        amount = self.get_area()//shape.get_area()
        return amount

    # def str(shape):
    #     string =


class Square(Rectangle):
    def __init__(self, side):
        self.height = side
        self.width = side

    def set_side(self, side):
        self.height = side
        self.width = side

    def set_width(self, side):
        self.height = side
        self.width = side

    def set_height(self, side):
        self.height = side
        self.width = side

    def __repr__(self):
        return f"Square(side={self.width})"

    def get_perimeter(self):
        return Rectangle.get_perimeter(self)

    def get_area(self):
        return Rectangle.get_area(self)

    def get_diagonal(self):
        return Rectangle.get_diagonal(self)

    def get_picture(self):
        return Rectangle.get_picture(self)
