from graphics import Rectangle, Point

class Player:
    def __init__(self, window):
        self.window = window
        self.width = 10
        self.height = 40
        self.step_size = 4
        self.color = "#ff0000"
        x = self.window.getWidth() - 40
        y = self.window.getHeight()/2
        self.y_goal = y
        self.player = Rectangle(
            Point(x - (self.width/2), y - (self.height/2)),
            Point(x + (self.width/2), y + (self.height/2))
        )
        self.player.setFill(self.color)
        self.player.draw(self.window)
        self.window.bind('<Motion>', self.__new_y_goal)

    def __new_y_goal(self, event):
        self.y_goal = event.y

    def get_position(self):
        pos = self.player.getCenter()
        return {
            "x": pos.getX(),
            "y": pos.getY()
        }

    def tick(self):
        # Move player
        y = self.get_position()["y"]
        if ((self.y_goal - y) < self.step_size and (self.y_goal - y) > -self.step_size): # apparenlty this is faster than abs()
            return
        if (self.y_goal > y):
            self.player.move(0, self.step_size)
        elif (self.y_goal < y):
            self.player.move(0, -self.step_size)
