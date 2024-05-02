import argparse
from calculators.lumpsum import returns as lumpsum_returns
from calculators.sip import returns as sip_returns
from decorator.storage import store_in_csv

@store_in_csv
def print_result(principal, time, rate, investment_type,future_value):
    """
    This method prints the result
    """
    print(
        f"For Your {investment_type} the  {principal} will be {future_value} in next {time} years"
        )


def argument_parser():
    """
    This method creates an argument parser
    """
    parser = argparse.ArgumentParser(
        description="Investment Calculator")
    parser.add_argument(
        'investment_type',
        type=str,
        choices=['lumpsum','sip'],
        help="investment type"
        )
    parser.add_argument(
        '-p',
        '--principal', 
        type=int,
        required=True,
        help="present value of investment")
    parser.add_argument(
        '-r',
        '--rate',
        type=int,
        required=True,
        help="expected yearly returns")
    parser.add_argument(
        '-t',
        '--time',
        type=int,
        required=True,
        help="time in years")
    return parser
if __name__ == "__main__":
    args = argument_parser().parse_args()
    if args.investment_type == 'lumpsum':
        result = lumpsum_returns(
            prinicpal= args.principal,
            intrest_rate=args.rate,
            time_in_years=args.time
        )
        print_result(args.principal, args.time, args.rate, args.investment_type, result)
    elif args.investment_type == 'sip':
        result = sip_returns(
            invested_amount = args.principal,
            return_rate=args.rate,
            total_period_years=args.time
        )
        print_result(args.principal, args.time, args.rate, args.investment_type,result)