#!/bin/sh

python3 -c "import sassy_q3c_models.asassn_q3c_orm;     print(sassy_q3c_models.asassn_q3c_orm.__doc__)"
python3 -c "import sassy_q3c_models.glade_plus_q3c_orm; print(sassy_q3c_models.glade_plus_q3c_orm.__doc__)"
python3 -c "import sassy_q3c_models.glade_q3c_orm;      print(sassy_q3c_models.glade_q3c_orm.__doc__)"
python3 -c "import sassy_q3c_models.gwgc_q3c_orm;       print(sassy_q3c_models.gwgc_q3c_orm.__doc__)"
python3 -c "import sassy_q3c_models.hecate_q3c_orm;     print(sassy_q3c_models.hecate_q3c_orm.__doc__)"
python3 -c "import sassy_q3c_models.milliquas_q3c_orm;  print(sassy_q3c_models.milliquas_q3c_orm.__doc__)"
python3 -c "import sassy_q3c_models.non_detections_orm; print(sassy_q3c_models.non_detections_orm.__doc__)"
python3 -c "import sassy_q3c_models.sassy_cron_q3c_orm; print(sassy_q3c_models.sassy_cron_q3c_orm.__doc__)"
python3 -c "import sassy_q3c_models.sdss12phot_q3c_orm; print(sassy_q3c_models.sdss12phot_q3c_orm.__doc__)"
python3 -c "import sassy_q3c_models.tns_q3c_orm;        print(sassy_q3c_models.tns_q3c_orm.__doc__)"
python3 -c "import sassy_q3c_models.ztf_q3c_orm;        print(sassy_q3c_models.ztf_q3c_orm.__doc__)"

python3 sassy_q3c_models/asassn_q3c_orm_cli.py     --help
python3 sassy_q3c_models/glade_plus_q3c_orm_cli.py --help
python3 sassy_q3c_models/glade_q3c_orm_cli.py      --help
python3 sassy_q3c_models/gwgc_q3c_orm_cli.py       --help
python3 sassy_q3c_models/hecate_q3c_orm_cli.py     --help
python3 sassy_q3c_models/milliquas_q3c_orm_cli.py  --help
python3 sassy_q3c_models/non_detections_orm_cli.py --help
python3 sassy_q3c_models/sassy_cron_q3c_orm_cli.py --help
python3 sassy_q3c_models/sdss12phot_q3c_orm_cli.py --help
python3 sassy_q3c_models/tns_q3c_orm_cli.py        --help
python3 sassy_q3c_models/ztf_q3c_orm_cli.py        --help
