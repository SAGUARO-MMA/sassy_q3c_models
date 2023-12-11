#!/usr/bin/env python3


# +
# import(s)
# -
from sassy_q3c_models.gaiadr3variable_q3c_orm_filters import *


# +
# __doc__ string
# -
__doc__ = """ python3 gaiadr3variable_q3c_orm_cli.py --help """


# +
# __text__
# -
__text__ = """
"""


# +
# function: gaiadr3variable_q3c_orm_cli()
# -
# noinspection PyBroadException
def gaiadr3variable_q3c_orm_cli(_args: Any = None):

    # check input(s)
    if _args is None:
        raise Exception('Invalid arguments')

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
    if request_args.get('gid'):
        request_args['gid'] = f'{_args.gid}'
    if request_args.get('name'):
        request_args['name'] = f'{_args.name}'
    if request_args.get('ra__gte'):
        request_args['ra__gte'] = f'{_args.ra__gte}'
    if request_args.get('ra__lte'):
        request_args['ra__lte'] = f'{_args.ra__lte}'
    if request_args.get('dec__gte'):
        request_args['dec__gte'] = f'{_args.dec__gte}'
    if request_args.get('dec__lte'):
        request_args['dec__lte'] = f'{_args.dec__lte}'
    if request_args.get('median_g__gte'):
        request_args['median_g__gte'] = f'{_args.median_g__gte}'
    if request_args.get('median_g__lte'):
        request_args['median_g__lte'] = f'{_args.median_g__lte}'
    if request_args.get('mean_g__gte'):
        request_args['mean_g__gte'] = f'{_args.mean_g__gte}'
    if request_args.get('mean_g__lte'):
        request_args['mean_g__lte'] = f'{_args.mean_g__lte}'

    if request_args.get('median_bp__gte'):
        request_args['median_bp__gte'] = f'{_args.median_bp__gte}'
    if request_args.get('median_bp__lte'):
        request_args['median_bp__lte'] = f'{_args.median_bp__lte}'
    if request_args.get('mean_bp__gte'):
        request_args['mean_bp__gte'] = f'{_args.mean_bp__gte}'
    if request_args.get('mean_bp__lte'):
        request_args['mean_bp__lte'] = f'{_args.mean_bp__lte}'
    if request_args.get('median_rp__gte'):
        request_args['median_rp__gte'] = f'{_args.median_rp__gte}'
    if request_args.get('median_rp__lte'):
        request_args['median_rp__lte'] = f'{_args.median_rp__lte}'
    if request_args.get('mean_rp__gte'):
        request_args['mean_rp__gte'] = f'{_args.mean_rp__gte}'
    if request_args.get('mean_rp__lte'):
        request_args['mean_rp__lte'] = f'{_args.mean_rp__lte}'

    if request_args.get('stetson_g__gte'):
        request_args['stetson_g__gte'] = f'{_args.stetson_g__gte}'
    if request_args.get('stetson_g__lte'):
        request_args['stetson_g__lte'] = f'{_args.stetson_g__lte}'
    if request_args.get('stetson_bp__gte'):
        request_args['stetson_bp__gte'] = f'{_args.stetson_bp__gte}'
    if request_args.get('stetson_bp__lte'):
        request_args['stetson_bp__lte'] = f'{_args.stetson_bp__lte}'
    if request_args.get('stetson_rp__gte'):
        request_args['stetson_rp__gte'] = f'{_args.stetson_rp__gte}'
    if request_args.get('stetson_rp__lte'):
        request_args['stetson_rp__lte'] = f'{_args.stetson_rp__lte}'

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
        query = session.query(GaiaDR3VariableQ3cRecord)
        if _args.verbose:
            print(f'query = {query}')
        query = gaiadr3variable_q3c_orm_filters(query, request_args)
        if _args.verbose:
            print(f'query = {query}')
    except Exception as _e2:
        raise Exception(f"failed to execute query, error='{_e2}'")

    # report output
    print(f"#{','.join(_ for _ in GAIADR3VARIABLE_HEADERS)}")
    for _e in GaiaDR3VariableQ3cRecord.serialize_list(query.all()):
        if verify_keys(_e, set(GAIADR3VARIABLE_HEADERS)):
            print(f"{','.join(str(_e[_l]) for _l in GAIADR3VARIABLE_HEADERS)}")


