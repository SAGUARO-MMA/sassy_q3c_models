#!/usr/bin/env python3


# +
# import(s)
# -
from sassy_q3c_models.tns_q3c_orm import *


# +
# function: tns_q3c_orm_filters()
# -
# noinspection PyBroadException
def tns_q3c_orm_filters(query: Any = None, request_args: dict = None):

    # return records within astrocone search (API: ?astrocone=M51,5.0)
    if request_args.get('astrocone'):
        try:
            _nam, _rad = request_args['astrocone'].split(',')
            _val = get_astropy_coords(_nam.strip().upper())
            if _val is not None:
                query = query.filter(func.q3c_radial_query(
                    TnsQ3cRecord.ra, TnsQ3cRecord.declination, float(_val[0]), float(_val[1]), float(_rad)))
        except:
            pass

    # return records within cone search (API: ?cone=23.5,29.2,5.0)
    if request_args.get('cone'):
        try:
            _ra, _dec, _rad = request_args['cone'].split(',')
            query = query.filter(func.q3c_radial_query(
                TnsQ3cRecord.ra, TnsQ3cRecord.declination, float(_ra), float(_dec), float(_rad)))
        except:
            pass

    # return records within ellipse search (API: ?ellipse=202.1,47.2,5.0,0.5,25.0)
    if request_args.get('ellipse'):
        try:
            _ra, _dec, _maj, _rat, _pos = request_args['ellipse'].split(',')
            query = query.filter(func.q3c_ellipse_query(
                TnsQ3cRecord.ra, TnsQ3cRecord.declination, float(_ra), float(_dec), float(_maj),
                float(_rat), float(_pos)))
        except:
            pass

    # return records with tid = value (API: ?tid=20)
    if request_args.get('tid'):
        query = query.filter(TnsQ3cRecord.tid == int(request_args['tid']))

    # return records with name like value (API: ?name=demo)
    if request_args.get('name'):
        query = query.filter(or_(
            TnsQ3cRecord.name_prefix.ilike(f"%{request_args['name']}%"),
            TnsQ3cRecord.name.ilike(f"%{request_args['name']}%"),
            TnsQ3cRecord.internal_names.ilike(f"%{request_args['name']}%")))

    # return records with report like value (API: ?report=demo)
    if request_args.get('report'):
        query = query.filter(or_(
            TnsQ3cRecord.reporters.ilike(f"%{request_args['report']}%"),
            TnsQ3cRecord.reporting_group.ilike(f"%{request_args['report']}%"),
            TnsQ3cRecord.source_group.ilike(f"%{request_args['report']}%")))

    # return records with ra >= value (API: ?ra__gte=0.0)
    if request_args.get('ra__gte'):
        query = query.filter(TnsQ3cRecord.ra >= float(request_args['ra__gte']))

    # return records with ra <= value (API: ?ra__lte=360.0)
    if request_args.get('ra__lte'):
        query = query.filter(TnsQ3cRecord.ra <= float(request_args['ra__lte']))

    # return records with dec >= value (API: ?dec__gte=-90.0)
    if request_args.get('dec__gte'):
        query = query.filter(TnsQ3cRecord.declination >= float(request_args['dec__gte']))

    # return records with dec <= value (API: ?dec__lte=90.0)
    if request_args.get('dec__lte'):
        query = query.filter(TnsQ3cRecord.declination <= float(request_args['dec__lte']))

    # return records with z >= value (API: ?z__gte=0.5)
    if request_args.get('z__gte'):
        query = query.filter(TnsQ3cRecord.redshift >= float(request_args['z__gte']))

    # return records with z <= value (API: ?z__lte=0.5)
    if request_args.get('z__lte'):
        query = query.filter(TnsQ3cRecord.redshift <= float(request_args['z__lte']))

    # sort results
    sort_value = request_args.get('sort_value', TNS_SORT_VALUE[0]).lower()
    sort_order = request_args.get('sort_order', TNS_SORT_ORDER[0]).lower()
    if sort_order in TNS_SORT_ORDER:
        if sort_order.startswith(TNS_SORT_ORDER[0]):
            query = query.order_by(getattr(TnsQ3cRecord, sort_value).asc())
        elif sort_order.startswith(TNS_SORT_ORDER[1]):
            query = query.order_by(getattr(TnsQ3cRecord, sort_value).desc())

    # return query
    return query
