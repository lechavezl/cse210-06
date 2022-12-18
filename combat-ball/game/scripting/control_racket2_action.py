from constants import *
from game.scripting.action import Action


class ControlRacket2Action(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):
        racket2 = cast.get_first_actor(SECOND_RACKET_GROUP)

        if self._keyboard_service.is_key_down(SECOND_LEFT): 
            racket2.swing_left()
        elif self._keyboard_service.is_key_down(SECOND_RIGHT): 
            racket2.swing_right()  
        else: 
            racket2.stop_moving()        