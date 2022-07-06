#!/usr/bin/env python3


# +
#  import(s)
# -
# noinspection PyUnresolvedReferences
from astropy.coordinates import SkyCoord
# noinspection PyUnresolvedReferences
from astropy.time import Time
# noinspection PyUnresolvedReferences
from datetime import datetime
# noinspection PyUnresolvedReferences
from datetime import timedelta
# noinspection PyUnresolvedReferences
from flask_sqlalchemy import SQLAlchemy
# noinspection PyUnresolvedReferences
from sqlalchemy import create_engine
# noinspection PyUnresolvedReferences
from sqlalchemy import func
# noinspection PyUnresolvedReferences
from sqlalchemy import or_
# noinspection PyUnresolvedReferences
from sqlalchemy.orm import sessionmaker
# noinspection PyUnresolvedReferences
from typing import Any
# noinspection PyUnresolvedReferences
from typing import Optional

# noinspection PyUnresolvedReferences
import argparse
# noinspection PyUnresolvedReferences
import csv
# noinspection PyUnresolvedReferences
import fastavro
# noinspection PyUnresolvedReferences
import glob
# noinspection PyUnresolvedReferences
import gzip
# noinspection PyUnresolvedReferences
import os
# noinspection PyUnresolvedReferences
import math
# noinspection PyUnresolvedReferences
import pprint
# noinspection PyUnresolvedReferences
import psycopg2
# noinspection PyUnresolvedReferences
import psycopg2.extras
# noinspection PyUnresolvedReferences
import random
# noinspection PyUnresolvedReferences
import requests
# noinspection PyUnresolvedReferences
import urllib.request


# +
# credential(s)
# -
# noinspection PyBroadException
try:
    DB_AVRO = os.getenv('DB_AVRO', f'{os.getcwd()}')
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_NAME = os.getenv('DB_NAME', None)
    DB_PASS = os.getenv('DB_PASS', None)
    DB_PORT = int(os.getenv('DB_PORT', 5432))
    DB_USER = os.getenv('DB_USER', None)
except:
    DB_AVRO = f'{os.getcwd()}'
    DB_HOST = 'localhost'
    DB_NAME = None
    DB_PASS = None
    DB_PORT = 5432
    DB_USER = None


# +
# initialize
# -
random.seed(os.getpid())


# +
# constant(s)
# -
DB_VARCHAR_1 = 1
DB_VARCHAR_2 = 2
DB_VARCHAR_4 = 4
DB_VARCHAR_8 = 8
DB_VARCHAR_16 = 16
DB_VARCHAR_24 = 24
DB_VARCHAR_32 = 32
DB_VARCHAR_64 = 64
DB_VARCHAR_128 = 128
DB_VARCHAR_256 = 256
DB_VARCHAR_512 = 512
DB_VARCHAR_1024 = 1024
DB_VARCHAR_2048 = 2048

DB_VARCHAR_10 = 10
DB_VARCHAR_20 = 20
DB_VARCHAR_25 = 25
DB_VARCHAR_30 = 30
DB_VARCHAR_40 = 40
DB_VARCHAR_45 = 45
DB_VARCHAR_200 = 200

DEGREE = "\u00B0"
MARKERS = ["o", "*", "d", "s", "+", "x"]
ORIGIN = 180.0
SQUARE = "\u25AB"
UPPER_H = "\u02B0"


# +
# function: get_astropy_coords()
# -
# noinspection PyBroadException
def get_astropy_coords(_oname: str = '') -> Optional[tuple]:
    """ return tuple of (RA, Dec) in decimal or None """
    try:
        _obj = SkyCoord.from_name(_oname)
        return float(_obj.ra.value), float(_obj.dec.value)
    except:
        pass


# +
# function: get_data()
# -
def get_data(_url: str = '', _file: str = '') -> None:
    """ write data from website to file """
    if _url.strip().lower().startswith('http') and _file.strip() != '':
        with open(_file, 'wb') as _fw:
            _fw.write(urllib.request.urlopen(_url).read())


# +
# function: get_gzip()
# -
def get_gzip(_url: str = '', _file: str = '') -> None:
    """ write gzip data from website to file """
    if _url.strip().lower().startswith('http') and _file.strip() != '':
        with open(_file, 'w') as _fw:
            _fw.write(f"{gzip.decompress(urllib.request.urlopen(_url).read()).decode('utf-8')}")


# +
# function: get_simbad2k_coords()
# -
# noinspection PyBroadException
def get_simbad2k_coords(_oname: str = '') -> Optional[tuple]:
    """ return tuple of (RA, Dec) in decimal or None """
    try:
        response = requests.get(f'https://simbad2k.lco.global/{_oname}?target_type=sidereal')
        response.raise_for_status()
        result = response.json()
        return float(result['ra_d']), float(result['dec_d'])
    except:
        pass


# +
# function: get_utc()
# -
# noinspection PyBroadException
def get_utc(ndays: int = 0) -> Optional[str]:
    """ return date in isot format for any ndays offset """
    try:
        return (datetime.utcnow() + timedelta(days=ndays)).isoformat()
    except:
        pass


# +
# function: verify_keys()
# -
# noinspection PyBroadException
def verify_keys(_d: dict = None, _s: set = None) -> bool:
    """ verify all keys in list are present in dictionary """
    try:
        return all(_k in _d for _k in _s)
    except:
        return False
