#!/usr/bin/env python3


# +
# import(s)
# -
from sassy_q3c_models.desi_spec_q3c_orm_filters import *


# +
# __doc__ string
# -
__doc__ = """python3 desi_spec_q3c_orm_cli.py --help"""


# +
# constant(s)
# -
ARXIV_PDF_URL = DESI_SPEC_PDF_URL
ARXIV_PDF_FIL = DESI_SPEC_PDF_URL.split("/")[-1]
ARXIV_DAT_URL = DESI_SPEC_DAT_URL
ARXIV_DAT_FIL = DESI_SPEC_DAT_URL.split("/")[-1]


# +
# __text__
# -
__text__ = """
    TARGETID                   | int64       | None         | ID (unique to file? and the whole survey?)
    SURVEY                     | char[7]     | None         | Survey name
    PROGRAM                    | char[6]     | None         | DESI program type - BRIGHT, DARK, BACKUP, OTHER
    HEALPIX                    | int32       | None         | HEALPixel containing this location at NSIDE=64 in the NESTED scheme
    SPGRPVAL                   | int32       | None         | Value by which spectra are grouped for a coadd (e.g. a YEARMMDD night)
    Z                          | float64     | None         | Redshift measured by Redrock
    ZERR                       | float64     | None         | Redshift error from redrock
    ZWARN                      | int64       | None         | Redshift warning bitmask from Redrock
    CHI2                       | float64     | None         | Best fit chi squared
    COEFF                      | float64[10] | None         | Redrock template coefficients
    NPIXELS                    | int64       | None         | Number of unmasked pixels contributing to the Redrock fit
    SPECTYPE                   | char[6]     | None         | Spectral type of Redrock best fit template (e.g. GALAXY, QSO, STAR)
    SUBTYPE                    | char[20]    | None         | Spectral subtype
    NCOEFF                     | int64       | None         | Number of Redrock template coefficients
    DELTACHI2                  | float64     | None         | chi2 difference between first- and second-best redrock template fits
    COADD_FIBERSTATUS          | int32       | None         | bitwise-AND of input FIBERSTATUS
    TARGET_RA                  | float64     | deg          | Barycentric Right Ascension in ICRS
    TARGET_DEC                 | float64     | deg          | Barycentric Declination in ICRS
    PMRA                       | float32     | mas yr^-1    | Reference catalog proper motion in the RA direction
    PMDEC                      | float32     | mas yr^-1    | Reference catalog proper motion in the Dec direction
    REF_EPOCH                  | float32     | yr           | Reference catalog reference epoch (e.g., 2015.5 for Gaia DR2)
    FA_TARGET                  | int64       | None         | Targeting bit internally used by fiberassign (linked with FA_TYPE)
    FA_TYPE                    | binary      | None         | Fiberassign internal target type (science, standard, sky, safe, suppsky)
    OBJTYPE                    | char[3]     | None         | Object type: TGT, SKY, NON, BAD
    SUBPRIORITY                | float64     | None         | Random subpriority [0-1] to break assignment ties
    OBSCONDITIONS              | int32       | None         | Flag the target to be observed in graytime
    RELEASE                    | int16       | None         | Legacy Surveys (LS) Release
    BRICKNAME                  | char[8]     | None         | Brick name from tractor input
    BRICKID                    | int32       | None         | Brick ID from tractor input
    BRICK_OBJID                | int32       | None         | OBJID (unique to brick, but not to file)
    MORPHTYPE                  | char[4]     | None         | Morphological Model type
    EBV                        | float32     | mag          | Galactic extinction E(B-V) reddening from SFD98
    FLUX_G                     | float32     | nanomaggy    | LS flux from tractor input (g)
    FLUX_R                     | float32     | nanomaggy    | LS flux from tractor input (r)
    FLUX_Z                     | float32     | nanomaggy    | LS flux from tractor input (z)
    FLUX_W1                    | float32     | nanomaggy    | WISE flux in W1
    FLUX_W2                    | float32     | nanomaggy    | WISE flux in W2
    FLUX_IVAR_G                | float32     | nanomaggy^-2 | Inverse Variance of FLUX_G
    FLUX_IVAR_R                | float32     | nanomaggy^-2 | |Inverse Variance of FLUX_R
    FLUX_IVAR_Z                | float32     | nanomaggy^-2 | Inverse Variance of FLUX_Z
    FLUX_IVAR_W1               | float32     | nanomaggy^-2 | Inverse Variance of FLUX_W1
    FLUX_IVAR_W2               | float32     | nanomaggy^-2 | Inverse Variance of FLUX_W2
    FIBERFLUX_G                | float32     | nanomaggy    | Predicted g-band flux within a fiber of diameter 1.5 arcsec from this object in 1 arcsec Gaussian seeing
    FIBERFLUX_R                | float32     | nanomaggy    | Predicted r-band flux within a fiber of diameter 1.5 arcsec from this object in 1 arcsec Gaussian seeing
    FIBERFLUX_Z                | float32     | nanomaggy    | Predicted z-band flux within a fiber of diameter 1.5 arcsec from this object in 1 arcsec Gaussian seeing
    FIBERTOTFLUX_G             | float32     | nanomaggy    | Predicted g-band flux within a fiber of diameter 1.5 arcsec from all sources at this location in 1 arcsec Gaussian seeing
    FIBERTOTFLUX_R             | float32     | nanomaggy    | Predicted r-band flux within a fiber of diameter 1.5 arcsec from all sources at this location in 1 arcsec Gaussian seeing
    FIBERTOTFLUX_Z             | float32     | nanomaggy    | Predicted z-band flux within a fiber of diameter 1.5 arcsec from all sources at this location in 1 arcsec Gaussian seeing
    MASKBITS                   | int16       | None         | Bitwise mask indicating that an object touches a pixel in the coadd/*/*/*maskbits* maps, as cataloged on the DR9 bitmasks page
    SERSIC                     | float32     | None         | Power-law index for the Sersic profile model (type="SER")
    SHAPE_R                    | float32     | arcsec       | Half-light radius of galaxy model for galaxy type type (>0)
    SHAPE_E1                   | float32     | None         | Ellipticity component 1 of galaxy model for galaxy type type
    SHAPE_E2                   | float32     | None         | Ellipticity component 2 of galaxy model for galaxy type type
    REF_ID                     | int64       | None         | Tyc1*1,000,000+Tyc2*10+Tyc3 for Tycho-2; “sourceid” for Gaia DR2
    REF_CAT                    | char[2]     | None         | Reference catalog source for this star: “T2” for Tycho-2, “G2” for Gaia DR2, “L3” for the SGA, empty otherwise
    GAIA_PHOT_G_MEAN_MAG       | float32     | mag          | Gaia G band magnitude
    GAIA_PHOT_BP_MEAN_MAG      | float32     | mag          | Gaia BP band magnitude
    GAIA_PHOT_RP_MEAN_MAG      | float32     | mag          | Gaia RP band magnitude
    PARALLAX                   | float32     | mas          | Reference catalog parallax
    PHOTSYS                    | char[1]     | None         | ‘N’ for the MzLS/BASS photometric system, ‘S’ for DECaLS
    PRIORITY_INIT              | int64       | None         | Target initial priority from target selection bitmasks and OBSCONDITIONS
    NUMOBS_INIT                | int64       | None         | Initial number of observations for target calculated across target selection bitmasks and OBSCONDITIONS
    CMX_TARGET                 | int64       | None         | Target selection bitmask for commissioning
    SV1_DESI_TARGET            | int64       | None         | DESI (dark time program) target selection bitmask for SV1
    SV1_BGS_TARGET             | int64       | None         | BGS (bright time program) target selection bitmask for SV1
    SV1_MWS_TARGET             | int64       | None         | MWS (bright time program) target selection bitmask for SV1
    SV1_SCND_TARGET            | int64       | None         | Secondary target selection bitmask for SV1
    SV2_DESI_TARGET            | int64       | None         | DESI (dark time program) target selection bitmask for SV2
    SV2_BGS_TARGET             | int64       | None         | BGS (bright time program) target selection bitmask for SV2
    SV2_MWS_TARGET             | int64       | None         | MWS (bright time program) target selection bitmask for SV2
    SV2_SCND_TARGET            | int64       | None         | Secondary target selection bitmask for SV2
    SV3_DESI_TARGET            | int64       | None         | DESI (dark time program) target selection bitmask for SV3
    SV3_BGS_TARGET             | int64       | None         | BGS (bright time program) target selection bitmask for SV3
    SV3_MWS_TARGET             | int64       | None         | MWS (bright time program) target selection bitmask for SV3
    SV3_SCND_TARGET            | int64       | None         | Secondary target selection bitmask for SV3
    DESI_TARGET                | int64       | None         | DESI (dark time program) target selection bitmask
    BGS_TARGET                 | int64       | None         | BGS (bright time program) target selection bitmask
    MWS_TARGET                 | int64       | None         | MWS (bright time program) target selection bitmask
    SCND_TARGET                | int64       | None         | Secondary target selection bitmask
    PLATE_RA                   | float64     | deg          | Barycentric Right Ascension in ICRS to be used by PlateMaker
    PLATE_DEC                  | float64     | deg          | Barycentric Declination in ICRS to be used by PlateMaker
    COADD_NUMEXP               | int16       | None         | Number of exposures in coadd
    COADD_EXPTIME              | float32     | s            | Summed exposure time for coadd
    COADD_NUMNIGHT             | int16       | None         | Number of nights in coadd
    COADD_NUMTILE              | int16       | None         | Number of tiles in coadd
    MEAN_DELTA_X               | float32     | mm           | Mean (over exposures) fiber difference requested - actual CS5 X location on focal plane
    RMS_DELTA_X                | float32     | mm           | RMS (over exposures) of the fiber difference between measured and requested CS5 X location on focal plane
    MEAN_DELTA_Y               | float32     | mm           | Mean (over exposures) fiber difference requested - actual CS5 Y location on focal plane
    RMS_DELTA_Y                | float32     | mm           | RMS (over exposures) of the fiber difference between measured and requested CS5 Y location on focal plane
    MEAN_FIBER_RA              | float64     | deg          | Mean (over exposures) RA of actual fiber position
    STD_FIBER_RA               | float32     | arcsec       | Standard deviation (over exposures) of RA of actual fiber position
    MEAN_FIBER_DEC             | float64     | deg          | Mean (over exposures) DEC of actual fiber position
    STD_FIBER_DEC              | float32     | arcsec       | Standard deviation (over exposures) of DEC of actual fiber position
    MEAN_PSF_TO_FIBER_SPECFLUX | float32     | None         | Mean of input exposures fraction of light from point-like source captured by 1.5 arcsec diameter fiber given atmospheric seeing
    TSNR2_GPBDARK_B            | float32     | None         | template (S/N)^2 for dark targets in guider pass band on B
    TSNR2_ELG_B                | float32     | None         | ELG B template (S/N)^2 
    TSNR2_GPBBRIGHT_B          | float32     | None         | template (S/N)^2 for bright targets in guider pass band on B
    TSNR2_LYA_B                | float32     | None         | LYA B template (S/N)^2
    TSNR2_BGS_B                | float32     | None         | BGS B template (S/N)^2
    TSNR2_GPBBACKUP_B          | float32     | None         | template (S/N)^2 for backup targets in guider pass band on B
    TSNR2_QSO_B                | float32     | None         | QSO B template (S/N)^2
    TSNR2_LRG_B                | float32     | None         | LRG B template (S/N)^2
    TSNR2_GPBDARK_R            | float32     | None         | template (S/N)^2 for dark targets in guider pass band on R
    TSNR2_ELG_R                | float32     | None         | ELG R template (S/N)^2
    TSNR2_GPBBRIGHT_R          | float32     | None         | template (S/N)^2 for bright targets in guider pass band on R
    TSNR2_LYA_R                | float32     | None         | LYA R template (S/N)^2
    TSNR2_BGS_R                | float32     | None         | BGS R template (S/N)^2
    TSNR2_GPBBACKUP_R          | float32     | None         | template (S/N)^2 for backup targets in guider pass band on R
    TSNR2_QSO_R                | float32     | None         | QSO R template (S/N)^2
    TSNR2_LRG_R                | float32     | None         | LRG R template (S/N)^2
    TSNR2_GPBDARK_Z            | float32     | None         | template (S/N)^2 for dark targets in guider pass band on Z
    TSNR2_ELG_Z                | float32     | None         | ELG Z template (S/N)^2
    TSNR2_GPBBRIGHT_Z          | float32     | None         | template (S/N)^2 for bright targets in guider pass band on Z
    TSNR2_LYA_Z                | float32     | None         | LYA Z template (S/N)^2
    TSNR2_BGS_Z                | float32     | None         | BGS Z template (S/N)^2
    TSNR2_GPBBACKUP_Z          | float32     | None         | template (S/N)^2 for backup targets in guider pass band on Z
    TSNR2_QSO_Z                | float32     | None         | QSO Z template (S/N)^2
    TSNR2_LRG_Z                | float32     | None         | LRG Z template (S/N)^2
    TSNR2_GPBDARK              | float32     | None         | template (S/N)^2 for dark targets in guider pass band
    TSNR2_ELG                  | float32     | None         | ELG template (S/N)^2 summed over B,R,Z
    TSNR2_GPBBRIGHT            | float32     | None         | template (S/N)^2 for bright targets in guider pass band
    TSNR2_LYA                  | float32     | None         | LYA template (S/N)^2 summed over B,R,Z
    TSNR2_BGS                  | float32     | None         | BGS template (S/N)^2 summed over B,R,Z
    TSNR2_GPBBACKUP            | float32     | None         | template (S/N)^2 for backup targets in guider pass band
    TSNR2_QSO                  | float32     | None         | QSO template (S/N)^2 summed over B,R,Z
    TSNR2_LRG                  | float32     | None         | LRG template (S/N)^2 summed over B,R,Z
    SV_NSPEC                   | int32       | None         | Number of coadded spectra for this TARGETID in SV (SV1+2+3)
    SV_PRIMARY                 | logical     | None         | Boolean flag (True/False) for the primary coadded spectrum in SV (SV1+2+3)
    ZCAT_NSPEC                 | int16       | None         | Number of times this TARGETID appears in this catalog
    ZCAT_PRIMARY               | logical     | None         | Boolean flag (True/False) for the primary coadded spectrum in this zcatalog"""


