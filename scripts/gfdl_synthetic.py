#!/usr/bin/env python

""" Script to generate synthetic GFDL CM4 output """

import os

import mdtf_test_data as td

DLON = 20
DLAT = 20
STARTYEAR = 1
NYEARS = 10

CASENAME = "GFDL.Synthetic"

# os.makedirs(f"{CASENAME}/mon")
os.makedirs(f"{CASENAME}/day")
# os.makedirs(f"{CASENAME}/3hr")
# os.makedirs(f"{CASENAME}/1hr")

# -- Create Daily Data
print("Generating daily data ...")

outfile = "precip"
stats = (2.9479988e-05, 6.57948e-05)
attrs = {
    "long_name": "Total precipitation rate",
    "units": "kg/m2/s",
    "cell_methods": "time: mean",
    "time_avg_info": "average_T1,average_T2,average_DT",
    "interp_method": "conserve_order1",
}
dset_out = td.synthetic.generate_synthetic_dataset(
    stats,
    DLON,
    DLAT,
    STARTYEAR,
    NYEARS,
    outfile,
    timeres="day",
    attrs=attrs,
    fmt="gfdl",
)
td.synthetic.write_to_netcdf(dset_out, f"{CASENAME}/day/{CASENAME}.{outfile}.day.nc")

outfile = "sphum"
attrs = {
    "long_name": "specific humidity",
    "units": "kg/kg",
    "cell_methods": "time: mean",
    "time_avg_info": "average_T1,average_T2,average_DT",
    "interp_method": "conserve_order2",
}
stats = [
    (2.207744273619028e-06, 3.1171239811556006e-08),
    (2.2120004814496497e-06, 4.2038056591309214e-08),
    (2.2173462639329955e-06, 6.085841164349404e-08),
    (2.195089336964884e-06, 1.2779378266714048e-07),
    (2.153154582629213e-06, 2.374897718482316e-07),
    (2.094266392305144e-06, 2.854812350960856e-07),
    (2.0205031887599034e-06, 2.8833915166615043e-07),
    (1.9574151792767225e-06, 3.129641470422939e-07),
    (1.9869351035595173e-06, 4.490039202664775e-07),
    (2.3005297862255247e-06, 7.08150935224694e-07),
    (3.968285909650149e-06, 2.2641079340246506e-06),
    (1.0366683454776648e-05, 9.786092959984671e-06),
    (3.099906462011859e-05, 3.574563379515894e-05),
    (8.375193283427507e-05, 0.00010662762360880151),
    (0.00018633835134096444, 0.0002450024476274848),
    (0.00037473972770385444, 0.0004942434024997056),
    (0.000682022946421057, 0.0008718980243429542),
    (0.0011107738828286529, 0.0013433881103992462),
    (0.0016250668559223413, 0.0018277750350534916),
    (0.0021864811424165964, 0.002303780522197485),
    (0.002785360673442483, 0.002752475207671523),
    (0.0034250598400831223, 0.003191043622791767),
    (0.004096926189959049, 0.003610411658883095),
    (0.0047650025226175785, 0.004022716544568539),
    (0.005404375027865171, 0.004434366710484028),
    (0.005979245062917471, 0.004850724712014198),
    (0.006488976068794727, 0.0052804104052484035),
    (0.0068984683603048325, 0.0056708799675107),
    (0.007145351730287075, 0.005889154504984617),
    (0.0072888461872935295, 0.005995234474539757),
    (0.007391186896711588, 0.006065600086003542),
    (0.007494122255593538, 0.006137644872069359),
]
dset_out = td.synthetic.generate_synthetic_dataset(
    stats,
    DLON,
    DLAT,
    STARTYEAR,
    NYEARS,
    outfile,
    timeres="day",
    attrs=attrs,
    fmt="gfdl",
)
td.synthetic.write_to_netcdf(dset_out, f"{CASENAME}/day/{CASENAME}.{outfile}.day.nc")

