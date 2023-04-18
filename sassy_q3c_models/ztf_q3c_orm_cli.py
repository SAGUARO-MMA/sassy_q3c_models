#!/usr/bin/env python3


# +
# import(s)
# -
from sassy_q3c_models.ztf_q3c_orm_filters import *


# +
# __doc__ string
# -
__doc__ = """ % python3 ztf_q3c_orm_cli.py --help """


# +
# constant(s)
# -
ARXIV_PDF_URL = ZTF_PDF_URL
ARXIV_PDF_FIL = ZTF_PDF_URL.split("/")[-1]
ARXIV_DAT_URL = ZTF_DAT_URL
ARXIV_DAT_FIL = ZTF_DAT_URL.split("/")[-1]


# +
# __text__
# -
__text__ = """
ZTF Avro Schemas v3.3

Schema Heirarchy
ZTF uses nested schemas to organize the data in the alert packet.
ztf.alert (defined in alert.avsc) is the top-level namespace. 
ztf.alert in turn relies on candidate.avsc, prv_candidate.avsc, and cutout.avsc.

ztf.alert contains the following fields:

Field              Type                                      Contents
candid             long                                      unique identifier for the subtraction candidate
candidate          ztf.alert.candidate                       candidate record
cutoutScience      ztf.alert.cutout or null                  cutout of the science image
cutoutTemplate     ztf.alert.cutout or null                  cutout of the coadded reference image
cutoutDifference   ztf.alert.cutout or null                  cutout of the resulting difference image
objectId           long                                      unique identifier for this object
publisher          string                                    origin of alert packet
prv_candidates     array of ztf.alert.prv_candidate or null  candidate records for 30 days’ past history
schemavsn          string                                    schema version used

ztf.alert.candidate contains the following fields:

Field              Type                                      Contents
aimage             [float, null], default: null              Windowed profile RMS afloat major axis from SExtractor [pixels]
aimagerat          [float, null], default: null              Ratio: aimage / fwhm
alert_candid       long                                      Not part of schema: unique identifier for the subtraction candidate
avro               string                                    Not part of schema: full pathname of avro file
bimage             [float, null], default: null              Windowed profile RMS afloat minor axis from SExtractor [pixels]
bimagerat          [float, null], default: null              Ratio: bimage / fwhm
candid             long                                      Candidate ID from operations DB
                                                             f or 0 => candidate is from negative (ref minus sci) subtraction
chinr              [float, null], default: null              DAOPhot chi parameter of nearest source in reference image PSF-catalog within 30 arcsec
chipsf             [float, null], default: null              Reduced chi-square for PSF-fit
classtar           [float, null], default: null              Star/Galaxy classification score from SExtractor
clrcoeff           [float, null], default: null              Color coefficient from linear fit from photometric calibration of science image
clrcounc           [float, null], default: null              Color coefficient uncertainty from linear fit (corresponding to clrcoeff)
clrmed             [float, null], default: null              Median color of all PS1 photometric calibrators used from science image processing [mag]
                                                             for filter (fid) = 1, 2, 3, PS1 color used = g-r, g-r, r-i respectively
clrrms             [float, null], default: null              RMS color (deviation from average) of all PS1 photometric calibrators used from science image processing [mag]
cutoutdifference   string                                    Not part of schema: full pathname of difference cutout file
cutoutscience      string                                    Not part of schema: full pathname of science cutout file
cutouttemplate     string                                    Not part of schema: full pathname of temeplate cutout file
dec                double                                    Declination of candidate; J2000 [deg]
decnr              double                                    Declination of nearest source in reference image PSF-catalog; J2000 [deg]
deltamaglatest     double                                    Not part of schema: Most recent delta magnitude
deltamagref        double                                    Not part of schema: Most recent delta magnitude reference
diffmaglim         [float, null], default: null              5-sigma mag limit in difference image based on PSF-fit photometry [mag]
distpsnr1          [float, null], default: null              Distance of closest source from PS1 catalog; if exists within 30 arcsec [arcsec]
distpsnr2          [float, null], default: null              Distance to second closest source from PS1 catalog; if exists within 30 arcsec [arcsec]
distpsnr3          [float, null], default: null              Distance to third closest source from PS1 catalog; if exists within 30 arcsec [arcsec]
distnr             [float, null], default: null              Distance to nearest source in reference image PSF-catalog within 30 arcsec [pixels]
drb                [float, null], default: null              RealBogus quality score from Deep-Learning-based classifier; range is 0 to 1 where closer to 1 is more reliable
drbversion         string                                    Version of Deep-Learning-based classifier model used to assign RealBogus (drb) quality score
dsnrms             [float, null], default: null              Ratio: D/stddev(D) on event position where D = difference image
dsdiff             [float, null], default: null              Difference of statistics: dsnrms - ssnrms
elong              [float, null], default: null              Ratio: aimage / bimage
exptime            [float, null], default: null              Integration time of camera exposure [sec]
fid                int                                       Filter Id (1; 2; 3)
filtername         string                                    Not part of schema: Filter Name (g; r; i)
field              [int, null], default: null                ZTF field ID
fwhm               [float, null], default: null              Full Width Half Max assuming a Gaussian core, from SExtractor [pixels]
gal_b              double                                    Not part of schema: galatic longitude
gal_l              double                                    Not part of schema: galatic latitude
isdiffpos          string                                    t or 1 => candidate is from positive (sci minus ref) subtraction
iso                string                                    Not part of schema: ISOT conversion from JD
jd                 double                                    Observation Julian date at start of exposure [days]
jdendhist          [double, null], default: null             Latest Julian date of epoch corresponding to ndethist [days]
jdendref           double                                    Observation Julian date of latest exposure used to generate reference image [days]
jdstarthist        [double, null], default: null             Earliest Julian date of epoch corresponding to ndethist [days]
jdstartref         double                                    Observation Julian date of earliest exposure used to generate reference image [days]
magap              [float, null], default: null              Aperture mag using 8 pixel diameter aperture [mag]
magapbig           [float, null], default: null              Aperture mag using 18 pixel diameter aperture [mag]
magdiff            [float, null], default: null              Difference: magap - magpsf [mag]
magfromlim         [float, null], default: null              Difference: diffmaglim - magap [mag]
maggaia            [float, null], default: null              Gaia (G-band) magnitude of closest source from Gaia DR1 catalog irrespective of magnitude
                                                             if exists within 90 arcsec [mag]
maggaiabright      [float, null], default: null              Gaia (G-band) magnitude of closest source from Gaia DR1 catalog brighter than magnitude 14
                                                             if exists within 90 arcsec [mag]
magnr              [float, null], default: null              Magnitude of nearest source in reference image PSF-catalog within 30 arcsec [mag]
magpsf             float                                     Magnitude from PSF-fit photometry [mag]
magzpsci           [float, null], default: null              Magnitude zero point for photometry estimates [mag]
magzpscirms        [float, null], default: null              RMS (deviation from average) in all differences between instrumental photometry and matched 
                                                             photometric calibrators from science image processing [mag]
magzpsciunc        [float, null], default: null              Magnitude zero point uncertainty (in magzpsci) [mag]
mindtoedge         [float, null], default: null              Distance to nearest edge in image [pixels]
nbad               [int, null], default: null                Number of prior-tagged bad pixels in a 5 x 5 pixel stamp
ncovhist           int                                       Number of times input candidate position fell on any field and readout-channel going back to beginning of survey
ndethist           int                                       Number of spatially-coincident detections falling within 1.5 arcsec going back to beginning of survey
                                                             only detections that fell on the same field and readout-channel ID where the input candidate was observed are 
                                                             counted. All raw detections down to a photometric S/N of ~ 3 are included.
neargaia           [float, null], default: null              Distance to closest source from Gaia DR1 catalog irrespective of magnitude; if exists within 90 arcsec [arcsec]
neargaiabright     [float, null], default: null              Distance to closest source from Gaia DR1 catalog brighter than magnitude 14; if exists within 90 arcsec [arcsec]
nframesref         int                                       Number of frames (epochal images) used to generate reference image
nid                [int, null], default: null                Night ID
nmatches           int                                       Number of PS1 photometric calibrators used to calibrate science image from science image processing
nmtchps            int                                       Number of source matches from PS1 catalog falling within 30 arcsec
nneg               [int, null], default: null                Number of negative pixels in a 5 x 5 pixel stamp
objectidps1        [long, null], default: null               Object ID of closest source from PS1 catalog; if exists within 30 arcsec
objectidps2        [long, null], default: null               Object ID of second closest source from PS1 catalog; if exists within 30 arcsec
objectidps3        [long, null], default: null               Object ID of third closest source from PS1 catalog; if exists within 30 arcsec
oid                string                                    Object ID
pdiffimfilename    [string, null], default: null             Filename of positive (sci minus ref) difference image
pid                long                                      Processing ID for image
programpi          [string, null], default: null             Principal investigator attached to program ID
programid          int                                       Program ID: encodes either public, collab, or caltech mode
publisher          string                                    origin of alert packet
ra                 double                                    Right Ascension of candidate; J2000 [deg]
ranr               double                                    Right Ascension of nearest source in reference image PSF-catalog; J2000 [deg]
rb                 [float, null], default: null              RealBogus quality score; range is 0 to 1 where closer to 1 is more reliable
rbversion          string                                    Version of               RealBogus model/classifier used to assign rb quality score
rcid               [int, null], default: null                Readout channel ID [00 .. 63]
rfid               long                                      Processing ID for reference image to facilitate archive retrieval
scorr              [double, null], default: null             Peak-pixel signal-to-noise ratio in point source matched-filtered detection image
seeratio           [float, null], default: null              Ratio: difffwhm / fwhm
sgmag1             [float, null], default: null              g-band PSF magnitude of closest source from PS1 catalog; if exists within 30 arcsec [mag]
sgmag2             [float, null], default: null              g-band PSF magnitude of second closest source from PS1 catalog; if exists within 30 arcsec [mag]
sgmag3             [float, null], default: null              g-band PSF magnitude of third closest source from PS1 catalog; if exists within 30 arcsec [mag]
sgscore1           [float, null], default: null              Star/Galaxy score of closest source from PS1 catalog 0 <= sgscore <= 1 where closer to 1 implies 
                                                             higher likelihood of being a star
sgscore2           [float, null], default: null              Star/Galaxy score of second closest source from PS1 catalog; if exists within 30 arcsec
                                                             0 <= sgscore <= 1 where closer to 1 implies higher likelihood of being a star
sgscore3           [float, null], default: null              Star/Galaxy score of third closest source from PS1 catalog; if exists within 30 arcsec
                                                             0 <= sgscore <= 1 where closer to 1 implies higher likelihood of being a star
sharpnr            [float, null], default: null              DAOPhot sharp parameter of nearest source in reference image PSF-catalog within 30 arcsec
sigmagap           [float, null], default: null              1-sigma uncertainty in magap [mag]
sigmagapbig        [float, null], default: null              1-sigma uncertainty in magapbig [mag]
sigmagnr           [float, null], default: null              1-sigma uncertainty in magnr within 30 arcsec [mag]
sigmapsf           float                                     1-sigma uncertainty in magpsf [mag]
simag1             [float, null], default: null              i-band PSF magnitude of closest source from PS1 catalog; if exists within 30 arcsec [mag]
simag2             [float, null], default: null              i-band PSF magnitude of second closest source from PS1 catalog; if exists within 30 arcsec [mag]
simag3             [float, null], default: null              i-band PSF magnitude of third closest source from PS1 catalog; if exists within 30 arcsec [mag]
sky                [float, null], default: null              Local sky background estimate [DN]
srmag1             [float, null], default: null              r-band PSF magnitude of closest source from PS1 catalog; if exists within 30 arcsec [mag]
srmag2             [float, null], default: null              r-band PSF magnitude of second closest source from PS1 catalog; if exists within 30 arcsec [mag]
srmag3             [float, null], default: null              r-band PSF magnitude of third closest source from PS1 catalog; if exists within 30 arcsec [mag]
ssdistnr           [float, null], default: null              Distance to nearest known solar system object; set to -999.0 if none [arcsec]
ssmagnr            [float, null], default: null              Magnitude of nearest known solar system object (usually V-band from MPC archive); set to -999.0 if none [mag]
ssnamenr           [string, null], default: null             Name of nearest known solar system object (from MPC archive); ‘null’ if none
ssnrms             [float, null], default: null              Ratio: S/stddev(S) on event position where S = image of convolution: D (x) PSF(D)
sumrat             [float, null], default: null              Ratio: sum(pixels) / sum(abs(pixels)) in a 5 x 5 pixel stamp where stamp is first median-filtered 
szmag1             [float, null], default: null              z-band PSF magnitude of closest source from PS1 catalog; if exists within 30 arcsec [mag]
szmag2             [float, null], default: null              z-band PSF magnitude of second closest source from PS1 catalog; if exists within 30 arcsec [mag]
szmag3             [float, null], default: null              z-band PSF magnitude of third closest source from PS1 catalog; if exists within 30 arcsec [mag]
tblid              [long, null], default: null               Internal pipeline table extraction ID
tooflag            [int, null], default: 0                   1 => candidate is from a Target-of-Opportunity (ToO) exposure; 0 => candidate is from a non-ToO exposure
xpos               [float, null], default: null              x-image position of candidate [pixels]
ypos               [float, null], default: null              y-image position of candidate [pixels]
zid                bigint                                    Database ID of candidate
zpclrcov           [float, null], default: null              Covariance in magzpsci and clrcoeff from science image processing [mag^2]
zpmed              [float, null], default: null              Magnitude zero point from median of all differences between instrumental photometry and matched 
                                                             photometric calibrators from science image processing [mag]

ztf.alert.prv_candidate

The prv_candidates field contains an array of one or more previous subtraction candidates at the position of the alert. 
These are obtained by a simple cone search at the position of the alert candidate on the last 30 days of history. 
If there are no previous candidates or upper limits, this field is null.

The fields for an individual prv_candidate are identical to candidate except for the omission of the PS1 and Gaia 
matches, previous detection history, tooflag, and reference image information.

Additionally, if the previous image has a nondetection at position of the new candidate, candid, isdiffpos, ra, dec, 
magpsf, sigmapsf, ranr, and decr will be null. In this case diffmaglim provides an estimate of the limiting magnitude 
over the entire image.

ztf.alert.cutout contains two fields:

Field              Type                                      Contents
fileName           string                                    Original cutout location
stampData          bytes                                     GZIP-compressed FITS cutout image
"""


