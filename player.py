class Player:
    def __init__(self, color, name):
        self.color = color
        self.name = name
        self.description = name + " is " + color

    def get_input(self):
        try:
            return int(input("What column do you want you piece in? "))
        except:
            raise