#!/usr/bin/env python3


# +
# import(s)
# -
from sassy_q3c_models.glade_plus_q3c_orm_filters import *


# +
# __doc__ string
# -
__doc__ = """ python3 glade_plus_q3c_orm_cli.py --help """


# +
# constant(s)
# -
ARXIV_PDF_URL = GLADE_PLUS_PDF_URL
ARXIV_PDF_FIL = GLADE_PLUS_PDF_URL.split("/")[-1]
ARXIV_DAT_URL = GLADE_PLUS_DAT_URL
ARXIV_DAT_FIL = GLADE_PLUS_DAT_URL.split("/")[-1]


# +
# __text__
# -
__text__ = """
Column     Name               Description
1          GLADE no           GLADE+ catalog number
2          PGC no             Principal Galaxies Catalogue number
3          GWGC name          Name in the GWGC catalog
4          HyperLEDA name     Name in the HyperLEDA catalog
5          2MASS name         Name in the 2MASS XSC catalog
6          WISExSCOS name     Name in the WISExSuperCOSMOS catalog (wiseX)
7          SDSS-DR16Q name    Name in the SDSS-DR16Q catalog
8          Object type flag   Q: the source is from the SDSS-DR16Q catalog
                              G:the source is from another catalog and has not been identified as a quasar
9          RA                 Right ascension (deg)
10         Dec                Declination (deg)
11         B                  Apparent B magnitude
12         B_err              Absolute error of apparent B magnitude
13         B flag             0: the B magnitude is measured
                              1: the B magnitude is calculated from the B_J magnitude
14         B_Abs              Absolute B magnitude
15         J                  Apparent J magnitude
16         J_err              Absolute error of apparent J magnitude
17         H                  Apparent H magnitude
18         H_err              Absolute error of apparent H magnitude
19         K                  Apparent K_s magnitude
20         K_err              Absolute error of apparent K_s magnitude
21         W1                 Apparent W1 magnitude
22         W1_err             Absolute error of apparent W1 magnitude
23         W2                 Apparent W2 magnitude
24         W2_err             Absolute error of apparent W2 magnitude
25         W1 flag            0: the W1 magnitude is measured
                              1: the W1 magnitude is calculated from the K_s magnitude
26         B_J                Apparent B_J magnitude
27         B_J err            Absolute error of apparent B_J magnitude
28         z_helio            Redshift in the heliocentric frame
29         z_cmb              Redshift converted to the Cosmic Microwave Background (CMB) frame
30         z flag             0: the CMB frame redshift and luminosity distance values given in columns 25 and 28 are not corrected for the peculiar velocity
                              1: they are corrected values
31         v_err              Error of redshift from the peculiar velocity estimation
32         z_err              Measurement error of heliocentric redshift
33         d_L                Luminosity distance in Mpc units
34         d_L err            Error of luminosity distance in Mpc units
35         dist flag          0: the galaxy has no measured redshift or distance value
                              1: it has a measured photometric redshift from which we have calculated its luminosity distance
                              2: it has a measured luminosity distance value from which we have calculated its redshift
                              3: it has a measured spectroscopic redshift from which we have calculated its luminosity distance
36         M*                 Stellar mass in 10^10 M_Sun units
37         M*_err             Absolute error of stellar mass in 10^10 M_Sun units
38         Merger rate        Base-10 logarithm of estimated BNS merger rate in the galaxy in Gyr^-1 units
39         Merger rate error  Absolute error of estimated BNS merger rate in the galaxy
"""


# +
# function: glade_plus_q3c_orm_cli()
# -
# noinspection PyBroadException
def glade_plus_q3c_orm_cli(_args: Any = None):

    # check input(s)
    if _args is None:
        raise Exception('Invalid arguments')

    # if --catalog is present, download the catalog
    if _args.catalog:
        if _args.verbose:
            print(f"Downloading catalog from {ARXIV_DAT_URL} to {ARXIV_DAT_FIL}")
        # noinspection PyUnresolvedReferences
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
    if _args.gid:
        request_args['gid'] = f'{_args.gid}'
    if _args.gn:
        request_args['gn'] = f'{_args.gn}'
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
    if _args.b__gte:
        request_args['b__gte'] = f'{_args.b__gte}'
    if _args.b__lte:
        request_args['b__lte'] = f'{_args.b__lte}'
    if _args.b_abs__gte:
        request_args['b_abs__gte'] = f'{_args.b_abs__gte}'
    if _args.b_abs__lte:
        request_args['b_abs__lte'] = f'{_args.b_abs__lte}'
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
    if _args.w1__gte:
        request_args['w1__gte'] = f'{_args.w1__gte}'
    if _args.w1__lte:
        request_args['w1__lte'] = f'{_args.w1__lte}'
    if _args.w2__gte:
        request_args['w2__gte'] = f'{_args.w2__gte}'
    if _args.w2__lte:
        request_args['w2__lte'] = f'{_args.w2__lte}'
    if _args.b_j__gte:
        request_args['b_j__gte'] = f'{_args.b_j__gte}'
    if _args.b_j__lte:
        request_args['b_j__lte'] = f'{_args.b_j__lte}'
    if _args.zhelio__gte:
        request_args['zhelio__gte'] = f'{_args.zhelio__gte}'
    if _args.zhelio__lte:
        request_args['zhelio__lte'] = f'{_args.zhelio__lte}'
    if _args.zcmb__gte:
        request_args['zcmb__gte'] = f'{_args.zcmb__gte}'
    if _args.zcmb__lte:
        request_args['zcmb__lte'] = f'{_args.zcmb__lte}'
    if _args.d_l__gte:
        request_args['d_l__gte'] = f'{_args.d_l__gte}'
    if _args.d_l__lte:
        request_args['d_l__lte'] = f'{_args.d_l__lte}'
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
        query = session.query(GladePlusQ3cRecord)
        if _args.verbose:
            print(f'query = {query}')
        query = glade_plus_q3c_orm_filters(query, request_args)
        if _args.verbose:
            print(f'query = {query}')
    except Exception as _e2:
        raise Exception(f"failed to execute query, error='{_e2}'")

    # report output
    print(f"#{','.join(_ for _ in GLADE_PLUS_HEADERS)}")
    for _e in GladePlusQ3cRecord.serialize_list(query.all()):
        if verify_keys(_e, set(GLADE_PLUS_HEADERS)):
            print(f"{','.join(str(_e[_l]) for _l in GLADE_PLUS_HEADERS)}")


