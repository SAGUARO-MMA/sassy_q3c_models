#!/usr/bin/env python3


# +
# import(s)
# -
from sassy_q3c_models import *


# +
# __doc__ string
# -
__doc__ = """
                                            Table "public.sassy_cron"
      Column       |            Type             | Collation | Nullable |                 Default                 
-------------------+-----------------------------+-----------+----------+-----------------------------------------
 zoid              | character varying(64)       |           |          | 
 zjd               | double precision            |           |          | 
 zmagap            | double precision            |           |          | 
 zmagpsf           | double precision            |           |          | 
 zmagdiff          | double precision            |           |          | 
 zfid              | integer                     |           |          | 
 zdrb              | double precision            |           |          | 
 zrb               | double precision            |           |          | 
 zsid              | integer                     |           |          | 
 zcandid           | bigint                      |           |          | 
 zssnamenr         | character varying(128)      |           |          | 
 zra               | double precision            |           |          | 
 zdec              | double precision            |           |          | 
 gid               | integer                     |           |          | 
 gra               | double precision            |           |          | 
 gdec              | double precision            |           |          | 
 gz                | double precision            |           |          | 
 gdist             | double precision            |           |          | 
 gsep              | double precision            |           |          | 
 tid               | integer                     |           |          | 
 objid             | integer                     |           |          | 
 name_prefix       | character varying(4)        |           |          | 
 name              | character varying(32)       |           |          | 
 ra                | double precision            |           |          | 
 declination       | double precision            |           |          | 
 redshift          | double precision            |           |          | 
 typeid            | integer                     |           |          | 
 objtype           | character varying(32)       |           |          | 
 reporting_groupid | integer                     |           |          | 
 reporting_group   | character varying(32)       |           |          | 
 source_groupid    | integer                     |           |          | 
 source_group      | character varying(32)       |           |          | 
 discoverydate     | timestamp without time zone |           |          | 
 discoverymag      | double precision            |           |          | 
 discmagfilter     | integer                     |           |          | 
 filtername        | character varying(8)        |           |          | 
 reporters         | character varying(2048)     |           |          | 
 time_received     | timestamp without time zone |           |          | 
 internal_names    | character varying(256)      |           |          | 
 creationdate      | timestamp without time zone |           |          | 
 lastmodified      | timestamp without time zone |           |          | 
 class_name        | character varying(64)       |           |          | ''::character varying
 class_prob        | double precision            |           |          | 'NaN'::double precision
 dpng              | character varying(200)      |           |          | ''::character varying
 spng              | character varying(200)      |           |          | ''::character varying
 tpng              | character varying(200)      |           |          | ''::character varying
 sid               | integer                     |           | not null | nextval('sassy_cron_sid_seq'::regclass)
Indexes:
    "sassy_cron_q3c_ang2ipix_idx" btree (q3c_ang2ipix(zra, zdec)) CLUSTER
"""


# +
# constant(s)
# -
SASSY_CRON_DAT_URL = ''
SASSY_CRON_PAG_URL = ''
SASSY_CRON_PDF_URL = ''
SASSY_CRON_SORT_ORDER = ['asc', 'desc', 'ascending', 'descending']
SASSY_CRON_SORT_VALUE = ['zoid', 'zjd', 'zmagap', 'zmagpsf', 'zmagdiff', 'zra', 'zdec', 'gz', 'gdist', 'gsep',
                         'class_name', 'class_prob', 'sid']
SASSY_CRON_HEADERS = ('zoid', 'zjd', 'zmagap', 'zmagpsf', 'zmagdiff', 'zfid', 'zdrb', 'zrb', 'zsid', 'zcandid',
                      'zssnamenr', 'zra', 'zdec', 'gid', 'gra', 'gdec', 'gz', 'gdist', 'gsep', 'tid', 'objid',
                      'name_prefix', 'name', 'ra', 'declination', 'redshift', 'typeid', 'objtype',
                      'reporting_groupid', 'reporting_group', 'source_groupid', 'source_group', 'discoverydate',
                      'discoverymag', 'discmagfilter', 'filtername', 'reporters', 'time_received', 'internal_names',
                      'creationdate', 'lastmodified', 'class_name', 'class_prob', 'dpng', 'spng', 'tpng', 'sid')


# +
# initialize sqlalchemy (deferred)
# -
db = SQLAlchemy()


