from graphics import GraphWin, Rectangle, Point, Text, Entry

from src.save_leaderboard import update_leaderboard, read_leaderboard

class Window:
    def __init__(self, game):
        self.width = 800
        self.height = 600
        self.game = game
        self.window = GraphWin("Pong", self.width, self.height)

    def start_menu(self):
        self.window.setBackground("#444444")

        rectangle = Rectangle(Point(10, 10), Point(self.width-10, self.height-10))
        rectangle.setFill("#222222")
        rectangle.draw(self.window)
        
        text = Text(Point(self.width/2, self.height/2), "Play")
        text.setFill("#ffffff")
        text.setSize(30)
        text.draw(self.window)

        leaderboard_btn = Text(Point(self.width/2, 30), "Leaderboard")
        leaderboard_btn.setFill("#ffffff")
        leaderboard_btn.setSize(15)
        leaderboard_btn.draw(self.window)

        credits = Text(Point(self.width/2, (self.height/2)+90), '''Eric Loges Binsfeld
Lucca Oliari Peixoto
Lucca Resende da Costa Paiva
Thiago Rios da Silva
''')
        credits.setFill("#ffffff")
        credits.setSize(12)
        credits.draw(self.window)
        
        while True:
            click = self.window.getMouse()
            if (20 <= click.getY() <= 50 and (self.width/2)-50 <= click.getX() <= (self.width/2)+50):
                self.leaderboard([
                    rectangle,
                    text,
                    leaderboard_btn,
                    credits
                ])
            else:
                break

        rectangle.undraw()
        text.undraw()
        leaderboard_btn.undraw()
        credits.undraw()
        self.status()

    def status(self):
        textlife = Text(Point(self.width/2, 15),f"Vidas restantes: {self.game.lives}")
        textlife.setFill('#ffffff')
        textlife.draw(self.window)
        textscore = Text(Point(self.width/ 2, 35), f"Score: {self.game.score}")
        textscore.setFill('#ffffff')
        textscore.draw(self.window)
        self.textlife = textlife
        self.textscore = textscore

    def leaderboard(self, items):
        # Undraw window elements
        for item in items:
            item.undraw()

        # Draw leaderboard

        # create text
        leaderboard_txt = Text(Point(self.width/2, 30), "Leaderboard")
        leaderboard_txt.setFill("#ffffff")
        leaderboard_txt.setSize(30)
        leaderboard_txt.draw(self.window)

        # create leaderboard
        leaderboard = "\n".join(read_leaderboard()[:20])
        leaderboard = Text(Point(self.width/2, self.height/2), leaderboard)
        leaderboard.setFill("#ffffff")
        leaderboard.setSize(15)
        leaderboard.draw(self.window)

        self.window.getMouse()

        # Undraw leaderboard
        leaderboard_txt.undraw()
        leaderboard.undraw()

        # Redraw window elements
        for item in items:
            item.draw(self.window)

    def game_over(self):
        window = self.window
        width, height = self.width, self.height
        for item in window.items:
            item.undraw()

        bg = Rectangle(Point(0, 0), Point(width, height))
        bg.setFill("#444444")
        bg.draw(window)

        text = Text(Point(width/2, (height/2) - 50), "Game Over")
        text.setFill("#ffffff")
        text.setSize(30)
        text.draw(window)

        input_box = Entry(Point(width/2, height/2), 20)
        input_box.setSize(20)
        input_box.draw(window)

        while True:
            input_box.setText(input_box.getText()[:10].upper())
            key = window.checkKey()
            if (key == "Return"):
                break
        nickname = input_box.getText()

        update_leaderboard(nickname, self.game.score)

        window.close()
