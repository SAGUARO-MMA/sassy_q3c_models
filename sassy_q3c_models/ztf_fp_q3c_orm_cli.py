#!/usr/bin/env python3


# +
# import(s)
# -
from sassy_q3c_models.ztf_fp_q3c_orm_filters import *


# +
# __doc__ string
# -
__doc__ = """ python3 ztf_fp_q3c_orm_cli.py --help """


# +
# __text__
# -
__text__ = """
ZtfFpQ3cRecord
--------------

Column              Description
------------------------------------------------------------------------------------------------------
fpid                Database index
candid              Candidate identifier
oid                 ZTF Object identifier
field               ZTF field ID
rcid                Readout channel ID [00 .. 63]
fid                 Filter ID (1=g; 2=R; 3=i)
pid                 Processing ID for image
rfid                Processing ID for reference image to facilitate archive retrieval
sciinpseeing        Effective FWHM of sci image [pixels]
scibckgnd           Background level in sci image [DN]
scisigpix           Robust sigma per pixel in sci image [DN]
magzpsci            Magnitude zero point for photometry estimates [mag]
magzpsciunc         Magnitude zero point uncertainty (in magzpsci) [mag]
magzpscirms         RMS (deviation from average) in all differences between instrumental photometry and 
                    matched photometric calibrators from science image processing [mag]
clrcoeff            Color coefficient from linear fit from photometric calibration of science image
clrcounc            Color coefficient uncertainty from linear fit (corresponding to clrcoeff)
exptime             Integration time of camera exposure [sec]
adpctdif1           Full science image astrometric RMS along R.A. with respect to Gaia1 [arcsec]
adpctdif2           Full science image astrometric RMS along Dec. with respect to Gaia1 [arcsec]
diffmaglim          Expected 5-sigma mag limit in difference image based on global noise estimate [mag]
programid           Program ID: encodes either public, collab, or caltech mode
jd                  Observation Julian date at start of exposure [days]
forcediffimflux     Forced difference image PSF-fit flux [DN]
forcediffimfluxunc  1-sigma uncertainty in forcediffimflux [DN]
procstatus          Forced photometry processing status codes (0 => no warnings); see documentation
distnr              Distance to nearest source in reference image PSF-catalog [arcsec]
ranr                Right Ascension of nearest source in reference image PSF-catalog; J2000 [deg]
decnr               Declination of nearest source in reference image PSF-catalog; J2000 [deg]
magnr               Magnitude of nearest source in reference image PSF-catalog [mag]
sigmagnr            1-sigma uncertainty in magnr [mag]
chinr               DAOPhot chi parameter of nearest source in reference image PSF-catalog
sharpnr             DAOPhot sharp parameter of nearest source in reference image PSF-catalog
------------------------------------------------------------------------------------------------------
"""


# +
# function: ztf_fp_q3c_orm_cli()
# -
# noinspection PyBroadException
def ztf_fp_q3c_orm_cli(_args: Any = None):

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
    if _args.fpid:
        request_args['fpid'] = f'{_args.fpid}'
    if _args.candid:
        request_args['candid'] = f'{_args.candid}'
    if _args.oid:
        request_args['oid'] = f'{_args.oid}'
    if _args.field:
        request_args['field'] = f'{_args.field}'
    if _args.fid:
        request_args['fid'] = f'{_args.fid}'
    if _args.jd__gte:
        request_args['jd__gte'] = f'{_args.jd__gte}'
    if _args.jd__lte:
        request_args['jd__lte'] = f'{_args.jd__lte}'

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
        query = session.query(ZtfFpQ3cRecord)
        if _args.verbose:
            print(f'query = {query}')
        query = ztf_fp_q3c_orm_filters(query, request_args)
        if _args.verbose:
            print(f'query = {query}')
    except Exception as _e2:
        raise Exception(f"failed to execute query, error='{_e2}'")

    # report output alphabetically
    print(f"#{','.join(_ for _ in ZTF_FP_Q3C_HEADERS)}")
    for _e in ZtfFpQ3cRecord.serialize_list(query.all()):
        print(f"{','.join(str(_e[_]) for _ in ZTF_FP_Q3C_HEADERS)}")


# +
# main()
# -
if __name__ == '__main__':

    # noinspection PyTypeChecker
    _p = argparse.ArgumentParser(description=f'Query ZtfFpQ3c', formatter_class=argparse.RawTextHelpFormatter)

    # database query argument(s)
    _p.add_argument(f'--astrocone', help=f'Astrocone search [name,radius (deg)]')
    _p.add_argument(f'--cone', help=f'Cone search [ra (deg),dec (deg),radius (deg)]')
    _p.add_argument(f'--ellipse', help=f'Ellipse search [ra (deg),dec (de),major_axis,axis_ratio,pos_angle (deg)]')
    _p.add_argument(f'--candid', help=f'fpid <int>')
    _p.add_argument(f'--oid', help=f'oid <str>')
    _p.add_argument(f'--fpid', help=f'fpid <int>')
    _p.add_argument(f'--field', help=f'field <int>')
    _p.add_argument(f'--fid', help=f'fid <int>')
    _p.add_argument(f'--jd__gte', help=f'JD <= <float>')
    _p.add_argument(f'--jd__lte', help=f'JD <= <float>')
    _p.add_argument(f'--sort_order', help=f"Sort order, one of {ZTF_FP_Q3C_SORT_ORDER}")
    _p.add_argument(f'--sort_value', help=f"Sort value, one of {ZTF_FP_Q3C_SORT_VALUE}")

    # non-database query argument(s)
    _p.add_argument(f'--text', default=False, action='store_true', help=f'if present, describe the catalog')
    _p.add_argument(f'--verbose', default=False, action='store_true', help=f'if present, produce more verbose output')
    _a = _p.parse_args()

    # execute
    try:
        ztf_fp_q3c_orm_cli(_args=_a)
    except Exception as _:
        print(f"{_}\n{__doc__}")
