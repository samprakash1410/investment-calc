import argparse
from calculators.lumpsum import returns as lumpsum_returns
from calculators.sip import returns as sip_returns


def argument_parser():
	@@ -15,7 +16,7 @@ def argument_parser():
    parser.add_argument(
        'investment_type',
        type=str,
        choices=['lumpsum','sip'],
        help="investment type"
        )
    parser.add_argument(
	@@ -29,7 +30,7 @@ def argument_parser():
        '--rate',
        type=int,
        required=True,
        help="expected yearly returns")
    parser.add_argument(
        '-t',
        '--time',
	@@ -41,9 +42,16 @@ def argument_parser():
if __name__ == "__main__":
    args = argument_parser().parse_args()
    if args.investment_type == 'lumpsum':
        result = lumpsum_returns(
            prinicpal= args.principal,
            intrest_rate=args.rate,
            time_in_years=args.time
        )
        print(f"Your investment of {args.principal} will be {result} in next {args.time} years")
    elif args.investment_type == 'sip':
        result = sip_returns(
            invested_amount = args.principal,
            return_rate=args.rate,
            total_period_years=args.time
        )
        print(f"Your investment of {args.principal} will be {round(result,2)} in next {args.time} years")