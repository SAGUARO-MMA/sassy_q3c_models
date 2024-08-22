#!/usr/bin/env python3


# +
# import(s)
# -
from sassy_q3c_models.ls_dr10_q3c_orm import *


# +
# function: ls_dr10_q3c_orm_filters() alphabetically
# -
# noinspection PyBroadException
def ls_dr10_q3c_orm_filters(query: Any = None, request_args: dict = None):

    # return records within astrocone search (API: ?astrocone=NGC1365,5.0)
    if request_args.get('astrocone'):
        try:
            _nam, _rad = request_args['astrocone'].split(',')
            _val = get_astropy_coords(_nam.strip().upper())
            if _val is not None:
                query = query.filter(func.q3c_radial_query(LsDr10Q3cRecord.ra, LsDr10Q3cRecord.declination, _val[0], _val[1], _rad))
        except:
            pass

    # return records within cone search (API: ?cone=23.5,29.2,5.0)
    if request_args.get('cone'):
        try:
            _ra, _dec, _rad = request_args['cone'].split(',')
            query = query.filter(func.q3c_radial_query(LsDr10Q3cRecord.ra, LsDr10Q3cRecord.declination, _ra, _dec, _rad))
        except:
            pass

    # return records within ellipse search (API: ?ellipse=202.1,47.2,5.0,0.5,25.0)
    if request_args.get('ellipse'):
        try:
            _ra, _dec, _maj, _rat, _pos = request_args['ellipse'].split(',')
            query = query.filter(
                func.q3c_ellipse_query(LsDr10Q3cRecord.ra, LsDr10Q3cRecord.declination, _ra, _dec, _maj, _rat, _pos))
        except:
            pass

    # return records with lid = value (API: ?lid=20)
    if request_args.get('lid'):
        query = query.filter(LsDr10Q3cRecord.lid == int(request_args['lid']))

    # return records with objid = value (API: ?objid=20)
    if request_args.get('objid'):
        query = query.filter(LsDr10Q3cRecord.objid == int(request_args['objid']))

    # return records with an RA >= value in deg (API: ?ra__gte=12.0)
    if request_args.get('ra__gte'):
        query = query.filter(LsDr10Q3cRecord.ra >= float(request_args['ra__gte']))

    # return records with an RA <= value in deg (API: ?ra__lte=12.0)
    if request_args.get('ra__lte'):
        query = query.filter(LsDr10Q3cRecord.ra <= float(request_args['ra__lte']))

    # return records with an Dec >= value in deg (API: ?dec__gte=20.0)
    if request_args.get('dec__gte'):
        query = query.filter(LsDr10Q3cRecord.declination >= float(request_args['dec__gte']))

    # return records with a Dec <= value in deg (API: ?dec__lte=20.0)
    if request_args.get('dec__lte'):
        query = query.filter(LsDr10Q3cRecord.declination <= float(request_args['dec__lte']))

    # return records with Z mean >= value (API: ?z_mean__gte=0.5)
    if request_args.get('z_mean__gte'):
        query = query.filter(LsDr10Q3cRecord.z_phot_mean >= float(request_args['z_mean__gte']))

    # return records with Z mean <= value (API: ?z_mean__lte=0.75)
    if request_args.get('z_mean__lte'):
        query = query.filter(LsDr10Q3cRecord.z_phot_mean <= float(request_args['z_mean__lte']))

    # return records with Z median >= value (API: ?z_median__gte=0.5)
    if request_args.get('z_median__gte'):
        query = query.filter(LsDr10Q3cRecord.z_phot_median >= float(request_args['z_median__gte']))

    # return records with Z median <= value (API: ?z_median__lte=0.75)
    if request_args.get('z_median__lte'):
        query = query.filter(LsDr10Q3cRecord.z_phot_median <= float(request_args['z_median__lte']))

    # return records with Z i mean >= value (API: ?iz_mean__gte=0.5)
    if request_args.get('iz_mean__gte'):
        query = query.filter(LsDr10Q3cRecord.z_phot_mean_i >= float(request_args['iz_mean__gte']))

    # return records with Z i mean <= value (API: ?iz_mean__lte=0.75)
    if request_args.get('iz_mean__lte'):
        query = query.filter(LsDr10Q3cRecord.z_phot_mean_i <= float(request_args['iz_mean__lte']))

    # return records with Z i median >= value (API: ?iz_median__gte=0.5)
    if request_args.get('iz_median__gte'):
        query = query.filter(LsDr10Q3cRecord.z_phot_median_i >= float(request_args['iz_median__gte']))

    # return records with Z i median <= value (API: ?iz_median__lte=0.75)
    if request_args.get('iz_median__lte'):
        query = query.filter(LsDr10Q3cRecord.z_phot_median_i <= float(request_args['iz_median__lte']))

    # return records with Z spec >= value (API: ?z_spec__gte=0.5)
    if request_args.get('z_spec__gte'):
        query = query.filter(LsDr10Q3cRecord.z_spec >= float(request_args['z_spec__gte']))

    # return records with Z spec <= value (API: ?z_spec__lte=0.75)
    if request_args.get('z_spec__lte'):
        query = query.filter(LsDr10Q3cRecord.z_spec <= float(request_args['z_spec__lte']))

    # return records with G flux >= value (API: ?g_flux__gte=0.5)
    if request_args.get('g_flux__gte'):
        query = query.filter(LsDr10Q3cRecord.flux_g >= float(request_args['g_flux__gte']))

    # return records with G flux <= value (API: ?g_flux__lte=0.75)
    if request_args.get('g_flux__lte'):
        query = query.filter(LsDr10Q3cRecord.flux_g <= float(request_args['g_flux__lte']))

    # return records with R flux >= value (API: ?r_flux__gte=0.5)
    if request_args.get('r_flux__gte'):
        query = query.filter(LsDr10Q3cRecord.flux_r >= float(request_args['r_flux__gte']))

    # return records with R flux <= value (API: ?r_flux__lte=0.75)
    if request_args.get('r_flux__lte'):
        query = query.filter(LsDr10Q3cRecord.flux_r <= float(request_args['r_flux__lte']))

    # return records with I flux >= value (API: ?i_flux__gte=0.5)
    if request_args.get('i_flux__gte'):
        query = query.filter(LsDr10Q3cRecord.flux_i >= float(request_args['i_flux__gte']))

    # return records with I flux <= value (API: ?i_flux__lte=0.75)
    if request_args.get('i_flux__lte'):
        query = query.filter(LsDr10Q3cRecord.flux_i <= float(request_args['i_flux__lte']))

    # return records with Z flux >= value (API: ?z_flux__gte=0.5)
    if request_args.get('z_flux__gte'):
        query = query.filter(LsDr10Q3cRecord.flux_z >= float(request_args['z_flux__gte']))

    # return records with Z flux <= value (API: ?z_flux__lte=0.75)
    if request_args.get('z_flux__lte'):
        query = query.filter(LsDr10Q3cRecord.flux_z <= float(request_args['z_flux__lte']))

    # return records with W1 flux >= value (API: ?w1_flux__gte=0.5)
    if request_args.get('w1_flux__gte'):
        query = query.filter(LsDr10Q3cRecord.flux_w1 >= float(request_args['w1_flux__gte']))

    # return records with W1 flux <= value (API: ?w1_flux__lte=0.75)
    if request_args.get('w1_flux__lte'):
        query = query.filter(LsDr10Q3cRecord.flux_w1 <= float(request_args['w1_flux__lte']))

    # return records with W2 flux >= value (API: ?w2_flux__gte=0.5)
    if request_args.get('w2_flux__gte'):
        query = query.filter(LsDr10Q3cRecord.flux_w2 >= float(request_args['w2_flux__gte']))

    # return records with W2 flux <= value (API: ?w2_flux__lte=0.75)
    if request_args.get('w2_flux__lte'):
        query = query.filter(LsDr10Q3cRecord.flux_w2 <= float(request_args['w2_flux__lte']))

    # return records with W3 flux >= value (API: ?w3_flux__gte=0.5)
    if request_args.get('w3_flux__gte'):
        query = query.filter(LsDr10Q3cRecord.flux_w3 >= float(request_args['w3_flux__gte']))

    # return records with W3 flux <= value (API: ?w3_flux__lte=0.75)
    if request_args.get('w3_flux__lte'):
        query = query.filter(LsDr10Q3cRecord.flux_w3 <= float(request_args['w3_flux__lte']))

    # return records with W4 flux >= value (API: ?w4_flux__gte=0.5)
    if request_args.get('w4_flux__gte'):
        query = query.filter(LsDr10Q3cRecord.flux_w4 >= float(request_args['w4_flux__gte']))

    # return records with W4 flux <= value (API: ?w4_flux__lte=0.75)
    if request_args.get('w4_flux__lte'):
        query = query.filter(LsDr10Q3cRecord.flux_w4 <= float(request_args['w4_flux__lte']))

    # sort results
    sort_value = request_args.get('sort_value', LSDR10_SORT_VALUE[0]).lower()
    sort_order = request_args.get('sort_order', LSDR10_SORT_ORDER[0]).lower()
    if sort_order in LSDR10_SORT_ORDER:
        if sort_order.startswith(LSDR10_SORT_ORDER[0]):
            query = query.order_by(getattr(LsDr10Q3cRecord, sort_value).asc())
        elif sort_order.startswith(LSDR10_SORT_ORDER[1]):
            query = query.order_by(getattr(LsDr10Q3cRecord, sort_value).desc())

    # return query
    return query
