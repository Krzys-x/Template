from graphics.surface import Surface

class Screen(Surface):
    def __init__(self, width: int, height: int):
        super().__init__(width, height)
    
    def display(self):
        # Combine char map into a single string (for faster print and less flickering)
        output = "\n" + "\n".join("".join(row) for row in self.char_map)
        #          \-> leave space for title

        # Print output to the console
        print(f"\033c{output}\033[0m")