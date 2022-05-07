#!/usr/bin/env python3


# +
# import(s)
# -
from sassy_q3c_models.asassn_q3c_orm_filters import *


# +
# __doc__ string
# -
__doc__ = """ python3 asassn_q3c_orm_cli.py --help """


# +
# constant(s)
# -
ARXIV_PDF_URL = ASASSN_PDF_URL
ARXIV_PDF_FIL = ASASSN_PDF_URL.split("/")[-1]
ARXIV_DAT_URL = ASASSN_DAT_URL
ARXIV_DAT_FIL = ASASSN_DAT_URL.split("/")[-1]


# +
# __text__
# -
__text__ = """
Column     Name                 Description
1          adbid                Database Number
2          aid                  Asassn Identifier
3          source_id            Source Identifier
4          asassn_name          Asassn Name
5          other_names          Other (Known) Names
6          ra                   RA (J2000 deg)
7          dec                  Declination (J2000 deg)
8          l                    Galactic Longtiude (deg)
9          b                    Galactic Latitude (deg)
10         mean_vmag            Mean V Magnitude
11         amplitude            Amplitude
12         period               Period
13         variable_type        Variable Type
14         class_probability    Class Probability
15         lksl_statistic       LKSL Statistic
16         rfr_score            RFR score
17         epoch_hjd            HJV Epoch
18         gdr2_id              GAIA DR2 Identifier
19         phot_g_mean_mag      Photometric Mean g Magnitude
20         e_phot_g_mean_mag    Error in Photometric Mean g Magnitude
21         phot_bp_mean_mag     Photometric Mean b Magnitude
22         e_phot_bp_mean_mag   Error in Photometric Mean b Magnitude
23         phot_rp_mean_mag     Photometric Mean r Magnitude
24         e_phot_rp_mean_mag   Error in Photometric Mean r Magnitude
25         bp_rp                B - R
26         parallax             Parallax
27         parallax_error       Error in Parallax
28         parallax_over_error  Over Error in parallax
29         pmra                 Proper Motion in RA
30         pmra_error           Error in Proper Motion in RA
31         pmdec                Proper Motion in Dec
32         pmdec_error          Error in Proper Motion in Dec
33         vt                   vt
34         dist                 Distance
35         allwise_id           WISE Identifier
36         j_mag                J Magnitude
37         e_j_mag              Error in J Magnitude
38         h_mag                H Magnitude
39         e_h_mag              Error in H Magnitude
40         k_mag                K Magnitude
41         e_k_mag              Error in K Magnitude
42         w1_mag               W1 Magnitude
43         e_w1_mag             Error in W1 Magnitude
44         w2_mag               W2 Magnitude
45         e_w2_mag             Error in W2 Magnitude
46         w3_mag               W3 Magnitude
47         e_w3_mag             Error in W3 Magnitude
48         w4_mag               W4 Magnitude
49         e_w4_mag             Error in W4 Magnitude
50         j_k                  J - K
51         w1_w2                W1 - W2
52         w3_w4                W3 - W4
53         apass_dr9_id         APASS DR9 Identifier
54         apass_vmag           APASS v Magnitude
55         e_apass_vmag         Error in APASS v Magnitude
56         apass_bmag           APASS b Magnitude
57         e_apass_bmag         Error in APASS b Magnitude
58         apass_gpmag          APASS g Magnitude
59         e_apass_gpmag        Error in APASS g Magnitude
60         apass_rpmag          APASS r Magnitude
61         e_apass_rpmag        Error in APASS r Magnitude
62         apass_ipmag          APASS i Magnitude
63         e_apass_ipmag        Error in APASS i Magnitude
64         b_v                  B - V
65         e_b_v                Error in B-V
66         vector_x             Vector X
67         vector_y             Vector Y
68         vector_z             Vector Z
69         reference            Reference
70         periodic             Periodic (boolean)
71         classified           Classified (boolean)
72         asassn_discovery     Asassn Discovery (boolean)
73         created_at           Creation Date
74         updated_at           Update Date
75         edr3_source_id       EDR3 Source Identifier
76         galex_id             GALEX Identifier
77         FUVmag               FUV Magnitude
78         e_FUVmag             Error in FUV Magnitude
79         NUVmag               NUV Magnitude
80         e_NUVmag             Error in NUV Magnitude
81         tic_id               tic Identifier
82         pm                   pm
83         ruwe                 ruwe
"""


