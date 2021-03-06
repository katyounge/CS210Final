from game.casting.color import Color

# -------------------------------------------------------------------------------------------------- 
# GENERAL GAME CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# GAME
GAME_NAME = "Space Shooter"
FRAME_RATE = 60

# SCREEN
SCREEN_WIDTH = 1040
SCREEN_HEIGHT = 680
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2

# FIELD
FIELD_TOP = 0
FIELD_BOTTOM = SCREEN_HEIGHT
FIELD_LEFT = 0
FIELD_RIGHT = SCREEN_WIDTH

# FONT
FONT_FILE = "space_shooter/assets/fonts\\zorque.otf"
FONT_SMALL = 32
FONT_LARGE = 48

# SOUND
WELCOME_SOUND = "space_shooter/assets/sounds\\space_music.mp3"
OVER_SOUND = "space_shooter/assets/sounds\\game_over.mp3"
LASER_SHOOT_SOUND = "space_shooter/assets/sounds\\laser_shoot.mp3"
LASER_HIT_SOUND = "space_shooter/assets/sounds\\laser_hit.mp3"
ASTEROID_HITS_SHIP_SOUND = "space_shooter/assets/sounds\\ship_crash.mp3"

# TEXT
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

# COLORS
BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
PURPLE = Color(255, 0, 255)

# KEYS
LEFT = "left"
RIGHT = "right"
UP = "up"
DOWN = "down"
SPACE = "space"
ENTER = "enter"
PAUSE = "p"

# SCENES
NEW_GAME = 0
TRY_AGAIN = 1
NEXT_LEVEL = 2
IN_PLAY = 3
GAME_OVER = 4

# -------------------------------------------------------------------------------------------------- 
# SCRIPTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# PHASES
INITIALIZE = 0
LOAD = 1
INPUT = 2
UPDATE = 3
OUTPUT = 4
UNLOAD = 5
RELEASE = 6

# -------------------------------------------------------------------------------------------------- 
# CASTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# STATS
STATS_GROUP = "stats"
DEFAULT_LIVES = 3
MAXIMUM_LIVES = 5

# HUD
HUD_MARGIN = 15
HITS_GROUP = "hits"
LIVES_GROUP = "lives"
SCORE_GROUP = "score"
HITS_FORMAT = "HITS: {}"
LIVES_FORMAT = "LIVES: {}"
SCORE_FORMAT = "SCORE: {}"

# ASTEROIDS
ASTEROID_GROUP = "asteroids"
ASTEROID_VELOCITY = 3
GRAY_ASTEROID_IMAGE = "space_shooter/assets/images\\asteroid1.png"
GRAY_ASTEROID_WIDTH = 44
GRAY_ASTEROID_HEIGHT = 44
GRAY_ASTEROID_B_IMAGE = "space_shooter/assets/images\\asteroid1b.png"
GRAY_ASTEROID_B_WIDTH = 33
GRAY_ASTEROID_B_HEIGHT = 39
GRAY_ASTEROID_C_IMAGE = "space_shooter/assets/images\\asteroid1c.png"
GRAY_ASTEROID_C_WIDTH = 25
GRAY_ASTEROID_C_HEIGHT = 27
BROWN_ASTEROID_IMAGE = "space_shooter/assets/images\\asteroid2.png"
BROWN_ASTEROID_WIDTH = 39
BROWN_ASTEROID_HEIGHT = 44
BROWN_ASTEROID_B_IMAGE = "space_shooter/assets/images\\asteroid2b.png"
BROWN_ASTEROID_B_WIDTH = 28
BROWN_ASTEROID_B_HEIGHT = 34
BROWN_ASTEROID_C_IMAGE = "space_shooter/assets/images\\asteroid2c.png"
BROWN_ASTEROID_C_WIDTH = 24
BROWN_ASTEROID_C_HEIGHT = 15
GREEN_ASTEROID_IMAGE = "space_shooter/assets/images\\asteroid3.png"
GREEN_ASTEROID_WIDTH = 43
GREEN_ASTEROID_HEIGHT = 44
GREEN_ASTEROID_B_IMAGE = "space_shooter/assets/images\\asteroid3b.png"
GREEN_ASTEROID_B_WIDTH = 34
GREEN_ASTEROID_B_HEIGHT = 36
GREEN_ASTEROID_C_IMAGE = "space_shooter/assets/images\\asteroid3c.png"
GREEN_ASTEROID_C_WIDTH = 21
GREEN_ASTEROID_C_HEIGHT = 22
ASTEROID_POINTS_GREEN = 10 # morgan added
ASTEROID_POINTS_GRAY = 5
ASTEROID_POINTS_BROWN = 8
ASTEROID_HIT = 1

# LASER
LASER_GROUP = "lasers"
LASER_IMAGE = "space_shooter/assets/images\\laser.png"
LASER_WIDTH = 4
LASER_HEIGHT = 6
LASER_VELOCITY = 6

# SHIP
SHIP_GROUP = "ships"
SHIP_IMAGES = ["space_shooter/assets/images\\ship.png"]
SHIP_WIDTH = 28
SHIP_HEIGHT = 39
SHIP_RATE = 6
SHIP_VELOCITY = 4

# DIALOG
DIALOG_GROUP = "dialogs"
ENTER_TO_START = "PRESS ENTER TO START"
HOW_TO_SHOOT = "PRESS SPACE BAR TO SHOOT"
WAS_GOOD_GAME = "GAME OVER"