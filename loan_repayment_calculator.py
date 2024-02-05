# %%
# -- Imports -- #
import logging
from numbers import Number
from typing import Callable


# %%
# --  Loan Repayment Function -- #
def loan_repayment_calc(
    amount: Number,
    interest: Number,
    repayment: Number | Callable,
    time_limit: int = None,
) -> None:
    """

    Parameters
    ----------
    `amount (float)`: total amount remaining to be paid on loan

    `interest (float)`: amount of interest paid on loan amount. No need to divide by 100, for exmaple 3.5% is 3.5 not 0.035

    `repayment (float | Callable)`: The amount repaid on an annual basis. TODO: implement callable, do I want this to be monthly?

    Return
    ------
    `None`

    """

    if interest < 1:
        logging.warning(
            # f"Please make sure that interest is not divided by 100. Did you mean {interest*100}, instead of {interest}",
            "Please make sure that interest is not divided by 100. Did you mean '%(arg1)s', instead of '%(arg2)s'",
            {"arg1": interest * 100, "arg2": interest},
        )
    if time_limit is None:
        time_limit = 30  # defaultly set time limit to 30 yrs

    interest = interest / 100
    months = 0
    total_interest_paid = 0
    if callable(repayment):
        raise NotImplementedError("callable repayments have not been implemented yet.")
    else:
        repayment = repayment / 12

    while amount > 0:
        # all done on a monthly basis
        interest_accrued = (amount * interest) / 12
        amount = amount - repayment + interest_accrued

        months += 1
        total_interest_paid += interest_accrued

        if (months / 12) > time_limit:
            print(
                f"Time limit of {time_limit} years has been reached, £{amount:.2f} left to repay."
            )
            return None

    years = months // 12
    months_left = months % 12
    print(f"Total time taken to repay loan: {years} year(s), {months_left} months.")
    print(f"Total amount of interest paid: £{total_interest_paid:.2f}.")


def main():
    # -- logging config -- #
    logging.basicConfig(
        format="%(asctime)s %(levelname)s: %(message)s",
        datefmt="%H:%M:%S",
    )

    # -- Salary & Interest -- #
    salary = ...
    interest = ...

    # -- Post Graduate -- #
    amount = ...
    repayment = (salary - 21_000) * 0.06
    print("\nPost Graduate:")
    loan_repayment_calc(amount, interest, repayment)

    # -- Undergraduate -- #
    amount = ...
    repayment = 0.09 * (salary - 27_295)
    print("\nUndergraduate:")
    loan_repayment_calc(amount, interest, repayment)


# %%
if __name__ == "__main__":
    main()

# %%
