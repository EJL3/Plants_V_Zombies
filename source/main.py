print('Author = Rizwan AR')

from . import tool
from . import constants as c
from .state import mainmenu, screen, level

def main():
    game = tool.Control()
    state_dict = {c.MAIN_MENU: mainmenu.Menu(),
                  c.GAME_VICTORY: screen.GameVictoryScreen(),
                  c.GAME_LOSE: screen.GameLoseScreen(),
                  c.LEVEL: level.Level()}
    game.setup_states(state_dict, c.MAIN_MENU)
    game.main()

