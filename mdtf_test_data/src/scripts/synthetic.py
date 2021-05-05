#!/usr/bin/env python

__all__ = ["create_output_dirs", "synthetic_main"]
""" Script to generate synthetic GFDL CM4 output """
import os
import synthetic as td

def create_output_dirs(CASENAME="") :
    """Create output data directories"""
    print("Creating output data directories")
    if not os.path.exists(f"{CASENAME}/day"):
        os.makedirs(f"{CASENAME}/day")
    if "ncar" in CASENAME :
        if not os.path.exists(f"{CASENAME}/mon"):
            os.makedirs(f"{CASENAME}/mon")
        if not os.path.exists(f"{CASENAME}/3hr"):
            os.makedirs(f"{CASENAME}/3hr")
        if not os.path.exists(f"{CASENAME}/1hr"):
            os.makedirs(f"{CASENAME}/1hr")
def synthetic_main(yaml_dict ={}, DLAT=20.0, DLON=20.0, STARTYEAR=1,NYEARS=10,CASENAME="",
                   TIME_RES="", DATA_FORMAT=""):
    """Main script to generate synthetic data using GFDL naming conventions"""
    create_output_dirs(CASENAME)
    # parse the yaml dictionary
    var_names = yaml_dict['variables.name']
    # -- Create Daily Data
    print("Generating daily data ...")
    for v in var_names:
        vinfo = yaml_dict[v]
        print(vinfo)
        dset_out = td.synthetic.generate_synthetic_dataset(
            yaml_dict[v + '.stats'],
            DLON,
            DLAT,
            STARTYEAR,
            NYEARS,
            v,
            timeres=TIME_RES,
            attrs=yaml_dict[v + '.atts'],
            fmt=DATA_FORMAT
        )
        td.synthetic.write_to_netcdf(dset_out, f"{CASENAME}/TIME_RES/{CASENAME}.{v}.day.nc")