#!/usr/bin/env python3


# +
# import(s)
# -
from sassy_q3c_models.sdss12phot_q3c_orm_filters import *


# +
# __doc__ string
# -
__doc__ = """ python3 sdss12phot_q3c_orm_cli.py --help """


# +
# constant(s)
# -
ARXIV_PDF_URL = SDSS12PHOT_PDF_URL
ARXIV_PDF_FIL = SDSS12PHOT_PDF_URL.split("/")[-1]
ARXIV_DAT_URL = SDSS12PHOT_DAT_URL
ARXIV_DAT_FIL = SDSS12PHOT_DAT_URL.split("/")[-1]


# +
# __text__
# -
__text__ = """
Column     Name               Description
1          ra                 Right Ascension ICRS (deg)
2          dec                Declination ICR) (dec)
3          mode               1: primary, 2: secondary
4          q_mode             [+] indicates clean photometry
5          classifier         Type of object (3=galaxy, 6=star)
6          sdss12             SDSS-DR12 name, based on J2000 position
7          m_sdss12           [*] The asterisk indicates that 2 different SDSS objects share the same SDSS12 name
8          ObsDate            Mean Observation date (yr)
9          quality            Quality of the observation: 1=bad 2=acceptable 3=good
10         umag               Model magnitude in u filter (mag)
11         e_umag             Error in umag
12         gmag               Model magnitude in g filter (mag)
13         e_gmag             Error in gmag
14         rmag               Model magnitude in r filter (mag)
15         e_rmag             Error in rmag
16         imag               Model magnitude in i filter (mag)
17         e_imag             Error in imag
18         zmag               Model magnitude in z filter (mag)
19         e_zmag             Error in zmag
20         zsp                Spectroscopic redshift (when SpObjID>0)
21         zsh                Spectroscopic redshift (when SpObjID>0)  ?????
22         e_zsh              Error in zsh                             ?????
23         lastcol            Unknown  (identified in csv as __zph_)   ?????
"""


# +
# function: sdss12phot_q3c_orm_cli()
# -
# noinspection PyBroadException
def sdss12phot_q3c_orm_cli(_args: Any = None):

    # check input(s)
    if _args is None:
        raise Exception('Invalid arguments')

    # if --catalog is present, download the catalog
    # if _args.catalog:
    #     if _args.verbose:
    #         print(f"Downloading catalog from {ARXIV_DAT_URL} to {ARXIV_DAT_FIL}")
    #     get_gzip(_url=ARXIV_DAT_URL, _file=ARXIV_DAT_FIL)
    #     return

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
    if _args.ra__gte:
        request_args['ra__gte'] = f'{_args.ra__gte}'
    if _args.ra__lte:
        request_args['ra__lte'] = f'{_args.ra__lte}'
    if _args.dec__gte:
        request_args['dec__gte'] = f'{_args.dec__gte}'
    if _args.dec__lte:
        request_args['dec__lte'] = f'{_args.dec__lte}'
    if _args.sid:
        request_args['sid'] = f'{_args.sid}'
    if _args.classifier:
        request_args['classifier'] = f'{_args.classifier}'
    if _args.quality:
        request_args['quality'] = f'{_args.quality}'
    if _args.name:
        request_args['name'] = f'{_args.name}'
    if _args.obsdate__gte:
        request_args['obsdate__gte'] = f'{_args.obsdate__gte}'
    if _args.obsdate__lte:
        request_args['obsdate__lte'] = f'{_args.obsdate__lte}'
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
    if _args.zsp__gte:
        request_args['zsp__gte'] = f'{_args.zsp__gte}'
    if _args.zsp__lte:
        request_args['zsp__lte'] = f'{_args.zsp__lte}'

    if _args.sort_order:
        request_args['sort_order'] = f'{_args.sort_order}'
    if _args.sort_value:
        request_args['sort_value'] = f'{_args.sort_value}'

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
        query = session.query(Sdss12PhotQ3cRecord)
        if _args.verbose:
            print(f'query = {query}')
        query = sdss12phot_q3c_orm_filters(query, request_args)
        if _args.verbose:
            print(f'query = {query}')
    except Exception as _e2:
        raise Exception(f"failed to execute query, error='{_e2}'")

    # report output alphabetically
    print(f"#{','.join(_ for _ in SDSS12PHOT_HEADERS)}")
    for _e in Sdss12PhotQ3cRecord.serialize_list(query.all()):
        if verify_keys(_e, set(SDSS12PHOT_HEADERS)):
            print(f"{','.join(str(_e[_l]) for _l in SDSS12PHOT_HEADERS)}")


