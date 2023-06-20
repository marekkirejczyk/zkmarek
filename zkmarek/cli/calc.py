import sys
from argparse import ArgumentParser
from zkmarek.crypto.ec_affine import ECAffine

from zkmarek.crypto.subgroup import Subgroup
from zkmarek.crypto.weierstrass_curve import WeierstrassCurve

class CalcCli:
    parser: ArgumentParser

    def __init__(self):
        self.parser = ArgumentParser(
            prog="script/calc",
            description="Calculates helpful values for elliptic curve cryptography",
            epilog="",
        )
        subparsers = self.parser.add_subparsers(dest='command', help='Choose a command')

        subgroup_parser = subparsers.add_parser('subgroups',
            help='Prints subgroups of an elliptic curve group for a given order')
        subgroup_parser.add_argument('subgroup', help='Prime field order', type=int)

        double_parser = subparsers.add_parser('double',
            help='Prints result of EC double operation for each point on a given curve')
        double_parser.add_argument('order', help='Prime field order', type=int)

    def run(self, args):
        args = self.parser.parse_args()
        if args.command == 'subgroups':
            self.subgroup(args.subgroup)
        elif args.command == 'double':
            self.double(args.order)
        else:
            self.parser.print_help()

    def double(self, order):
        print(f"Calculating double of points on elliptic curve with order: {order}")
        curve = WeierstrassCurve(0, 7, order)
        print(" point   |  double  |   slope")
        for p in ECAffine.generate_points(curve):
            d = p.double()
            print(f"{p:8} | {d:8} | {p.slope()}")

    def subgroup(self, order):
        print(f"Subgroups of elliptic curve with order: {order}")
        print(f"In [] group generators, in () non-generators, (0,0) is the neutral element)")
        groups = Subgroup.generate_all(WeierstrassCurve(0, 7, order))
        for group in groups:
            sorted_points = sorted(group.points,
                key=lambda p: p.x.value * order + p.y.value
            )
            print(", ".join(map(lambda g: point_to_str(g,  g in group.all_generators) , sorted_points)))

def point_to_str(p, is_generator):
    if is_generator:
        return f"[{p.x.value:2},{p.y.value:2}]"
    else:
        return f"({p.x.value:2},{p.y.value:2})"

if __name__ == "__main__":
    CalcCli().run(sys.argv[1:])
