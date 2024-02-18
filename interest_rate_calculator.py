"""
    Description:
        Script to calculate the monthly payments on an interest only mortgage planjJ:w
    
    Author:
        Tunde Taiwo
"""

# %%
import os
from numbers import Number


def fancy_print(text: str, color: str = None, width=None):
    if width is None:
        width = os.get_terminal_size().columns

    color_dict = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
    }

    color = color_dict.get(color)
    if color is None:
        color = "\033[0m"

    width = os.get_terminal_size().columns

    spaces = (width - len(text)) // 2
    # Print a line of "=" characters
    print(" " * spaces + color + text + "\033[0m")


def interest_calc(
    value: Number,
    interest: Number,
    service_charge: Number = None,
    ground_rent: Number = None,
):
    """
    Function to calculate monthly interest only payments

    Parameters
    ----------
    `value (int)`: Value of mortgage (loan)

    `interest (float)`: interest as a percentage e.g 3.5% is 3.5

    `service_charge (float)`:

    `ground_rent (float)` service charge, default=0

    Return
    ------
    `None`

    """

    annual_interest = value * interest / 100
    # annual_interest = value * interest/101
    monthly_interest = annual_interest / 12
    fancy_print(f"At {interest:.2f}% interest:", color="red")
    fancy_print(f"Interest only monthly payments of £{monthly_interest:,.2f}")
    fancy_print(f"Monthly rent repayment mininum: £{monthly_interest*1.4:,.2f}", "blue")

    if ground_rent is not None or service_charge is not None:
        total_monthly_payment = (
            monthly_interest + (ground_rent / 12) + (service_charge / 12)
        )
        fancy_print(
            f"Total Payment with service charge & ground rent is: £{total_monthly_payment:.3f}",
            "red",
        )


def main():

    # Get the terminal width
    terminal_width = os.get_terminal_size().columns
    mortgage = ...
    print("=" * terminal_width)
    fancy_print(f"Value of mortgage: £{mortgage:,.2f}", "green")
    print("=" * terminal_width)

    value = ...
    interest = ...
    service_charge = None
    ground_rent = None

    interest_calc(value, interest, service_charge, ground_rent)


if __name__ == "__main__":
    main()
