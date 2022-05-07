#!/usr/bin/env python3


# +
# import(s)
# -
from sassy_q3c_models import *
from sassy_q3c_models.non_detections_orm import NonDetectionsRecord
from sassy_q3c_models.non_detections_orm import db as db_nd


# +
# __doc__ string
# -
__doc__ = """
                                         Table "public.ztf_q3c"
      Column      |          Type          | Collation | Nullable |               Default                
------------------+------------------------+-----------+----------+--------------------------------------
 aimage           | double precision       |           |          | 
 aimagerat        | double precision       |           |          | 
 alert_candid     | bigint                 |           |          | 
 avro             | character varying(256) |           | not null | 
 bimage           | double precision       |           |          | 
 bimagerat        | double precision       |           |          | 
 candid           | bigint                 |           |          | 
 chinr            | double precision       |           |          | 
 chipsf           | double precision       |           |          | 
 classtar         | double precision       |           |          | 
 clrcoeff         | double precision       |           |          | 
 clrcounc         | double precision       |           |          | 
 clrmed           | double precision       |           |          | 
 clrrms           | double precision       |           |          | 
 cutoutdifference | character varying(192) |           |          | 
 cutoutscience    | character varying(192) |           |          | 
 cutouttemplate   | character varying(192) |           |          | 
 dec              | double precision       |           | not null | 
 decnr            | double precision       |           | not null | 
 deltamaglatest   | double precision       |           |          | 
 deltamagref      | double precision       |           |          | 
 diffmaglim       | double precision       |           |          | 
 distpsnr1        | double precision       |           |          | 
 distpsnr2        | double precision       |           |          | 
 distpsnr3        | double precision       |           |          | 
 distnr           | double precision       |           |          | 
 drb              | double precision       |           |          | 
 drbversion       | character varying(64)  |           |          | 
 dsnrms           | double precision       |           |          | 
 dsdiff           | double precision       |           |          | 
 elong            | double precision       |           |          | 
 exptime          | double precision       |           |          | 
 fid              | integer                |           | not null | 
 filtername       | character varying(1)   |           | not null | 
 field            | integer                |           |          | 
 fwhm             | double precision       |           |          | 
 gal_b            | double precision       |           | not null | 
 gal_l            | double precision       |           | not null | 
 isdiffpos        | character varying(1)   |           | not null | 
 iso              | character varying(32)  |           | not null | 
 jd               | double precision       |           | not null | 
 jdendhist        | double precision       |           |          | 
 jdendref         | double precision       |           | not null | 
 jdstarthist      | double precision       |           |          | 
 jdstartref       | double precision       |           | not null | 
 magap            | double precision       |           |          | 
 magapbig         | double precision       |           |          | 
 magdiff          | double precision       |           |          | 
 magfromlim       | double precision       |           |          | 
 maggaia          | double precision       |           |          | 
 maggaiabright    | double precision       |           |          | 
 magnr            | double precision       |           |          | 
 magpsf           | double precision       |           | not null | 
 magzpsci         | double precision       |           |          | 
 magzpscirms      | double precision       |           |          | 
 magzpsciunc      | double precision       |           |          | 
 mindtoedge       | double precision       |           |          | 
 nbad             | integer                |           |          | 
 ncovhist         | integer                |           | not null | 
 ndethist         | integer                |           | not null | 
 neargaia         | double precision       |           |          | 
 neargaiabright   | double precision       |           |          |
 nframesref       | integer                |           | not null | 
 nid              | integer                |           |          | 
 nmatches         | integer                |           |          | 
 nmtchps          | integer                |           | not null | 
 nneg             | integer                |           |          | 
 objectidps1      | bigint                 |           |          | 
 objectidps2      | bigint                 |           |          | 
 objectidps3      | bigint                 |           |          | 
 oid              | character varying(64)  |           | not null | 
 pdiffimfilename  | character varying(256) |           |          | 
 pid              | bigint                 |           | not null | 
 programid        | integer                |           | not null | 
 programpi        | character varying(128) |           |          | 
 publisher        | character varying(128) |           | not null | 
 ra               | double precision       |           | not null | 
 ranr             | double precision       |           | not null | 
 rb               | double precision       |           |          | 
 rbversion        | character varying(64)  |           | not null | 
 rcid             | integer                |           |          | 
 rfid             | bigint                 |           | not null | 
 scorr            | double precision       |           |          | 
 seeratio         | double precision       |           |          | 
 sgmag1           | double precision       |           |          | 
 sgmag2           | double precision       |           |          | 
 sgmag3           | double precision       |           |          | 
 sgscore1         | double precision       |           |          | 
 sgscore2         | double precision       |           |          | 
 sgscore3         | double precision       |           |          | 
 sharpnr          | double precision       |           |          | 
 sigmagap         | double precision       |           |          | 
 sigmagapbig      | double precision       |           |          | 
 sigmagnr         | double precision       |           |          | 
 sigmapsf         | double precision       |           | not null | 
 simag1           | double precision       |           |          | 
 simag2           | double precision       |           |          | 
 simag3           | double precision       |           |          | 
 sky              | double precision       |           |          | 
 srmag1           | double precision       |           |          | 
 srmag2           | double precision       |           |          | 
 srmag3           | double precision       |           |          | 
 ssdistnr         | double precision       |           |          | 
 ssmagnr          | double precision       |           |          | 
 ssnamenr         | character varying(128) |           | not null | 
 ssnrms           | double precision       |           |          | 
 sumrat           | double precision       |           |          | 
 szmag1           | double precision       |           |          | 
 szmag2           | double precision       |           |          | 
 szmag3           | double precision       |           |          | 
 tblid            | bigint                 |           |          | 
 tooflag          | smallint               |           | not null | 
 xpos             | double precision       |           |          | 
 ypos             | double precision       |           |          | 
 zid              | integer                |           | not null | nextval('ztf_q3c_zid_seq'::regclass)
 zpclrcov         | double precision       |           |          | 
 zpmed            | double precision       |           |          | 
Indexes:
    "ztf_q3c_pkey" PRIMARY KEY, btree (zid)
    "idx_ztf_q3c_alert_candid" btree (alert_candid)
    "idx_ztf_q3c_classtar" btree (classtar)
    "idx_ztf_q3c_dec" btree ("dec")
    "idx_ztf_q3c_deltamaglatest" btree (deltamaglatest)
    "idx_ztf_q3c_deltamagref" btree (deltamagref)
    "idx_ztf_q3c_drb" btree (drb)
    "idx_ztf_q3c_elong" btree (elong)
    "idx_ztf_q3c_fwhm" btree (fwhm)
    "idx_ztf_q3c_gal_b" btree (gal_b)
    "idx_ztf_q3c_gal_l" btree (gal_l)
    "idx_ztf_q3c_jd" btree (jd)
    "idx_ztf_q3c_magap" btree (magap)
    "idx_ztf_q3c_magpsf" btree (magpsf)
    "idx_ztf_q3c_nbad" btree (nbad)
    "idx_ztf_q3c_oid" btree (oid)
    "idx_ztf_q3c_ra" btree (ra)
    "idx_ztf_q3c_rb" btree (rb)
    "idx_ztf_q3c_sigmapsf" btree (sigmapsf)
    "idx_ztf_q3c_ssdistnr" btree (ssdistnr)
    "ztf_q3c_q3c_ang2ipix_idx" btree (q3c_ang2ipix(ra, "dec"))
"""