outfile = "WVP"
attrs = {
    "long_name": "Column integrated water vapor",
    "units": "kg/m2",
    "cell_methods": "time: mean",
    "time_avg_info": "average_T1,average_T2,average_DT",
    "interp_method": "conserve_order1",
}
stats = (19.95419692993164, 17.587417602539062)
dset_out = td.synthetic.generate_synthetic_dataset(
    stats,
    DLON,
    DLAT,
    STARTYEAR,
    NYEARS,
    outfile,
    timeres="day",
    attrs=attrs,
    fmt="gfdl",
)
td.synthetic.write_to_netcdf(dset_out, f"{CASENAME}/day/{CASENAME}.{outfile}.day.nc")

outfile = "pr"
attrs = {
    "long_name": "Precipitation",
    "units": "kg m-2 s-1",
    "cell_methods": "time: mean",
    "cell_measures": "area: area",
    "time_avg_info": "average_T1,average_T2,average_DT",
    "standard_name": "precipitation_flux",
    "interp_method": "conserve_order1",
}
stats = (2.726781713136006e-05, 3.357814784976654e-05)
dset_out = td.synthetic.generate_synthetic_dataset(
    stats,
    DLON,
    DLAT,
    STARTYEAR,
    NYEARS,
    outfile,
    timeres="day",
    attrs=attrs,
    fmt="gfdl",
)
td.synthetic.write_to_netcdf(dset_out, f"{CASENAME}/day/{CASENAME}.{outfile}.day.nc")

outfile = "rlut"
attrs = {
    "long_name": "TOA Outgoing Longwave Radiation",
    "units": "W m-2",
    "cell_methods": "time: mean",
    "cell_measures": "area: area",
    "time_avg_info": "average_T1,average_T2,average_DT",
    "standard_name": "toa_outgoing_longwave_flux",
    "interp_method": "conserve_order2",
}
stats = (223.1096954345703, 41.8108024597168)
dset_out = td.synthetic.generate_synthetic_dataset(
    stats,
    DLON,
    DLAT,
    STARTYEAR,
    NYEARS,
    outfile,
    timeres="day",
    attrs=attrs,
    fmt="gfdl",
)
td.synthetic.write_to_netcdf(dset_out, f"{CASENAME}/day/{CASENAME}.{outfile}.day.nc")

outfile = "wap"
attrs = {
    "long_name": "omega (=dp/dt)",
    "units": "Pa s-1",
    "cell_methods": "time: mean",
    "cell_measures": "area: area",
    "time_avg_info": "average_T1,average_T2,average_DT",
    "standard_name": "lagrangian_tendency_of_air_pressure",
    "interp_method": "conserve_order2",
}
stats = [
    (0.022114235907793045, 0.108857661485672),
    (0.020489402115345, 0.10649824142456055),
    (0.01603768952190876, 0.09876697510480881),
    (0.004802089650183916, 0.055379338562488556),
    (0.000631575589068234, 0.04406093433499336),
    (0.00042018044041469693, 0.041750285774469376),
    (0.0002493239298928529, 0.03950018063187599),
    (2.3192718799691647e-05, 0.03357333317399025),
    (-5.8706071285996586e-05, 0.02723444253206253),
    (-5.285129736876115e-05, 0.01841943897306919),
    (-1.7103078789659776e-05, 0.009559356607496738),
    (-4.2390460293972865e-05, 0.0038361854385584593),
    (-3.946907236240804e-05, 0.0024431110359728336),
    (-4.4129035813966766e-05, 0.0019120794022455812),
    (-4.2927695176331326e-05, 0.0013438733294606209),
    (-3.689007644425146e-05, 0.0010005877120420337),
    (-2.3388127374346368e-05, 0.0005884375423192978),
    (-1.1117307622043882e-05, 0.00034648788277991116),
    (-3.2235393518931232e-06, 0.00013902815408073366),
]
dset_out = td.synthetic.generate_synthetic_dataset(
    stats,
    DLON,
    DLAT,
    STARTYEAR,
    NYEARS,
    outfile,
    timeres="day",
    attrs=attrs,
    fmt="gfdl",
)
td.synthetic.write_to_netcdf(dset_out, f"{CASENAME}/day/{CASENAME}.{outfile}.day.nc")