# +
# main()
# -
if __name__ == '__main__':

    # noinspection PyTypeChecker
    _p = argparse.ArgumentParser(description=f'Query GaiaDR3VariableQ3c', formatter_class=argparse.RawTextHelpFormatter)

    # database query argument(s)
    _p.add_argument(f'--astrocone', help=f'Astrocone search [name,radius (deg)]')
    _p.add_argument(f'--cone', help=f'Cone search [ra (deg),dec (deg),radius (deg)]')
    _p.add_argument(f'--ellipse', help=f'Ellipse search [ra (deg),dec (deg),major_axis,axis_ratio,pos_angle (deg)]')

    _p.add_argument(f'--gid', help=f'Database ID <int>')
    _p.add_argument(f'--name', help=f'Name like <str>')
    _p.add_argument(f'--ra__gte', help=f'RA (deg) >= <float>')
    _p.add_argument(f'--ra__lte', help=f'RA (deg) <= <float>')
    _p.add_argument(f'--dec__gte', help=f'Dec (deg) >= <float>')
    _p.add_argument(f'--dec__lte', help=f'Dec (deg) <= <float>')
    _p.add_argument(f'--median_g__gte', help=f'Median g (mag) >= <float>')
    _p.add_argument(f'--median_g__lte', help=f'Median g (mag) <= <float>')
    _p.add_argument(f'--mean_g__gte', help=f'Mean g (mag) >= <float>')
    _p.add_argument(f'--mean_g__lte', help=f'Mean g (mag) <= <float>')
    _p.add_argument(f'--median_bp__gte', help=f'Median bp (mag) >= <float>')
    _p.add_argument(f'--median_bp__lte', help=f'Median bp (mag) <= <float>')
    _p.add_argument(f'--mean_bp__gte', help=f'Mean bp (mag) >= <float>')
    _p.add_argument(f'--mean_bp__lte', help=f'Mean bp (mag) <= <float>')
    _p.add_argument(f'--median_rp__gte', help=f'Median rp (mag) >= <float>')
    _p.add_argument(f'--median_rp__lte', help=f'Median rp (mag) <= <float>')
    _p.add_argument(f'--mean_rp__gte', help=f'Mean rp (mag) >= <float>')
    _p.add_argument(f'--mean_rp__lte', help=f'Mean rp (mag) <= <float>')
    _p.add_argument(f'--stetson_g__gte', help=f'Stetson g (mag) >= <float>')
    _p.add_argument(f'--stetson_g__lte', help=f'Stetson g (mag) <= <float>')
    _p.add_argument(f'--stetson_bp__gte', help=f'Stetson bp (mag) >= <float>')
    _p.add_argument(f'--stetson_bp__lte', help=f'Stetson bp (mag) <= <float>')
    _p.add_argument(f'--stetson_rp__gte', help=f'Stetson rp (mag) >= <float>')
    _p.add_argument(f'--stetson_rp__lte', help=f'Stetson rp (mag) <= <float>')

    _p.add_argument(f'--sort_order', help=f"Sort order, one of {GAIADR3VARIABLE_SORT_ORDER}")
    _p.add_argument(f'--sort_value', help=f"Sort value, one of {GAIADR3VARIABLE_SORT_VALUE}")

    # non-database query argument(s)
    _p.add_argument(f'--text', default=False, action='store_true', help=f'if present, describe the catalog')
    _p.add_argument(f'--verbose', default=False, action='store_true', help=f'if present, produce more verbose output')
    _a = _p.parse_args()

    # execute
    try:
        gaiadr3variable_q3c_orm_cli(_args=_a)
    except Exception as _:
        if bool(_a.verbose):
            print(f"{_}")
        print(f"Use: {__doc__}")
