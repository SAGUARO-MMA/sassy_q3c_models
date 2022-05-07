#!/usr/bin/env python3


# +
# import(s)
# -
from sassy_q3c_models.hecate_q3c_orm import *


# +
# function: hecate_q3c_orm_filters()
# -
# noinspection PyBroadException
def hecate_q3c_orm_filters(query: Any = None, request_args: dict = None):

    # return records within astrocone search (API: ?astrocone=M51,5.0)
    if request_args.get('astrocone'):
        try:
            _nam, _rad = request_args['astrocone'].split(',')
            _val = get_astropy_coords(_nam.strip().upper())
            if _val is not None:
                query = query.filter(func.q3c_radial_query(
                    HecateQ3cRecord.ra, HecateQ3cRecord.dec, float(_val[0]), float(_val[1]), float(_rad)))
        except:
            pass

    # return records within cone search (API: ?cone=23.5,29.2,5.0)
    if request_args.get('cone'):
        try:
            _ra, _dec, _rad = request_args['cone'].split(',')
            query = query.filter(func.q3c_radial_query(
                HecateQ3cRecord.ra, HecateQ3cRecord.dec, float(_ra), float(_dec), float(_rad)))
        except:
            pass

    # return records within ellipse search (API: ?ellipse=202.1,47.2,5.0,0.5,25.0)
    if request_args.get('ellipse'):
        try:
            _ra, _dec, _maj, _rat, _pos = request_args['ellipse'].split(',')
            query = query.filter(
                func.q3c_ellipse_query(
                    HecateQ3cRecord.ra, HecateQ3cRecord.dec, float(_ra), float(_dec), float(_maj),
                    float(_rat), float(_pos)))
        except:
            pass

    # return records with hid = value (API: ?hid=20)
    if request_args.get('hid'):
        query = query.filter(HecateQ3cRecord.hid == int(request_args['hid']))

    # return records with name like value (API: ?name=demo)
    if request_args.get('name'):
        query = query.filter(or_(
            HecateQ3cRecord.objname.ilike(f"%{request_args['name']}%"),
            HecateQ3cRecord.id_ned.ilike(f"%{request_args['name']}%"),
            HecateQ3cRecord.id_nedd.ilike(f"%{request_args['name']}%"),
            HecateQ3cRecord.id_iras.ilike(f"%{request_args['name']}%"),
            HecateQ3cRecord.id_2mass.ilike(f"%{request_args['name']}%"),
            HecateQ3cRecord.sdss_photid.ilike(f"%{request_args['name']}%"),
            HecateQ3cRecord.sdss_specid.ilike(f"%{request_args['name']}%")))

    # return records with ra >= value (API: ?ra__gte=0.0)
    if request_args.get('ra__gte'):
        query = query.filter(HecateQ3cRecord.ra >= float(request_args['ra__gte']))

    # return records with ra <= value (API: ?ra__lte=360.0)
    if request_args.get('ra__lte'):
        query = query.filter(HecateQ3cRecord.ra <= float(request_args['ra__lte']))

    # return records with dec >= value (API: ?dec__gte=-90.0)
    if request_args.get('dec__gte'):
        query = query.filter(HecateQ3cRecord.dec >= float(request_args['dec__gte']))

    # return records with dec <= value (API: ?dec__lte=90.0)
    if request_args.get('dec__lte'):
        query = query.filter(HecateQ3cRecord.dec <= float(request_args['dec__lte']))

    # return records with d >= value (API: ?d__gte=50.5)
    if request_args.get('d__gte'):
        query = query.filter(HecateQ3cRecord.d >= float(request_args['d__gte']))

    # return records with d <= value (API: ?d__lte=50.5)
    if request_args.get('d__lte'):
        query = query.filter(HecateQ3cRecord.d <= float(request_args['d__lte']))

    # return records with ut >= value (API: ?ut=12.5)
    if request_args.get('ut__gte'):
        query = query.filter(HecateQ3cRecord.ut >= float(request_args['ut__gte']))

    # return records with ut <= value (API: ?ut=12.5)
    if request_args.get('ut__lte'):
        query = query.filter(HecateQ3cRecord.ut <= float(request_args['ut__lte']))

    # return records with bt >= value (API: ?bt=12.5)
    if request_args.get('bt__gte'):
        query = query.filter(HecateQ3cRecord.bt >= float(request_args['bt__gte']))

    # return records with bt <= value (API: ?bt=12.5)
    if request_args.get('bt__lte'):
        query = query.filter(HecateQ3cRecord.bt <= float(request_args['bt__lte']))

    # return records with vt >= value (API: ?vt=12.5)
    if request_args.get('vt__gte'):
        query = query.filter(HecateQ3cRecord.vt >= float(request_args['vt__gte']))

    # return records with vt <= value (API: ?vt=12.5)
    if request_args.get('vt__lte'):
        query = query.filter(HecateQ3cRecord.vt <= float(request_args['vt__lte']))

    # return records with it >= value (API: ?it=12.5)
    if request_args.get('it__gte'):
        query = query.filter(HecateQ3cRecord.it >= float(request_args['it__gte']))

    # return records with it <= value (API: ?it=12.5)
    if request_args.get('it__lte'):
        query = query.filter(HecateQ3cRecord.it <= float(request_args['it__lte']))

    # return records with j >= value (API: ?j__gte=13.5)
    if request_args.get('j__gte'):
        query = query.filter(HecateQ3cRecord.j >= float(request_args['j__gte']))

    # return records with j <= value (API: ?j__lte=13.5)
    if request_args.get('j__lte'):
        query = query.filter(HecateQ3cRecord.j <= float(request_args['j__lte']))

    # return records with h >= value (API: ?h__gte=12.5)
    if request_args.get('h__gte'):
        query = query.filter(HecateQ3cRecord.h >= float(request_args['h__gte']))

    # return records with h <= value (API: ?h__lte=12.5)
    if request_args.get('h__lte'):
        query = query.filter(HecateQ3cRecord.h <= float(request_args['h__lte']))

    # return records with k >= value (API: ?k__gte=14.5)
    if request_args.get('k__gte'):
        query = query.filter(HecateQ3cRecord.k >= float(request_args['k__gte']))

    # return records with k <= value (API: ?k__lte=14.5)
    if request_args.get('k__lte'):
        query = query.filter(HecateQ3cRecord.k <= float(request_args['k__lte']))

    # return records with u >= value (API: ?u=12.5)
    if request_args.get('u__gte'):
        query = query.filter(HecateQ3cRecord.u >= float(request_args['u__gte']))

    # return records with u <= value (API: ?u=12.5)
    if request_args.get('u__lte'):
        query = query.filter(HecateQ3cRecord.u <= float(request_args['u__lte']))

    # return records with g >= value (API: ?g=12.5)
    if request_args.get('g__gte'):
        query = query.filter(HecateQ3cRecord.u >= float(request_args['g__gte']))

    # return records with g <= value (API: ?g=12.5)
    if request_args.get('g__lte'):
        query = query.filter(HecateQ3cRecord.g <= float(request_args['g__lte']))

    # return records with r >= value (API: ?r=12.5)
    if request_args.get('r__gte'):
        query = query.filter(HecateQ3cRecord.r >= float(request_args['r__gte']))

    # return records with r <= value (API: ?r=12.5)
    if request_args.get('r__lte'):
        query = query.filter(HecateQ3cRecord.r <= float(request_args['r__lte']))

    # return records with i >= value (API: ?i=12.5)
    if request_args.get('i__gte'):
        query = query.filter(HecateQ3cRecord.i >= float(request_args['i__gte']))

    # return records with i <= value (API: ?i=12.5)
    if request_args.get('i__lte'):
        query = query.filter(HecateQ3cRecord.i <= float(request_args['i__lte']))

    # return records with z >= value (API: ?z=12.5)
    if request_args.get('z__gte'):
        query = query.filter(HecateQ3cRecord.z >= float(request_args['z__gte']))

    # return records with z <= value (API: ?z=12.5)
    if request_args.get('z__lte'):
        query = query.filter(HecateQ3cRecord.z <= float(request_args['z__lte']))

    # sort results
    sort_value = request_args.get('sort_value', HECATE_SORT_VALUE[0]).lower()
    sort_order = request_args.get('sort_order', HECATE_SORT_ORDER[0]).lower()
    if sort_order in HECATE_SORT_ORDER:
        if sort_order.startswith(HECATE_SORT_ORDER[0]):
            query = query.order_by(getattr(HecateQ3cRecord, sort_value).asc())
        elif sort_order.startswith(HECATE_SORT_ORDER[1]):
            query = query.order_by(getattr(HecateQ3cRecord, sort_value).desc())

    # return query
    return query
