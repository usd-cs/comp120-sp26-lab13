"""
Module: tip_calculator

A Tkinter application to calculate tips.
"""

import tkinter as tk
from tkinter import ttk
from typing import Callable
from __future__ import annotations


class TipCalculatorModel:
    """ The Model class of the Tip Calculator application. It does the
    computation associated with the program, including logging data to a file
    on request. """

    # instance variable(s)
    log_filename: str  # name of the file where we will log tip amounts

    def __init__(self, log_filename: str) -> None:
        self.log_filename = log_filename

    def calculate_tip(self, bill_amount: float, tip_percent: float) -> float:
        """ Calculates the tip given the bill and the percent. """
        return bill_amount * tip_percent

    def save_to_log(self, tip_percent: float) -> None:
        """ Append the tip percent into a file named <self.log_filename>.  """

        # TODO: implement this function using a with statement. We want to
        # append to the existing file, not overwrite it, so use the 'a' mode
        # when opening.

        pass


class TipCalculatorView(ttk.Frame):
    """ The view class of the Tip Calculator application. It creates the GUI
    layout and responds to events and sends them to the controller, but not
    much else. """

    # instance variables
    controller: TipCalculatorController  # the application controller
    bill_amount: ttk.Entry  # the text entry box for the bill amount
    ta_label: ttk.Label  # the label where the tip amount will be displayed
    message_label: ttk.Label  # the label where special messages will be displayed

    def __init__(self, parent: tk.Tk, controller: TipCalculatorController) -> None:
        super().__init__(parent)
        self.create_layout()

    def create_layout(self) -> None:
        """ Creates the grid-based layout. """

        # Create top-level frames
        input_frame = ttk.Frame(self)

        # TODO: create two more frames named buttons_frame and messages_frame

        # TODO: use the pack method to place the the input, buttons, and
        # messages frames in a single column

        # TODO: Create the widgets associated with entering the bill amount.
        # These should live within input_frame.
        # Note that the Entry box should be an instance variable
        # (named self.bill_amount) so we can access it outside of this
        # function.

        # TODO: use the pack layout manager to place the input_frame widgets
        # side-by-side

        # Create the buttons to indicate the amount needed.
        # These buttons should be placed inside the buttons_frame.
        tip15_button = ttk.Button(buttons_frame, text='15% (Good)')

        # TODO: create the remaining 3 tip buttons (20, 25, and 0%)

        # TODO: set the 'command' attribute for all of the buttons using the
        # create_tip_handler method defined below.

        # TODO: Use the grid layout to place the tip percent buttons

        # TODO: create widgets for the messages frame.
        # Note that both of these should be instance variables (self._ta_label
        # and self.message_label) so that they can be accessed in other
        # methods.
        # The tip amount label should initially read: "Tip Amount: $0.00"
        # while the special message should initially be blank (i.e. an empty
        # string).

        # TODO: use pack to place the two message labels


    def configure_tip_buttons(self, controller: TipCalculatorController) -> None:
        """ Sets the 'command' attribute for all of the tip buttons using the
        controller's create_tip_handler method. """

        pass # dummy implementation


    def show_message(self, message: str) -> None:
        """ Sets the text for the message label. """
        self.message_label['text'] = message


    def clear_message(self) -> None:
        """ Clears out the message label. """
        self.message_label['text'] = ""


    def show_tip_amount(self, tip_amount: float) -> None:
        """ Sets the text for the tip amount label.

        The format of the message should be: "Tip Amount: $X.XX" with only two
        decimal places.
        """

        # TODO: implement this method (it only needs a single line of code)
        # Note that you should use an f-String to properly format the text for
        # the tip amount label.
        pass



class TipCalculatorController:
    """ The Controller class of the Tip Calculator application. It responds to
    events sent to it by the view, computing tips using the model, and
    updating the view as necessary. """

    # instance variables
    model: TipCalculatorModel  # the model that the controller should control
    view: TipCalculatorView  # the view that the controller should control

    def __init__(self, model: TipCalculatorModel, view: TipCalculatorView) -> None:
        self.model = model
        self.view = view
        self.view.configure_tip_buttons(self)


    def create_tip_handler(self, bill_amount: str, tip_amount: float) -> Callable[[], None]:
        """ Returns a function that tells the controller to calculate the tip. """
        def tip_handler() -> None:
            self.calculate(bill_amount, tip_amount)

        return tip_handler


    def calculate(self, bill_amount: str, tip_percent: float) -> None:
        """ Verifies that the bill amount is OK, then calculates the tip to be
        displayed in the app, saving the amount to the model's log file.

        If there is a problem with the bill amount, a message is displayed and
        no tip is shown.

        Precondition: self.view has been set (is not None)
        """

        # TODO: tell the view (self.view) to clear out any old message

        # TODO: if bill_amount if blank, show the message "Please enter a bill
        # amount" and return without doing anything else. Use the view's
        # show_message method for displaying this message.

        # TODO: Convert the bill amount to a float value. If it's NOT in the
        # correct format, this will raise a ValueError.  Catch that (using
        # try-catch) and show the message "Incorrect bill amount format"
        # before returning from the function.

        # TODO: Calculate the tip amount using the model's (self.model)
        # calculate_tip method.

        # TODO: If the tip amount is negative, show the message "Bill amount
        # may not be negative", then return

        # TODO: Tell the model (self.model) to save the tip amount to the log
        # file.

        # TODO: Tell the view to show the tip amount



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
        # 2. A TipCalculatorController with the name controller
        # 3. A TipCalculatorView with the name view

        model = TipCalculatorModel("tip_log.txt") # create the model
        
        # TODO: create the controller and view objects (2 and 3 from above)
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
