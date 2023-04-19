#!/usr/bin/env python3


# +
# import(s)
# -
from sassy_q3c_models.ps1_q3c_orm_filters import *


# +
# __doc__ string
# -
__doc__ = """ python3 ps1_q3c_orm_cli.py --help """


DB_HOST = 'localhost'
DB_PORT = 5432
DB_NAME = 'sassy'
DB_USER = 'sassy'
DB_PASS = 'SASSy_520'


# +
# __text__
# -
__text__ = """
pid            bigint      Database (local) identifier.
objid          bigint      The main PS1 source identifier, should be used to match with other 
                           PS1 tables (see F16). Not unique.
psps_objid     bigint      A unique PS1 source identifier, can be used to match with MeanObject 
                           and ObjectThin (see F16).
ra             float       The PS1 J2000 equatorial right ascension coordinate of the source, 
                           in degrees (see F16).
dec            float       The PS1 J2000 equatorial declination coordinate of the source, in degrees (see F16).
l              float       The PS1 J2000 Galactic longitude coordinate of the source, in degrees (see F16).
b              float       The PS1 J2000 Galactic latitude coordinate of the source, in degrees (see F16).
obj_class      varchar[8]  The class assigned to the source, using the fiducial decision boundary b=0.7 
                           (see Sect. 4.1 of B20). Can take the following values: "GALAXY", "STAR", "QSO" or "UNSURE".
prob_galaxy    float       The probability-like neural network output for the galaxy class. Corresponds to the 
                           P_{class} general notation in the text. Refer to Sect. 4.1 of B20 for more details.
prob_star      float       The probability-like neural network output for the star class. Corresponds to the 
                           P_{class} general notation in the text. Refer to Sect. 4.1 of B20 for more details.
prob_qso       float       The probability-like neural network output for the quasar class. Corresponds to the 
                           P_{class} general notation in the text. Refer to Sect. 4.1 of B20 for more details.
extra_class    int         The extrapolation flag for the classification, 0 if non-extrapolated, 1 if extrapolated. 
                           Definition: d_{SOM} > 1.562 (see Sect. 3.3 of B20).
celld_class    int         The distance to the nearest SOM cell centre in the classification SOM. 
                           Denoted d_{SOM} in the text (see Sect. 3.3 of B20).
cellid_Class   int         The identifier of the nearest SOM cell in the classification SOM (see Sect. 3.3 of B20).
z_phot         float       The Monte-Carlo photometric redshift estimate z_{phot}. Slightly less accurate than 
                           z_{phot,0}. Refer to Sect. 3.4 and 4.2 of B20 for more details.
z_err          float       The calibrated redshift error estimate \tilde{\Delta z}_{phot} = 1.986 \Delta z_{phot}. 
                           Refer to Sect. 3.4 and 4.2 of B20 for more details.
z_zero         float       The base photometric redshift estimate z_{phot,0}. Refer to Sect. 3.4 and 4.2 of B20 
                           for more details.
extra_photoz   int         The extrapolation flag for the photo-z estimation, 0 if non-extrapolated, 1 if extrapolated. 
                           Definition:  d_{SOM} > 1.246 (see Sect. 3.3 of B20).
celld_photoz   float       The distance to the nearest SOM cell centre in the photo-z SOM. Denoted d_{SOM} in the text 
                           (see Sect. 3.3 of B20).
cellid_photoz  int         The identifier of the nearest SOM cell in the photo-z SOM (see Sect. 3.3 of B20).
ps_score       float       The machine learning score (ps_score) computed by Tachibana & Miller 2018, 
                           where a score of 0 corresponds to extended sources and 1 corresponds to point sources.
"""

# +
# function: ps1_q3c_orm_cli()
# -
# noinspection PyBroadException
def ps1_q3c_orm_cli(_args: Any = None):

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
    if _args.pid:
        request_args['pid'] = f'{_args.pid}'
    if _args.objid:
        request_args['objid'] = f'{_args.objid}'
    if _args.psps_objid:
        request_args['psps_objid'] = f'{_args.psps_objid}'
    if _args.ra__gte:
        request_args['ra__gte'] = f'{_args.ra__gte}'
    if _args.ra__lte:
        request_args['ra__lte'] = f'{_args.ra__lte}'
    if _args.dec__gte:
        request_args['dec__gte'] = f'{_args.dec__gte}'
    if _args.dec__lte:
        request_args['dec__lte'] = f'{_args.dec__lte}'
    if _args.ps_score__gte:
        request_args['ps_score__gte'] = f'{_args.ps_score__gte}'
    if _args.ps_score__lte:
        request_args['ps_score__lte'] = f'{_args.ps_score__lte}'

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
        query = session.query(Ps1Q3cRecord)
        if _args.verbose:
            print(f'query = {query}')
        query = ps1_q3c_orm_filters(query, request_args)
        if _args.verbose:
            print(f'query = {query}')
    except Exception as _e2:
        raise Exception(f"failed to execute query, error='{_e2}'")

    # report output alphabetically
    print(f"#{','.join(_ for _ in PS1_HEADERS)}")
    for _e in Ps1Q3cRecord.serialize_list(query.all()):
        print(f"{','.join(str(_e[_l]) for _l in PS1_HEADERS)}")


# +
# main()
# -
if __name__ == '__main__':

    # noinspection PyTypeChecker
    _p = argparse.ArgumentParser(description=f'Query Ps1Q3c', formatter_class=argparse.RawTextHelpFormatter)

    # database query argument(s)
    _p.add_argument(f'--astrocone', help=f'Astrocone search [name,radius (deg)]')
    _p.add_argument(f'--cone', help=f'Cone search [ra (deg),dec (deg),radius (deg)]')
    _p.add_argument(f'--ellipse', help=f'Ellipse search [ra (deg),dec (deg),major_axis,axis_ratio,pos_angle (deg)]')
    _p.add_argument(f'--pid', help=f'pid <int>')
    _p.add_argument(f'--objid', help=f'Object Identifier <bigint>')
    _p.add_argument(f'--psps_objid', help=f'PS1 Identifier <bigint>')
    _p.add_argument(f'--ra__gte', help=f'RA >= <float>')
    _p.add_argument(f'--ra__lte', help=f'RA <= <float>')
    _p.add_argument(f'--dec__gte', help=f'Dec >= <float>')
    _p.add_argument(f'--dec__lte', help=f'Dec <= <float>')
    _p.add_argument(f'--ps_score__gte', help=f'Machine Learning Score >= <float>')
    _p.add_argument(f'--ps_score__lte', help=f'Machine Learning Score <= <float>')
    _p.add_argument(f'--sort_order', help=f"Sort order, one of {PS1_SORT_ORDER}")
    _p.add_argument(f'--sort_value', help=f"Sort value, one of {PS1_SORT_VALUE}")

    # non-database query argument(s)
    _p.add_argument(f'--text', default=False, action='store_true', help=f'if present, describe the catalog')
    _p.add_argument(f'--verbose', default=False, action='store_true', help=f'if present, produce more verbose output')
    _a = _p.parse_args()

    # execute
    try:
        ps1_q3c_orm_cli(_args=_a)
    except Exception as _:
        print(f"{_}\nUse: {__doc__}")
