'''
This code in this file is written completely or partially based on this tutorial:
https://rogueliketutorials.com/tutorials/tcod/v2/
'''

class Impossible(Exception):
    """Exception raised when an action is impossible to be performed.

    The reason is given as the exception message.
    """

class QuitWithoutSaving(SystemExit):
    """Can be raised to exit the game without automatically saving."""