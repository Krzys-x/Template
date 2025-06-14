import pynput
import pygame
import random

from graphics.screen import Screen
from game.scene import Scene
from game.scenes.start_menu_scene import StartMenuScene
from game.scenes.option_menu_scene import OptionMenuScene

class Game:
    def __init__(self):
        # Prevnt game from running without initialization
        self.running = False

        # Initialize everything
        self.screen = Screen(100, 60)
        self.clock = pygame.time.Clock()
        self.pressed_keys = set()
        self.listener = None
        self.in_fight = False
        self.in_fight_enemy = None

        self.scenes: list[Scene] = [
            StartMenuScene(
                start_game = self.start_game,
                exit_game = self.exit_game
            ),
            OptionMenuScene(
                exit_game = self.exit_game
            )
        ]
        self.scene = 0

        # Let game run
        self.running = True
    
    def go_to_option_menu(self):
        # Change scene to option menu
        self.scene = 1

    def exit_game(self):
        # Exit game
        self.running = False
        if self.listener:
            self.listener.stop()

    def start_game(self):
        # Start game logic
        self.scene = 1

    def handle_key_press_events(self, key):
        if key == pynput.keyboard.Key.esc:
            self.running = False
            return
        self.scenes[self.scene].handle_key_press(key)

    def hadle_key_release_events(self, key):
        self.scenes[self.scene].handle_key_release(key)

    def on_key_press(self, key):
        self.pressed_keys.add(key)
        self.handle_key_press_events(key)

    def on_key_release(self, key):
        self.pressed_keys.discard(key)
        self.hadle_key_release_events(key)

    def render(self):
        # Clear screen
        self.screen.clear()

        # Render scene
        self.scenes[self.scene].render(self.screen)

    def run(self):
        # Create input listener
        self.listener = pynput.keyboard.Listener(on_press=self.on_key_press, on_release=self.on_key_release)
        self.listener.start()

        # Run game loop
        while self.running:
            # Limit frame rate
            self.clock.tick(5)

            # Check if listener is still running
            if not self.listener.running:
                self.running = False
                break

            # Handle game logic here
            self.scenes[self.scene].handle_logic(self.pressed_keys)
            
            # Show screen to terminal
            self.screen.display()

            # render game to screen
            self.render()