# +
# constant(s)
# -
ZTF_PDF_URL = 'https://arXiv.org/pdf/1902.01932.pdf'
ZTF_DAT_URL = 'https://ztf.uw.edu/alerts/public'
ZTF_CANDIDATE_RADIUS = 0.000416667
ZTF_FILTERS = {1: 'g', 2: 'r', 3: 'i'}
ZTF_FILTERS_R = {_v: _k for _k, _v in ZTF_FILTERS.items()}
ZTF_SORT_ORDER = ['asc', 'desc', 'ascending', 'descending']
ZTF_SORT_VALUE = ['alert_candid', 'candid', 'classtar', 'dec', 'deltamaglatest', 'deltamagref', 'diffmaglim',
                  'distnr', 'drb', 'fid', 'filtername', 'iso', 'jd', 'magap', 'magapbig', 'magdiff', 'magfromlim',
                  'maggaia', 'maggaiabright', 'magnr', 'magpsf', 'oid', 'ra', 'rb', 'ssnamenr', 'zid']
ZTF_HEADERS = ('aimage', 'aimagerat', 'alert_candid', 'avro', 'bimage', 'bimagerat', 'candid', 'chinr', 'chipsf',
               'classtar', 'clrcoeff', 'clrcounc', 'clrmed', 'clrrms', 'cutoutdifference', 'cutoutscience',
               'cutouttemplate', 'dec', 'decnr', 'deltamaglatest', 'deltamagref', 'diffmaglim', 'distpsnr1',
               'distpsnr2', 'distpsnr3', 'distnr', 'drb', 'drbversion', 'dsnrms', 'dsdiff', 'elong', 'exptime',
               'fid', 'filtername', 'field', 'fwhm', 'gal_b', 'gal_l', 'isdiffpos', 'iso', 'jd', 'jdendhist',
               'jdendref', 'jdstarthist', 'jdstartref', 'magap', 'magapbig', 'magdiff', 'magfromlim', 'maggaia',
               'maggaiabright', 'magnr', 'magpsf', 'magzpsci', 'magzpscirms', 'magzpsciunc', 'mindtoedge', 'nbad',
               'ncovhist', 'ndethist', 'neargaia', 'neargaiabright', 'nframesref', 'nid', 'nmatches', 'nmtchps',
               'nneg', 'objectidps1', 'objectidps2', 'objectidps3', 'oid', 'pdiffimfilename', 'pid', 'programid',
               'programpi', 'publisher', 'ra', 'ranr', 'rb', 'rbversion', 'rcid', 'rfid', 'scorr', 'seeratio',
               'sgmag1', 'sgmag2', 'sgmag3', 'sgscore1', 'sgscore2', 'sgscore3', 'sharpnr', 'sigmagap',
               'sigmagapbig', 'sigmagnr', 'sigmapsf', 'simag1', 'simag2', 'simag3', 'sky', 'srmag1', 'srmag2',
               'srmag3', 'ssdistnr', 'ssmagnr', 'ssnamenr', 'ssnrms', 'sumrat', 'szmag1', 'szmag2', 'szmag3',
               'tblid', 'tooflag', 'xpos', 'ypos', 'zid', 'zpclrcov', 'zpmed')


