# sassy_q3c_models

Pythonic object request models (ORMs) for the SASSyII database tables (mainly) using Q3C indexing.


## Set Up

```bash
 % git clone https://github.com/SAGUARO-MMA/sassy_q3c_models.git
 % cd sassy_q3c_models
 % python3 -m pip install -r requirements.txt
 % python3 setup.py install
```

or

```bash
 % pip install git+https://github.com/SAGUARO-MMA/sassy_q3c_models.git
```


## Requirement(s)

 - Python3 (v3.6 or later)
 - PostGreSQL (v13 or later)
 - Q3C (v2.0 or later, https://github.com/segasai/q3c)

## Tutorial

Normally, this would only be of interest to people working on SASSyII or similar software as this 
code will not have the database or tables backing it after install. If you are not part of the SASSyII 
team but *really* want to try it out (or just want a tutorial on how this stuff hangs 
together), do the following (which assumes you have a standard PostGreSQL installation) using the GWGC 
catalog (as it's the smallest):

 - Execute using /bin/bash (change as you see fit):
   - export DB_HOST='localhost'
   - export DB_PORT=5432
   - export DB_NAME='mydb'
   - export DB_USER='myu'
   - export DB_PASS='myp'
 - Create the database table by executing:
   - cd sassy_q3c_models/bin
   - bash gwgc.table.sh `${DB_HOST}` `${DB_PORT}` `${DB_NAME}` `${DB_USER}` `${DB_PASS}`
 - Get and check the catalog by executing:
   - cd sassy_q3c_models/sassy_q3c_models
   - python3 gwgc_q3c_orm_cli.py --catalog --verbose
   - mv gwgc.dat.gz gwgc.dat
   - wc -l gwgc.dat
     - 53312 gwgc.dat
   - md5sum gwgc.dat
     - d42cbe71e33a56d8fbc214c673e594ad gwgc.dat
 - Load the catalog by executing:
   - cd sassy_q3c_models/sassy_q3c_models
   - python3 gwgc_q3c_read.py --file=gwgc.dat
 - Execute a simple check:
   - cd sassy_q3c_models/bin
   - mv sassy_q3c_models/sassy_q3c_models/gwgc.dat .
   - bash gwgc_q3c.check.sh `${DB_HOST}` `${DB_PORT}` `${DB_NAME}` `${DB_USER}` `${DB_PASS}`

You can do similar things with the other, well known, static catalogs (*i.e. viz.,* create the database
table, get the catalog and then read the catalog in with the appropriate read file). For the dynamic catalogs 
(non_detections and ztf), you will find the data uploads a significant burden so seek advice first.
For TNS, they have a nightly data dump that can be used to re-produce the public data but, for that,
you will need an account and a bot key.

`SassyCron` is a derivative data product that you should contact the author about.

## Use Case(s)

### direct import
```bash 
 % python3
 >>> import sassy_q3c_models.asassn_q3c_orm_cli
 >>> import sassy_q3c_models.gaiadr3variable_q3c_orm_cli
 >>> import sassy_q3c_models.glade_plus_q3c_orm_cli
 >>> import sassy_q3c_models.gwgc_q3c_orm_cli
 >>> import sassy_q3c_models.hecate_q3c_orm_cli
 >>> import sassy_q3c_models.milliquas_q3c_orm_cli
 >>> import sassy_q3c_models.non_detections_orm_cli
 >>> import sassy_q3c_models.ps1_q3c_orm_cli
 >>> import sassy_q3c_models.sdss12photoz_q3c_orm_cli
 >>> import sassy_q3c_models.tns_q3c_orm_cli
 >>> import sassy_q3c_models.ztf_q3c_orm_cli
```

### from import

```bash 
 % python3
 >>> from sassy_q3c_models.asassn import *
 >>> from sassy_q3c_models.gaiadr3variable_q3c_orm_cli import *
 >>> from sassy_q3c_models.glade_plus_q3c_orm_cli import *
 >>> from sassy_q3c_models.gwgc_q3c_orm_cli import *
 >>> from sassy_q3c_models.hecate_q3c_orm_cli import *
 >>> from sassy_q3c_models.milliquas_q3c_orm_cli import *
 >>> from sassy_q3c_models.non_detections_orm_cli import *
 >>> from sassy_q3c_models.ps1_q3c_orm_cli import *
 >>> from sassy_q3c_models.sdss12photoz_q3c_orm_cli import *
 >>> from sassy_q3c_models.tns_q3c_orm_cli import *
 >>> from sassy_q3c_models.ztf_q3c_orm_cli import *
```

### your project

Add the following to your requirement.txt:

```bash
  git+https://github.com/SAGUARO-MMA/sassy_q3c_models.git
```

## Database Table(s)

```bash
 python3 -c "import sassy_q3c_models.asassn_q3c_orm;          print(sassy_q3c_models.asassn_q3c_orm.__doc__)"
 python3 -c "import sassy_q3c_models.glade_plus_q3c_orm;      print(sassy_q3c_models.glade_plus_q3c_orm.__doc__)"
 python3 -c "import sassy_q3c_models.gwgc_q3c_orm;            print(sassy_q3c_models.gwgc_q3c_orm.__doc__)"
 python3 -c "import sassy_q3c_models.gaiadr3variable_q3c_orm; print(sassy_q3c_models.gaiadr3variable_q3c_orm.__doc__)"
 python3 -c "import sassy_q3c_models.hecate_q3c_orm;          print(sassy_q3c_models.hecate_q3c_orm.__doc__)"
 python3 -c "import sassy_q3c_models.milliquas_q3c_orm;       print(sassy_q3c_models.milliquas_q3c_orm.__doc__)"
 python3 -c "import sassy_q3c_models.non_detections_orm;      print(sassy_q3c_models.non_detections_orm.__doc__)"
 python3 -c "import sassy_q3c_models.ps1_q3c_orm;             print(sassy_q3c_models.ps1_q3c_orm.__doc__)"
 python3 -c "import sassy_q3c_models.sdss12photoz_q3c_orm;    print(sassy_q3c_models.sdss12photoz_q3c_orm.__doc__)"
 python3 -c "import sassy_q3c_models.tns_q3c_orm;             print(sassy_q3c_models.tns_q3c_orm.__doc__)"
 python3 -c "import sassy_q3c_models.ztf_q3c_orm;             print(sassy_q3c_models.ztf_q3c_orm.__doc__)"
```

## Command Line Interface(s)
 
```bash
 % cd <your_installation_directory>
 % python3 asassn_q3c_orm_cli.py --help
 % python3 gaiadr3variable_q3c_orm_cli.py --help
 % python3 glade_plus_q3c_orm_cli.py --help
 % python3 gwgc_q3c_orm_cli.py --help
 % python3 hecate_q3c_orm_cli.py --help
 % python3 milliquas_q3c_orm_cli.py --help
 % python3 non_detections_orm_cli.py --help
 % python3 ps1_q3c_orm_cli.py --help
 % python3 sdss12photoz_q3c_orm_cli.py --help
 % python3 tns_q3c_orm_cli.py --help
 % python3 ztf_q3c_orm_cli.py --help
```

--------------------------------------

Last Modified: 20230823

Last Author: Phil Daly (pndaly@arizona.edu)
