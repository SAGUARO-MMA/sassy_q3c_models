#!/bin/sh

python3 -c "import sassy_q3c_models.asassn_q3c_orm;          print(sassy_q3c_models.asassn_q3c_orm.__doc__)"
python3 -c "import sassy_q3c_models.fermi_lat_q3c_orm;       print(sassy_q3c_models.fermi_lat_q3c_orm.__doc__)"
python3 -c "import sassy_q3c_models.glade_plus_q3c_orm;      print(sassy_q3c_models.glade_plus_q3c_orm.__doc__)"
python3 -c "import sassy_q3c_models.gwgc_q3c_orm;            print(sassy_q3c_models.gwgc_q3c_orm.__doc__)"
python3 -c "import sassy_q3c_models.gaiadr3variable_q3c_orm; print(sassy_q3c_models.gaiadr3variable_q3c_orm.__doc__)"
python3 -c "import sassy_q3c_models.hecate_q3c_orm;          print(sassy_q3c_models.hecate_q3c_orm.__doc__)"
python3 -c "import sassy_q3c_models.milliquas_q3c_orm;       print(sassy_q3c_models.milliquas_q3c_orm.__doc__)"
python3 -c "import sassy_q3c_models.non_detections_orm;      print(sassy_q3c_models.non_detections_orm.__doc__)"
python3 -c "import sassy_q3c_models.ps1_q3c_orm;             print(sassy_q3c_models.ps1_q3c_orm.__doc__)"
python3 -c "import sassy_q3c_models.romabzcat_q3c_orm;       print(sassy_q3c_models.romabzcat_q3c_orm.__doc__)"
python3 -c "import sassy_q3c_models.sdss12photoz_q3c_orm;    print(sassy_q3c_models.sdss12photoz_q3c_orm.__doc__)"
python3 -c "import sassy_q3c_models.tns_q3c_orm;             print(sassy_q3c_models.tns_q3c_orm.__doc__)"
python3 -c "import sassy_q3c_models.ztf_fp_q3c_orm;          print(sassy_q3c_models.ztf_fp_q3c_orm.__doc__)"
python3 -c "import sassy_q3c_models.ztf_q3c_orm;             print(sassy_q3c_models.ztf_q3c_orm.__doc__)"

python3 sassy_q3c_models/asassn_q3c_orm_cli.py          --help
python3 sassy_q3c_models/afermi_latq3c_orm_cli.py       --help
python3 sassy_q3c_models/gaiadr3variable_q3c_orm_cli.py --help
python3 sassy_q3c_models/glade_plus_q3c_orm_cli.py      --help
python3 sassy_q3c_models/gwgc_q3c_orm_cli.py            --help
python3 sassy_q3c_models/hecate_q3c_orm_cli.py          --help
python3 sassy_q3c_models/milliquas_q3c_orm_cli.py       --help
python3 sassy_q3c_models/non_detections_orm_cli.py      --help
python3 sassy_q3c_models/ps1_q3c_orm_cli.py             --help
python3 sassy_q3c_models/romabzcat_q3c_orm_cli.py       --help
python3 sassy_q3c_models/sdss12photoz_q3c_orm_cli.py    --help
python3 sassy_q3c_models/tns_q3c_orm_cli.py             --help
python3 sassy_q3c_models/ztf_fp_q3c_orm_cli.py          --help
python3 sassy_q3c_models/ztf_q3c_orm_cli.py             --help
