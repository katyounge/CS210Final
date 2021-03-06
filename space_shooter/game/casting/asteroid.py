from constants import *
from game.casting.actor import Actor
from game.casting.point import Point


class Asteroid(Actor):
    """A space rock."""
    
    def __init__(self, body, image, points, hits, debug = False):
        """Constructs a new Asteroid.

        Args:
            body: A new instance of Body.
            image: A new instance of Image.
            debug: If it is being debugged. 
            points: point value of each asteroid
        """
        super().__init__(debug)
        self._body = body
        self._image = image
        self._points = points # morgan added
        self._hits = hits 

    def get_body(self):
        """Gets the asteroid's body.
        
        Returns:
            An instance of Body.
        """
        return self._body

    def get_image(self):
        """Gets the asteroid's image.
        
        Returns:
            An instance of Image.
        """
        return self._image

    def set_image(self, next_image):
        """Changes the asteroid's image with a
        new one.
        Arg:
            next_image: A new instance of Image
            to replace the old one.
        
        Returns:
            An instance of Image.
        """
        self._image = next_image
        
        return self._image
        
    def fall(self):
        """Release the asteroid downward."""
        
        vx = 0
        vy = ASTEROID_VELOCITY
        velocity = Point(vx, vy)
        self._body.set_velocity(velocity)
    
    def get_points(self): # morgan added
        """Gets the asteroids's points.
        
        Returns:
            A number representing the asteroids's points.
        """
        return self._points

    def get_hits(self): 
        """Gets the # of asteroids hit.
        
        Returns:
            A number representing that one asteroid was hit.
        """
        return self._hits