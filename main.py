from dataframe import *
import argparse


def main():
    df = dataframe()

    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Input file", type=str)
    subparsers = parser.add_subparsers()

    parser_lm = subparsers.add_parser('list-missing')
    parser_lm.set_defaults(function=df.list_missing)

    parser_cm = subparsers.add_parser('count-missing')
    parser_cm.set_defaults(function=df.count_nrows_missing)

    parser_i = subparsers.add_parser('impute')
    parser_i.add_argument('--method', type=str, required=True)
    parser_i.add_argument('--attributes', type=str, nargs='+', required=True)
    parser_i.add_argument('--output', type=str)
    parser_i.set_defaults(function=df.impute)

    parser_rm = subparsers.add_parser('remove-missing')
    parser_rm.add_argument('--type', type=str, required=True)
    parser_rm.add_argument('--threshold', type=int, required=True)
    parser_rm.add_argument('--output', type=str)
    parser_rm.set_defaults(function=df.remove_missing)

    parser_rd = subparsers.add_parser('remove-duplicate')
    parser_rd.add_argument('--output', type=str, required=True)
    parser_rd.set_defaults(function=df.remove_duplicate)

    parser_n = subparsers.add_parser('normalize')
    parser_n.add_argument('--method', type=str, required=True)
    parser_n.add_argument('--attribute', type=str, required=True)
    parser_n.add_argument('--output', type=str)
    parser_n.set_defaults(function=df.normalize)

    parser_m = subparsers.add_parser('mutate')
    parser_m.add_argument('--new-attr', type=str, required=True)
    parser_m.add_argument('--expression', type=str, required=True)
    parser_m.add_argument('--output', type=str)
    parser_m.set_defaults(function=df.mutate)

    args = parser.parse_args()

    if args.input is not None:
        df.load_csv(args.input)

    args.function(args)


if __name__ == '__main__':
    main()
