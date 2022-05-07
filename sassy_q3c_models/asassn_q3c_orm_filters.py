#!/usr/bin/env python3


# +
# import(s)
# -
from sassy_q3c_models.asassn_q3c_orm import *


# +
# function: asassn_q3c_orm_filters()
# -
# noinspection PyBroadException
def asassn_q3c_orm_filters(query: Any = None, request_args: dict = None):

    # return records within astrocone search (API: ?astrocone=M51,5.0)
    if request_args.get('astrocone'):
        try:
            _nam, _rad = request_args['astrocone'].split(',')
            _val = get_astropy_coords(_nam.strip().upper())
            if _val is not None:
                query = query.filter(func.q3c_radial_query(
                    AsAssnQ3cRecord.ra, AsAssnQ3cRecord.dec, float(_val[0]), float(_val[1]), float(_rad)))
        except:
            pass

    # return records within cone search (API: ?cone=23.5,29.2,5.0)
    if request_args.get('cone'):
        try:
            _ra, _dec, _rad = request_args['cone'].split(',')
            query = query.filter(func.q3c_radial_query(
                AsAssnQ3cRecord.ra, AsAssnQ3cRecord.dec, float(_ra), float(_dec), float(_rad)))
        except:
            pass

    # return records within ellipse search (API: ?ellipse=202.1,47.2,5.0,0.5,25.0)
    if request_args.get('ellipse'):
        try:
            _ra, _dec, _maj, _rat, _pos = request_args['ellipse'].split(',')
            query = query.filter(func.q3c_ellipse_query(
                AsAssnQ3cRecord.ra, AsAssnQ3cRecord.dec, float(_ra), float(_dec), float(_maj),
                float(_rat), float(_pos)))
        except:
            pass

    # return records with aid = value (API: ?aid=20)
    if request_args.get('aid'):
        query = query.filter(AsAssnQ3cRecord.aid == int(request_args['aid']))

    # return records with name like value (API: ?name=demo)
    if request_args.get('name'):
        query = query.filter(or_(
            AsAssnQ3cRecord.asassn_id.ilike(f"%{request_args['name']}%"),
            AsAssnQ3cRecord.source_id.ilike(f"%{request_args['name']}%"),
            AsAssnQ3cRecord.asassn_name.ilike(f"%{request_args['name']}%"),
            AsAssnQ3cRecord.other_names.ilike(f"%{request_args['name']}%"),
            AsAssnQ3cRecord.allwise_id.ilike(f"%{request_args['name']}%"),
            AsAssnQ3cRecord.edr3_source_id.ilike(f"%{request_args['name']}%"),
            AsAssnQ3cRecord.galex_id.ilike(f"%{request_args['name']}%"),
            AsAssnQ3cRecord.tic_id.ilike(f"%{request_args['name']}%")))

    # return records with ra >= value (API: ?ra__gte=0.0)
    if request_args.get('ra__gte'):
        query = query.filter(AsAssnQ3cRecord.ra >= float(request_args['ra__gte']))

    # return records with ra <= value (API: ?ra__lte=360.0)
    if request_args.get('ra__lte'):
        query = query.filter(AsAssnQ3cRecord.ra <= float(request_args['ra__lte']))

    # return records with dec >= value (API: ?dec__gte=-90.0)
    if request_args.get('dec__gte'):
        query = query.filter(AsAssnQ3cRecord.dec >= float(request_args['dec__gte']))

    # return records with dec <= value (API: ?dec__lte=90.0)
    if request_args.get('dec__lte'):
        query = query.filter(AsAssnQ3cRecord.dec <= float(request_args['dec__lte']))

    # return records with dist >= value (API: ?dist__gte=0.0)
    if request_args.get('dist__gte'):
        query = query.filter(AsAssnQ3cRecord.dist >= float(request_args['dist__gte']))

    # return records with dist <= value (API: ?dist__lte=50.0)
    if request_args.get('dist__lte'):
        query = query.filter(AsAssnQ3cRecord.dist <= float(request_args['dist__lte']))

    # return records with j >= value (API: ?j__gte=12.5)
    if request_args.get('j__gte'):
        query = query.filter(AsAssnQ3cRecord.j_mag >= float(request_args['j__gte']))

    # return records with j <= value (API: ?j__lte=12.5)
    if request_args.get('j__lte'):
        query = query.filter(AsAssnQ3cRecord.j_mag <= float(request_args['j__lte']))

    # return records with h >= value (API: ?h__gte=12.5)
    if request_args.get('h__gte'):
        query = query.filter(AsAssnQ3cRecord.h_mag >= float(request_args['h__gte']))

    # return records with h <= value (API: ?h__lte=12.5)
    if request_args.get('h__lte'):
        query = query.filter(AsAssnQ3cRecord.h_mag <= float(request_args['h__lte']))

    # return records with k >= value (API: ?k__gte=12.5)
    if request_args.get('k__gte'):
        query = query.filter(AsAssnQ3cRecord.k_mag >= float(request_args['k__gte']))

    # return records with k <= value (API: ?k__lte=12.5)
    if request_args.get('k__lte'):
        query = query.filter(AsAssnQ3cRecord.k_mag <= float(request_args['k__lte']))

    # return records with v >= value (API: ?v__gte=12.5)
    if request_args.get('v__gte'):
        query = query.filter(AsAssnQ3cRecord.mean_vmag >= float(request_args['v__gte']))

    # return records with v <= value (API: ?v__lte=12.5)
    if request_args.get('v__lte'):
        query = query.filter(AsAssnQ3cRecord.mean_vmag <= float(request_args['v__lte']))

    # return records with amplitude >= value (API: ?amplitude__gte=12.5)
    if request_args.get('amplitude__gte'):
        query = query.filter(AsAssnQ3cRecord.amplitude >= float(request_args['amplitude__gte']))

    # return records with amplitude <= value (API: ?amplitude__lte=12.5)
    if request_args.get('amplitude__lte'):
        query = query.filter(AsAssnQ3cRecord.amplitude <= float(request_args['amplitude__lte']))

    # return records with period >= value (API: ?period__gte=13.5)
    if request_args.get('period__gte'):
        query = query.filter(AsAssnQ3cRecord.period >= float(request_args['period__gte']))

    # return records with period__lte <= value (API: ?period__lte=13.5)
    if request_args.get('period__lte'):
        query = query.filter(AsAssnQ3cRecord.period <= float(request_args['period__lte']))

    # return records with lksl >= value (API: ?lksl__gte=12.5)
    if request_args.get('lksl__gte'):
        query = query.filter(AsAssnQ3cRecord.lksl_statistic >= float(request_args['lksl__gte']))

    # return records with lksl <= value (API: ?lksl__lte=12.5)
    if request_args.get('lksl__lte'):
        query = query.filter(AsAssnQ3cRecord.lksl_statistic <= float(request_args['lksl__lte']))

    # return records with parallax >= value (API: ?parallax__gte=14.5)
    if request_args.get('parallax__gte'):
        query = query.filter(AsAssnQ3cRecord.parallax >= float(request_args['parallax__gte']))

    # return records with parallax <= value (API: ?parallax__lte=14.5)
    if request_args.get('parallax__lte'):
        query = query.filter(AsAssnQ3cRecord.parallax <= float(request_args['parallax__lte']))

    # return records with class probability >= value (API: ?probability__gte=14.5)
    if request_args.get('probability__gte'):
        query = query.filter(AsAssnQ3cRecord.class_probability >= float(request_args['probability__gte']))

    # return records with class probability <= value (API: ?probability__lte=14.5)
    if request_args.get('probability__lte'):
        query = query.filter(AsAssnQ3cRecord.class_probability <= float(request_args['probability__lte']))

    # return records with vtype like value (API: ?vtype=demo)
    if request_args.get('vtype'):
        query = query.filter(AsAssnQ3cRecord.variable_type.ilike(f"%{request_args['vtype']}%"))

    # sort results
    sort_value = request_args.get('sort_value', ASASSN_SORT_VALUE[0]).lower()
    sort_order = request_args.get('sort_order', ASASSN_SORT_ORDER[0]).lower()
    if sort_order in ASASSN_SORT_ORDER:
        if sort_order.startswith(ASASSN_SORT_ORDER[0]):
            query = query.order_by(getattr(AsAssnQ3cRecord, sort_value).asc())
        elif sort_order.startswith(ASASSN_SORT_ORDER[1]):
            query = query.order_by(getattr(AsAssnQ3cRecord, sort_value).desc())

    # return query
    return query