# +
# main()
# -
if __name__ == '__main__':

    # noinspection PyTypeChecker
    _p = argparse.ArgumentParser(description=f'Query SDSS12PHOT Q3C database', formatter_class=argparse.RawTextHelpFormatter)

    # database query argument(s)
    _p.add_argument(f'--astrocone', help=f'Astrocone search [name,radius (deg)]')
    _p.add_argument(f'--cone', help=f'Cone search [ra (deg),dec (deg),radius (deg)]')
    _p.add_argument(f'--ellipse', help=f'Ellipse search [ra (deg),dec (de),major_axis,axis_ratio,pos_angle (deg)]')
    _p.add_argument(f'--ra__gte', help=f'RA >= <float>')
    _p.add_argument(f'--ra__lte', help=f'RA <= <float>')
    _p.add_argument(f'--dec__gte', help=f'Dec >= <float>')
    _p.add_argument(f'--dec__lte', help=f'Dec <= <float>')
    _p.add_argument(f'--sid', help=f'sid <int>')
    _p.add_argument(f'--classifier', help=f'Classifier <int>')
    _p.add_argument(f'--quality', help=f'Quality <int>')
    _p.add_argument(f'--name', help=f'Name <str>')
    _p.add_argument(f'--obsdate__gte', help=f'Observation date >= <float>')
    _p.add_argument(f'--obsdate__lte', help=f'Observation date <= <float>')
    _p.add_argument(f'--u__gte', help=f'u mag >= <float>')
    _p.add_argument(f'--u__lte', help=f'u mag <= <float>')
    _p.add_argument(f'--g__gte', help=f'g mag >= <float>')
    _p.add_argument(f'--g__lte', help=f'g mag <= <float>')
    _p.add_argument(f'--r__gte', help=f'r mag >= <float>')
    _p.add_argument(f'--r__lte', help=f'r mag <= <float>')
    _p.add_argument(f'--i__gte', help=f'i mag >= <float>')
    _p.add_argument(f'--i__lte', help=f'i mag <= <float>')
    _p.add_argument(f'--z__gte', help=f'z mag >= <float>')
    _p.add_argument(f'--z__lte', help=f'z mag <= <float>')
    _p.add_argument(f'--zsp__gte', help=f'Redshift mag >= <float>')
    _p.add_argument(f'--zsp__lte', help=f'Redshift mag <= <float>')

    _p.add_argument(f'--sort_order', help=f"Sort order, one of {SDSS12PHOT_SORT_ORDER}")
    _p.add_argument(f'--sort_value', help=f"Sort value, one of {SDSS12PHOT_SORT_VALUE}")

    # non-database query argument(s)ß
    # _p.add_argument(f'--catalog', default=False, action='store_true', help=f'if present, download the catalog')
    _p.add_argument(f'--paper', default=False, action='store_true', help=f'if present, download the science paper')
    _p.add_argument(f'--text', default=False, action='store_true', help=f'if present, describe the catalog')
    _p.add_argument(f'--verbose', default=False, action='store_true', help=f'if present, produce more verbose output')
    _a = _p.parse_args()

    # execute
    try:
        sdss12phot_q3c_orm_cli(_args=_a)
    except Exception as _:
        if bool(_a.verbose):
            print(f"{_}")
        print(f"Use: {__doc__}")
