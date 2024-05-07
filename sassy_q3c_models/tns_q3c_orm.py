#!/usr/bin/env python3


# +
# import(s)
# -
from sassy_q3c_models import *


# +
# __doc__ string
# -
__doc__ = """
                                                                  Table "public.tns_q3c"
        Column         |            Type             | Collation | Nullable |               Default                | Storage  | Stats target | Description 
-----------------------+-----------------------------+-----------+----------+--------------------------------------+----------+--------------+-------------
 tid                   | integer                     |           | not null | nextval('tns_q3c_tid_seq'::regclass) | plain    |              | 
 objid                 | integer                     |           |          |                                      | plain    |              | 
 name_prefix           | character varying(4)        |           |          |                                      | extended |              | 
 name                  | character varying(32)       |           |          |                                      | extended |              | 
 ra                    | double precision            |           |          |                                      | plain    |              | 
 declination           | double precision            |           |          |                                      | plain    |              | 
 redshift              | double precision            |           |          |                                      | plain    |              | 
 typeid                | integer                     |           |          |                                      | plain    |              | 
 objtype               | character varying(32)       |           |          |                                      | extended |              | 
 reporting_groupid     | integer                     |           |          |                                      | plain    |              | 
 reporting_group       | character varying(32)       |           |          |                                      | extended |              | 
 source_groupid        | integer                     |           |          |                                      | plain    |              | 
 source_group          | character varying(32)       |           |          |                                      | extended |              | 
 discoverydate         | timestamp without time zone |           |          |                                      | plain    |              | 
 discoverymag          | double precision            |           |          |                                      | plain    |              | 
 discmagfilter         | integer                     |           |          |                                      | plain    |              | 
 filtername            | character varying(24)       |           |          |                                      | extended |              | 
 reporters             | character varying(2048)     |           |          |                                      | extended |              | 
 time_received         | timestamp without time zone |           |          |                                      | plain    |              | 
 internal_names        | character varying(256)      |           |          |                                      | extended |              | 
 discovery_ads_bibcode | character varying(256)      |           |          |                                      | extended |              | 
 class_ads_bibcodes    | character varying(256)      |           |          |                                      | extended |              | 
 creationdate          | timestamp without time zone |           |          |                                      | plain    |              | 
 lastmodified          | timestamp without time zone |           |          |                                      | plain    |              | 
Indexes:
    "tns_q3c_pkey" PRIMARY KEY, btree (tid)
    "tns_q3c_q3c_ang2ipix_idx" btree (q3c_ang2ipix(ra, declination)) CLUSTER
Access method: heap
"""


# +
# constant(s)
# -
TNS_COLUMNS = 23
TNS_DAT_URL = "https://www.wis-tns.org/system/files/tns_public_objects/tns_public_objects.csv.zip"
TNS_PAG_URL = "https://www.wis-tns.org"
TNS_PDF_URL = "https://www.wis-tns.org/sites/default/files/presentations/TNS_LSSTC_Brokers_workshop_Apr_2021.pdf"
TNS_SORT_ORDER = ['asc', 'desc', 'ascending', 'descending']
TNS_SORT_VALUE = ['tid', 'name', 'ra', 'dec', 'redshift']
TNS_HEADERS = ('tid', 'objid', 'name_prefix', 'name', 'ra', 'declination', 'redshift', 'typeid', 'objtype',
               'reporting_groupid', 'reporting_group', 'source_groupid', 'source_group', 'discoverydate',
               'discoverymag', 'discmagfilter', 'filtername', 'reporters', 'time_received', 'internal_names',
               'Discovery_ADS_bibcode', 'Class_ADS_bibcodes', 'creationdate', 'lastmodified')

# +
# initialize sqlalchemy (deferred)
# -
db = SQLAlchemy()


# +
# class: TnsQ3cRecord(), inherits from db.Model
# -
# noinspection PyUnresolvedReferences
class TnsQ3cRecord(db.Model):

    # +
    # define table
    # -
    __tablename__ = 'tns_q3c'
    tid = db.Column(db.Integer, primary_key=True)
    objid = db.Column(db.Integer)
    name_prefix = db.Column(db.String(DB_VARCHAR_4))
    name = db.Column(db.String(DB_VARCHAR_32))
    ra = db.Column(db.Float)
    declination = db.Column(db.Float)
    redshift = db.Column(db.Float)
    typeid = db.Column(db.Integer)
    objtype = db.Column(db.String(DB_VARCHAR_32))
    reporting_groupid = db.Column(db.Integer)
    reporting_group = db.Column(db.String(DB_VARCHAR_32))
    source_groupid = db.Column(db.Integer)
    source_group = db.Column(db.String(DB_VARCHAR_32))
    discoverydate = db.Column(db.DateTime)
    discoverymag = db.Column(db.Float)
    discmagfilter = db.Column(db.Integer)
    filtername = db.Column(db.String(DB_VARCHAR_24))
    reporters = db.Column(db.String(DB_VARCHAR_2048))
    time_received = db.Column(db.DateTime)
    internal_names = db.Column(db.String(DB_VARCHAR_256))
    discovery_ads_bibcode = db.Column(db.String(DB_VARCHAR_256))
    class_ads_bibcodes = db.Column(db.String(DB_VARCHAR_256))
    creationdate = db.Column(db.DateTime)
    lastmodified = db.Column(db.DateTime)

    # +
    # method: serialized()
    # -
    def serialized(self):
        return {
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
            'discovery_ads_bibcode': self.discovery_ads_bibcode,
            'class_ads_bibcodes': self.class_ads_bibcodes,
            'creationdate': self.creationdate,
            'lastmodified': self.lastmodified
        }

    # +
    # (overload) method: __str__()
    # -
    def __str__(self):
        return self.tid

    # +
    # (static) method: serialize_list()
    # -
    @staticmethod
    def serialize_list(m_records):
        return [_a.serialized() for _a in m_records]
