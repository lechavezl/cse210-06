from game.casting.color import Color

# -------------------------------------------------------------------------------------------------- 
# GENERAL GAME CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# GAME
GAME_NAME = "Combat Ball"
FRAME_RATE = 60

# SCREEN
SCREEN_WIDTH = 1040
SCREEN_HEIGHT = 680
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2

# FIELD
FIELD_TOP = 60
FIELD_BOTTOM = SCREEN_HEIGHT
FIELD_LEFT = 0
FIELD_RIGHT = SCREEN_WIDTH

# FONT
FONT_FILE = "combat-ball/assets/fonts/zorque.otf"
FONT_SMALL = 32
FONT_LARGE = 48

# SOUND
BOUNCE_SOUND = "combat-ball/assets/sounds/boing.wav"
WELCOME_SOUND = "combat-ball/assets/sounds/start.wav"
OVER_SOUND = "combat-ball/assets/sounds/over.wav"

# TEXT
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

# COLORS
BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
PURPLE = Color(255, 0, 255)

# KEYS
LEFT = "a"
RIGHT = "d"
SPACE = "space"
ENTER = "enter"
PAUSE = "p"
SECOND_LEFT = "j"
SECOND_RIGHT = "l"

# SCENES
NEW_GAME = 0
TRY_AGAIN = 1
NEXT_LEVEL = 2
IN_PLAY = 3
GAME_OVER = 4

# LEVELS
LEVEL_FILE = "combat-ball/assets/data/level-{:03}.txt"
BASE_LEVELS = 5

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

# SECOND STATS
SECOND_STATS_GROUP = "second_stats"
SECOND_DEFAULT_LIVES = 3
SECOND_MAXIMUM_LIVES = 5

# HUD
HUD_MARGIN = 15
LEVEL_GROUP = "level"
LIVES_GROUP = "lives"
SECOND_LIVES_GROUP = "second_lives"
SCORE_GROUP = "score"
LEVEL_FORMAT = "LEVEL: {}"
LIVES_FORMAT = "PLAYER 1 LIVES: {}"
SECOND_LIVES_FORMAT = "PLAYER 2 LIVES: {}"
SCORE_FORMAT = "SCORE: {}"

# BALL
BALL_GROUP = "balls"
BALL_IMAGE = "combat-ball/assets/images/000.png"
BALL_WIDTH = 28
BALL_HEIGHT = 28
BALL_VELOCITY = 6

# RACKET
RACKET_GROUP = "rackets"
SECOND_RACKET_GROUP = "second_rackets"
RACKET_IMAGES = [f"combat-ball/assets/images/{n:03}.png" for n in range(100, 103)]
RACKET_WIDTH = 106
RACKET_HEIGHT = 28
RACKET_RATE = 6
RACKET_VELOCITY = 7

# SECOND RACKET
SECOND_RACKET_GROUP = "second_rackets"
SECOND_RACKET_IMAGES = [f"combat-ball/assets/images/{n:03}.png" for n in range(103, 105)]
SECOND_RACKET_WIDTH = 106
SECOND_RACKET_HEIGHT = 28
SECOND_RACKET_RATE = 6
SECOND_RACKET_VELOCITY = 7

# DIALOG
DIALOG_GROUP = "dialogs"
ENTER_TO_START = "PRESS ENTER TO START"
PREP_TO_LAUNCH = "PREPARING TO LAUNCH"
WAS_GOOD_GAME = "GAME OVER"