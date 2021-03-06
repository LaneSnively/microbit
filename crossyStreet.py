from microbit import *
import machine


class Car:
    """
    Car which moves vertically up and down the screen
    """
    def __init__(self):
        self.x = 2
        self.y = -1

    def get_positions(self):
        return ((self.x, self.y), (self.x, self.y + 1 if self.y < 4 else 0))

    def move(self):
        self.y = (self.y + 1) % 5

    def draw(self):
        for x, y in self.get_positions():
            display.set_pixel(x, y, 9)


class Player:
    """
    Left-right moving player which can be controlled with buttons
    """
    RIGHT = 1
    LEFT = -1
    STOPPED = 0
    LEFT_EDGE = 0
    RIGHT_EDGE = 4

    def __init__(self):
        self.alive = True
        self.score = 0
        self.just_scored = False
        self.x = self.LEFT_EDGE
        self.y = 2
        self.direction = self.STOPPED

    def get_position(self):
        return (self.x, self.y)

    def die(self):
        self.alive = False
        i = 2
        while(i < 10):
            display.show(Image.ALL_CLOCKS, delay = i * 10)
            sleep(75)
            display.scroll(str(self.score))
            sleep(75)
            display.show(Image.ALL_CLOCKS, delay = i * 2)
            sleep(75)
            i += 1
        
        display.show(Image.GHOST)
        sleep(5000)
        machine.reset()

    def move(self):
        """
        Move the player one step further in their
        current direction
        """
        self.just_scored = False
        self.x += self.direction
        if self.x in (self.LEFT_EDGE, self.RIGHT_EDGE):
            # Player reached the edge - another run survived!
            if self.direction != self.STOPPED:
                self.score += 1
                self.just_scored = True

            self.direction = self.STOPPED

    def draw(self):
        display.set_pixel(self.x, self.y, 9)

    def act_on_input(self):
        # If we're standing still, look for a button press.
        if self.direction == self.STOPPED:
            if button_b.was_pressed() and self.x == self.LEFT_EDGE:
                self.direction = self.RIGHT

            elif button_a.was_pressed() and self.x == self.RIGHT_EDGE:
                self.direction = self.LEFT


class Game:
    def __init__(self):
        display.scroll("crossy street")
        self.car = Car()
        self.player = Player()
        self.frame_rate = 7

    def detect_collisions(self):
        """
        Have the player and the car collided?
        """
        return self.player.get_position() in self.car.get_positions()

    def do_frame(self):
        """
        Called once per frame to advance the game state
        """
        # Adjust the speed as the player's score gets higher
        # (But don't let it exceed the actual frame rate)
        if self.player.score % 2 == 0:
            self.frame_rate = max(7, min(15, self.player.score))

        if self.player.alive:
            display.clear()

            self.car.move()
            self.player.act_on_input()
            self.player.move()

            if self.detect_collisions():
                self.player.die()
            else:
                self.car.draw()
                self.player.draw()


game = Game()
while True:
    timestamp = running_time()

    game.do_frame()

    # Keep the frame rate consistent
    new_timestamp = running_time()
    time_taken = (new_timestamp - timestamp)
    interval = 1000 // game.frame_rate
    if time_taken < interval:
        sleep(interval - time_taken)
    timestamp = new_timestamp
