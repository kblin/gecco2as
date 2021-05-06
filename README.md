gecco2as - Convert GECCO result tables into antiSMASH sideload JSON files
=========================================================================

Small script to convert [GECCO](https://gecco.embl.de/) result tables into
[antiSMASH](https://antismash.secondarymetabolites.org/)
[sideload JSON](https://docs.antismash.secondarymetabolites.org/sideloading/) files.


Installation
------------

Grab the `gecco2as.py` script from GitHub, it will run with Python 3.6 and newer and has no dependencies.


Running
-------

Provided the `gecco2as.py` script is in your local directory, run it like this:

```
./gecco2as.py example.clusters.tsv > example.sideload.json
```


License
-------

All code is available under the Apache License version 2, see the
[`LICENSE`](LICENSE) file for details.
