import sys
from sc2_flowcharts.builds import pvt_colossus, pvz_dt_drop, pvp_proxy_robo, tvz_standard
import argparse

ALL_BUILDS = {
    "pvt_colossus": pvt_colossus,
    "pvz_dt_drop": pvz_dt_drop,
    "pvp_proxy_robo": pvp_proxy_robo,
    "tvz_standard": tvz_standard,
}

def parser():
    """Argument parser for the CLI."""
    parser = argparse.ArgumentParser(description="Generate SC2 build order flowcharts.")
    parser.add_argument(
        "--out",
        type=str,
        default="./windows",
        help="Output folder",
    )
    return parser

def render_graph(build, filename, directory="./windows", format="png"):
    """Render the graph to a file."""
    graph = build()
    graph.render(filename=filename, directory=directory, format=format, cleanup=True)
    print(f"Graph rendered to {directory}/{filename}.{format}")

def main():
    """Console script for sc2_flowcharts."""
    args = parser().parse_args()
    for build_name, build_fun in ALL_BUILDS.items():

        render_graph(build_fun, build_name, directory=args.out, format="png")

    return 0

if __name__ == "__main__":
    sys.exit(main())