# +
# initialize sqlalchemy (deferred)
# -
db = SQLAlchemy()


# +
# class: ZtfQ3cRecord(), inherits from db.Model
# -
# noinspection PyUnresolvedReferences
class ZtfQ3cRecord(db.Model):

    # +
    # define table
    # -
    __tablename__ = 'ztf_q3c'
    aimage = db.Column(db.Float, nullable=True, default=None)
    aimagerat = db.Column(db.Float, nullable=True, default=None)
    alert_candid = db.Column(db.BigInteger, nullable=True, default=None, index=True, unique=True)
    avro = db.Column(db.String(256), nullable=False)
    bimage = db.Column(db.Float, nullable=True, default=None)
    bimagerat = db.Column(db.Float, nullable=True, default=None)
    candid = db.Column(db.BigInteger, nullable=True, default=None)
    chinr = db.Column(db.Float, nullable=True, default=None)
    chipsf = db.Column(db.Float, nullable=True, default=None)
    classtar = db.Column(db.Float, nullable=True, default=None, index=True)
    clrcoeff = db.Column(db.Float, nullable=True, default=None)
    clrcounc = db.Column(db.Float, nullable=True, default=None)
    clrmed = db.Column(db.Float, nullable=True, default=None)
    clrrms = db.Column(db.Float, nullable=True, default=None)
    cutoutdifference = db.Column(db.String(192), nullable=True, default=None)
    cutoutscience = db.Column(db.String(192), nullable=True, default=None)
    cutouttemplate = db.Column(db.String(192), nullable=True, default=None)
    dec = db.Column(db.Float, nullable=False, index=True)
    decnr = db.Column(db.Float, nullable=False)
    deltamaglatest = db.Column(db.Float, nullable=True, default=None, index=True)
    deltamagref = db.Column(db.Float, nullable=True, default=None, index=True)
    diffmaglim = db.Column(db.Float, nullable=True, default=None)
    distpsnr1 = db.Column(db.Float, nullable=True, default=None)
    distpsnr2 = db.Column(db.Float, nullable=True, default=None)
    distpsnr3 = db.Column(db.Float, nullable=True, default=None)
    distnr = db.Column(db.Float, nullable=True, default=None)
    drb = db.Column(db.Float, nullable=True, default=None, index=True)
    drbversion = db.Column(db.String(64), nullable=True, default='')
    dsnrms = db.Column(db.Float, nullable=True, default=None)
    dsdiff = db.Column(db.Float, nullable=True, default=None)
    elong = db.Column(db.Float, nullable=True, default=None, index=True)
    exptime = db.Column(db.Float, nullable=True, default=None)
    fid = db.Column(db.Integer, nullable=False)
    filtername = db.Column(db.String(1), nullable=False)
    field = db.Column(db.Integer, nullable=True, default=None)
    fwhm = db.Column(db.Float, nullable=True, default=None, index=True)
    gal_b = db.Column(db.Float, nullable=False, index=True)
    gal_l = db.Column(db.Float, nullable=False, index=True)
    isdiffpos = db.Column(db.String(1), nullable=False)
    iso = db.Column(db.String(32), nullable=False)
    jd = db.Column(db.Float, nullable=False, index=True)
    jdendhist = db.Column(db.Float, nullable=True, default=None)
    jdendref = db.Column(db.Float, nullable=False)
    jdstarthist = db.Column(db.Float, nullable=True, default=None)
    jdstartref = db.Column(db.Float, nullable=False)
    magap = db.Column(db.Float, nullable=True, default=None, index=True)
    magapbig = db.Column(db.Float, nullable=True, default=None)
    magdiff = db.Column(db.Float, nullable=True, default=None)
    magfromlim = db.Column(db.Float, nullable=True, default=None)
    maggaia = db.Column(db.Float, nullable=True, default=None)
    maggaiabright = db.Column(db.Float, nullable=True, default=None)
    magnr = db.Column(db.Float, nullable=True, default=None)
    magpsf = db.Column(db.Float, nullable=False, index=True)
    magzpsci = db.Column(db.Float, nullable=True, default=None)
    magzpscirms = db.Column(db.Float, nullable=True, default=None)
    magzpsciunc = db.Column(db.Float, nullable=True, default=None)
    mindtoedge = db.Column(db.Float, nullable=True, default=None)
    nbad = db.Column(db.Integer, nullable=True, default=None, index=True)
    ncovhist = db.Column(db.Integer, nullable=False)
    ndethist = db.Column(db.Integer, nullable=False)
    neargaia = db.Column(db.Float, nullable=True, default=None)
    neargaiabright = db.Column(db.Float, nullable=True, default=None)
    nframesref = db.Column(db.Integer, nullable=False)
    nid = db.Column(db.Integer, nullable=True, default=None)
    nmatches = db.Column(db.Integer, nullable=True, default=None)
    nmtchps = db.Column(db.Integer, nullable=False)
    nneg = db.Column(db.Integer, nullable=True, default=None)
    objectidps1 = db.Column(db.BigInteger, nullable=True, default=None, index=True)
    objectidps2 = db.Column(db.BigInteger, nullable=True, default=None, index=True)
    objectidps3 = db.Column(db.BigInteger, nullable=True, default=None, index=True)
    oid = db.Column(db.String(64), nullable=False, index=True)
    pdiffimfilename = db.Column(db.String(256), nullable=True, default=None)
    pid = db.Column(db.BigInteger, nullable=False)
    programid = db.Column(db.Integer, nullable=False)
    programpi = db.Column(db.String(128), nullable=True, default=None)
    publisher = db.Column(db.String(128), nullable=False, default='')
    ra = db.Column(db.Float, nullable=False, index=True)
    ranr = db.Column(db.Float, nullable=False)
    rb = db.Column(db.Float, nullable=True, default=None, index=True)
    rbversion = db.Column(db.String(64), nullable=False, default='')
    rcid = db.Column(db.Integer, nullable=True, default=None)
    rfid = db.Column(db.BigInteger, nullable=False)
    scorr = db.Column(db.Float, nullable=True)
    seeratio = db.Column(db.Float, nullable=True, default=None)
    sgmag1 = db.Column(db.Float, nullable=True, default=None)
    sgmag2 = db.Column(db.Float, nullable=True, default=None)
    sgmag3 = db.Column(db.Float, nullable=True, default=None)
    sgscore1 = db.Column(db.Float, nullable=True, default=None)
    sgscore2 = db.Column(db.Float, nullable=True, default=None)
    sgscore3 = db.Column(db.Float, nullable=True, default=None)
    sharpnr = db.Column(db.Float, nullable=True, default=None)
    sigmagap = db.Column(db.Float, nullable=True, default=None)
    sigmagapbig = db.Column(db.Float, nullable=True, default=None)
    sigmagnr = db.Column(db.Float, nullable=True, default=None)
    sigmapsf = db.Column(db.Float, nullable=False, index=True)
    simag1 = db.Column(db.Float, nullable=True, default=None)
    simag2 = db.Column(db.Float, nullable=True, default=None)
    simag3 = db.Column(db.Float, nullable=True, default=None)
    sky = db.Column(db.Float, nullable=True, default=None)
    srmag1 = db.Column(db.Float, nullable=True, default=None)
    srmag2 = db.Column(db.Float, nullable=True, default=None)
    srmag3 = db.Column(db.Float, nullable=True, default=None)
    ssdistnr = db.Column(db.Float, nullable=True, default=None, index=True)
    ssmagnr = db.Column(db.Float, nullable=True, default=None)
    ssnamenr = db.Column(db.String(128), nullable=False, default='')
    ssnrms = db.Column(db.Float, nullable=True, default=None)
    sumrat = db.Column(db.Float, nullable=True, default=None)
    szmag1 = db.Column(db.Float, nullable=True, default=None)
    szmag2 = db.Column(db.Float, nullable=True, default=None)
    szmag3 = db.Column(db.Float, nullable=True, default=None)
    tblid = db.Column(db.BigInteger, nullable=True, default=None)
    tooflag = db.Column(db.SmallInteger, nullable=False, default=0)
    xpos = db.Column(db.Float, nullable=True, default=None)
    ypos = db.Column(db.Float, nullable=True, default=None)
    zid = db.Column(db.Integer, primary_key=True)
    zpclrcov = db.Column(db.Float, nullable=True, default=None)
    zpmed = db.Column(db.Float, nullable=True, default=None)

    # +
    # property: non_detections()
    # -
    @property
    def non_detections(self):
        nd_query = db_nd.session.query(NonDetectionsRecord)
        nd_query = nd_query.filter(NonDetectionsRecord.oid == self.oid)
        return nd_query.order_by(NonDetectionsRecord.jd.desc())

    # +
    # property: previous_candidates()
    # -
    @property
    def previous_candidates(self):
        pc_query = db.session.query(ZtfQ3cRecord)
        pc_query = pc_query.filter(func.q3c_radial_query(
            ZtfQ3cRecord.ra, ZtfQ3cRecord.dec, self.ra, self.dec, ZTF_CANDIDATE_RADIUS))
        pc_query = pc_query.filter(ZtfQ3cRecord.zid != int(self.zid))
        return pc_query.order_by(ZtfQ3cRecord.jd.desc())

    # +
    # method: serialized()
    # -
    def serialized(self, show_previous: bool = False) -> dict:
        record = {
            'zid': self.zid,
            'oid': self.oid,
            'publisher': self.publisher,
            'alert_candid': self.alert_candid,
            'avro': self.avro,
            'ra': self.ra,
            'dec': self.dec,
            'candidate': {
                'aimage': self.aimage,
                'aimagerat': self.aimagerat,
                'bimage': self.bimage,
                'bimagerat': self.bimagerat,
                'candid': self.candid,
                'chinr': self.chinr,
                'chipsf': self.chipsf,
                'classtar': self.classtar,
                'clrcoeff': self.clrcoeff,
                'clrcounc': self.clrcounc,
                'clrmed': self.clrmed,
                'clrrms': self.clrrms,
                'cutoutdifference': self.cutoutdifference,
                'cutoutscience': self.cutoutscience,
                'cutouttemplate': self.cutouttemplate,
                'decnr': self.decnr,
                'deltamaglatest': self.deltamaglatest,
                'deltamagref': self.deltamagref,
                'diffmaglim': self.diffmaglim,
                'distpsnr1': self.distpsnr1,
                'distpsnr2': self.distpsnr2,
                'distpsnr3': self.distpsnr3,
                'distnr': self.distnr,
                'drb': self.drb,
                'drbversion': self.drbversion,
                'dsnrms': self.dsnrms,
                'dsdiff': self.dsdiff,
                'elong': self.elong,
                'exptime': self.exptime,
                'fid': self.fid,
                'filtername': self.filtername,
                'field': self.field,
                'fwhm': self.fwhm,
                'gal_b': self.gal_b,
                'gal_l': self.gal_l,
                'isdiffpos': self.isdiffpos,
                'iso': self.iso,
                'jd': self.jd,
                'jdendhist': self.jdendhist,
                'jdendref': self.jdendref,
                'jdstarthist': self.jdstarthist,
                'jdstartref': self.jdstartref,
                'magap': self.magap,
                'magapbig': self.magapbig,
                'magdiff': self.magdiff,
                'magfromlim': self.magfromlim,
                'maggaia': self.maggaia,
                'maggaiabright': self.maggaiabright,
                'magnr': self.magnr,
                'magpsf': self.magpsf,
                'magzpsci': self.magzpsci,
                'magzpscirms': self.magzpscirms,
                'magzpsciunc': self.magzpsciunc,
                'mindtoedge': self.mindtoedge,
                'nbad': self.nbad,
                'ncovhist': self.ncovhist,
                'ndethist': self.ndethist,
                'neargaia': self.neargaia,
                'neargaiabright': self.neargaiabright,
                'nframesref': self.nframesref,
                'nid': self.nid,
                'nmatches': self.nmatches,
                'nmtchps': self.nmtchps,
                'nneg': self.nneg,
                'objectidps1': self.objectidps1,
                'objectidps2': self.objectidps2,
                'objectidps3': self.objectidps3,
                'pdiffimfilename': self.pdiffimfilename,
                'pid': self.pid,
                'programid': self.programid,
                'programpi': self.programpi,
                'ranr': self.ranr,
                'rb': self.rb,
                'rbversion': self.rbversion,
                'rcid': self.rcid,
                'rfid': self.rfid,
                'scorr': self.scorr,
                'seeratio': self.seeratio,
                'sgmag1': self.sgmag1,
                'sgmag2': self.sgmag2,
                'sgmag3': self.sgmag3,
                'sgscore1': self.sgscore1,
                'sgscore2': self.sgscore2,
                'sgscore3': self.sgscore3,
                'sharpnr': self.sharpnr,
                'sigmagap': self.sigmagap,
                'sigmagapbig': self.sigmagapbig,
                'sigmagnr': self.sigmagnr,
                'sigmapsf': self.sigmapsf,
                'simag1': self.simag1,
                'simag2': self.simag2,
                'simag3': self.simag3,
                'sky': self.sky,
                'srmag1': self.srmag1,
                'srmag2': self.srmag2,
                'srmag3': self.srmag3,
                'ssdistnr': self.ssdistnr,
                'ssmagnr': self.ssmagnr,
                'ssnamenr': self.ssnamenr,
                'ssnrms': self.ssnrms,
                'sumrat': self.sumrat,
                'szmag1': self.szmag1,
                'szmag2': self.szmag2,
                'szmag3': self.szmag3,
                'tblid': self.tblid,
                'tooflag': self.tooflag,
                'xpos': self.xpos,
                'ypos': self.ypos,
                'zpclrcov': self.zpclrcov,
                'zpmed': self.zpmed
            }
        }
        if show_previous:
            _pc = ZtfQ3cRecord.serialize_list(self.previous_candidates)
            _nd = NonDetectionsRecord.serialize_list(self.non_detections)
            if _pc and _nd:
                ZtfQ3cRecord.add_records(_pc, _nd)
                record['previous_candidates'] = _pc
        return record

    # +
    # (static) method: add_records()
    # -
    # noinspection PyTypeChecker
    @staticmethod
    def add_records(pc: list = None, nd: list = None):
        for _c in nd:
            low, high = 0, len(pc)
            while low < high:
                mid = (low+high)//2
                if pc[mid]['candidate']['jd'] < _c['candidate']['jd']:
                    low = mid+1
                else:
                    high = mid
            pc.insert(low, _c)
        return pc

    # +
    # (overload) method: __str__()
    # -
    def __str__(self):
        return self.oid

    # +
    # (static) method: serialize_list()
    # -
    @staticmethod
    def serialize_list(m_alerts):
        return [_a.serialized() for _a in m_alerts]
