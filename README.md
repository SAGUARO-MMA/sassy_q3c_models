# sassy\_q3c\_models

Pythonic object request models (ORMs) for the SASSyII database tables (mainly) using Q3C indexing.


## Set Up

```bash
 % git clone https://github.com/SAGUARO-MMA/sassy\_q3c\_models.git
 % cd sassy\_q3c\_models
 % python3 -m pip install -r requirements.txt
 % python3 setup.py install
```

or

```bash
 % pip install git+https://github.com/SAGUARO-MMA/sassy\_q3c\_models.git
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
   - export DB\_HOST='localhost'
   - export DB\_PORT=5432
   - export DB\_NAME='mydb'
   - export DB\_USER='myu'
   - export DB\_PASS='myp'
 - Create the database table by executing:
   - cd sassy\_q3c\_models/bin
   - bash gwgc.table.sh `${DB\_HOST}` `${DB\_PORT}` `${DB\_NAME}` `${DB\_USER}` `${DB\_PASS}`
 - Get and check the catalog by executing:
   - cd sassy\_q3c\_models/sassy\_q3c\_models
   - python3 gwgc\_q3c\_orm\_cli.py --catalog --verbose
   - mv gwgc.dat.gz gwgc.dat
   - wc -l gwgc.dat
     - 53312 gwgc.dat
   - md5sum gwgc.dat
     - d42cbe71e33a56d8fbc214c673e594ad gwgc.dat
 - Load the catalog by executing:
   - cd sassy\_q3c\_models/sassy\_q3c\_models
   - python3 gwgc\_q3c\_read.py --file=gwgc.dat
 - Execute a simple check:
   - cd sassy\_q3c\_models/bin
   - mv sassy\_q3c\_models/sassy\_q3c\_models/gwgc.dat .
   - bash gwgc\_q3c.check.sh `${DB\_HOST}` `${DB\_PORT}` `${DB\_NAME}` `${DB\_USER}` `${DB\_PASS}`

You can do similar things with the other, well known, static catalogs (*i.e. viz.,* create the database
table, get the catalog and then read the catalog in with the appropriate read file). For the dynamic catalogs 
(non\_detections and ztf), you will find the data uploads a significant burden so seek advice first.
For TNS, they have a nightly data dump that can be used to re-produce the public data but, for that,
you will need an account and a bot key.

`SassyCron` is a derivative data product that you should contact the author about.

## Use Case(s)

### direct import
```bash 
 % python3
 >>> import sassy\_q3c\_models.asassn\_q3c\_orm\_cli
 >>> import sassy\_q3c\_models.desi\_spec\_q3c\_orm\_cli
 >>> import sassy\_q3c\_models.fermi\_lat\_q3c\_orm\_cli
 >>> import sassy\_q3c\_models.gaiadr3variable\_q3c\_orm\_cli
 >>> import sassy\_q3c\_models.glade\_plus\_q3c\_orm\_cli
 >>> import sassy\_q3c\_models.gwgc\_q3c\_orm\_cli
 >>> import sassy\_q3c\_models.hecate\_q3c\_orm\_cli
 >>> import sassy\_q3c\_models.ls\_dr10\_q3c\_orm\_cli
 >>> import sassy\_q3c\_models.milliquas\_q3c\_orm\_cli
 >>> import sassy\_q3c\_models.non\_detections\_orm\_cli
 >>> import sassy\_q3c\_models.ps1\_q3c\_orm\_cli
 >>> import sassy\_q3c\_models.roma\_bzcat\_q3c\_orm\_cli
 >>> import sassy\_q3c\_models.sdss12photoz\_q3c\_orm\_cli
 >>> import sassy\_q3c\_models.tns\_q3c\_orm\_cli
 >>> import sassy\_q3c\_models.ztf\_fp\_q3c\_orm\_cli
 >>> import sassy\_q3c\_models.ztf\_q3c\_orm\_cli
```

### from import

```bash 
 % python3
 >>> from sassy\_q3c\_models.asassn\_q3c\_orm\_cli import *
 >>> from sassy\_q3c\_models.desi\_spec\_q3c\_orm\_cli import *
 >>> from sassy\_q3c\_models.fermi\_lat\_q3c\_orm\_cli import *
 >>> from sassy\_q3c\_models.gaiadr3variable\_q3c\_orm\_cli import *
 >>> from sassy\_q3c\_models.glade\_plus\_q3c\_orm\_cli import *
 >>> from sassy\_q3c\_models.gwgc\_q3c\_orm\_cli import *
 >>> from sassy\_q3c\_models.hecate\_q3c\_orm\_cli import *
 >>> from sassy\_q3c\_models.ls\_dr10\_q3c\_orm\_cli import *
 >>> from sassy\_q3c\_models.milliquas\_q3c\_orm\_cli import *
 >>> from sassy\_q3c\_models.non\_detections\_orm\_cli import *
 >>> from sassy\_q3c\_models.ps1\_q3c\_orm\_cli import *
 >>> from sassy\_q3c\_models.roma\_bzcat\_q3c\_orm\_cli import *
 >>> from sassy\_q3c\_models.sdss12photoz\_q3c\_orm\_cli import *
 >>> from sassy\_q3c\_models.tns\_q3c\_orm\_cli import *
 >>> from sassy\_q3c\_models.ztf\_fp\_q3c\_orm\_cli import *
 >>> from sassy\_q3c\_models.ztf\_q3c\_orm\_cli import *
