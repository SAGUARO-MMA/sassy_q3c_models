#!/usr/bin/env python3


# +
# import(s)
# -
from sassy_q3c_models.sdss12photoz_q3c_orm import *


# +
# function: sdss12photoz_q3c_orm_filters()
# -
# noinspection PyBroadException
def sdss12photoz_q3c_orm_filters(query: Any = None, request_args: dict = None):


    # return records within astrocone search (API: ?astrocone=NGC1365,5.0)
    if request_args.get('astrocone'):
        try:
            _nam, _rad = request_args['astrocone'].split(',')
            _val = get_astropy_coords(_nam.strip().upper())
            if _val is not None:
                query = query.filter(func.q3c_radial_query(Sdss12PhotoZQ3cRecord.ra, Sdss12PhotoZQ3cRecord.dec, _val[0], _val[1], _rad))
        except:
            pass

    # return records within cone search (API: ?cone=23.5,29.2,5.0)
    if request_args.get('cone'):
        try:
            _ra, _dec, _rad = request_args['cone'].split(',')
            query = query.filter(func.q3c_radial_query(Sdss12PhotoZQ3cRecord.ra, Sdss12PhotoZQ3cRecord.dec, _ra, _dec, _rad))
        except:
            pass

    # return records within ellipse search (API: ?ellipse=202.1,47.2,5.0,0.5,25.0)
    if request_args.get('ellipse'):
        try:
            _ra, _dec, _maj, _rat, _pos = request_args['ellipse'].split(',')
            query = query.filter(
                func.q3c_ellipse_query(Sdss12PhotoZQ3cRecord.ra, Sdss12PhotoZQ3cRecord.dec, _ra, _dec, _maj, _rat, _pos))
        except:
            pass

    # return records with an RA >= value in deg (API: ?ra__gte=12.0)
    if request_args.get('ra__gte'):
        query = query.filter(Sdss12PhotoZQ3cRecord.ra >= float(request_args['ra__gte']))

    # return records with an RA <= value in deg (API: ?ra__lte=12.0)
    if request_args.get('ra__lte'):
        query = query.filter(Sdss12PhotoZQ3cRecord.ra <= float(request_args['ra__lte']))

    # return records with an Dec >= value in deg (API: ?dec__gte=20.0)
    if request_args.get('dec__gte'):
        query = query.filter(Sdss12PhotoZQ3cRecord.dec >= float(request_args['dec__gte']))

    # return records with a Dec <= value in deg (API: ?dec__lte=20.0)
    if request_args.get('dec__lte'):
        query = query.filter(Sdss12PhotoZQ3cRecord.dec <= float(request_args['dec__lte']))

    # return records with sid = value (API: ?sid=20)
    if request_args.get('sid'):
        query = query.filter(Sdss12PhotoZQ3cRecord.sid == int(request_args['sid']))

    # return records where classifier = value (API: ?classifier=1)
    if request_args.get('classifier'):
        query = query.filter(Sdss12PhotoZQ3cRecord.classifier == int(request_args['classifier']))

    # return records where quality = value (API: ?quality=1)
    if request_args.get('quality'):
        query = query.filter(Sdss12PhotoZQ3cRecord.quality == int(request_args['quality']))

    # return records with name like value (API: ?name=NGC1365)
    if request_args.get('name'):
        query = query.filter(or_(
            Sdss12PhotoZQ3cRecord.sdss12.ilike(f"%{request_args['name']}%"),
            Sdss12PhotoZQ3cRecord.sdssid.ilike(f"%{request_args['name']}%")))

    # return records where the obsdate >= value (API: ?obsdate__gte=2015.2)
    if request_args.get('obsdate__gte'):
        query = query.filter(Sdss12PhotoZQ3cRecord.obsdate >= float(request_args['obsdate__gte']))

    # return records where the obsdate <= value (API: ?obsdate__lte=2015.2)
    if request_args.get('obsdate__lte'):
        query = query.filter(Sdss12PhotoZQ3cRecord.obsdate <= float(request_args['obsdate__lte']))

    # return records where the u >= value (API: ?u__gte=5.2)
    if request_args.get('u__gte'):
        query = query.filter(or_(
            Sdss12PhotoZQ3cRecord.umag >= float(request_args['u__gte']),
            Sdss12PhotoZQ3cRecord.u_prime_mag >= float(request_args['u__gte']),
            Sdss12PhotoZQ3cRecord.u_pmag >= float(request_args['u__gte']),
            Sdss12PhotoZQ3cRecord.u_upmag >= float(request_args['u__gte']),
            Sdss12PhotoZQ3cRecord.abs_u_mag >= float(request_args['u__gte'])))

    # return records where the u <= value (API: ?u__lte=5.2)
    if request_args.get('u__lte'):
        query = query.filter(or_(
            Sdss12PhotoZQ3cRecord.umag <= float(request_args['u__lte']),
            Sdss12PhotoZQ3cRecord.u_prime_mag <= float(request_args['u__lte']),
            Sdss12PhotoZQ3cRecord.u_pmag <= float(request_args['u__lte']),
            Sdss12PhotoZQ3cRecord.u_upmag <= float(request_args['u__lte']),
            Sdss12PhotoZQ3cRecord.abs_u_mag <= float(request_args['u__lte'])))

    # return records where the g >= value (API: ?g__gte=5.2)
    if request_args.get('g__gte'):
        query = query.filter(or_(
            Sdss12PhotoZQ3cRecord.gmag >= float(request_args['g__gte']),
            Sdss12PhotoZQ3cRecord.g_prime_mag >= float(request_args['g__gte']),
            Sdss12PhotoZQ3cRecord.g_pmag >= float(request_args['g__gte']),
            Sdss12PhotoZQ3cRecord.g_upmag >= float(request_args['g__gte']),
            Sdss12PhotoZQ3cRecord.abs_g_mag >= float(request_args['g__gte'])))

    # return records where the g <= value (API: ?g__lte=5.2)
    if request_args.get('g__lte'):
        query = query.filter(or_(
            Sdss12PhotoZQ3cRecord.gmag <= float(request_args['g__lte']),
            Sdss12PhotoZQ3cRecord.g_prime_mag <= float(request_args['g__lte']),
            Sdss12PhotoZQ3cRecord.g_pmag <= float(request_args['g__lte']),
            Sdss12PhotoZQ3cRecord.g_upmag <= float(request_args['g__lte']),
            Sdss12PhotoZQ3cRecord.abs_g_mag <= float(request_args['g__lte'])))

    # return records where the r >= value (API: ?r__gte=5.2)
    if request_args.get('r__gte'):
        query = query.filter(or_(
            Sdss12PhotoZQ3cRecord.rmag >= float(request_args['r__gte']),
            Sdss12PhotoZQ3cRecord.r_prime_mag >= float(request_args['r__gte']),
            Sdss12PhotoZQ3cRecord.r_pmag >= float(request_args['r__gte']),
            Sdss12PhotoZQ3cRecord.r_upmag >= float(request_args['r__gte']),
            Sdss12PhotoZQ3cRecord.abs_r_mag >= float(request_args['r__gte'])))

    # return records where the r <= value (API: ?r__lte=5.2)
    if request_args.get('r__lte'):
        query = query.filter(or_(
            Sdss12PhotoZQ3cRecord.rmag <= float(request_args['r__lte']),
            Sdss12PhotoZQ3cRecord.r_prime_mag <= float(request_args['r__lte']),
            Sdss12PhotoZQ3cRecord.r_pmag <= float(request_args['r__lte']),
            Sdss12PhotoZQ3cRecord.r_upmag <= float(request_args['r__lte']),
            Sdss12PhotoZQ3cRecord.abs_r_mag <= float(request_args['r__lte'])))

    # return records where the i >= value (API: ?i__gte=5.2)
    if request_args.get('i__gte'):
        query = query.filter(or_(
            Sdss12PhotoZQ3cRecord.imag >= float(request_args['i__gte']),
            Sdss12PhotoZQ3cRecord.i_prime_mag >= float(request_args['i__gte']),
            Sdss12PhotoZQ3cRecord.i_pmag >= float(request_args['i__gte']),
            Sdss12PhotoZQ3cRecord.i_upmag >= float(request_args['i__gte']),
            Sdss12PhotoZQ3cRecord.abs_i_mag >= float(request_args['i__gte'])))

    # return records where the i <= value (API: ?i__lte=5.2)
    if request_args.get('i__lte'):
        query = query.filter(or_(
            Sdss12PhotoZQ3cRecord.imag <= float(request_args['i__lte']),
            Sdss12PhotoZQ3cRecord.i_prime_mag <= float(request_args['i__lte']),
            Sdss12PhotoZQ3cRecord.i_pmag <= float(request_args['i__lte']),
            Sdss12PhotoZQ3cRecord.i_upmag <= float(request_args['i__lte']),
            Sdss12PhotoZQ3cRecord.abs_i_mag <= float(request_args['i__lte'])))

    # return records where the z >= value (API: ?z__gte=5.2)
    if request_args.get('z__gte'):
        query = query.filter(or_(
            Sdss12PhotoZQ3cRecord.zmag >= float(request_args['z__gte']),
            Sdss12PhotoZQ3cRecord.z_prime_mag >= float(request_args['z__gte']),
            Sdss12PhotoZQ3cRecord.z_pmag >= float(request_args['z__gte']),
            Sdss12PhotoZQ3cRecord.z_upmag >= float(request_args['z__gte']),
            Sdss12PhotoZQ3cRecord.abs_z_mag >= float(request_args['z__gte'])))

    # return records where the z <= value (API: ?z__lte=5.2)
    if request_args.get('z__lte'):
        query = query.filter(or_(
            Sdss12PhotoZQ3cRecord.zmag <= float(request_args['z__lte']),
            Sdss12PhotoZQ3cRecord.z_prime_mag <= float(request_args['z__lte']),
            Sdss12PhotoZQ3cRecord.z_pmag <= float(request_args['z__lte']),
            Sdss12PhotoZQ3cRecord.z_upmag <= float(request_args['z__lte']),
            Sdss12PhotoZQ3cRecord.abs_z_mag <= float(request_args['z__lte'])))

    # return records where the zsp >= value (API: ?zsp__gte=5.2)
    if request_args.get('zsp__gte'):
        query = query.filter(Sdss12PhotoZQ3cRecord.zsp >= float(request_args['zsp__gte']))

    # return records where the zsp <= value (API: ?zsp__lte=5.2)
    if request_args.get('zsp__lte'):
        query = query.filter(Sdss12PhotoZQ3cRecord.zsp <= float(request_args['zsp__lte']))

    # return records where the zph >= value (API: ?zph=5.2)
    if request_args.get('zph__gte'):
        query = query.filter(Sdss12PhotoZQ3cRecord.zph >= float(request_args['zph__gte']))

    # return records where the zph <= value (API: ?zph=5.2)
    if request_args.get('zph__lte'):
        query = query.filter(Sdss12PhotoZQ3cRecord.zph <= float(request_args['zph__lte']))

    # return records where the ave_zph >= value (API: ?ave_zph=5.2)
    if request_args.get('ave_zph__gte'):
        query = query.filter(Sdss12PhotoZQ3cRecord.ave_zph >= float(request_args['ave_zph__gte']))

    # return records where the ave_zph <= value (API: ?ave_zph=5.2)
    if request_args.get('ave_zph__lte'):
        query = query.filter(Sdss12PhotoZQ3cRecord.ave_zph <= float(request_args['ave_zph__lte']))

    # sort results
    sort_value = request_args.get('sort_value', SDSS12PHOTOZ_SORT_VALUE[0]).lower()
    sort_order = request_args.get('sort_order', SDSS12PHOTOZ_SORT_ORDER[0]).lower()
    if sort_order in SDSS12PHOTOZ_SORT_ORDER:
        if sort_order.startswith(SDSS12PHOTOZ_SORT_ORDER[0]):
            query = query.order_by(getattr(Sdss12PhotoZQ3cRecord, sort_value).asc())
        elif sort_order.startswith(SDSS12PHOTOZ_SORT_ORDER[1]):
            query = query.order_by(getattr(Sdss12PhotoZQ3cRecord, sort_value).desc())

    # return query
    return query
