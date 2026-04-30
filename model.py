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