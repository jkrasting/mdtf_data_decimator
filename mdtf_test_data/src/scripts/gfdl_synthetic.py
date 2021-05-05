#!/usr/bin/env python

__all__ = ["gfdl_syn_main"]
""" Script to generate synthetic GFDL CM4 output """
import os
import synthetic as td

def gfdl_syn_main(yaml_dict ={}, DLAT=20.0, DLON=20.0, STARTYEAR=1,NYEARS=10,CASENAME=""):
    """Main script to generate synthetic data using GFDL naming conventions"""
    if not os.path.exists(f"{CASENAME}/day"):
        os.makedirs(f"{CASENAME}/day")

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
            timeres="day",
            attrs=yaml_dict[v + '.atts'],
            fmt="gfdl"
        )
        td.synthetic.write_to_netcdf(dset_out, f"{CASENAME}/day/{CASENAME}.{v}.day.nc")