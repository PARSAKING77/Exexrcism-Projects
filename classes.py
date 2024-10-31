"""Solution to Ellen's Alien Game exercise."""


class Alien:
    total_aliens_created = 0  # Class variable to keep track of total aliens created

    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = 3
        Alien.total_aliens_created += 1  # Increment the total aliens created

    def hit(self):
        if self.health > 0:
            self.health -= 1

    def is_alive(self):
        return self.health > 0

    def teleport(self, new_x, new_y):
        self.x_coordinate = new_x
        self.y_coordinate = new_y

    def collision_detection(self, other_object):
        # Placeholder for collision detection logic
        pass

def new_aliens_collection(start_positions):
    return [Alien(x, y) for x, y in start_positions]



#TODO:  create the new_aliens_collection() function below to call your Alien class with a list of coordinates.
