class Surface:
    def __init__(self, width, height):
        self.width, self.height = width, height
        self.clear()
    
    def clear(self):
        # create a new empty char map
        self.char_map = [[" " for _ in range(self.width)] for _ in range(self.height)]
    
    def blit(self, other_surface, pos: tuple[int, int] = (0, 0), replace_to_spaces: bool = True):
        start_x, start_y = pos

        # get char map
        if hasattr(other_surface, 'char_map'):
            char_map = other_surface.char_map
        else:
            # assume it's already a char map
            char_map = other_surface

        # Iterate for row in other char map
        for y, row in enumerate(char_map):
            # If row is below the surface, stop
            if start_y + y >= self.height:
                break
            
            # If row is above the surface, skip
            if start_y + y < 0:
                continue

            # Iterate for char in row
            for x, char in enumerate(row):
                # If char is to the right of the surface, stop
                if start_x + x >= self.width:
                    break

                # If char is to the left of the surface, skip
                if start_x + x < 0:
                    continue

                # change char in self.char_map if requiraments met
                if replace_to_spaces or char[-1] != " ":
                    self.char_map[start_y + y][start_x + x] = char
        
    
    def load_from_file(self, file_name: str, offset: tuple[int, int] = (0, 0), color: str = "\033[0m", directory: str = "graphics\\char_maps\\"):
        try:
            with open(directory + file_name, "r") as file:
                # get txt data
                data = file.read()

                # create char map from data
                char_map = [(item[0] + item[1] for item in zip([color] * self.width, list(line))) for line in data.splitlines()]

                # clear and blit char map to self char map
                self.clear()

                self.blit(char_map, pos = offset, replace_to_spaces = True)

        except Exception as e:
            print(f"Error {e}: While loading '{file_name}' in dir '{directory}'.")
            return