# +
# function: ztf_q3c_orm_cli()
# -
# noinspection PyBroadException
def ztf_q3c_orm_cli(_args: Any = None):

    # check input(s)
    if _args is None:
        raise Exception('Invalid arguments')

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
    if _args.alert_candid:
        request_args['alert_candid'] = f'{_args.alert_candid}'
    if _args.astrocone:
        request_args['astrocone'] = f'{_args.astrocone}'
    if _args.classtar__gte:
        request_args['classtar__gte'] = f'{_args.classtar__gte}'
    if _args.classtar__lte:
        request_args['classtar__lte'] = f'{_args.classtar__lte}'
    if _args.cone:
        request_args['cone'] = f'{_args.cone}'
    if _args.dec__gte:
        request_args['dec__gte'] = f'{_args.dec__gte}'
    if _args.dec__lte:
        request_args['dec__lte'] = f'{_args.dec__lte}'
    if _args.deltamaglatest__gte:
        request_args['deltamaglatest__gte'] = f'{_args.deltamaglatest__gte}'
    if _args.deltamaglatest__lte:
        request_args['deltamaglatest__lte'] = f'{_args.deltamaglatest__lte}'
    if _args.deltamagref__gte:
        request_args['deltamagref__gte'] = f'{_args.deltamagref__gte}'
    if _args.deltamagref__lte:
        request_args['deltamagref__lte'] = f'{_args.deltamagref__lte}'
    if _args.distnr__gte:
        request_args['distnr__gte'] = f'{_args.distnr__gte}'
    if _args.distnr__lte:
        request_args['distnr__lte'] = f'{_args.distnr__lte}'
    if _args.drb__gte:
        request_args['drb__gte'] = f'{_args.drb__gte}'
    if _args.drb__lte:
        request_args['drb__lte'] = f'{_args.drb__lte}'
    if _args.ellipse:
        request_args['ellipse'] = f'{_args.ellipse}'
    if _args.fid:
        request_args['fid'] = f'{_args.fid}'
    if _args.filtername:
        request_args['filtername'] = f'{_args.filtername}'
    if _args.iso__gte:
        request_args['iso__gte'] = f'{_args.iso__gte}'
    if _args.iso__lte:
        request_args['iso__lte'] = f'{_args.iso__lte}'
    if _args.jd__gte:
        request_args['jd__gte'] = f'{_args.jd__gte}'
    if _args.jd__lte:
        request_args['jd__lte'] = f'{_args.jd__lte}'
    if _args.magap__gte:
        request_args['magap__gte'] = f'{_args.magap__gte}'
    if _args.magap__lte:
        request_args['magap__lte'] = f'{_args.magap__lte}'
    if _args.magpsf__gte:
        request_args['magpsf__gte'] = f'{_args.magpsf__gte}'
    if _args.magpsf__lte:
        request_args['magpsf__lte'] = f'{_args.magpsf__lte}'
    if _args.objectidps:
        request_args['objectidps'] = f'{_args.objectidps}'
    if _args.oid:
        request_args['oid'] = f'{_args.oid}'
    if _args.ra__gte:
        request_args['ra__gte'] = f'{_args.ra__gte}'
    if _args.ra__lte:
        request_args['ra__lte'] = f'{_args.ra__lte}'
    if _args.rb__gte:
        request_args['rb__gte'] = f'{_args.rb__gte}'
    if _args.rb__lte:
        request_args['rb__lte'] = f'{_args.rb__lte}'
    if _args.sigmapsf__gte:
        request_args['sigmapsf__gte'] = f'{_args.sigmapsf__gte}'
    if _args.sigmapsf__lte:
        request_args['sigmapsf__lte'] = f'{_args.sigmapsf__lte}'
    if _args.ssnamenr:
        request_args['ssnamenr'] = f'{_args.ssnamenr}'
    if _args.zid:
        request_args['zid'] = f'{_args.zid}'
    if _args.zid__csv:
        request_args['zid'] = f'{_args.zid__csv}'

    # set up access to database
    try:
        if _args.verbose:
            print(f'connection string = postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
        engine = create_engine(f'postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
        if _args.verbose:
            print(f'engine = {engine}')
        _session = sessionmaker(bind=engine)
        if _args.verbose:
            print(f'Session = {_session}')
        session = _session()
        if _args.verbose:
            print(f'session = {session}')
    except Exception as _e1:
        raise Exception(f"failed to connect to database, error='{_e1}'")

    # execute query
    try:
        query = session.query(ZtfQ3cRecord)
        query = ztf_q3c_orm_filters(query, request_args)
        query = query.order_by(ZtfQ3cRecord.jd.desc())
        if _args.verbose:
            print(f'query = {query}')
    except Exception as _e2:
        raise Exception(f"failed to execute query, error='{_e2}'")

    # report output alphabetically
    print(f"#{','.join(_ for _ in ZTF_HEADERS)}")
    for _e in ZtfQ3cRecord.serialize_list(query.all()):
        print(f"_e={_e}")
        _pc = _e.pop('previous_candidates', [])
        _f = {**_e, **_e.pop('candidate')}
        if verify_keys(_f, set(ZTF_HEADERS)):
            print(f"{','.join(str(_f[_l]) for _l in ZTF_HEADERS)}")
    for _e in query.all():
        # get csv
        if _args.zid__csv:
            print(f"GETTING CSV")
            print(f"csv={_e.get_csv()}")



# +
# function: main()
# -
if __name__ == '__main__':

    # noinspection PyTypeChecker
    _p = argparse.ArgumentParser(description=f'Query ZTF Q3C database', formatter_class=argparse.RawTextHelpFormatter)

    # database query argument(s)
    _p.add_argument(f'--astrocone', help=f'Astrocone search [name,radius (deg)]')
    _p.add_argument(f'--cone', help=f'Cone search [ra (deg),dec (deg),radius (deg)]')
    _p.add_argument(f'--ellipse', help=f'Ellipse search [ra (deg),dec (de),major_axis,axis_ratio,pos_angle (deg)]')
    _p.add_argument(f'--alert_candid', help=f'Candidate ID <int>')
    _p.add_argument(f'--classtar__gte', help=f'Classification index >= <float>')
    _p.add_argument(f'--classtar__lte', help=f'Classification index <= <float>')
    _p.add_argument(f'--dec__gte', help=f'Dec >= <float>')
    _p.add_argument(f'--dec__lte', help=f'Dec <= <float>')
    _p.add_argument(f'--deltamaglatest__gte', help=f'DeltaMagLatest >= <float>')
    _p.add_argument(f'--deltamaglatest__lte', help=f'DeltaMagLatest <= <float>')
    _p.add_argument(f'--deltamagref__gte', help=f'DeltaMagRef >= <float>')
    _p.add_argument(f'--deltamagref__lte', help=f'DeltaMagRef <= <float>')
    _p.add_argument(f'--distnr__gte', help=f'Distance to nearest object >= <float>')
    _p.add_argument(f'--distnr__lte', help=f'Distance to nearest object <= <float>')
    _p.add_argument(f'--drb__gte', help=f'Deep-Learning Real-Bogus score >= <float>')
    _p.add_argument(f'--drb__lte', help=f'Deep-Learning Real-Bogus score <= <float>')
    _p.add_argument(f'--fid', help=f'filter <int>')
    _p.add_argument(f'--filtername', help=f'filter <str>')
    _p.add_argument(f'--iso__gte', help=f'ISO time >= <str>')
    _p.add_argument(f'--iso__lte', help=f'ISO time <= <str>')
    _p.add_argument(f'--jd__gte', help=f'Julian Day >= <float>')
    _p.add_argument(f'--jd__lte', help=f'Julian Day <= <float>')
    _p.add_argument(f'--magap__gte', help=f'Aperture magnitude >= <float>')
    _p.add_argument(f'--magap__lte', help=f'Aperture magnitude <= <float>')
    _p.add_argument(f'--magpsf__gte', help=f'Magnitude >= <float>')
    _p.add_argument(f'--magpsf__lte', help=f'Magnitude <= <float>')
    _p.add_argument(f'--objectidps', help=f'IDPS object <int>')
    _p.add_argument(f'--oid', help=f'Object ID <str>')
    _p.add_argument(f'--ra__gte', help=f'RA >= <float>')
    _p.add_argument(f'--ra__lte', help=f'RA <= <float>')
    _p.add_argument(f'--rb__gte', help=f'Real-Bogus score >= <float>')
    _p.add_argument(f'--rb__lte', help=f'Real-Bogus score <= <float>')
    _p.add_argument(f'--sigmapsf__gte', help=f'Magnitude sigma >= <float>')
    _p.add_argument(f'--sigmapsf__lte', help=f'Magnitude sigma <= <float>')
    _p.add_argument(f'--ssnamenr', help=f'Solar system name <str>')
    _p.add_argument(f'--zid', help=f'ZTF id <int>')
    _p.add_argument(f'--zid__csv', help=f'ZTF id <int> (get csv)')

    # non-database query argument(s)
    _p.add_argument(f'--paper', default=False, action='store_true', help=f'if present, download the science paper')
    _p.add_argument(f'--text', default=False, action='store_true', help=f'if present, describe the catalog')
    _p.add_argument(f'--verbose', default=False, action='store_true', help=f'if present, produce more verbose output')
    _a = _p.parse_args()

    # execute
    try:
        ztf_q3c_orm_cli(_args=_a)
    except Exception as _:
        print(f"{_}\nUse: {__doc__}")
