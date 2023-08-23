#!/usr/bin/env python3


# +
# import(s)
# -
from sassy_q3c_models.gaiadr3variable_q3c_orm import *


# +
# function: gaiadr3variable_q3c_orm_filters()
# -
# noinspection PyBroadException
def gaiadr3variable_q3c_orm_filters(query: Any = None, request_args: dict = None):

    # return records within astrocone search (API: ?astrocone=M51,5.0)
    if request_args.get('astrocone'):
        try:
            _nam, _rad = request_args['astrocone'].split(',')
            _val = get_astropy_coords(_nam.strip().upper())
            if _val is not None:
                query = query.filter(func.q3c_radial_query(
                    GaiaDR3VariableQ3cRecord.ra, GaiaDR3VariableQ3cRecord.dec, float(_val[0]), float(_val[1]), float(_rad)))
        except:
            pass

    # return records within cone search (API: ?cone=23.5,29.2,5.0)
    if request_args.get('cone'):
        try:
            _ra, _dec, _rad = request_args['cone'].split(',')
            query = query.filter(func.q3c_radial_query(
                GaiaDR3VariableQ3cRecord.ra, GaiaDR3VariableQ3cRecord.dec, float(_ra), float(_dec), float(_rad)))
        except:
            pass

    # return records within ellipse search (API: ?ellipse=202.1,47.2,5.0,0.5,25.0)
    if request_args.get('ellipse'):
        try:
            _ra, _dec, _maj, _rat, _pos = request_args['ellipse'].split(',')
            query = query.filter(func.q3c_ellipse_query(
                GaiaDR3VariableQ3cRecord.ra, GaiaDR3VariableQ3cRecord.dec, float(_ra), float(_dec), float(_maj),
                float(_rat), float(_pos)))
        except:
            pass

    # return records with gid = value (API: ?gid=20)
    if request_args.get('gid'):
        query = query.filter(GaiaDR3VariableQ3cRecord.gid == int(request_args['gid']))

    # return records with name like value (API: ?name=demo)
    if request_args.get('name'):
        query = query.filter(or_(
            GaiaDR3VariableQ3cRecord.source_id.ilike(f"%{request_args['name']}%")))

    # return records with ra >= value (API: ?ra__gte=0.0)
    if request_args.get('ra__gte'):
        query = query.filter(GaiaDR3VariableQ3cRecord.ra >= float(request_args['ra__gte']))

    # return records with ra <= value (API: ?ra__lte=360.0)
    if request_args.get('ra__lte'):
        query = query.filter(GaiaDR3VariableQ3cRecord.ra <= float(request_args['ra__lte']))

    # return records with dec >= value (API: ?dec__gte=-90.0)
    if request_args.get('dec__gte'):
        query = query.filter(GaiaDR3VariableQ3cRecord.dec >= float(request_args['dec__gte']))

    # return records with dec <= value (API: ?dec__lte=90.0)
    if request_args.get('dec__lte'):
        query = query.filter(GaiaDR3VariableQ3cRecord.dec <= float(request_args['dec__lte']))

    # return records with median_g >= value (API: ?median_g__gte=12.5)
    if request_args.get('median_g__gte'):
        query = query.filter(GaiaDR3VariableQ3cRecord.median_mag_g_fov >= float(request_args['median_g__gte']))
    # return records with median_g <= value (API: ?median_g__lte=12.5)
    if request_args.get('median_g__lte'):
        query = query.filter(GaiaDR3VariableQ3cRecord.median_mag_g_fov <= float(request_args['median_g__lte']))
    # return records with mean_g >= value (API: ?mean_g__gte=12.5)
    if request_args.get('mean_g__gte'):
        query = query.filter(GaiaDR3VariableQ3cRecord.mean_mag_g_fov >= float(request_args['mean_g__gte']))
    # return records with mean_g <= value (API: ?mean_g__lte=12.5)
    if request_args.get('mean_g__lte'):
        query = query.filter(GaiaDR3VariableQ3cRecord.mean_mag_g_fov <= float(request_args['mean_g__lte']))
    # return records with mean_g >= value (API: ?mean_g__gte=12.5)
    if request_args.get('stetson_g__gte'):
        query = query.filter(GaiaDR3VariableQ3cRecord.stetson_mag_g_fov >= float(request_args['stetson_g__gte']))
    # return records with stetson_g <= value (API: ?stetson_g__lte=12.5)
    if request_args.get('stetson_g__lte'):
        query = query.filter(GaiaDR3VariableQ3cRecord.stetson_mag_g_fov <= float(request_args['stetson_g__lte']))

    # return records with median_bp >= value (API: ?median_bp__gte=12.5)
    if request_args.get('median_bp__gte'):
        query = query.filter(GaiaDR3VariableQ3cRecord.median_mag_bp_fov >= float(request_args['median_bp__gte']))
    # return records with median_bp <= value (API: ?median_bp__lte=12.5)
    if request_args.get('median_bp__lte'):
        query = query.filter(GaiaDR3VariableQ3cRecord.median_mag_bp_fov <= float(request_args['median_bp__lte']))
    # return records with mean_bp >= value (API: ?mean_bp__gte=12.5)
    if request_args.get('mean_bp__gte'):
        query = query.filter(GaiaDR3VariableQ3cRecord.mean_mag_bp_fov >= float(request_args['mean_bp__gte']))
    # return records with mean_bp <= value (API: ?mean_bp__lte=12.5)
    if request_args.get('mean_bp__lte'):
        query = query.filter(GaiaDR3VariableQ3cRecord.mean_mag_bp_fov <= float(request_args['mean_bp__lte']))
    # return records with mean_bp >= value (API: ?mean_bp__gte=12.5)
    if request_args.get('stetson_bp__gte'):
        query = query.filter(GaiaDR3VariableQ3cRecord.stetson_mag_bp_fov >= float(request_args['stetson_bp__gte']))
    # return records with stetson_bp <= value (API: ?stetson_bp__lte=12.5)
    if request_args.get('stetson_bp__lte'):
        query = query.filter(GaiaDR3VariableQ3cRecord.stetson_mag_bp_fov <= float(request_args['stetson_bp__lte']))

    # return records with median_rp >= value (API: ?median_g__gte=12.5)
    if request_args.get('median_rp__gte'):
        query = query.filter(GaiaDR3VariableQ3cRecord.median_mag_rp_fov >= float(request_args['median_rp__gte']))
    # return records with median_rp <= value (API: ?median_g__lte=12.5)
    if request_args.get('median_rp__lte'):
        query = query.filter(GaiaDR3VariableQ3cRecord.median_mag_rp_fov <= float(request_args['median_rp__lte']))
    # return records with mean_rp >= value (API: ?mean_g__gte=12.5)
    if request_args.get('mean_rp__gte'):
        query = query.filter(GaiaDR3VariableQ3cRecord.mean_mag_rp_fov >= float(request_args['mean_rp__gte']))
    # return records with mean_rp <= value (API: ?mean_g__lte=12.5)
    if request_args.get('mean_rp__lte'):
        query = query.filter(GaiaDR3VariableQ3cRecord.mean_mag_rp_fov <= float(request_args['mean_rp__lte']))
    # return records with mean_rp >= value (API: ?mean_g__gte=12.5)
    if request_args.get('stetson_rp__gte'):
        query = query.filter(GaiaDR3VariableQ3cRecord.stetson_mag_rp_fov >= float(request_args['stetson_rp__gte']))
    # return records with stetson_rp <= value (API: ?stetson_g__lte=12.5)
    if request_args.get('stetson_rp__lte'):
        query = query.filter(GaiaDR3VariableQ3cRecord.stetson_mag_rp_fov <= float(request_args['stetson_rp__lte']))

    # return records with parallax >= value (API: ?parallax__gte=14.5)
    if request_args.get('parallax__gte'):
        query = query.filter(GaiaDR3VariableQ3cRecord.parallax >= float(request_args['parallax__gte']))

    # return records with parallax <= value (API: ?parallax__lte=14.5)
    if request_args.get('parallax__lte'):
        query = query.filter(GaiaDR3VariableQ3cRecord.parallax <= float(request_args['parallax__lte']))

    # return records with classification like value (API: ?classification=demo)
    if request_args.get('classification'):
        query = query.filter(GaiaDR3VariableQ3cRecord.classification.ilike(f"%{request_args['classification']}%"))

    # return records with best_class_name like value (API: ?best_class_name=demo)
    if request_args.get('best_class_name'):
        query = query.filter(GaiaDR3VariableQ3cRecord.best_class_name.ilike(f"%{request_args['best_class_name']}%"))

    # return records with best_class_score like value (API: ?best_class_score=demo)
    if request_args.get('best_class_score'):
        query = query.filter(GaiaDR3VariableQ3cRecord.best_class_score.ilike(f"%{request_args['best_class_score']}%"))

    # return records with in_vari_classification_result = value (API: ?in_vari_classification_result='t')
    if request_args.get('in_vari_classification_result'):
        query = query.filter(GaiaDR3VariableQ3cRecord.in_vari_classification_result == str(request_args['in_vari_classification_result']))
    # return records with in_vari_rrlyrae = value (API: ?in_vari_rrlyrae='t')
    if request_args.get('in_vari_rrlyrae'):
        query = query.filter(GaiaDR3VariableQ3cRecord.in_vari_rrlyrae == str(request_args['in_vari_rrlyrae']))
    # return records with in_vari_cepheid = value (API: ?in_vari_cepheid='t')
    if request_args.get('in_vari_cepheid'):
        query = query.filter(GaiaDR3VariableQ3cRecord.in_vari_cepheid == str(request_args['in_vari_cepheid']))
    # return records with in_vari_planetary_transit = value (API: ?in_vari_planetary_transit='t')
    if request_args.get('in_vari_planetary_transit'):
        query = query.filter(GaiaDR3VariableQ3cRecord.in_vari_planetary_transit == str(request_args['in_vari_planetary_transit']))
    # return records with in_vari_short_timescale = value (API: ?in_vari_short_timescale='t')
    if request_args.get('in_vari_short_timescale'):
        query = query.filter(GaiaDR3VariableQ3cRecord.in_vari_short_timescale == str(request_args['in_vari_short_timescale']))
    # return records with in_vari_long_period_variable = value (API: ?in_vari_long_period_variable='t')
    if request_args.get('in_vari_long_period_variable'):
        query = query.filter(GaiaDR3VariableQ3cRecord.in_vari_long_period_variable == str(request_args['in_vari_long_period_variable']))
    # return records with in_vari_eclipsing_binary = value (API: ?in_vari_eclipsing_binary='t')
    if request_args.get('in_vari_eclipsing_binary'):
        query = query.filter(GaiaDR3VariableQ3cRecord.in_vari_eclipsing_binary == str(request_args['in_vari_eclipsing_binary']))
    # return records with in_vari_rotation_modulation = value (API: ?in_vari_rotation_modulation='t')
    if request_args.get('in_vari_rotation_modulation'):
        query = query.filter(GaiaDR3VariableQ3cRecord.in_vari_rotation_modulation == str(request_args['in_vari_rotation_modulation']))
    # return records with in_vari_ms_oscillator = value (API: ?in_vari_ms_oscillator='t')
    if request_args.get('in_vari_ms_oscillator'):
        query = query.filter(GaiaDR3VariableQ3cRecord.in_vari_ms_oscillator == str(request_args['in_vari_ms_oscillator']))
    # return records with in_vari_agn = value (API: ?in_vari_agn='t')
    if request_args.get('in_vari_agn'):
        query = query.filter(GaiaDR3VariableQ3cRecord.in_vari_agn == str(request_args['in_vari_agn']))
    # return records with in_vari_microlensing = value (API: ?in_vari_microlensing='t')
    if request_args.get('in_vari_microlensing'):
        query = query.filter(GaiaDR3VariableQ3cRecord.in_vari_microlensing == str(request_args['in_vari_microlensing']))
    # return records with in_vari_compact_companion = value (API: ?in_vari_compact_companion='t')
    if request_args.get('in_vari_compact_companion'):
        query = query.filter(GaiaDR3VariableQ3cRecord.in_vari_compact_companion == str(request_args['in_vari_compact_companion']))

    # sort results
    sort_value = request_args.get('sort_value', GAIADR3VARIABLE_SORT_VALUE[0]).lower()
    sort_order = request_args.get('sort_order', GAIADR3VARIABLE_SORT_ORDER[0]).lower()
    if sort_order in GAIADR3VARIABLE_SORT_ORDER:
        if sort_order.startswith(GAIADR3VARIABLE_SORT_ORDER[0]):
            query = query.order_by(getattr(GaiaDR3VariableQ3cRecord, sort_value).asc())
        elif sort_order.startswith(GAIADR3VARIABLE_SORT_ORDER[1]):
            query = query.order_by(getattr(GaiaDR3VariableQ3cRecord, sort_value).desc())

    # return query
    return query
