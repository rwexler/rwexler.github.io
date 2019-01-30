---
layout: page
title: Links
permalink: /links/
---

This page contains a number of links to resources that I find useful.

* [SeeK-path](https://www.materialscloud.org/work/tools/seekpath) - find k-point paths for band structure and phonon dispersion plots using crystal structure  
* [atomsk](http://atomsk.univ-lille1.fr/index.php) - easily generate different types of crystallographic defects  
* [Colby Energy Converter](http://www.colby.edu/chemistry/PChem/Hartree.html) - useful conversions between different energy units  
* [Halas Energy Converter](http://halas.rice.edu/conversions) - this one gives you energy to natural frequencies too  
* [matgenie](http://matgenie.materialsvirtuallab.org/) - generate slab model given Miller index and vacuum/slab size  
  
These are some books that I highly recommend.
  
* [Materials Modelling using Density Functional Theory](https://www.amazon.com/Materials-Modelling-Density-Functional-Theory/dp/0199662444) - great introduction to practical DFT calculations  
* [Fundamental Concepts in Heterogeneous Catalysis](https://onlinelibrary.wiley.com/doi/book/10.1002/9781118892114) - a compact but comprehensive introduction to theoretical and computational catalysis  
  
Codes I've written to automate some processes. Please let me know if you encounter any difficulties.
  
* [VASP to xsf structure file converter](https://github.com/rwexler/tools/blob/master/structure/vasp2xsf.py) - just type `python vasp2xsf.py <filename>.POSCAR.vasp`  
* [cfg to xsf structure file converter](https://github.com/rwexler/tools/blob/master/structure/cfg2xsf.py) - just type `python cfg2xsf.py <filename>.cfg`  
* [Restart QE vc-relax](https://github.com/rwexler/tools/blob/master/qe/re-vc-relax.py) - first change `<filename>.in` to `<filename>.in.old`, then run `python re-vc-relax.py <filename>.out` (note: PBS script should be called `runscript`)
