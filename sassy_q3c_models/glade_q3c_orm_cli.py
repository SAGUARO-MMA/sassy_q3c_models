#!/usr/bin/env python3


# +
# import(s)
# -
from sassy_q3c_models.glade_q3c_orm_filters import *


# +
# __doc__ string
# -
__doc__ = """ python3 glade_q3c_orm_cli.py --help """


# +
# constant(s)
# -
ARXIV_PDF_URL = GLADE_PDF_URL
ARXIV_PDF_FIL = GLADE_PDF_URL.split("/")[-1]
ARXIV_DAT_URL = GLADE_DAT_URL
ARXIV_DAT_FIL = GLADE_DAT_URL.split("/")[-1]


# +
# __text__
# -
__text__ = """
Column     Name               Description
1          PGC                PGC number
2          GWGC               Name in the GWGC catalog
3          HyperLEDA          Name in the HyperLEDA catalog
4          2MASS              Name in the 2MASS XSC catalog
5          SDSS               Name in the SDSS-DR12 QSO catalog
6          flag1              Q: source is from the SDSS-DR12 QSO catalog
                              C: source is a globular cluster
                              G: source is from another catalog and not identified as a globular cluster
7          RA                 Right ascension [deg]
8          Dec                Declination [deg]
9          Dist               Luminosity distance [Mpc]
10         Dist_err           Error of distance [Mpc]
11         z                  Redshift
12         B                  Apparent B magnitude
13         B_err              Error of apparent B magnitude
14         B_abs              Absolute B magnitude
15         J                  Apparent J magnitude
16         J_err              Error of apparent J magnitude
17         H                  Apparent H magnitude
18         H_err              Error of apparent H magnitude
19         K                  Apparent K magnitude
20         K_err              Error of apparent K magnitude
21         flag2              0: galaxy had neither measured distance nor measured redshift value
                              1: galaxy had measured redshift value, from which we have calculated distance using the 
                              following cosmological parameters: H_0=70/km/s/Mpc, Omega_M=0.27 and Omega_Lambda=0.73
                              2: galaxy had measured distance value from which we have calculated redshift using the 
                              following cosmological parameters: H_0=70/km/s/Mp, Omega_M=0.27 and Omega_Lambda=0.73
                              3: measured photometric redshift of the galaxy has been changed to spectroscopic 
                              redshift, from which we have calculated distance using the following cosmological 
                              parameters: H_0=70/km/s/Mpc, Omega_M=0.27 and Omega_Lambda=0.73
22         flag3              0: velocity field correction has not been applied to the object
                              1: we have subtracted the radial velocity of the object

"""


# +
# function: glade_q3c_orm_cli()
# -
# noinspection PyBroadException
def glade_q3c_orm_cli(_args: Any = None):

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
    if _args.b__gte:
        request_args['b__gte'] = f'{_args.b__gte}'
    if _args.b__lte:
        request_args['b__lte'] = f'{_args.b__lte}'
    if _args.b_abs__gte:
        request_args['b_abs__gte'] = f'{_args.b_abs__gte}'
    if _args.b_abs__lte:
        request_args['b_abs__lte'] = f'{_args.b_abs__lte}'
    if _args.cone:
        request_args['cone'] = f'{_args.cone}'
    if _args.dec__gte:
        request_args['dec__gte'] = f'{_args.dec__gte}'
    if _args.dec__lte:
        request_args['dec__lte'] = f'{_args.dec__lte}'
    if _args.dist__gte:
        request_args['dist__gte'] = f'{_args.dist__gte}'
    if _args.dist__lte:
        request_args['dist__lte'] = f'{_args.dist__lte}'
    if _args.disterr__gte:
        request_args['disterr__gte'] = f'{_args.disterr__gte}'
    if _args.disterr__lte:
        request_args['disterr__lte'] = f'{_args.disterr__lte}'
    if _args.ellipse:
        request_args['ellipse'] = f'{_args.ellipse}'
    if _args.flag1:
        request_args['flag1'] = f'{_args.flag1}'
    if _args.flag2__gte:
        request_args['flag2__gte'] = f'{_args.flag2__gte}'
    if _args.flag2__lte:
        request_args['flag2__lte'] = f'{_args.flag2__lte}'
    if _args.flag3__gte:
        request_args['flag3__gte'] = f'{_args.flag3__gte}'
    if _args.flag3__lte:
        request_args['flag3__lte'] = f'{_args.flag3__lte}'
    if _args.gid:
        request_args['gid'] = f'{_args.gid}'
    if _args.gwgc:
        request_args['gwgc'] = f'{_args.gwgc}'
    if _args.h__gte:
        request_args['h__gte'] = f'{_args.h__gte}'
    if _args.h__lte:
        request_args['h__lte'] = f'{_args.h__lte}'
    if _args.hyperleda:
        request_args['hyperleda'] = f'{_args.hyperleda}'
    if _args.j__gte:
        request_args['j__gte'] = f'{_args.j__gte}'
    if _args.j__lte:
        request_args['j__lte'] = f'{_args.j__lte}'
    if _args.k__gte:
        request_args['k__gte'] = f'{_args.k__gte}'
    if _args.k__lte:
        request_args['k__lte'] = f'{_args.k__lte}'
    if _args.pgc:
        request_args['pgc'] = f'{_args.pgc}'
    if _args.ra__gte:
        request_args['ra__gte'] = f'{_args.ra__gte}'
    if _args.ra__lte:
        request_args['ra__lte'] = f'{_args.ra__lte}'
    if _args.sdss:
        request_args['sdss'] = f'{_args.sdss}'
    if _args.sort_order:
        request_args['sort_order'] = f'{_args.sort_order}'
    if _args.sort_value:
        request_args['sort_value'] = f'{_args.sort_value}'
    if _args.twomass:
        request_args['twomass'] = f'{_args.twomass}'
    if _args.z__gte:
        request_args['z__gte'] = f'{_args.z__gte}'
    if _args.z__lte:
        request_args['z__lte'] = f'{_args.z__lte}'

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
        query = session.query(GladeQ3cRecord)
        if _args.verbose:
            print(f'query = {query}')
        query = glade_q3c_orm_filters(query, request_args)
        if _args.verbose:
            print(f'query = {query}')
    except Exception as _e2:
        raise Exception(f"failed to execute query, error='{_e2}'")

    # report output
    print(f"#{','.join(_ for _ in GLADE_HEADERS)}")
    for _e in GladeQ3cRecord.serialize_list(query.all()):
        if verify_keys(_e, set(GLADE_HEADERS)):
            print(f"{','.join(str(_e[_l]) for _l in GLADE_HEADERS)}")