# +
# function: desi_spec_q3c_orm_cli()
# -
# noinspection PyBroadException
def desi_spec_q3c_orm_cli(_args: Any = None):

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
    if _args.did:
        request_args['did'] = f'{_args.did}'
    if _args.spectype:
        request_args['spectype'] = f'{_args.spectype}'
    if _args.objtype:
        request_args['objtype'] = f'{_args.objtype}'
    if _args.brickname:
        request_args['brickname'] = f'{_args.brickname}'
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
        query = session.query(DesiSpecQ3cRecord)
        if _args.verbose:
            print(f'query = {query}')
        query = desi_spec_q3c_orm_filters(query, request_args)
        if _args.verbose:
            print(f'query = {query}')
    except Exception as _e2:
        raise Exception(f"failed to execute query, error='{_e2}'")

    # report output alphabetically
    _keys = ['fid'] + DESI_SPEC_KEYS
    print(f"#{','.join(_ for _ in _keys)}")
    for _e in DesiSpecQ3cRecord.serialize_list(query.all()):
        # if verify_keys(_e, set(_keys)):
        print(f"{','.join(str(_e[_l]) for _l in _keys)}")


# +
# main()
# -
if __name__ == '__main__':

    # noinspection PyTypeChecker
    _p = argparse.ArgumentParser(description=f'Query DESI_SPEC Q3C database', formatter_class=argparse.RawTextHelpFormatter)

    # database query argument(s)
    _p.add_argument(f'--astrocone', help=f'Astrocone search [name,radius (deg)]')
    _p.add_argument(f'--cone', help=f'Cone search [ra (deg),dec (deg),radius (deg)]')
    _p.add_argument(f'--ellipse', help=f'Ellipse search [ra (deg),dec (de),major_axis,axis_ratio,pos_angle (deg)]')
    _p.add_argument(f'--did', help=f'did <int>')
    _p.add_argument(f'--spectype', help=f'spectral type <str>')
    _p.add_argument(f'--objtype', help=f'object type <str>')
    _p.add_argument(f'--brickname', help=f'brick name <str>')
    _p.add_argument(f'--ra__gte', help=f'Target RA >= <float>')
    _p.add_argument(f'--ra__lte', help=f'Target RA <= <float>')
    _p.add_argument(f'--dec__gte', help=f'Target Dec >= <float>')
    _p.add_argument(f'--dec__lte', help=f'Target Dec <= <float>')
    _p.add_argument(f'--z__gte', help=f'Redshift >= <float>')
    _p.add_argument(f'--z__lte', help=f'Redshift <= <float>')
    _p.add_argument(f'--sort_order', help=f"Sort order, one of {DESI_SPEC_SORT_ORDER}")
    _p.add_argument(f'--sort_value', help=f"Sort value, one of {DESI_SPEC_SORT_VALUE}")

    # non-database query argument(s)ß
    _p.add_argument(f'--text', default=False, action='store_true', help=f'if present, describe the catalog')
    _p.add_argument(f'--verbose', default=False, action='store_true', help=f'if present, produce more verbose output')
    _a = _p.parse_args()

    # execute
    try:
        desi_spec_q3c_orm_cli(_args=_a)
    except Exception as _:
        if bool(_a.verbose):
            print(f"{_}")
        print(f"Use: {__doc__}")
