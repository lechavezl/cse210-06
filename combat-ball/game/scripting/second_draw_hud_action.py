from constants import *
from game.scripting.action import Action


class SecondDrawHudAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        second_stats = cast.get_first_actor(SECOND_STATS_GROUP)
        self._draw_label(cast, SECOND_LIVES_GROUP, SECOND_LIVES_FORMAT, second_stats.get_lives())

   
    def _draw_label(self, cast, group, format_str, data):
        the_value_to_display = format_str.format(data)
        label = cast.get_first_actor(group)
        text = label.get_text()
        text.set_value(the_value_to_display)
        position = label.get_position()
        self._video_service.draw_text(text, position)