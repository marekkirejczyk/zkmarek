import sys
from argparse import ArgumentParser

from zkmarek.crypto.subgroup import Subgroup
from zkmarek.crypto.weierstrass_curve import WeierstrassCurve

class CalcCli:
    parser: ArgumentParser

    def __init__(self):
        self.parser = ArgumentParser(
            prog="script/calc",
            description="Calculates subgroups of elliptic curve",
            epilog="",
        )
        self.parser.add_argument('order', type=int, help='order of the curve')

    def run(self, args):
        args = self.parser.parse_args()
        print(f"Calculating subgroups of elliptic curve with order: {args.order}")
        groups = Subgroup.generate_all(WeierstrassCurve(0, 7, args.order))
        for group in groups:
            sorted_points = sorted(group.points, key=lambda p: p.x.value * args.order + p.y.value)
            print(", ".join(map(lambda g: f"{g}" , sorted_points)))

if __name__ == "__main__":
    CalcCli().run(sys.argv[1:])
