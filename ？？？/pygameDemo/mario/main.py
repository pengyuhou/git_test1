# 游戏入口
import pygame
from source import tools,set_up
from source.states import main_menu,level,load_screen


def main():

    state_dict = {
        'main_menu':main_menu.MainMenu(),
        'load_screen':load_screen.loadScreen(),
        'level':level.Level()
    }

    game = tools.Game(state_dict,'main_menu')

    game.run()

if __name__ == "__main__":
    main()


