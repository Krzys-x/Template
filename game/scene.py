import pynput

from graphics.screen import Screen

class Scene:
    def __init__(self, name: str, static_objects: list, handlable_objects: list, keyboard_press_events: dict[pynput.keyboard.Key | pynput.keyboard.KeyCode, callable] = {},
                 handle_logic: callable = None, render: callable = None):
        # Initialize scene attributes
        self.name = name
        self.static_objects = static_objects
        self.handlable_objects = handlable_objects
        self.keyboard_press_events = keyboard_press_events
        self.handle_logic = handle_logic if handle_logic is not None else lambda pressed_keys: None
        self.render = render if render is not None else self.default_render
    
    def default_render(self, screen: Screen):
        # schow scene name
        if len(self.name) + 2 <= screen.width:
            print(f"\033[1;1H{"-" * ((screen.width - len(self.name)) // 2)}{self.name}{"-" * ((screen.width - len(self.name)) // 2 + ((screen.width - len(self.name)) % 2))}")
        else:
            print(f"\033[1;1H-{self.name}-")

        # render objects
        for obj in self.static_objects + self.handlable_objects:
            surface, position = obj # surface can be some other object that has char_map
            screen.blit(surface.char_map, pos = position)
    
    def handle_key_press(self, key: pynput.keyboard.Key | pynput.keyboard.KeyCode):
        # Handle key press event
        if key in self.keyboard_press_events:
            self.keyboard_press_events[key]()
    
    def handle_key_release(self, key: pynput.keyboard.Key | pynput.keyboard.KeyCode):
        # Not used = no need to implement
        pass