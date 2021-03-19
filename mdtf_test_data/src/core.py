#!/usr/bin/python
""" mdtf_test_data driver program """
import argparse
import util.cli
import util.read_yaml
from scripts import gfdl_synthetic, ncar_synthetic
import sys
import os


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
    cli_info = util.cli.cli_holder(args.convention, args.startyear,
                          args.nyears, args.dlat, args.dlon)
    #cli_vars = vars(cli_info)
    assert cli_info.dlat <= 30.0 and cli_info.dlat >= 0.5, "Error: dlat value is invalid; valid range is [0.5 30.0]"
    assert cli_info.dlon <= 60.0 and cli_info.dlon >= 0.5, "Error: dlon value is invalid; valid range is [0.5 60.0]"
    if cli_info.convention == 'GFDL':
       print("importing GFDL variable information")
       # default behavior is to run script from mdtf_test_data directory
       cur_dir = os.getcwd()
       print("current directory is", cur_dir)
       assert(os.path.basename(cur_dir) == "mdtf_test_data")

       input_data = util.read_yaml.read_yaml("config/gfdl_day.yaml")
       vars = [val for key, val in input_data.items() if key=="name"]
       var_meta = [val for key, val in input_data.items() if key=="atts"]
       print(vars)
       print(var_meta[0]["stats"])

       #print("Calling GFDL SYNTHETIC")
       #gfdl_synthetic.gfdl_syn_main(DLAT=cli_info.dlat, DLON=cli_info.dlon,
       #                 STARTYEAR=cli_info.startyear, NYEARS=cli_info.nyears, CASENAME="gfdl.synthetic")
    elif cli_info.convention == 'CESM':
       print("Calling NCAR SYNTHETIC")
       ncar_synthetic.ncar_syn_main(DLAT=cli_info.dlat, DLON=cli_info.dlon,
                        STARTYEAR=cli_info.startyear, NYEARS=cli_info.nyears, CASENAME="ncar.synthetic")

# [print(key,':',value) for key, value in cli_vars.items()]
if __name__ == '__main__':
    main()
    sys.exit()