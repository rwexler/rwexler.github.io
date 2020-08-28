---
layout: post
title: "Removing duplicate atoms from structures"
date:   2020-08-20
categories: remove duplicate atoms structures
---

Sometimes ![ICSD](https://icsd.products.fiz-karlsruhe.de/) structures contain duplicate atoms...I learned 
the hard way. I was recently running some ![VASP](https://www.vasp.at/) calculations and was getting errors 
like `WARNING: CNORMN: search vector ill defined`. Additionally, I was finding that changing `ALGO` to `All` 
was producing the same error, leading to my conclusion that I likely had a problematic structure. Using 
![pymatgen](https://pymatgen.org/), you can quickly check if a structure contains duplicate atoms.

```python
from pymatgen.core.structure import Structure
s = Structure.from_file('POSCAR')
print(s.is_valid())
```      

With that said and to the best of my knowledge, ![pymatgen](https://pymatgen.org/) doesn't have a method for 
removing duplicate atoms. For that, I turned to ![atomsk](https://atomsk.univ-lille.fr/), *is a tool to 
convert and manipulate atomic data files*. ![atomsk](https://atomsk.univ-lille.fr/) has an option for
removing duplicate atoms (https://atomsk.univ-lille.fr/doc/en/option_rmd.html); it's really easy to use and
it works great! What worked for me was

```commandline
atomsk POSCAR -rmd 0.2 pos
```

which gave

```commandline
  ___________________________________________________
 |              ___________                          |
 |     o---o    A T O M S K                          |
 |    o---o|    Version master                       |
 |    |   |o    (C) 2010 Pierre Hirel                |
 |    o---o     https://atomsk.univ-lille.fr         |
 |___________________________________________________|
 >>> Opening the input file: POSCAR
 ..> Input file was read successfully (54 atoms).
 >>> Removing atoms that are closer than 0.200 A.
 >>> Constructing neighbor list...
 ..> 18 atoms were removed, 36 atoms left.
 >>> Writing output file(s) (36 atoms):
 <?> This file already exists: POSCAR
     Do you want to overwrite it (y/n) (Y=overwrite all)?
```

to which I answered `n` and gave `POSCAR.final` as a filename. The final message was

```commandline
 ..> Successfully wrote POSCAR file: POSCAR.final
 \o/ Program terminated successfully!
     Total time: 12.311 s.; CPU time: 0.007 s.
```

Bye bye duplicate atoms!
