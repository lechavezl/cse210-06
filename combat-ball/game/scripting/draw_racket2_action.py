from constants import *
from game.scripting.action import Action


class DrawRacket2Action(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        racket2 = cast.get_first_actor(SECOND_RACKET_GROUP)
        body = racket2.get_body()

        if racket2.is_debug():
            rectangle = body.get_rectangle()
            self._video_service.draw_rectangle(rectangle, PURPLE)
            
        animation = racket2.get_animation()
        image = animation.next_image()
        position = body.get_position()
        self._video_service.draw_image(image, position)