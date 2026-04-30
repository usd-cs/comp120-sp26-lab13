from model import TipCalculatorModel
from view import TipCalculatorView
from typing import Callable
from __future__ import annotations

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

