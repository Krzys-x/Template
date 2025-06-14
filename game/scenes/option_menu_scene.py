import pynput

from game.scene import Scene
from graphics.surface import Surface

class OptionMenuScene(Scene):
    def __init__(self, exit_game: callable):
        # Initialize main menu scene with static objects and keyboard events
        surface1 = Surface(100, 60)
        surface1.blit(
            [
                "Take your action",
                "",
                "1. Exit game"
            ]
        )
        super().__init__(
            name = "Option Menu",
            static_objects = [
                (surface1, (0, 0))
            ],
            handlable_objects = [],
            keyboard_press_events = {
                pynput.keyboard.KeyCode.from_char("1"): exit_game
            }
        )