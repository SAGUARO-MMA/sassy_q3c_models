#!/usr/bin/env python3


# +
# import(s)
# -
from sassy_q3c_models.tns_q3c_orm_filters import *


# +
# __doc__ string
# -
__doc__ = """ python3 tns_q3c_orm_cli.py --help """


# +
# constant(s)
# -
ARXIV_PDF_URL = TNS_PDF_URL
ARXIV_PDF_FIL = TNS_PDF_URL.split("/")[-1]
ARXIV_DAT_URL = TNS_DAT_URL
ARXIV_DAT_FIL = TNS_DAT_URL.split("/")[-1]


# +
# __text__
# -
__text__ = """
As of January 1, 2016 the Transient Name Server (TNS) is the official IAU mechanism for 
reporting new astronomical transients such as supernova candidates. Once spectroscopically 
confirmed, new supernova discoveries are officially designated a SN name (of the form 
SN 2016A and so on, as before).

This is a continuation of the IAU naming scheme for supernovae which was handled by the 
Central Bureau for Astronomical Telegrams until the end of 2015, and has been approved 
as the official IAU naming scheme by the IAU Executive Committee from 1st January 2016.

Variable stars, including in particular Galactic nova candidates, should be reported in 
the same manner as before. Please do not submit reports regarding such objects to this 
web application.

This service is provided by the IAU supernova working group, free of charge to registered 
users, who can also choose to receive automated email alerts regarding new discoveries.
"""


# +
# constant(s)
# -
TNS_BOT_ID = os.getenv("TNS_BOT_ID", -1)
TNS_BOT_KEY = os.getenv("TNS_BOT_KEY", "")
TNS_BOT_NAME = os.getenv("TNS_BOT_NAME", "")
TNS_PASS = os.getenv("TNS_PASS", "")
TNS_USER = os.getenv("TNS_USER", "")


# +
# function: get_tns_data()
# -
def get_tns_data(_url: str = '', _file: str = ''):
    _h = {'User-Agent': 'tns_marker{"tns_id":"125165", "type":"bot", "name":"SASSy"}'}
    _d = f'api_key={TNS_BOT_KEY}'
    _u = urllib.request.Request(url=_url, data=_d.encode('utf-8'), method='POST', headers=_h)
    with open(_file, 'wb') as _fw:
        _fw.write(urllib.request.urlopen(_u).read())


# +
# function: get_tns_pdf()
# -
def get_tns_pdf(_url: str = '', _file: str = ''):
    _h = {'User-Agent': 'tns_marker{"tns_id":936, "type":"user", "name":"phil_daly"}'}
    _u = urllib.request.Request(url=_url, method='POST', headers=_h)
    with open(_file, 'wb') as _fw:
        _fw.write(urllib.request.urlopen(_url).read())


# +
# function: tns_q3c_orm_cli()
# -
# noinspection PyBroadException
def tns_q3c_orm_cli(_args: Any = None):

    # check input(s)
    if _args is None:
        raise Exception('Invalid arguments')

    # if --catalog is present, download the catalog
    if _args.catalog:
        if _args.verbose:
            print(f"Downloading catalog from {ARXIV_DAT_URL} to {ARXIV_DAT_FIL}")
        get_tns_data(_url=ARXIV_DAT_URL, _file=ARXIV_DAT_FIL)
        return

    # if --paper is present, download the science paper
    if _args.paper:
        if _args.verbose:
            print(f"Downloading science paper from {ARXIV_PDF_URL} to {ARXIV_PDF_FIL}")
        get_tns_pdf(_url=ARXIV_PDF_URL, _file=ARXIV_PDF_FIL)
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
    if _args.tid:
        request_args['tid'] = f'{_args.tid}'
    if _args.name:
        request_args['name'] = f'{_args.name}'
    if _args.report:
        request_args['report'] = f'{_args.report}'
    if _args.ra__gte:
        request_args['ra__gte'] = f'{_args.ra__gte}'
    if _args.ra__lte:
        request_args['ra__lte'] = f'{_args.ra__lte}'
    if _args.dec__gte:
        request_args['dec__gte'] = f'{_args.dec__gte}'
    if _args.dec__lte:
        request_args['dec__lte'] = f'{_args.dec__lte}'
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
        query = session.query(TnsQ3cRecord)
        if _args.verbose:
            print(f'query = {query}')
        query = tns_q3c_orm_filters(query, request_args)
        if _args.verbose:
            print(f'query = {query}')
    except Exception as _e2:
        raise Exception(f"failed to execute query, error='{_e2}'")

    # report output
    print(f"#{','.join(_ for _ in TNS_HEADERS)}")
    for _e in TnsQ3cRecord.serialize_list(query.all()):
        if verify_keys(_e, set(TNS_HEADERS)):
            print(f"{','.join(str(_e[_l]) for _l in TNS_HEADERS)}")


# +
# main()
# -
if __name__ == '__main__':

    # noinspection PyTypeChecker
    _p = argparse.ArgumentParser(description=f'Query TNS Q3C', formatter_class=argparse.RawTextHelpFormatter)

    # database query argument(s)
    _p.add_argument(f'--astrocone', help=f'Astrocone search [name,radius (deg)]')
    _p.add_argument(f'--cone', help=f'Cone search [ra (deg),dec (deg),radius (deg)]')
    _p.add_argument(f'--ellipse', help=f'Ellipse search [ra (deg),dec (deg),major_axis,axis_ratio,pos_angle (deg)]')
    _p.add_argument(f'--tid', help=f'tid <int>')
    _p.add_argument(f'--name', help=f'name like <str>')
    _p.add_argument(f'--report', help=f'Reporters or group like <str>')
    _p.add_argument(f'--ra__gte', help=f'RA (deg) >= <float>')
    _p.add_argument(f'--ra__lte', help=f'RA (deg) <= <float>')
    _p.add_argument(f'--dec__gte', help=f'Dec (deg) >= <float>')
    _p.add_argument(f'--dec__lte', help=f'Dec (deg) <= <float>')
    _p.add_argument(f'--z__gte', help=f'Redshift >= <float>')
    _p.add_argument(f'--z__lte', help=f'Redshift <= <float>')
    _p.add_argument(f'--sort_order', help=f"Sort order, one of {TNS_SORT_ORDER}")
    _p.add_argument(f'--sort_value', help=f"Sort value, one of {TNS_SORT_VALUE}")

    # non-database query argument(s)
    _p.add_argument(f'--catalog', default=False, action='store_true', help=f'if present, download the data catalog')
    _p.add_argument(f'--paper', default=False, action='store_true', help=f'if present, download the science paper')
    _p.add_argument(f'--text', default=False, action='store_true', help=f'if present, describe the catalog')
    _p.add_argument(f'--verbose', default=False, action='store_true', help=f'if present, produce more verbose output')
    _a = _p.parse_args()

    # execute
    try:
        tns_q3c_orm_cli(_args=_a)
    except Exception as _:
        if bool(_a.verbose):
            print(f"{_}")
        print(f"Use: {__doc__}")