# +
# function: asassn_q3c_orm_cli()
# -
# noinspection PyBroadException
def asassn_q3c_orm_cli(_args: Any = None):

    # check input(s)
    if _args is None:
        raise Exception('Invalid arguments')

    # if --catalog is present, download the catalog
    if _args.catalog:
        if _args.verbose:
            print(f"Downloading catalog from {ARXIV_DAT_URL} to {ARXIV_DAT_FIL}")
        get_data(_url=ARXIV_DAT_URL, _file=ARXIV_DAT_FIL)
        return

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
    if _args.aid:
        request_args['aid'] = f'{_args.aid}'
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
    if _args.dist__gte:
        request_args['dist__gte'] = f'{_args.dist__gte}'
    if _args.dist__lte:
        request_args['dist__lte'] = f'{_args.dist__lte}'
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
    if _args.v__gte:
        request_args['v__gte'] = f'{_args.v__gte}'
    if _args.v__lte:
        request_args['v__lte'] = f'{_args.v__lte}'
    if _args.amplitude__gte:
        request_args['amplitude__gte'] = f'{_args.amplitude__gte}'
    if _args.amplitude__lte:
        request_args['amplitude__lte'] = f'{_args.amplitude__lte}'
    if _args.period__gte:
        request_args['period__gte'] = f'{_args.period__gte}'
    if _args.period__lte:
        request_args['period__lte'] = f'{_args.period__lte}'
    if _args.lksl__gte:
        request_args['lksl__gte'] = f'{_args.lksl__gte}'
    if _args.lksl__lte:
        request_args['lksl__lte'] = f'{_args.lksl__lte}'
    if _args.parallax__gte:
        request_args['parallax__gte'] = f'{_args.parallax__gte}'
    if _args.parallax__lte:
        request_args['parallax__lte'] = f'{_args.parallax__lte}'
    if _args.probability__gte:
        request_args['probability__gte'] = f'{_args.probability__gte}'
    if _args.probability__lte:
        request_args['probability__lte'] = f'{_args.probability__lte}'
    if _args.vtype:
        request_args['vtype'] = f'{_args.vtype}'
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
        query = session.query(AsAssnQ3cRecord)
        if _args.verbose:
            print(f'query = {query}')
        query = asassn_q3c_orm_filters(query, request_args)
        if _args.verbose:
            print(f'query = {query}')
    except Exception as _e2:
        raise Exception(f"failed to execute query, error='{_e2}'")

    # report output
    print(f"#{','.join(_ for _ in ASASSN_HEADERS)}")
    for _e in AsAssnQ3cRecord.serialize_list(query.all()):
        if verify_keys(_e, set(ASASSN_HEADERS)):
            print(f"{','.join(str(_e[_l]) for _l in ASASSN_HEADERS)}")


# +
# main()
# -
if __name__ == '__main__':

    # get command line parser
    _p = argparse.ArgumentParser(description=f'Query AsAssn Q3C', formatter_class=argparse.RawTextHelpFormatter)

    # database query argument(s)
    _p.add_argument(f'--astrocone', help=f'Astrocone search [name,radius (deg)]')
    _p.add_argument(f'--cone', help=f'Cone search [ra (deg),dec (deg),radius (deg)]')
    _p.add_argument(f'--ellipse', help=f'Ellipse search [ra (deg),dec (de),major_axis,axis_ratio,pos_angle (deg)]')
    _p.add_argument(f'--aid', help=f'gid <int>')
    _p.add_argument(f'--name', help=f'name like <str>')
    _p.add_argument(f'--ra__gte', help=f'RA (deg) >= <float>')
    _p.add_argument(f'--ra__lte', help=f'RA (deg) <= <float>')
    _p.add_argument(f'--dec__gte', help=f'Dec (deg) >= <float>')
    _p.add_argument(f'--dec__lte', help=f'Dec (deg) <= <float>')
    _p.add_argument(f'--dist__gte', help=f'Distance (Mpc) >= <float>')
    _p.add_argument(f'--dist__lte', help=f'Distance (Mpc) <= <float>')
    _p.add_argument(f'--j__gte', help=f'J magnitude >= <float>')
    _p.add_argument(f'--j__lte', help=f'J magnitude >= <float>')
    _p.add_argument(f'--h__gte', help=f'H magnitude >= <float>')
    _p.add_argument(f'--h__lte', help=f'H magnitude <= <float>')
    _p.add_argument(f'--k__gte', help=f'K magnitude <= <float>')
    _p.add_argument(f'--k__lte', help=f'K magnitude <= <float>')
    _p.add_argument(f'--v__gte', help=f'Mean V magnitude >= <float>')
    _p.add_argument(f'--v__lte', help=f'Mean V magnitude <= <float>')
    _p.add_argument(f'--amplitude__gte', help=f'Amplitude >= <float>')
    _p.add_argument(f'--amplitude__lte', help=f'Amplitude <= <float>')
    _p.add_argument(f'--period__gte', help=f'Period >= <float>')
    _p.add_argument(f'--period__lte', help=f'Period <= <float>')
    _p.add_argument(f'--lksl__gte', help=f'LKSL Statistic >= <float>')
    _p.add_argument(f'--lksl__lte', help=f'LKSL Statistic <= <float>')
    _p.add_argument(f'--parallax__gte', help=f'Parallax >= <float>')
    _p.add_argument(f'--parallax__lte', help=f'Parallax <= <float>')
    _p.add_argument(f'--probability__gte', help=f'Class Probability >= <float>')
    _p.add_argument(f'--probability__lte', help=f'Class Probability <= <float>')
    _p.add_argument(f'--vtype', help=f'Variable type like <str>')
    _p.add_argument(f'--sort_order', help=f"Sort order, one of {ASASSN_SORT_ORDER}")
    _p.add_argument(f'--sort_value', help=f"Sort value, one of {ASASSN_SORT_VALUE}")

    # non-database query argument(s)
    _p.add_argument(f'--catalog', default=False, action='store_true', help=f'if present, download the catalog')
    _p.add_argument(f'--paper', default=False, action='store_true', help=f'if present, download the science paper')
    _p.add_argument(f'--text', default=False, action='store_true', help=f'if present, describe the catalog')
    _p.add_argument(f'--verbose', default=False, action='store_true', help=f'if present, produce more verbose output')
    _a = _p.parse_args()

    # execute
    try:
        asassn_q3c_orm_cli(_args=_a)
    except Exception as _:
        if bool(_a.verbose):
            print(f"{_}")
        print(f"Use: {__doc__}")
