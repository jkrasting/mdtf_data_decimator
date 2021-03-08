#!/usr/bin/python
""" mdtf_test_data driver program """
import argparse
import mdtf_test_data.util.cli
import mdtf_test_data.scripts
import sys


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
    cli_info = mdtf_test_data.util.cli.cli_holder(args.convention, args.startyear,
                          args.nyears, args.dlat, args.dlon)
    #cli_vars = vars(cli_info)
    assert cli_info.dlat <= 30.0 and cli_info.dlat >= 0.5, "Error: dlat value is invalid; valid range is [0.5 30.0]"
    assert cli_info.dlon <= 60.0 and cli_info.dlon >= 0.5, "Error: dlon value is invalid; valid range is [0.5 60.0]"
    if cli_info.convention == 'GFDL':
       print("Calling GFDL SYNTHETIC")
       mdtf_test_data.scripts.gfdl_synthetic.gfdl_syn_main(DLAT=cli_info.dlat, DLON=cli_info.dlon,
                        STARTYEAR=cli_info.startyear, NYEARS=cli_info.nyears, CASENAME=cli_info.convention)
    #else if cli_info.convention == 'CESM':
    #    call scripts.ncar_synthetic(cli_info)

# [print(key,':',value) for key, value in cli_vars.items()]
if __name__ == '__main__':
    main()
    sys.exit()