```

### your project

Add the following to your requirement.txt:

```bash
  git+https://github.com/SAGUARO-MMA/sassy\_q3c\_models.git
```

## Database Table(s)

```bash
 python3 -c "import sassy\_q3c\_models.asassn\_q3c\_orm;             print(sassy\_q3c\_models.asassn\_q3c\_orm.\_\_doc\_\_)"
 python3 -c "import sassy\_q3c\_models.desi\_spec\_q3c\_orm;         print(sassy\_q3c\_models.desi\_spec\_q3c\_orm.\_\_doc\_\_)"
 python3 -c "import sassy\_q3c\_models.fermi\_lat\_q3c\_orm;         print(sassy\_q3c\_models.fermi\_lat\_q3c\_orm.\_\_doc\_\_)"
 python3 -c "import sassy\_q3c\_models.glade\_plus\_q3c\_orm;        print(sassy\_q3c\_models.glade\_plus\_q3c\_orm.\_\_doc\_\_)"
 python3 -c "import sassy\_q3c\_models.gwgc\_q3c\_orm;               print(sassy\_q3c\_models.gwgc\_q3c\_orm.\_\_doc\_\_)"
 python3 -c "import sassy\_q3c\_models.gaiadr3variable\_q3c\_orm;    print(sassy\_q3c\_models.gaiadr3variable\_q3c\_orm.\_\_doc\_\_)"
 python3 -c "import sassy\_q3c\_models.hecate\_q3c\_orm;             print(sassy\_q3c\_models.hecate\_q3c\_orm.\_\_doc\_\_)"
 python3 -c "import sassy\_q3c\_models.ls\_dr10\_q3c\_orm;           print(sassy\_q3c\_models.ls\_dr10\_q3c\_orm.\_\_doc\_\_)"
 python3 -c "import sassy\_q3c\_models.milliquas\_q3c\_orm;          print(sassy\_q3c\_models.milliquas\_q3c\_orm.\_\_doc\_\_)"
 python3 -c "import sassy\_q3c\_models.non\_detections\_orm;         print(sassy\_q3c\_models.non\_detections\_orm.\_\_doc\_\_)"
 python3 -c "import sassy\_q3c\_models.ps1\_q3c\_orm;                print(sassy\_q3c\_models.ps1\_q3c\_orm.\_\_doc\_\_)"
 python3 -c "import sassy\_q3c\_models.romabzcat\_q3c\_orm;          print(sassy\_q3c\_models.romabzcat\_q3c\_orm.\_\_doc\_\_)"
 python3 -c "import sassy\_q3c\_models.sdss12photoz\_q3c\_orm;       print(sassy\_q3c\_models.sdss12photoz\_q3c\_orm.\_\_doc\_\_)"
 python3 -c "import sassy\_q3c\_models.tns\_q3c\_orm;                print(sassy\_q3c\_models.tns\_q3c\_orm.\_\_doc\_\_)"
 python3 -c "import sassy\_q3c\_models.ztf\_fp\_q3c\_orm;            print(sassy\_q3c\_models.ztf\_fp\_q3c\_orm.\_\_doc\_\_)"
 python3 -c "import sassy\_q3c\_models.ztf\_q3c\_orm;                print(sassy\_q3c\_models.ztf\_q3c\_orm.\_\_doc\_\_)"
```

## Command Line Interface(s)
 
```bash
 % cd <your\_installation\_directory>
 % python3 asassn\_q3c\_orm\_cli.py --help
 % python3 desi\_spec\_q3c\_orm\_cli.py --help
 % python3 fermi\_lat\_q3c\_orm\_cli.py --help
 % python3 gaiadr3variable\_q3c\_orm\_cli.py --help
 % python3 glade\_plus\_q3c\_orm\_cli.py --help
 % python3 gwgc\_q3c\_orm\_cli.py --help
 % python3 hecate\_q3c\_orm\_cli.py --help
 % python3 ls\_dr10\_q3c\_orm\_cli.py --help
 % python3 milliquas\_q3c\_orm\_cli.py --help
 % python3 non\_detections\_orm\_cli.py --help
 % python3 ps1\_q3c\_orm\_cli.py --help
 % python3 romabzcat\_q3c\_orm\_cli.py --help
 % python3 sdss12photoz\_q3c\_orm\_cli.py --help
 % python3 tns\_q3c\_orm\_cli.py --help
 % python3 ztf\_q3c\_orm\_cli.py --help
 % python3 ztf\_fp\_q3c\_orm\_cli.py --help
```

--------------------------------------

Last Modified: 20240711

Last Author: Phil Daly (pndaly@arizona.edu)
