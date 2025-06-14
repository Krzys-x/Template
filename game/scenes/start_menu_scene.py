import pynput

from game.scene import Scene
from graphics.surface import Surface

class StartMenuScene(Scene):
    def __init__(self, start_game: callable, exit_game: callable):
        # Initialize main menu scene with static objects and keyboard events
        surface1 = Surface(100, 60)
        surface1.blit(
            [
                "Welcome to the Krzys' project! Press a correct key for a chosen action.",
                "",
                "1. Start game",
                "2. Exit",
                "",
                "Project is intially created by:",
                "Krzysztof Rogajło"
            ]
        )
        super().__init__(
            name = "Start Menu",
            static_objects = [
                (surface1, (0, 0))
            ],
            handlable_objects = [],
            keyboard_press_events = {
                pynput.keyboard.KeyCode.from_char("1"): start_game,
                pynput.keyboard.KeyCode.from_char("2"): exit_game
            }
        )