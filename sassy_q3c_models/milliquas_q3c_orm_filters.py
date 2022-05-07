#!/usr/bin/env python3


# +
# import(s)
# -
from sassy_q3c_models.milliquas_q3c_orm import *


# +
# function: milliquas_q3c_orm_filters()
# -
# noinspection PyBroadException
def milliquas_q3c_orm_filters(query: Any = None, request_args: dict = None):

    # return records within astrocone search (API: ?astrocone=M51,5.0)
    if request_args.get('astrocone'):
        try:
            _nam, _rad = request_args['astrocone'].split(',')
            _val = get_astropy_coords(_nam.strip().upper())
            if _val is not None:
                query = query.filter(func.q3c_radial_query(
                    MilliQuasQ3cRecord.ra, MilliQuasQ3cRecord.dec, float(_val[0]), float(_val[1]), float(_rad)))
        except:
            pass

    # return records within cone search (API: ?cone=23.5,29.2,5.0)
    if request_args.get('cone'):
        try:
            _ra, _dec, _rad = request_args['cone'].split(',')
            query = query.filter(func.q3c_radial_query(
                MilliQuasQ3cRecord.ra, MilliQuasQ3cRecord.dec, float(_ra), float(_dec), float(_rad)))
        except:
            pass

    # return records within ellipse search (API: ?ellipse=202.1,47.2,5.0,0.5,25.0)
    if request_args.get('ellipse'):
        try:
            _ra, _dec, _maj, _rat, _pos = request_args['ellipse'].split(',')
            query = query.filter(func.q3c_ellipse_query(
                MilliQuasQ3cRecord.ra, MilliQuasQ3cRecord.dec, float(_ra), float(_dec), float(_maj),
                float(_rat), float(_pos)))
        except:
            pass

    # return records with mid = value (API: ?mid=20)
    if request_args.get('mid'):
        query = query.filter(MilliQuasQ3cRecord.mid == int(request_args['mid']))

    # return records with name like value (API: ?name=demo)
    if request_args.get('name'):
        query = query.filter(or_(
            MilliQuasQ3cRecord.name.ilike(f"%{request_args['name']}%"),
            MilliQuasQ3cRecord.xname.ilike(f"%{request_args['name']}%"),
            MilliQuasQ3cRecord.rname.ilike(f"%{request_args['name']}%"),
            MilliQuasQ3cRecord.lobe1.ilike(f"%{request_args['name']}%"),
            MilliQuasQ3cRecord.lobe2.ilike(f"%{request_args['name']}%")))

    # return records with type like value (API: ?type=demo)
    if request_args.get('type'):
        query = query.filter(MilliQuasQ3cRecord.objtype.ilike(f"%{request_args['type']}%"))

    # return records with ra >= value (API: ?ra__gte=0.0)
    if request_args.get('ra__gte'):
        query = query.filter(MilliQuasQ3cRecord.ra >= float(request_args['ra__gte']))

    # return records with ra <= value (API: ?ra__lte=360.0)
    if request_args.get('ra__lte'):
        query = query.filter(MilliQuasQ3cRecord.ra <= float(request_args['ra__lte']))

    # return records with dec >= value (API: ?dec__gte=-90.0)
    if request_args.get('dec__gte'):
        query = query.filter(MilliQuasQ3cRecord.dec >= float(request_args['dec__gte']))

    # return records with dec <= value (API: ?dec__lte=90.0)
    if request_args.get('dec__lte'):
        query = query.filter(MilliQuasQ3cRecord.dec <= float(request_args['dec__lte']))

    # return records with r >= value (API: ?r__gte=12.5)
    if request_args.get('r__gte'):
        query = query.filter(MilliQuasQ3cRecord.rmag >= float(request_args['r__gte']))

    # return records with r <= value (API: ?r__lte=12.5)
    if request_args.get('r__lte'):
        query = query.filter(MilliQuasQ3cRecord.rmag <= float(request_args['r__lte']))

    # return records with b >= value (API: ?b__gte=12.5)
    if request_args.get('b__gte'):
        query = query.filter(MilliQuasQ3cRecord.bmag >= float(request_args['b__gte']))

    # return records with b <= value (API: ?b__lte=12.5)
    if request_args.get('b__lte'):
        query = query.filter(MilliQuasQ3cRecord.bmag <= float(request_args['b__lte']))

    # return records with q >= value (API: ?q__gte=75)
    if request_args.get('q__gte'):
        query = query.filter(MilliQuasQ3cRecord.qpct >= int(request_args['q__gte']))

    # return records with q <= value (API: ?q__lte=75)
    if request_args.get('q__lte'):
        query = query.filter(MilliQuasQ3cRecord.qpct <= int(request_args['q__lte']))

    # return records with z >= value (API: ?z__gte=0.5)
    if request_args.get('z__gte'):
        query = query.filter(MilliQuasQ3cRecord.z >= float(request_args['z__gte']))

    # return records with z <= value (API: ?z__lte=0.5)
    if request_args.get('z__lte'):
        query = query.filter(MilliQuasQ3cRecord.z <= float(request_args['z__lte']))

    # sort results
    sort_value = request_args.get('sort_value', MILLIQUAS_SORT_VALUE[0]).lower()
    sort_order = request_args.get('sort_order', MILLIQUAS_SORT_ORDER[0]).lower()
    if sort_order in MILLIQUAS_SORT_ORDER:
        if sort_order.startswith(MILLIQUAS_SORT_ORDER[0]):
            query = query.order_by(getattr(MilliQuasQ3cRecord, sort_value).asc())
        elif sort_order.startswith(MILLIQUAS_SORT_ORDER[1]):
            query = query.order_by(getattr(MilliQuasQ3cRecord, sort_value).desc())

    # return query
    return query
