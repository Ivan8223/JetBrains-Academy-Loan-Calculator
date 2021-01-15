import argparse
from math import ceil
from math import log


def nominal_interest_rate(interest):
    return interest / (12 * 100)


def number_of_monthly_payments(principle,
                               annuity_payment,
                               interest):
    i = nominal_interest_rate(interest)
    number_of_payments = ceil(log((annuity_payment
                                   / (annuity_payment - i * principle)),
                                  (i + 1)))

    years, months = divmod(number_of_payments, 12)

    overpayment = annuity_payment * number_of_payments - principle

    print(f"It will take "
          f"{'' if years == 0 else (f'{years} year ' if years == 1 else f'{years} years ')}"
          f"{'and ' if months and years else ''}"
          f"{'' if months == 0 else (f'{months} month ' if months == 1 else f'{months} months ')}"
          f"to repay this loan!"
          f"\nOverpayment = {ceil(overpayment)}")


def annuity_monthly_payment(principle,
                            periods,
                            interest):
    i = nominal_interest_rate(interest)
    annuity_payment = ceil(principle * (i * (i + 1) ** periods
                                        / ((i + 1) ** periods - 1)))
    overpayment = annuity_payment * periods - principle

    print(f"Your annuity payment = {annuity_payment}!"
          f"\nOverpayment = {ceil(overpayment)}")


def loan_principal(annuity_payment,
                   periods,
                   interest):
    i = nominal_interest_rate(interest)
    principal = annuity_payment / (i * (1 + i) ** periods
                                   / ((1 + i) ** periods - 1))
    overpayment = annuity_payment * periods - principal

    print(f"Your loan principal = {ceil(principal)}!"
          f"\nOverpayment = {ceil(overpayment)}")


def differentiated_payments(principle,
                            periods,
                            interest):
    i = nominal_interest_rate(interest)
    overpayment = -principle

    for m in range(1, periods + 1):
        monthly_payment = ceil(principle / periods + i
                               * (principle - principle * (m - 1) / periods))
        overpayment += monthly_payment

        print(f"Month {m}: payment is "
              f"{monthly_payment}")

    print(f"\nOverpayment = {overpayment}")


def error_message():
    print("Incorrect parameters")


parser = argparse.ArgumentParser(usage='', description='This god damn loan calculator '
                                                       'will calculate whatever option you need.')

parser.add_argument("--type", type=str, help="Can be either 'annuity' or 'diff'", choices=["annuity", "diff"])
parser.add_argument("--payment", type=int, help="If --type=diff, their combination is invalid")
parser.add_argument("--principal", type=int, help="Valid with every combination")
parser.add_argument("--periods", type=int, help="Denotes the number of months and/or years needed to repay the credit")
parser.add_argument("--interest", type=float, help="Must always be specified.")

args = parser.parse_args()

if args.interest:
    if args.type == 'annuity':
        if args.principal and args.payment and not args.periods:
            number_of_monthly_payments(args.principal,
                                       args.payment,
                                       args.interest)
        elif args.principal and args.periods and not args.payment:
            annuity_monthly_payment(args.principal,
                                    args.periods,
                                    args.interest)
        elif args.payment and args.periods and not args.principal:
            loan_principal(args.payment,
                           args.periods,
                           args.interest)
        else:
            error_message()
    elif args.type == 'diff':
        if args.principal and args.periods and not args.payment:
            differentiated_payments(args.principal,
                                    args.periods,
                                    args.interest)
        else:
            error_message()
    else:
        error_message()
else:
    error_message()
