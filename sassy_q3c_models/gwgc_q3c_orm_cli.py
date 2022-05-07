#!/usr/bin/env python3


# +
# import(s)
# -
from sassy_q3c_models.gwgc_q3c_orm_filters import *


# +
# __doc__ string
# -
__doc__ = """ python3 gwgc_q3c_orm_cli.py --help """


# +
# constant(s)
# -
ARXIV_PDF_URL = GWGC_PDF_URL
ARXIV_PDF_FIL = GWGC_PDF_URL.split("/")[-1]
ARXIV_DAT_URL = GWGC_DAT_URL
ARXIV_DAT_FIL = GWGC_DAT_URL.split("/")[-1]


# +
# __text__
# -
__text__ = """

VII/267             Gravitational Wave Galaxy Catalogue           (White+ 2011)
================================================================================
A List of Galaxies for Gravitational Wave Searches
      White D.J.,  Daw E.J., Dhillon V.S.
    <Class. Quantum Grav. 28, 085016 (2011); arXiv:1103.0695>
================================================================================
ADC_Keywords: Galaxy catalogs

Abstract:
    We present a list of galaxies within 100Mpc, which we call the
    Gravitational Wave Galaxy Catalogue (GWGC), that is currently being
    used in follow-up searches of electromagnetic counterparts from
    gravitational wave searches. Due to the time constraints of rapid
    follow-up, a locally available catalogue of reduced, homogenized data
    is required. To achieve this we used four existing catalogues: an
    updated version of the Tully Nearby Galaxy Catalog (cat. VII/145),
    145 the Catalog of Neighboring Galaxies (Karachentsev et al. 2004,
    Cat. J/AJ/127/2031), the V8k catalogue (Tully et al.
    2009AJ....138..323T, http://edd.ifa.hawaii.edu/) and HyperLEDA
    (http://leda.univ-lyon1.fr/). The GWGC contains information on sky
    position, distance, blue magnitude, major and minor diameters,
    position angle, and galaxy type for 53,255 galaxies. Errors on these
    quantities are either taken directly from the literature or estimated
    based on our understanding of the uncertainties associated with the
    measurement method. By using the PGC numbering system developed for
    HyperLEDA, the catalogue has a reduced level of degeneracies compared
    to catalogues with a similar purpose and is easily updated. We also
    include 150 Milky Way globular clusters. Finally, we compare the GWGC
    to previously used catalogues, and find the GWGC to be more complete
    within 100 Mpc due to our use of more up-to-date input catalogues and
    the fact that we have not made a blue luminosity cut.

Description:

File Summary:
--------------------------------------------------------------------------------
 FileName  Lrecl  Records   Explanations
--------------------------------------------------------------------------------
ReadMe        80        .   This file
gwgc.dat     148    53312   The Gravitational Wave Galaxy Catalogue
--------------------------------------------------------------------------------

See also:
    VII/145 : Nearby Galaxies Catalogue (NBG) (Tully 1988)
    J/AJ/127/2031 : Catalog of neighboring galaxies (Karachentsev+, 2004)
    http://leda.univ-lyon1.fr/ : The HYPERLEDA home page
    http://edd.ifa.hawaii.edu/ : The Extragalactic Distance Database (EDD)

Byte-by-byte Description of file: gwgc.dat
--------------------------------------------------------------------------------
   Bytes Format Units    Label    Explanations
--------------------------------------------------------------------------------
   1-  7  I7    ---      PGC      [2,4715229]? Identifier from HYPERLEDA
                                  (empty for globular clusters)
   9- 36  A28   ---      Name     Common name of galaxy or globular
  38- 46  F9.5  h        RAhour   Right ascension (J2000, decimal hours)
  48- 55  F8.4  deg      DEdeg    Declination (J2000)
  57- 60  F4.1  ---      TT       [-9,10]? Morphological type code (1)
  62- 66  F5.2  mag      Bmag     ? Apparent blue magnitude
  68- 74  F7.3  arcmin   a        ? Major diameter (arcmins)
  76- 82  F7.3  arcmin e_a        ? Error in major diameter (arcmins)
  84- 90  F7.3  arcmin   b        ? Minor diameter (arcmins)
  92- 98  F7.3  arcmin e_b        ? Error in minor diameter (arcmins)
 100-104  F5.3  ---      b/a      [0,1]? Ratio of minor to major diameters
 106-110  F5.3  ---    e_b/a      ? Error on ratio of minor to major diameters
 112-116  F5.1  deg      PA       [0,180]? Position angle of galaxy
                                    (deg from north through east)
 118-123  F6.2  mag      BMAG     ? Absolute blue magnitude
 125-131  F7.2  Mpc      Dist     ? Distance (Mpc)
 133-138  F6.2  Mpc    e_Dist     ? error on Distance (Mpc)
 140-143  F4.2  mag    e_Bmag     ? error on Apparent blue magnitude
 145-148  F4.2  mag    e_BMAG     ? error on Absolute blue magnitude
--------------------------------------------------------------------------------
Note (1): Numerical morphology type (-6 to +10 for ellipticals to irregular);
     -9 is assigned for the Milky Way globular clusters.
--------------------------------------------------------------------------------


Acknowledgements:
    Roy Williams (Caltech, USA), Darren White (U. Sheffield, UK)
================================================================================
(End)                                   Francois Ochsenbein [CDS]    11-Jan-2012
"""


