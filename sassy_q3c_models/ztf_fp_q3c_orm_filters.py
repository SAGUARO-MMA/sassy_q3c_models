#!/usr/bin/env python3


# +
# import(s)
# -
from sassy_q3c_models.ztf_fp_q3c_orm import *


# +
# function: ztf_fp_q3c_orm_filters()
# -
# noinspection PyBroadException
def ztf_fp_q3c_orm_filters(query: Any = None, request_args: dict = None):

    # return records within astrocone search (API: ?astrocone=M51,5.0)
    if request_args.get('astrocone'):
        try:
            _nam, _rad = request_args['astrocone'].split(',')
            _val = get_astropy_coords(_nam.strip().upper())
            if _val is not None:
                query = query.filter(func.q3c_radial_query(
                    ZtfFpQ3cRecord.ranr, ZtfFpQ3cRecord.decnr, float(_val[0]), float(_val[1]), float(_rad)))
        except:
            pass

    # return records within cone search (API: ?cone=23.5,29.2,5.0)
    if request_args.get('cone'):
        try:
            _ra, _dec, _rad = request_args['cone'].split(',')
            query = query.filter(func.q3c_radial_query(
                ZtfFpQ3cRecord.ranr, ZtfFpQ3cRecord.decnr, float(_ra), float(_dec), float(_rad)))
        except:
            pass

    # return records within ellipse search (API: ?ellipse=202.1,47.2,5.0,0.5,25.0)
    if request_args.get('ellipse'):
        try:
            _ra, _dec, _maj, _rat, _pos = request_args['ellipse'].split(',')
            query = query.filter(func.q3c_ellipse_query(
                ZtfFpQ3cRecord.ranr, ZtfFpQ3cRecord.decnr, float(_ra), float(_dec), float(_maj),
                float(_rat), float(_pos)))
        except:
            pass
    # return records with a given fpid (API: ?fpid=1)
    if request_args.get('fpid'):
        query = query.filter(ZtfFpQ3cRecord.fpid == int(request_args['fpid']))

    # return records with a given field (API: ?field=1)
    if request_args.get('field'):
        query = query.filter(ZtfFpQ3cRecord.field == int(request_args['field']))

    # return records with a given fid (API: ?fid=1)
    if request_args.get('fid'):
        query = query.filter(ZtfFpQ3cRecord.fid == int(request_args['fid']))

    # return records with a JD >= date (API: ?jd__gte=2458302.6906713)
    if request_args.get('jd__gte'):
        query = query.filter(ZtfFpQ3cRecord.jd >= request_args['jd__gte'])

    # return records with a JD <= date (API: ?jd__lte=2458302.6906713)
    if request_args.get('jd__lte'):
        query = query.filter(ZtfFpQ3cRecord.jd <= request_args['jd__lte'])

    # sort results
    sort_by = request_args.get('sort_value', 'jd')
    sort_order = request_args.get('sort_order', 'desc')
    if sort_order == 'desc':
        query = query.order_by(getattr(ZtfFpQ3cRecord, sort_by).desc())
    elif sort_order == 'asc':
        query = query.order_by(getattr(ZtfFpQ3cRecord, sort_by).asc())

    # return query
    return query
