#!/usr/bin/python
""" mdtf_test_data driver program """
import argparse
import os
import sys
import scripts.gfdl_synthetic
import scripts.ncar_synthetic

class cli_holder(object):
    "Object with command line info from argparse"
    def __init__(self, convention, startyear, nyears, dlat, dlon):
        self.convention = convention
        self.startyear = startyear
        self.nyears = nyears
        self.dlat = dlat
        self.dlon = dlon
def main():
    """The the central nervous system of the mdtf_test_data package"""
    print("Starting mdtf_test_data")
    #Define the the CLI arguments and call the parser.
    parser = argparse.ArgumentParser(description="parse mdtf_test_data command-line arguments")
    # @TODO add support for CMIP convention
    parser.add_argument("--convention","-c", type=str, help="Model convention", choices=['GFDL', 'CESM'],
                    required=True, default="")
    parser.add_argument("--startyear", type=int, help="Start year of time period",
                    required=False, default=1)
    parser.add_argument("--nyears", type=int, help="Total length of time period in years",
                    required=False, default=10)
    parser.add_argument("--dlat", type=float, help="Latitude resolution in degrees",
                    required=False, default=20.0)
    parser.add_argument("--dlon", type=float, help="Longitude resolution in degrees",
                    required=False, default=20.0)
    args = parser.parse_args()
    cli_info = cli_holder(args.convention, args.startyear,
                          args.nyears, args.dlat, args.dlon)
    #cli_vars = vars(cli_info)
    assert cli_info.dlat <= 30.0 and cli_info.dlat >= 0.5, "Error: dlat value is invalid; valid range is [0.5 30.0]"
    assert cli_info.dlon <= 60.0 and cli_info.dlon >= 0.5, "Error: dlon value is invalid; valid range is [0.5 60.0]"
    if cli_info == 'GFDL':
        call scripts.gfdl_synthetic(cli_info)
    else if cli_info == 'CESM':
        call scripts.ncar_synthetic(cli_info)

# [print(key,':',value) for key, value in cli_vars.items()]
if __name__ == '__main__':
    main()
    sys.exit()