# +
# function: gwgc_q3c_orm_cli()
# -
# noinspection PyBroadException
def gwgc_q3c_orm_cli(_args: Any = None):

    # check input(s)
    if _args is None:
        raise Exception('Invalid arguments')

    # if --catalog is present, download the catalog
    if _args.catalog:
        if _args.verbose:
            print(f"Downloading catalog from {ARXIV_DAT_URL} to {ARXIV_DAT_FIL}")
        get_gzip(_url=ARXIV_DAT_URL, _file=ARXIV_DAT_FIL)
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
    if _args.a__gte:
        request_args['a__gte'] = f'{_args.a__gte}'
    if _args.a__lte:
        request_args['a__lte'] = f'{_args.a__lte}'
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
    if _args.b_app__gte:
        request_args['b_app__gte'] = f'{_args.b_app__gte}'
    if _args.b_app__lte:
        request_args['b_app__lte'] = f'{_args.b_app__lte}'
    if _args.b_div_a__gte:
        request_args['b_div_a__gte'] = f'{_args.b_div_a__gte}'
    if _args.b_div_a__lte:
        request_args['b_div_a__lte'] = f'{_args.b_div_a__lte}'
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
    if _args.ellipse:
        request_args['ellipse'] = f'{_args.ellipse}'
    if _args.gid:
        request_args['gid'] = f'{_args.gid}'
    if _args.name:
        request_args['name'] = f'{_args.name}'
    if _args.pa__gte:
        request_args['pa__gte'] = f'{_args.pa__gte}'
    if _args.pa__lte:
        request_args['pa__lte'] = f'{_args.pa__lte}'
    if _args.pgc:
        request_args['pgc'] = f'{_args.pgc}'
    if _args.sort_order:
        request_args['sort_order'] = f'{_args.sort_order}'
    if _args.sort_value:
        request_args['sort_value'] = f'{_args.sort_value}'
    if _args.ra__gte:
        request_args['ra__gte'] = f'{_args.ra__gte}'
    if _args.ra__lte:
        request_args['ra__lte'] = f'{_args.ra__lte}'
    if _args.tt__gte:
        request_args['tt__gte'] = f'{_args.tt__gte}'
    if _args.tt__lte:
        request_args['tt__lte'] = f'{_args.tt__lte}'

    # set up access to database
    try:
        if _args.verbose:
            print(f'connecting via postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
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
        query = session.query(GwgcQ3cRecord)
        if _args.verbose:
            print(f'query = {query}')
        query = gwgc_q3c_orm_filters(query, request_args)
        if _args.verbose:
            print(f'query = {query}')
    except Exception as _e2:
        raise Exception(f"failed to execute query, error='{_e2}'")

    # report output alphabetically
    print(f"#{','.join(_ for _ in GWGC_HEADERS)}")
    for _e in GwgcQ3cRecord.serialize_list(query.all()):
        if verify_keys(_e, set(GWGC_HEADERS)):
            print(f"{','.join(str(_e[_l]) for _l in GWGC_HEADERS)}")


# +
# main()
# -
if __name__ == '__main__':

    # noinspection PyTypeChecker
    _p = argparse.ArgumentParser(description=f'Query GWGC Q3C database', formatter_class=argparse.RawTextHelpFormatter)

    # database query argument(s)
    _p.add_argument(f'--astrocone', help=f'Astrocone search [name,radius (deg)]')
    _p.add_argument(f'--cone', help=f'Cone search [ra (deg),dec (deg),radius (deg)]')
    _p.add_argument(f'--ellipse', help=f'Ellipse search [ra (deg),dec (de),major_axis,axis_ratio,pos_angle (deg)]')
    _p.add_argument(f'--a__gte', help=f'Major axis >= <float>')
    _p.add_argument(f'--a__lte', help=f'Major axis <= <float>')
    _p.add_argument(f'--b__gte', help=f'Minor axis >= <float>')
    _p.add_argument(f'--b__lte', help=f'Minor axis <= <float>')
    _p.add_argument(f'--b_abs__gte', help=f'Absolute B magnitude <float>')
    _p.add_argument(f'--b_abs__lte', help=f'Absolute B magnitude <float>')
    _p.add_argument(f'--b_app__gte', help=f'Apparent B magnitude <float>')
    _p.add_argument(f'--b_app__lte', help=f'Apparent B magnitude <float>')
    _p.add_argument(f'--b_div_a__gte', help=f'Axis ratio >= <float>')
    _p.add_argument(f'--b_div_a__lte', help=f'Axis ratio <= <float>')
    _p.add_argument(f'--dec__gte', help=f'Dec >= <float>')
    _p.add_argument(f'--dec__lte', help=f'Dec <= <float>')
    _p.add_argument(f'--dist__gte', help=f'Distance >= <float>')
    _p.add_argument(f'--dist__lte', help=f'Distance <= <float>')
    _p.add_argument(f'--gid', help=f'gid <int>')
    _p.add_argument(f'--name', help=f'name <str>')
    _p.add_argument(f'--pa__gte', help=f'Position angle >= <float>')
    _p.add_argument(f'--pa__lte', help=f'Position angle <= <float>')
    _p.add_argument(f'--pgc', help=f'pgc <int>')
    _p.add_argument(f'--ra__gte', help=f'RA >= <float>')
    _p.add_argument(f'--ra__lte', help=f'RA <= <float>')
    _p.add_argument(f'--tt__gte', help=f'Morphological type >= <float>')
    _p.add_argument(f'--tt__lte', help=f'Morphological type <= <float>')
    _p.add_argument(f'--sort_order', help=f"Sort order, one of {GWGC_SORT_ORDER}")
    _p.add_argument(f'--sort_value', help=f"Sort value, one of {GWGC_SORT_VALUE}")

    # non-database query argument(s)ß
    _p.add_argument(f'--catalog', default=False, action='store_true', help=f'if present, download the catalog')
    _p.add_argument(f'--paper', default=False, action='store_true', help=f'if present, download the science paper')
    _p.add_argument(f'--text', default=False, action='store_true', help=f'if present, describe the catalog')
    _p.add_argument(f'--verbose', default=False, action='store_true', help=f'if present, produce more verbose output')
    _a = _p.parse_args()

    # execute
    try:
        gwgc_q3c_orm_cli(_args=_a)
    except Exception as _:
        if bool(_a.verbose):
            print(f"{_}")
        print(f"Use: {__doc__}")