# +
# class: SassyCronQ3cRecord(), inherits from db.Model
# -
# noinspection PyPep8Naming,PyUnresolvedReferences
class SassyCronQ3cRecord(db.Model):

    # +
    # member variable(s)
    # -
    __tablename__ = 'sassy_cron'
    zoid = db.Column(db.String(DB_VARCHAR_64))
    zjd = db.Column(db.Float)
    zmagap = db.Column(db.Float)
    zmagpsf = db.Column(db.Float)
    zmagdiff = db.Column(db.Float)
    zfid = db.Column(db.Integer)
    zdrb = db.Column(db.Float)
    zrb = db.Column(db.Float)
    zsid = db.Column(db.Integer)
    zcandid = db.Column(db.BigInteger)
    zssnamenr = db.Column(db.String(DB_VARCHAR_128))
    zra = db.Column(db.Float)
    zdec = db.Column(db.Float)
    gid = db.Column(db.Integer)
    gra = db.Column(db.Float)
    gdec = db.Column(db.Float)
    gz = db.Column(db.Float)
    gdist = db.Column(db.Float)
    gsep = db.Column(db.Float)
    tid = db.Column(db.Integer)
    objid = db.Column(db.Integer)
    name_prefix = db.Column(db.String(DB_VARCHAR_4))
    name = db.Column(db.String(DB_VARCHAR_32))
    ra = db.Column(db.Float)
    declination = db.Column(db.Float)
    redshift = db.Column(db.Float)
    typeid = db.Column(db.Integer)
    objtype = db.Column(db.String(DB_VARCHAR_32))
    reporting_groupid = db.Column(db.Float)
    reporting_group = db.Column(db.String(DB_VARCHAR_32))
    source_groupid = db.Column(db.Integer)
    source_group = db.Column(db.String(DB_VARCHAR_32))
    discoverydate = db.Column(db.DateTime)
    discoverymag = db.Column(db.Float)
    discmagfilter = db.Column(db.Integer)
    filtername = db.Column(db.String(DB_VARCHAR_8))
    reporters = db.Column(db.String(DB_VARCHAR_2048))
    time_received = db.Column(db.DateTime)
    internal_names = db.Column(db.String(DB_VARCHAR_256))
    creationdate = db.Column(db.DateTime)
    lastmodified = db.Column(db.DateTime)
    class_name = db.Column(db.String(DB_VARCHAR_64))
    class_prob = db.Column(db.Float)
    dpng = db.Column(db.String(DB_VARCHAR_200))
    spng = db.Column(db.String(DB_VARCHAR_200))
    tpng = db.Column(db.String(DB_VARCHAR_200))
    sid = db.Column(db.Integer, primary_key=True)

    # +
    # method: serialized()
    # -
    def serialized(self):
        return {
            'zoid': self.zoid,
            'zjd': self.zjd,
            'zmagap': self.zmagap,
            'zmagpsf': self.zmagpsf,
            'zmagdiff': self.zmagdiff,
            'zfid': self.zfid,
            'zdrb': self.zdrb,
            'zrb': self.zrb,
            'zsid': self.zsid,
            'zcandid': self.zcandid,
            'zssnamenr': self.zssnamenr,
            'zra': self.zra,
            'zdec': self.zdec,
            'gid': self.gid,
            'gra': self.gra,
            'gdec': self.gdec,
            'gz': self.gz,
            'gdist': self.gdist,
            'gsep': self.gsep,
            'tid': self.tid,
            'objid': self.objid,
            'name_prefix': self.name_prefix,
            'name': self.name,
            'ra': self.ra,
            'declination': self.declination,
            'redshift': self.redshift,
            'typeid': self.typeid,
            'objtype': self.objtype,
            'reporting_groupid': self.reporting_groupid,
            'reporting_group': self.reporting_group,
            'source_groupid': self.source_groupid,
            'source_group': self.source_group,
            'discoverydate': self.discoverydate,
            'discoverymag': self.discoverymag,
            'discmagfilter': self.discmagfilter,
            'filtername': self.filtername,
            'reporters': self.reporters,
            'time_received': self.time_received,
            'internal_names': self.internal_names,
            'creationdate': self.creationdate,
            'lastmodified': self.lastmodified,
            'class_name': self.class_name,
            'class_prob': self.class_prob,
            'dpng': self.dpng,
            'spng': self.spng,
            'tpng': self.tpng,
            'sid': self.sid
        }

    # +
    # (overload) method: __str__()
    # -
    def __str__(self):
        return f'{self.zcandid}'

    # +
    # (static) method: serialize_list()
    # -
    @staticmethod
    def serialize_list(slist=None):
        return [_a.serialized() for _a in slist]