# +
# main()
# -
if __name__ == '__main__':

    # noinspection PyTypeChecker,PyUnresolvedReferences
    _p = argparse.ArgumentParser(description=f'Query GLADE+ Q3C', formatter_class=argparse.RawTextHelpFormatter)

    # database query argument(s)
    _p.add_argument(f'--astrocone', help=f'Astrocone search [name,radius (deg)]')
    _p.add_argument(f'--cone', help=f'Cone search [ra (deg),dec (deg),radius (deg)]')
    _p.add_argument(f'--ellipse', help=f'Ellipse search [ra (deg),dec (deg),major_axis,axis_ratio,pos_angle (deg)]')
    _p.add_argument(f'--gid', help=f'gid <int>')
    _p.add_argument(f'--gn', help=f'gn <int>')
    _p.add_argument(f'--name', help=f'name like <str>')
    _p.add_argument(f'--ra__gte', help=f'RA (deg) >= <float>')
    _p.add_argument(f'--ra__lte', help=f'RA (deg) <= <float>')
    _p.add_argument(f'--dec__gte', help=f'Dec (deg) >= <float>')
    _p.add_argument(f'--dec__lte', help=f'Dec (deg) <= <float>')
    _p.add_argument(f'--b__gte', help=f'B magnitude >= <float>')
    _p.add_argument(f'--b__lte', help=f'B magnitude <= <float>')
    _p.add_argument(f'--b_abs__gte', help=f'B absolute magnitude >= <float>')
    _p.add_argument(f'--b_abs__lte', help=f'B absolute magnitude <= <float>')
    _p.add_argument(f'--j__gte', help=f'J magnitude >= <float>')
    _p.add_argument(f'--j__lte', help=f'J magnitude <= <float>')
    _p.add_argument(f'--h__gte', help=f'h magnitude >= <float>')
    _p.add_argument(f'--h__lte', help=f'H magnitude <= <float>')
    _p.add_argument(f'--k__gte', help=f'K magnitude >= <float>')
    _p.add_argument(f'--k__lte', help=f'K magnitude <= <float>')
    _p.add_argument(f'--w1__gte', help=f'W1 apparent magnitude >= <float>')
    _p.add_argument(f'--w1__lte', help=f'W1 apparent magnitude <= <float>')
    _p.add_argument(f'--w2__gte', help=f'W2 apparent magnitude >= <float>')
    _p.add_argument(f'--w2__lte', help=f'W2 apparent magnitude <= <float>')
    _p.add_argument(f'--b_j__gte', help=f'B_J magnitude >= <float>')
    _p.add_argument(f'--b_j__lte', help=f'B_J magnitude <= <float>')
    _p.add_argument(f'--zhelio__gte', help=f'Heliocentric redshift >= <float>')
    _p.add_argument(f'--zhelio__lte', help=f'Heliocentric redshift <= <float>')
    _p.add_argument(f'--zcmb__gte', help=f'CMB redshift >= <float>')
    _p.add_argument(f'--zcmb__lte', help=f'CMB redshift <= <float>')
    _p.add_argument(f'--d_l__gte', help=f'Luminosity distance (Mpc) >= <float>')
    _p.add_argument(f'--d_l__lte', help=f'Luminosity distance (Mpc) <= <float>')
    _p.add_argument(f'--sort_order', help=f"Sort order, one of {GLADE_PLUS_SORT_ORDER}")
    _p.add_argument(f'--sort_value', help=f"Sort value, one of {GLADE_PLUS_SORT_VALUE}")

    # non-database query argument(s)
    _p.add_argument(f'--catalog', default=False, action='store_true', help=f'if present, download the catalog')
    _p.add_argument(f'--paper', default=False, action='store_true', help=f'if present, download the science paper')
    _p.add_argument(f'--text', default=False, action='store_true', help=f'if present, describe the catalog')
    _p.add_argument(f'--verbose', default=False, action='store_true', help=f'if present, produce more verbose output')
    _a = _p.parse_args()

    # execute
    try:
        glade_plus_q3c_orm_cli(_args=_a)
    except Exception as _:
        if bool(_a.verbose):
            print(f"{_}")
        print(f"Use: {__doc__}")
