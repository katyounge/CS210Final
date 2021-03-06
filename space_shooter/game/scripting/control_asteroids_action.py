from constants import *
import random
from game.scripting.action import Action
from game.casting.point import Point
from game.casting.image import Image
from game.casting.asteroid import Asteroid
from game.casting.body import Body


class ControlAsteroidsAction(Action):
    """Handles the creation and movement of the Astroid actors"""

    def __init__(self, keyboard_service):
        """Creates the CollideBordersAction
        
        Args:
            keyboard_service: An object that handles keyboard actions.
        """
        self._keyboard_service = keyboard_service
        self._count = 0
        
    def execute(self, cast, script, callback):
        """Executes the movement of all the astroid actors.
        
        Args:
            cast: an object that holds all actors needed for the scene 
            script: an object that tells the actors what to do.
            callback: Calls the actions to be executed.
        """
        
        self._count += 1

        if (self._count % 80) == 0: 
            asteroid = self._add_asteroid(cast)
            asteroid.fall()
        
     
    def _add_asteroid(self, cast):
        """adds astroid actors.
        
        Args:
            cast: an object that holds all actors needed for the scene
        """
        
        asteroid_options = [GREEN_ASTEROID_IMAGE, GRAY_ASTEROID_IMAGE, BROWN_ASTEROID_IMAGE]
        image_file = random.choice(asteroid_options)
        if image_file == GREEN_ASTEROID_IMAGE:
            x = random.randint(0, (SCREEN_WIDTH - GREEN_ASTEROID_WIDTH))
            y = 0 - GREEN_ASTEROID_HEIGHT
            size = Point(GREEN_ASTEROID_WIDTH, GREEN_ASTEROID_HEIGHT)
            points = ASTEROID_POINTS_GREEN
            

        elif image_file == GRAY_ASTEROID_IMAGE:
            x = random.randint(0, (SCREEN_WIDTH - GRAY_ASTEROID_WIDTH))
            y = 0 - GRAY_ASTEROID_HEIGHT
            size = Point(GRAY_ASTEROID_WIDTH, GRAY_ASTEROID_HEIGHT)
            points = ASTEROID_POINTS_GRAY
            

        elif image_file == BROWN_ASTEROID_IMAGE:
            x = random.randint(0, (SCREEN_WIDTH - BROWN_ASTEROID_WIDTH))
            y = 0 - GREEN_ASTEROID_HEIGHT
            size = Point(BROWN_ASTEROID_WIDTH, BROWN_ASTEROID_HEIGHT)
            points = ASTEROID_POINTS_BROWN
        
        image = Image(image_file)
        position = Point(x, y)
        velocity = Point(0, ASTEROID_VELOCITY)
        body = Body(position, size, velocity)
        
        hits = ASTEROID_HIT

        asteroid = Asteroid(body, image, points, hits) # morgan added points
        cast.add_actor(ASTEROID_GROUP, asteroid)
        return asteroid



    