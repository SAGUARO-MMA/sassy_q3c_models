#!/usr/bin/env python3


# +
# import(s)
# -
from sassy_q3c_models.sassy_cron_q3c_orm_filters import *


# +
# __doc__ string
# -
__doc__ = """ python3 sassy_cron_q3c_orm_cli.py --help """


# +
# __text__
# -
__text__ = """
+------------------+-----------------------------+
|     Column       |            Type             |
+------------------+-----------------------------+
|zoid              | character varying(64)       |
|zjd               | double precision            |
|zmagap            | double precision            |
|zmagpsf           | double precision            |
|zmagdiff          | double precision            |
|zfid              | integer                     |
|zdrb              | double precision            |
|zrb               | double precision            |
|zsid              | integer                     |
|zcandid           | bigint                      |
|zssnamenr         | character varying(128)      |
|zra               | double precision            |
|zdec              | double precision            |
|gid               | integer                     |
|gra               | double precision            |
|gdec              | double precision            |
|gz                | double precision            |
|gdist             | double precision            |
|gsep              | double precision            |
|tid               | integer                     |
|objid             | integer                     |
|name_prefix       | character varying(4)        |
|name              | character varying(32)       |
|ra                | double precision            |
|declination       | double precision            |
|redshift          | double precision            |
|typeid            | integer                     |
|objtype           | character varying(32)       |
|reporting_groupid | integer                     |
|reporting_group   | character varying(32)       |
|source_groupid    | integer                     |
|source_group      | character varying(32)       |
|discoverydate     | timestamp without time zone |
|discoverymag      | double precision            |
|discmagfilter     | integer                     |
|filtername        | character varying(8)        |
|reporters         | character varying(2048)     |
|time_received     | timestamp without time zone |
|internal_names    | character varying(256)      |
|creationdate      | timestamp without time zone |
|lastmodified      | timestamp without time zone |
|class_name        | character varying(64)       |
|class_prob        | double precision            |
|dpng              | character varying(200)      |
|spng              | character varying(200)      |
|tpng              | character varying(200)      |
+------------------+-----------------------------+
"""


# +
# function: sassy_cron_q3c_orm_cli()
# -
# noinspection PyBroadException
def sassy_cron_q3c_orm_cli(_args: Any = None):

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
    if _args.class_name:
        request_args['class_name'] = f'{_args.class_name}'
    if _args.gdist__gte:
        request_args['gdist__gte'] = f'{_args.gdist__gte}'
    if _args.gdist__lte:
        request_args['gdist__lte'] = f'{_args.gdist__lte}'
    if _args.gsep__gte:
        request_args['gsep__gte'] = f'{_args.gsep__gte}'
    if _args.gsep__lte:
        request_args['gsep__lte'] = f'{_args.gsep__lte}'
    if _args.gz__gte:
        request_args['gz__gte'] = f'{_args.gz__gte}'
    if _args.gz__lte:
        request_args['gz__lte'] = f'{_args.gz__lte}'
    if _args.zoid:
        request_args['zoid'] = f'{_args.zoid}'
    if _args.zfid:
        request_args['zfid'] = f'{_args.zfid}'
    if _args.zra__gte:
        request_args['zra__gte'] = f'{_args.zra__gte}'
    if _args.zra__lte:
        request_args['zra__lte'] = f'{_args.zra__lte}'
    if _args.zdec__gte:
        request_args['zdec__gte'] = f'{_args.zdec__gte}'
    if _args.zdec__lte:
        request_args['zdec__lte'] = f'{_args.zdec__lte}'

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
        query = session.query(SassyCronQ3cRecord)
        if _args.verbose:
            print(f'query = {query}')
        query = sassy_cron_q3c_orm_filters(query, request_args)
        if _args.verbose:
            print(f'query = {query}')
    except Exception as _e2:
        raise Exception(f"failed to execute query, error='{_e2}'")

    # report output
    print(f"#{','.join(_ for _ in SASSY_CRON_HEADERS)}")
    for _e in SassyCronQ3cRecord.serialize_list(query.all()):
        if verify_keys(_e, set(SASSY_CRON_HEADERS)):
            print(f"{','.join(str(_e[_l]) for _l in SASSY_CRON_HEADERS)}")


# +
# main()
# -
if __name__ == '__main__':

    # noinspection PyTypeChecker
    _p = argparse.ArgumentParser(description=f'Query SassyCron', formatter_class=argparse.RawTextHelpFormatter)

    # database query argument(s)
    _p.add_argument(f'--astrocone', help=f'Astrocone search [name,radius (deg)]')
    _p.add_argument(f'--cone', help=f'Cone search [ra (deg),dec (deg),radius (deg)]')
    _p.add_argument(f'--ellipse', help=f'Ellipse search [ra (deg),dec (deg),major_axis,axis_ratio,pos_angle (deg)]')
    _p.add_argument(f'--class_name', help=f'class name like <str>')
    _p.add_argument(f'--gdist__gte', help=f'Distance >= <float>')
    _p.add_argument(f'--gdist__lte', help=f'Distance >= <float>')
    _p.add_argument(f'--gsep__gte', help=f'Separation <= <float>')
    _p.add_argument(f'--gsep__lte', help=f'Separation <= <float>')
    _p.add_argument(f'--gz__gte', help=f'Redshift >= <float>')
    _p.add_argument(f'--gz__lte', help=f'Redshift <= <float>')
    _p.add_argument(f'--zoid', help=f'ZTF name like <str>')
    _p.add_argument(f'--zfid', help=f'ZTF filter number <int>')
    _p.add_argument(f'--zra__gte', help=f'RA (deg) >= <float>')
    _p.add_argument(f'--zra__lte', help=f'RA (deg) <= <float>')
    _p.add_argument(f'--zdec__gte', help=f'Dec (deg) >= <float>')
    _p.add_argument(f'--zdec__lte', help=f'Dec (deg) <= <float>')
    _p.add_argument(f'--sort_order', help=f"Sort order, one of {SASSY_CRON_SORT_ORDER}")
    _p.add_argument(f'--sort_value', help=f"Sort value, one of {SASSY_CRON_SORT_VALUE}")

    # non-database query argument(s)
    _p.add_argument(f'--text', default=False, action='store_true', help=f'if present, describe the catalog')
    _p.add_argument(f'--verbose', default=False, action='store_true', help=f'if present, produce more verbose output')
    _a = _p.parse_args()

    # execute
    try:
        sassy_cron_q3c_orm_cli(_args=_a)
    except Exception as _:
        if bool(_a.verbose):
            print(f"{_}")
        print(f"Use: {__doc__}")