# +
# main()
# -
if __name__ == '__main__':

    # noinspection PyTypeChecker
    _p = argparse.ArgumentParser(description=f'Query GLADE Q3C', formatter_class=argparse.RawTextHelpFormatter)

    # non-database query argument(s)
    _p.add_argument(f'--astrocone', help=f'Astrocone search <name,radius>')
    _p.add_argument(f'--b__gte', help=f'b__gte >= <float>')
    _p.add_argument(f'--b__lte', help=f'b__lte <= <float>')
    _p.add_argument(f'--b_abs__gte', help=f'b_abs__gte >= <float>')
    _p.add_argument(f'--b_abs__lte', help=f'b_abs__lte <= <float>')
    _p.add_argument(f'--cone', help=f'Cone search <ra,dec,radius>')
    _p.add_argument(f'--dec__gte', help=f'dec__gte >= <float>')
    _p.add_argument(f'--dec__lte', help=f'dec__lte <= <float>')
    _p.add_argument(f'--dist__gte', help=f'dist__gte >= <float>')
    _p.add_argument(f'--dist__lte', help=f'dist__lte <= <float>')
    _p.add_argument(f'--disterr__gte', help=f'disterr__gte >= <float>')
    _p.add_argument(f'--disterr__lte', help=f'disterr__lte <= <float>')
    _p.add_argument(f'--ellipse', help=f'Ellipse search <ra,dec,major_axis,axis_ratio,position_angle>')
    _p.add_argument(f'--flag1', help=f'flag1 <str>')
    _p.add_argument(f'--flag2__gte', help=f'flag2__gte >= <int>')
    _p.add_argument(f'--flag2__lte', help=f'flag2__lte <= <int>')
    _p.add_argument(f'--flag3__gte', help=f'flag3__gte >= <int>')
    _p.add_argument(f'--flag3__lte', help=f'flag3__lte <= <int>')
    _p.add_argument(f'--gid', help=f'gid = <int>')
    _p.add_argument(f'--gwgc', help=f'GWGC name <str>')
    _p.add_argument(f'--h__gte', help=f'h__gte >= <float>')
    _p.add_argument(f'--h__lte', help=f'h__lte <= <float>')
    _p.add_argument(f'--hyperleda', help=f'HyperLEDA name <str>')
    _p.add_argument(f'--j__gte', help=f'j__gte >= <float>')
    _p.add_argument(f'--j__lte', help=f'j__lte <= <float>')
    _p.add_argument(f'--k__gte', help=f'k__gte >= <float>')
    _p.add_argument(f'--k__lte', help=f'k__lte <= <float>')
    _p.add_argument(f'--pgc', help=f'pgc = <int>')
    _p.add_argument(f'--ra__gte', help=f'ra__gte >= <float>')
    _p.add_argument(f'--ra__lte', help=f'ra__lte <= <float>')
    _p.add_argument(f'--sdss', help=f'SDSS name <str>')
    _p.add_argument(f'--twomass', help=f'2MASS name <str>')
    _p.add_argument(f'--z__gte', help=f'z__gte >= <float>')
    _p.add_argument(f'--z__lte', help=f'z__lte <= <float>')
    _p.add_argument(f'--sort_order', help=f"Sort order, one of {GLADE_SORT_ORDER}")
    _p.add_argument(f'--sort_value', help=f"Sort value, one of {GLADE_SORT_VALUE}")

    # non-database query argument(s)
    _p.add_argument(f'--catalog', default=False, action='store_true', help=f'if present, download the catalog')
    _p.add_argument(f'--paper', default=False, action='store_true', help=f'if present, download the science paper')
    _p.add_argument(f'--text', default=False, action='store_true', help=f'if present, describe the catalog')
    _p.add_argument(f'--verbose', default=False, action='store_true', help=f'if present, produce more verbose output')
    _a = _p.parse_args()

    # execute
    try:
        glade_q3c_orm_cli(_args=_a)
    except Exception as _:
        if bool(_a.verbose):
            print(f"{_}")
        print(f"Use: {__doc__}")
