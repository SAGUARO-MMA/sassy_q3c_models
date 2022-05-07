#!/usr/bin/env python3


# +
# import(s)
# -
from sassy_q3c_models.non_detections_orm_filters import *


# +
# __doc__ string
# -
__doc__ = """ python3 non_detections_orm_cli.py --help """


# +
# __text__
# -
__text__ = """
NonDetectionsRecord
-------------------

Column         Description
-----------------------------------------
nid            database index
oid            object identifier
diffmaglim     non-detections magnitude
jd             julian date of observation
fid            filter number
"""


# +
# function: non_detections_orm_cli()
# -
# noinspection PyBroadException
def non_detections_orm_cli(_args: Any = None):

    # check input(s)
    if _args is None:
        raise Exception('Invalid arguments')

    # if --text is present, describe of the catalog
    if _args.text:
        return print(__text__)

    # get input(s)
    request_args = {}
    if _args.nid:
        request_args['nid'] = f'{_args.nid}'
    if _args.oid:
        request_args['oid'] = f'{_args.oid}'
    if _args.diffmaglim__gte:
        request_args['diffmaglim__gte'] = f'{_args.diffmaglim__gte}'
    if _args.diffmaglim__lte:
        request_args['diffmaglim__lte'] = f'{_args.diffmaglim__lte}'
    if _args.jd__gte:
        request_args['jd__gte'] = f'{_args.jd__gte}'
    if _args.jd__lte:
        request_args['jd__lte'] = f'{_args.jd__lte}'
    if _args.fid:
        request_args['fid'] = f'{_args.fid}'

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
        query = session.query(NonDetectionsRecord)
        if _args.verbose:
            print(f'query = {query}')
        query = non_detections_orm_filters(query, request_args)
        if _args.verbose:
            print(f'query = {query}')
    except Exception as _e2:
        raise Exception(f"failed to execute query, error='{_e2}'")

    # report output alphabetically
    print(f"#{','.join(_ for _ in NON_DETECTIONS_HEADERS)}")
    for _e in NonDetectionsRecord.serialize_list(query.all()):
        if 'candidate' in _e and verify_keys(_e['candidate'], set(NON_DETECTIONS_HEADERS)):
            print(f"{','.join(str(_e['candidate'][_l]) for _l in NON_DETECTIONS_HEADERS)}")


# +
# main()
# -
if __name__ == '__main__':

    # noinspection PyTypeChecker
    _p = argparse.ArgumentParser(description=f'Query NonDetections', formatter_class=argparse.RawTextHelpFormatter)

    # database query argument(s)
    _p.add_argument(f'--nid', help=f'nid <int>')
    _p.add_argument(f'--oid', help=f'oid <str>')
    _p.add_argument(f'--diffmaglim__gte', help=f'DiffMagLim <= <float>')
    _p.add_argument(f'--diffmaglim__lte', help=f'DiffMagLim <= <float>')
    _p.add_argument(f'--jd__gte', help=f'JD <= <float>')
    _p.add_argument(f'--jd__lte', help=f'JD <= <float>')
    _p.add_argument(f'--fid', help=f'fid <int>')
    _p.add_argument(f'--sort_order', help=f"Sort order, one of {NON_DETECTIONS_SORT_ORDER}")
    _p.add_argument(f'--sort_value', help=f"Sort value, one of {NON_DETECTIONS_SORT_VALUE}")

    # non-database query argument(s)
    _p.add_argument(f'--text', default=False, action='store_true', help=f'if present, describe the catalog')
    _p.add_argument(f'--verbose', default=False, action='store_true', help=f'if present, produce more verbose output')
    _a = _p.parse_args()

    # execute
    try:
        non_detections_orm_cli(_args=_a)
    except Exception as _:
        if bool(_a.verbose):
            print(f"{_}")
        print(f"Use: {__doc__}")