outfile = "va"
attrs = {
    "long_name": "Northward Wind",
    "units": "m s-1",
    "cell_methods": "time: mean",
    "cell_measures": "area: area",
    "time_avg_info": "average_T1,average_T2,average_DT",
    "standard_name": "northward_wind",
    "interp_method": "conserve_order2",
}
stats = [
    (0.1940714418888092, 2.8362390995025635),
    (0.23061925172805786, 3.013427972793579),
    (0.16851991415023804, 2.731928586959839),
    (-0.01123608648777008, 2.8133063316345215),
    (-0.04125901311635971, 3.03869366645813),
    (-0.02492545358836651, 3.4207561016082764),
    (-0.02121681720018387, 4.016183376312256),
    (-0.01546641904860735, 4.689133167266846),
    (-0.013392372988164425, 4.983587265014648),
    (-0.018137166276574135, 4.9434494972229),
    (-0.018187088891863823, 4.3697896003723145),
    (0.025878533720970154, 3.3325064182281494),
    (0.01972961612045765, 3.1699655055999756),
    (0.00756301311776042, 3.540755271911621),
    (0.002088402397930622, 4.39123010635376),
    (0.0015588417882099748, 5.08877420425415),
    (-0.0017910711467266083, 6.02992057800293),
    (-0.01341389212757349, 6.709871768951416),
    (-0.04953442141413689, 8.147346496582031),
]
dset_out = td.synthetic.generate_synthetic_dataset(
    stats,
    DLON,
    DLAT,
    STARTYEAR,
    NYEARS,
    outfile,
    timeres="day",
    attrs=attrs,
    fmt="gfdl",
)
td.synthetic.write_to_netcdf(dset_out, f"{CASENAME}/day/{CASENAME}.{outfile}.day.nc")

outfile = "ua"
attrs = {
    "long_name": "Eastward Wind",
    "units": "m s-1",
    "cell_methods": "time: mean",
    "cell_measures": "area: area",
    "time_avg_info": "average_T1,average_T2,average_DT",
    "standard_name": "eastward_wind",
    "interp_method": "conserve_order2",
}
stats = [
    (0.021314790472388268, 4.512881278991699),
    (0.5326619744300842, 5.954967498779297),
    (1.43429434299469, 6.151541233062744),
    (3.5169997215270996, 6.718076705932617),
    (5.064070701599121, 7.533307075500488),
    (6.97215461730957, 8.621078491210938),
    (9.392412185668945, 10.132266998291016),
    (12.26109790802002, 12.243420600891113),
    (13.543569564819336, 13.345138549804688),
    (14.137928009033203, 13.860307693481445),
    (13.190452575683594, 13.078526496887207),
    (9.251249313354492, 10.972661972045898),
    (5.768674850463867, 11.529572486877441),
    (4.316129684448242, 13.369094848632812),
    (4.139902591705322, 16.318357467651367),
    (4.689526557922363, 18.68798065185547),
    (6.583802700042725, 22.241039276123047),
    (9.023049354553223, 25.71630859375),
    (12.582330703735352, 32.460975646972656),
]
dset_out = td.synthetic.generate_synthetic_dataset(
    stats,
    DLON,
    DLAT,
    STARTYEAR,
    NYEARS,
    outfile,
    timeres="day",
    attrs=attrs,
    fmt="gfdl",
)
td.synthetic.write_to_netcdf(dset_out, f"{CASENAME}/day/{CASENAME}.{outfile}.day.nc")
