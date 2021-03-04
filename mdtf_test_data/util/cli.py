#!/usr/bin/python
""" Command line interface tool """
import argparse

def cli_parser = argparse.ArgumentParser(
    description="parse mdtf_test_data command-line arguments")
    # @TODO add support for CMIP convention
    cli_parser.add_argument("--convention","-c", type=str, help="Model convention", choices=['GFDL', 'CESM'],
                    required=True, default="")
    cli_parser.add_argument("--startyear", type=int, help="Start year of time period",
                    required=False, default=1)
    cli_parser.add_argument("--nyears", type=int, help="Total length of time period in years",
                    required=False, default=10)
    cli_parser.add_argument("--dlat", type=float,int, help="Latitude resolution in degrees",
                    required=False, default=20)
    cli_parser.add_argument("--dlon", type=float,int, help="Longitude resolution in degrees",
                    required=False, default=20)