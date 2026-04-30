import tkinter as tk
from tkinter import ttk

from model import TipCalculatorModel
from controller import TipCalculatorController

class TipCalculatorView(ttk.Frame):
    """ The view class of the Tip Calculator application. It creates the GUI
    layout and responds to events and sends them to the controller, but not
    much else. """

    # instance variables
    bill_amount: ttk.Entry  # the text entry box for the bill amount
    ta_label: ttk.Label  # the label where the tip amount will be displayed
    message_label: ttk.Label  # the label where special messages will be displayed

    def __init__(self, parent: tk.Tk) -> None:
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