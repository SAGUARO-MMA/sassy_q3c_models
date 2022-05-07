#!/usr/bin/env python3


# +
# import(s)
# -
from sassy_q3c_models.hecate_q3c_orm_filters import *


# +
# __doc__ string
# -
__doc__ = """ % python3 hecate_q3c_orm_cli.py --help """


# +
# constant(s)
# -
ARXIV_PDF_URL = HECATE_PDF_URL
ARXIV_PDF_FIL = HECATE_PDF_URL.split("/")[-1]
ARXIV_DAT_URL = HECATE_DAT_URL
ARXIV_DAT_FIL = HECATE_DAT_URL.split("/")[-1]


# +
# __text__
# -
__text__ = """
Column     Name               Description
1          pgc                Principal Catalogue of Galaxies number
2          objname            Object name in the HyperLEDA
3          id_ned             Name in NED
4          id_nedd            Name in NED-Distance Catalogue
5          id_iras            Name in IRAS-RBGS, or in RIFSCz if in the form Fxxxxx+xxxx
6          id_2mass           ID in 2MASS-LGA, 2MASS-XSC, or 2MASS-PSC (see flag_2mass)
7          sdss_photid        SDSS photometric ID (consistent with DR8 releases and later)
8          sdss_specid        SDSS spectroscopic ID (consistent with DR8 releases and later)
9          ra                 Decimal right ascension J2000.0 (deg)
10         dec                Decimal declination J2000.0 (deg)
11         f_astrom           Astrometric precision flag:
                              -1 for ~0.1 arcsec, 0 for 1 arcsec, 1 for 10 arcsec, etc
12         r1                 D25 semi-major axis (arcmin)
13         r2                 D25 semi-minor axis (arcmin)
14         pa                 D25 positional angle, North-to-Northeast (deg)
15         rsource            Source of the galaxy-size information:
                              H=HyperLEDA, S=SDSS, 2=2MASS, 6=2dFGS, W=WINGS, Y=SkyMapper, 
                              A=Amiga-CIG, K=UNGC, V=VIII/77, 1=KKH2001, 7=KKH2007, N=NED.
16         rflag              Galaxy-size information flag:
                              0=missing, 1=all axes and positional angle defined, 2=r2 and/or 
                              pa were missing and they were set equal to r1 and 0 (circular isophote)
17         t                  Numerical Hubble-type following the de Vaucouleurs et al. 1976 system
18         e_t                Uncertainty on the numerical Hubble-type
19         incl               Inclination (deg)
20         v                  Heliocentric radial velocity (km/s)
21         e_v                Uncertainty on the heliocentric radial velocity (km/s)
22         v_vir              Virgo-infall corrected radial velocity (km/s)
23         e_v_vir            Uncertainty on the Virgo-infall corrected radial velocity (km/s)
24         ndist              Number of redshift-independent measurements in NED-D used for the computation of the distance
25         edist              If True, the NED-D distance measurements had uncertainties
26         d                  Distance (Mpc)
27         e_d                Uncertainty on the distance (Mpc)
28         d_lo68             Lower bound of the 68% confidence interval of the distance (Mpc)
29         d_hi68             Upper bound of the 68% confidence interval of the distance (Mpc)
30         d_lo95             Lower bound of the 95% confidence interval of the distance (Mpc)
31         d_hi95             Upper bound of the 95% confidence interval of the distance (Mpc) 
32         dmethod            Method for the estimation of the distance:
                              N=using NED-D distance measurements, 
                              Z=regression, Zv=regression for Virgo Cluster members, 
                              C=distance from NED-D measurements but uncertainty from regression, 
                              Cv=distance from NED-D measurements but uncertainty from Virgo Cluster regressor
33         ut                 Total U-band apparent magnitude (mag)
34         bt                 Total B-band apparent magnitude (mag)
35         vt                 Total V-band apparent magnitude (mag)
36         it                 Total I-band apparent magnitude (mag)
37         e_ut               Uncertainty on the total U-band apparent magnitude (mag)
38         e_bt               Uncertainty on the total B-band apparent magnitude (mag)
39         e_vt               Uncertainty on the total V-band apparent magnitude (mag)
40         e_it               Uncertainty on the total I-band apparent magnitude (mag)
41         ag                 Galactic absorption in B-band (mag)
42         ai                 Intrinsic absorption in B-band (mag)
43         s12                12μm-band flux from IRAS (Jy)
44         s25                25μm-band flux from IRAS (Jy)
45         s60                60μm-band flux from IRAS (Jy)
46         s100               100μm-band flux from IRAS (Jy)
47         q12                Quality flag for the 12μm-band flux from IRAS (Jy):
                              0=not in IRAS, 1=upper limit, 2=moderate, 3=high, 4=flux from IRAS-RBGS
48         q25                Quality flag for the 25μm-band flux from IRAS (Jy):
                              0=not in IRAS, 1=upper limit, 2=moderate, 3=high, 4=flux from IRAS-RBGS
49         q60                0=not in IRAS, Quality flag for the 60μm-band flux from IRAS (Jy):
                              0=not in IRAS, 1=upper limit, 2=moderate, 3=high, 4=flux from IRAS-RBGS
50         q100               Quality flag for the 100μm-band flux from IRAS (Jy):
                              0=not in IRAS, 1=upper limit, 2=moderate, 3=high, 4=flux from IRAS-RBGS
51         wf1                33μm-band (W1) apparent magnitude in the WISE forced photometry catalog (mag)
52         wf2                46μm-band (W2) apparent magnitude in the WISE forced photometry catalog (mag)
53         wf3                12μm-band (W3) apparent magnitude in the WISE forced photometry catalog (mag)
54         wf4                22μm-band (W4) apparent magnitude in the WISE forced photometry catalog (mag)
55         e_wf1              Uncertainty on the 33μm-band (W1) apparent magnitude in the WISE forced photometry catalog (mag)
56         e_wf2              Uncertainty on the 46μm-band (W2) apparent magnitude in the WISE forced photometry catalog (mag)
57         e_wf3              Uncertainty on the 12μm-band (W3) apparent magnitude in the WISE forced photometry catalog (mag)
58         e_wf4              Uncertainty on the 22μm-band (W4) apparent magnitude in the WISE forced photometry catalog (mag)
59         wfpoint            True if point source in the WISE forced photometry catalog
60         wftreat            True if treated as point source in the WISE forced photometry catalog
61         j                  J-band apparent magnitude in 2MASS (mag)
62         h                  H-band apparent magnitude in 2MASS (mag)
63         k                  J-band apparent magnitude in 2MASS (mag)
64         e_j                Uncertainty on the J-band apparent magnitude in 2MASS (mag)
65         e_h                Uncertainty on the H-band apparent magnitude in 2MASS (mag)
66         e_k                Uncertainty on the K-band apparent magnitude in 2MASS (mag)
67         flag_2mass         Source of the 2MASS ID and magnitudes:
                              0=none, 1=LGA, 2=XSC, 3=PSC
68         u                  u-band SDSS apparent magnitude (mag)
69         g                  g-band SDSS apparent magnitude (mag)
70         r                  r-band SDSS apparent magnitude (mag)
71         i                  i-band SDSS apparent magnitude (mag)
72         z                  z-band SDSS apparent magnitude (mag)
73         e_u                Uncertainty on the u-band SDSS apparent magnitude (mag)
74         e_g                Uncertainty on the g-band SDSS apparent magnitude (mag)
75         e_r                Uncertainty on the r-band SDSS apparent magnitude (mag)
76         e_i                Uncertainty on the i-band SDSS apparent magnitude (mag)
77         e_z                Uncertainty on the z-band SDSS apparent magnitude (mag)
78         logL_TIR           Decimal logarithm of the total-infrared (TIR) luminosity in solar luminosities (383x1033 erg/s)
79         logL_FIR           Decimal logarithm of the far-infrared (FIR) luminosity in solar luminosities
80         logL_60u           Decimal logarithm of the 60um-band luminosity in solar luminosities
81         logL_12u           Decimal logarithm of the 12um-band luminosity in solar luminosities
82         logL_22u           Decimal logarithm of the 22um-band luminosity in solar luminosities
83         logL_K             Decimal logarithm of the K-band luminosity in solar luminosities
84         ML_ratio           Mass-to-light ratio for the 2MASS K-band using SDSS g-r colour (Bell et al 2003)
85         logSFR_TIR         Decimal logarithm of the TIR-based star-formation rate in solar masses per year
86         logSFR_FIR         Decimal logarithm of the FIR-based star-formation rate in solar masses per year
87         logSFR_60u         Decimal logarithm of the 60um-based star-formation rate in solar masses per year
88         logSFR_12u         Decimal logarithm of the 12um-based star-formation rate in solar masses per year
89         logSFR_22u         Decimal logarithm of the 22um-based star-formation rate in solar masses per year
90         logSFR_HEC         Decimal logarithm of the homogenised star-formation rate in solar masses per year

91         SFR_HEC_flag       Flag indicating the source of the photometry and the SFR indicator used in the homogenised SFR:
                              RT=IRAS-RBGS photometry and TIR indicator
                              FT=RIFSCz photometry and TIR indicator
                              FF=RIFSCz photometry and FIR indicator
                              W3=WISE W3-band forced photometry and indicator
                              W4=WISE W4-band forced photometry and indicator
92         logM_HEC           Decimal logarithm of the total stellar mass in solar masses
93         logSFR_GSW         Decimal logarithm of the SED-based star-formation rate from the GSWLC-2 in solar masses per year
94         logM_GSW           Decimal logarithm of the SED-based stellar mass from the GSWLC-2 in solar masses
95         min_snr            Minimum signal-to-noise ratio of the emission lines used for the activity classification (class_sp)
96         metal              12+log(O/H) gas-phase metallicity
97         flag_metal         Metallicity flag:
                              -1=missing
                              0=reliable
                              1=O3N2 ratio >2 (outside the PP04 range)
                              2=low signal-to-noise ratio (<3 for the weakest line)
98         class_sp           Nuclear activity classification using the method in Stampoulis et al 2019:
                              0=star-forming, 1=Seyfert, 2=LINER, 3=composite, -1=unknown
99         agn_s17            AGN classification in She et al 2017:
                              Y=AGN, N=non-AGN, ?=unknown
100        agn_hec            Adopted activity classification based on the combination of class_sp and agn_s17: 
                              Y=AGN, N=non-AGN, ?=unknown
"""


