"""
Module: tip_calculator

A Tkinter application to calculate tips.
"""

import tkinter as tk

# import our MVC components
from model import TipCalculatorModel
from view import TipCalculatorView
from controller import TipCalculatorController

class TipCalculatorApp:
    """ Our Tk-based application, using the MVC model. It sets up the Tk
    application, creates all three of the MVC components, making sure they are
    linked together. """

    # instance variable(s)
    window: tk.Tk  # the main Tk application window

    def __init__(self) -> None:
        self.window = tk.Tk()
        self.window.title('Tip Calculator')

        # create the MVC objects:
        # 1. A TipCalculatorModel with the name model
        # 2. A TipCalculatorView with the name view
        # 3. A TipCalculatorController with the name controller


        model = TipCalculatorModel("tip_log.txt") # create the model
        
        # TODO: create the view and controller objects (2 and 3 from above)
        # Refer to the __init__ methods for these classes so you know what to
        # pass when creating them.

        # TODO: place the view using the pack layout (it will be the only thing in
        # the main/top-level window)


    def start(self) -> None:
        """ Starts the application's event loop, waiting for user input. """
        self.window.mainloop()


if __name__ == '__main__':
    # create a TipCalculatorApp object and tell it to start using its start
    # method
    app = TipCalculatorApp()
    app.start()
