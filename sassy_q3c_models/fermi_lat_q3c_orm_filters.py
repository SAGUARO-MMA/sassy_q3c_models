#!/usr/bin/env python3


# +
# import(s)
# -
from sassy_q3c_models.fermi_lat_q3c_orm import *


# +
# function: fermi_lat_q3c_orm_filters() alphabetically
# -
# noinspection PyBroadException
def fermi_lat_q3c_orm_filters(query: Any = None, request_args: dict = None):

    # return records within astrocone search (API: ?astrocone=NGC1365,5.0)
    if request_args.get('astrocone'):
        _nam, _rad = request_args['astrocone'].split(',')
        _val = get_astropy_coords(_nam.strip().upper())
        if _val is not None:
            query = query.filter(func.q3c_radial_query(FermiLatQ3cRecord.ra, FermiLatQ3cRecord.dec, _val[0], _val[1], _rad))

    # return records within cone search (API: ?cone=23.5,29.2,5.0)
    if request_args.get('cone'):
        _ra, _dec, _rad = request_args['cone'].split(',')
        query = query.filter(func.q3c_radial_query(FermiLatQ3cRecord.ra, FermiLatQ3cRecord.dec, _ra, _dec, _rad))

    # return records within ellipse search (API: ?ellipse=202.1,47.2,5.0,0.5,25.0)
    if request_args.get('ellipse'):
        _ra, _dec, _maj, _rat, _pos = request_args['ellipse'].split(',')
        query = query.filter(
            func.q3c_ellipse_query(FermiLatQ3cRecord.ra, FermiLatQ3cRecord.dec, _ra, _dec, _maj, _rat, _pos))

    # return records with fid = value (API: ?fid=20)
    if request_args.get('fid'):
        query = query.filter(FermiLatQ3cRecord.fid == int(request_args['fid']))

    # return records with an RA >= value in deg (API: ?ra__gte=12.0)
    if request_args.get('ra__gte'):
        query = query.filter(FermiLatQ3cRecord.ra >= float(request_args['ra__gte']))

    # return records with an RA <= value in deg (API: ?ra__lte=12.0)
    if request_args.get('ra__lte'):
        query = query.filter(FermiLatQ3cRecord.ra <= float(request_args['ra__lte']))

    # return records with an Dec >= value in deg (API: ?dec__gte=20.0)
    if request_args.get('dec__gte'):
        query = query.filter(FermiLatQ3cRecord.dec >= float(request_args['dec__gte']))

    # return records with a Dec <= value in deg (API: ?dec__lte=20.0)
    if request_args.get('dec__lte'):
        query = query.filter(FermiLatQ3cRecord.dec <= float(request_args['dec__lte']))

    # return records where b >= value (API: ?b__gte=1.0)
    if request_args.get('b__gte'):
        query = query.filter(FermiLatQ3cRecord.b >= float(request_args['b__gte']))

    # return records where b <= value (API: ?b__lte=1.0)
    if request_args.get('b__lte'):
        query = query.filter(FermiLatQ3cRecord.b <= float(request_args['b__lte']))

    # return records where l >= value (API: ?l__gte=1.0)
    if request_args.get('l__gte'):
        query = query.filter(FermiLatQ3cRecord.l >= float(request_args['l__gte']))

    # return records where l <= value (API: ?l__lte=1.0)
    if request_args.get('l__lte'):
        query = query.filter(FermiLatQ3cRecord.l <= float(request_args['l__lte']))

    # return records where lbllac >= value (API: ?lbllac__gte=1.0)
    if request_args.get('lbllac__gte'):
        query = query.filter(FermiLatQ3cRecord.lbllac >= float(request_args['lbllac__gte']))

    # return records where lbllac <= value (API: ?lbllac__lte=1.0)
    if request_args.get('lbllac__lte'):
        query = query.filter(FermiLatQ3cRecord.l <= float(request_args['lbllac__lte']))

    # return records with name like value (API: ?name=NGC1365)
    if request_args.get('name'):
        query = query.filter(FermiLatQ3cRecord.name.ilike(f"%{request_args['name']}%"))

    # return records with classification like value (API: ?classification=BLLac)
    if request_args.get('classification'):
        query = query.filter(FermiLatQ3cRecord.classification.ilike(f"%{request_args['classification']}%"))

    # sort results
    sort_value = request_args.get('sort_value', FERMI_LAT_SORT_VALUE[0]).lower()
    sort_order = request_args.get('sort_order', FERMI_LAT_SORT_ORDER[0]).lower()
    if sort_order in FERMI_LAT_SORT_ORDER:
        if sort_order.startswith(FERMI_LAT_SORT_ORDER[0]):
            query = query.order_by(getattr(FermiLatQ3cRecord, sort_value).asc())
        elif sort_order.startswith(FERMI_LAT_SORT_ORDER[1]):
            query = query.order_by(getattr(FermiLatQ3cRecord, sort_value).desc())

    # return query
    return query
