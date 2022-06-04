from time import sleep


class GraphicTool:
    DEFAULT_SIZE_ROW = 100
    DEFAULT_WAIT_SECS = 1

    @staticmethod
    def row(size=DEFAULT_SIZE_ROW):
        print('-' * size)

    @staticmethod
    def title(msg: str, size_upper_row=DEFAULT_SIZE_ROW, size_lower_row=DEFAULT_SIZE_ROW, center_msg_to=DEFAULT_SIZE_ROW):
        GraphicTool.row(size_upper_row)
        print(msg.center(center_msg_to))
        GraphicTool.row(size_lower_row)

    @staticmethod
    def print_menu_options(menu_options: list):
        for i in range(len(menu_options)):
            print(f"({i + 1}) - {menu_options[i]}")

    @staticmethod
    def clean_prompt():
        from os import name, system
        system('cls' if name == 'nt' else 'clear')

    @staticmethod
    def wait(secs=DEFAULT_WAIT_SECS):
        sleep(secs)