# +
# function: hecate_q3c_orm_cli()
# -
# noinspection PyBroadException
def hecate_q3c_orm_cli(_args: Any = None):

    # check input(s)
    if _args is None:
        raise Exception('Invalid arguments')

    # if --paper is present, download the science paper
    if _args.paper:
        if _args.verbose:
            print(f"Downloading science paper from {ARXIV_PDF_URL} to {ARXIV_PDF_FIL}")
        get_data(_url=ARXIV_PDF_URL, _file=ARXIV_PDF_FIL)
        return

    # if --text is present, describe of the catalog
    if _args.text:
        return print(__text__)

    # get input(s)
    request_args = {}
    if _args.astrocone:
        request_args['astrocone'] = f'{_args.astrocone}'
    if _args.cone:
        request_args['cone'] = f'{_args.cone}'
    if _args.ellipse:
        request_args['ellipse'] = f'{_args.ellipse}'
    if _args.hid:
        request_args['hid'] = f'{_args.hid}'
    if _args.name:
        request_args['name'] = f'{_args.name}'
    if _args.ra__gte:
        request_args['ra__gte'] = f'{_args.ra__gte}'
    if _args.ra__lte:
        request_args['ra__lte'] = f'{_args.ra__lte}'
    if _args.dec__gte:
        request_args['dec__gte'] = f'{_args.dec__gte}'
    if _args.dec__lte:
        request_args['dec__lte'] = f'{_args.dec__lte}'
    if _args.d__gte:
        request_args['d__gte'] = f'{_args.d__gte}'
    if _args.d__lte:
        request_args['d__lte'] = f'{_args.d__lte}'
    if _args.ut__gte:
        request_args['ut__gte'] = f'{_args.ut__gte}'
    if _args.ut__lte:
        request_args['ut__lte'] = f'{_args.ut__lte}'
    if _args.bt__gte:
        request_args['bt__gte'] = f'{_args.bt__gte}'
    if _args.bt__lte:
        request_args['bt__lte'] = f'{_args.bt__lte}'
    if _args.vt__gte:
        request_args['vt__gte'] = f'{_args.vt__gte}'
    if _args.vt__lte:
        request_args['vt__lte'] = f'{_args.vt__lte}'
    if _args.it__gte:
        request_args['it__gte'] = f'{_args.it__gte}'
    if _args.it__lte:
        request_args['it__lte'] = f'{_args.it__lte}'
    if _args.j__gte:
        request_args['j__gte'] = f'{_args.j__gte}'
    if _args.j__lte:
        request_args['j__lte'] = f'{_args.j__lte}'
    if _args.h__gte:
        request_args['h__gte'] = f'{_args.h__gte}'
    if _args.h__lte:
        request_args['h__lte'] = f'{_args.h__lte}'
    if _args.k__gte:
        request_args['k__gte'] = f'{_args.k__gte}'
    if _args.k__lte:
        request_args['k__lte'] = f'{_args.k__lte}'
    if _args.u__gte:
        request_args['u__gte'] = f'{_args.u__gte}'
    if _args.u__lte:
        request_args['u__lte'] = f'{_args.u__lte}'
    if _args.g__gte:
        request_args['g__gte'] = f'{_args.g__gte}'
    if _args.g__lte:
        request_args['g__lte'] = f'{_args.g__lte}'
    if _args.r__gte:
        request_args['r__gte'] = f'{_args.r__gte}'
    if _args.r__lte:
        request_args['r__lte'] = f'{_args.r__lte}'
    if _args.i__gte:
        request_args['i__gte'] = f'{_args.i__gte}'
    if _args.i__lte:
        request_args['i__lte'] = f'{_args.i__lte}'
    if _args.z__gte:
        request_args['z__gte'] = f'{_args.z__gte}'
    if _args.z__lte:
        request_args['z__lte'] = f'{_args.z__lte}'

    if _args.sort_order:
        request_args['sort_order'] = f'{_args.sort_order}'
    if _args.sort_value:
        request_args['sort_value'] = f'{_args.sort_value}'

    # set up access to database
    try:
        if _args.verbose:
            print(f'connection string = postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
        engine = create_engine(f'postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
        if _args.verbose:
            print(f'engine = {engine}')
        get_session = sessionmaker(bind=engine)
        if _args.verbose:
            print(f'Session = {get_session}')
        session = get_session()
        if _args.verbose:
            print(f'session = {session}')
    except Exception as _e1:
        raise Exception(f"failed to connect to database, error='{_e1}'")

    # execute query
    try:
        if _args.verbose:
            print(f'executing query')
        query = session.query(HecateQ3cRecord)
        if _args.verbose:
            print(f'query = {query}')
        query = hecate_q3c_orm_filters(query, request_args)
        if _args.verbose:
            print(f'query = {query}')
    except Exception as _e2:
        raise Exception(f"failed to execute query, error='{_e2}'")

    # report output
    print(f"#{','.join(_ for _ in HECATE_HEADERS)}")
    for _e in HecateQ3cRecord.serialize_list(query.all()):
        if verify_keys(_e, set(HECATE_HEADERS)):
            print(f"{','.join(str(_e[_l]) for _l in HECATE_HEADERS)}")


# +
# main()
# -
if __name__ == '__main__':

    # noinspection PyTypeChecker
    _p = argparse.ArgumentParser(description=f'Query HECATE Q3C', formatter_class=argparse.RawTextHelpFormatter)

    # database query argument(s)
    _p.add_argument(f'--astrocone', help=f'Astrocone search [name,radius (deg)]')
    _p.add_argument(f'--cone', help=f'Cone search [ra (deg),dec (deg),radius (deg)]')
    _p.add_argument(f'--ellipse', help=f'Ellipse search [ra (deg),dec (deg),major_axis,axis_ratio,pos_angle (deg)]')
    _p.add_argument(f'--hid', help=f'hid <int>')
    _p.add_argument(f'--name', help=f'name like <str>')
    _p.add_argument(f'--ra__gte', help=f'RA (deg) >= <float>')
    _p.add_argument(f'--ra__lte', help=f'RA (deg) <= <float>')
    _p.add_argument(f'--dec__gte', help=f'Dec (deg) >= <float>')
    _p.add_argument(f'--dec__lte', help=f'Dec (deg) <= <float>')
    _p.add_argument(f'--d__gte', help=f'Distance (Mpc) >= <float>')
    _p.add_argument(f'--d__lte', help=f'Distance (Mpc) <= <float>')
    _p.add_argument(f'--ut__gte', help=f'U apparent magnitude >= <float>')
    _p.add_argument(f'--ut__lte', help=f'U apparent magnitude <= <float>')
    _p.add_argument(f'--bt__gte', help=f'B apparent magnitude >= <float>')
    _p.add_argument(f'--bt__lte', help=f'B apparent magnitude <= <float>')
    _p.add_argument(f'--vt__gte', help=f'V apparent magnitude >= <float>')
    _p.add_argument(f'--vt__lte', help=f'V apparent magnitude <= <float>')
    _p.add_argument(f'--it__gte', help=f'I apparent magnitude >= <float>')
    _p.add_argument(f'--it__lte', help=f'I apparent magnitude <= <float>')
    _p.add_argument(f'--j__gte', help=f'J magnitude >= <float>')
    _p.add_argument(f'--j__lte', help=f'J magnitude <= <float>')
    _p.add_argument(f'--h__gte', help=f'h magnitude >= <float>')
    _p.add_argument(f'--h__lte', help=f'H magnitude <= <float>')
    _p.add_argument(f'--k__gte', help=f'K magnitude >= <float>')
    _p.add_argument(f'--k__lte', help=f'K magnitude <= <float>')
    _p.add_argument(f'--u__gte', help=f'u apparent magnitude >= <float>')
    _p.add_argument(f'--u__lte', help=f'u apparent magnitude <= <float>')
    _p.add_argument(f'--g__gte', help=f'g apparent magnitude >= <float>')
    _p.add_argument(f'--g__lte', help=f'g apparent magnitude <= <float>')
    _p.add_argument(f'--r__gte', help=f'r apparent magnitude >= <float>')
    _p.add_argument(f'--r__lte', help=f'r apparent magnitude <= <float>')
    _p.add_argument(f'--i__gte', help=f'i apparent magnitude >= <float>')
    _p.add_argument(f'--i__lte', help=f'i apparent magnitude <= <float>')
    _p.add_argument(f'--z__gte', help=f'z apparent magnitude >= <float>')
    _p.add_argument(f'--z__lte', help=f'z apparent magnitude <= <float>')
    _p.add_argument(f'--sort_order', help=f"Sort order, one of {HECATE_SORT_ORDER}")
    _p.add_argument(f'--sort_value', help=f"Sort value, one of {HECATE_SORT_VALUE}")

    # non-database query argument(s)
    _p.add_argument(f'--paper', default=False, action='store_true', help=f'if present, download the science paper')
    _p.add_argument(f'--text', default=False, action='store_true', help=f'if present, describe the catalog')
    _p.add_argument(f'--verbose', default=False, action='store_true', help=f'if present, produce more verbose output')
    _a = _p.parse_args()

    # execute
    try:
        hecate_q3c_orm_cli(_args=_a)
    except Exception as _:
        if bool(_a.verbose):
            print(f"{_}")
        print(f"Use: {__doc__}")
