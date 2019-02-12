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
* [Molecular structures](http://www.cse.anl.gov/OldCHMwebsiteContent/compmat/g2-97_cart_neut.txt) - cartesian coordinates for a bunch of molecules
  
These are some books that I highly recommend.
  
* [Materials Modelling using Density Functional Theory](https://www.amazon.com/Materials-Modelling-Density-Functional-Theory/dp/0199662444) - great introduction to practical DFT calculations  
* [Fundamental Concepts in Heterogeneous Catalysis](https://onlinelibrary.wiley.com/doi/book/10.1002/9781118892114) - a compact but comprehensive introduction to theoretical and computational catalysis  
  
Codes I've written to automate some processes. Please let me know if you encounter any difficulties.
  
* [VASP to xsf structure file converter](https://github.com/rwexler/tools/blob/master/structure/vasp2xsf.py) - just type `python vasp2xsf.py <filename>.POSCAR.vasp`  
* [cfg to xsf structure file converter](https://github.com/rwexler/tools/blob/master/structure/cfg2xsf.py) - just type `python cfg2xsf.py <filename>.cfg`  
* [Restart QE vc-relax](https://github.com/rwexler/tools/blob/master/qe/re-vc-relax.py) - first change `<filename>.in` to `<filename>.in.old`, then run `python re-vc-relax.py <filename>.out` (note: PBS script should be called `runscript`)
* [k-convergence in QE](https://github.com/rwexler/tools/blob/master/qe/k-pt-conv.py) - modify `values` and then type `python k-pt-conv.py <filename>.in`
* [plane wave convergence in QE](https://github.com/rwexler/tools/blob/master/qe/pw-conv.py) - modify `values` and then type `python pw-conv.py <filename>.in`
* [csv of Lowdin charges](https://github.com/rwexler/tools/blob/master/qe/lowdin-csv.py) - wrangles Lowdin charges in a csv file, just type `python lowdin-csv.py <filename>.out` with `projwfc.x` output
* [Phonon free energy](https://github.com/rwexler/tools/blob/master/phonons/harmonic.py) - calculates the phonon free energy for a range of temperatures using QE `ph.x` output, just type `python harmonic.py dynmat.out`
* [QE to xsf converter](https://github.com/rwexler/tools/blob/master/qe/qe2xsf.py) - just type `python qe2xsf.py <filename prefix>` where the prefix is everything that comes before the `.`
* [Restart QE relax](https://github.com/rwexler/tools/blob/master/qe/re-relax.py) - run `python re-relax.py <filename prefix>` (currently doesn't support fixed atoms)

Here are some tools I use on a regular basis.

* [VESTA](http://jp-minerals.org/vesta/en/) - static crystal structure visualization
* [VMD](https://www.ks.uiuc.edu/Research/vmd/) - efficient visualization of molecular dynamics simulations
* [FileZilla](https://filezilla-project.org/) - GUI for file transfers
* [Inkscape](https://inkscape.org/) - free vector graphics software
* [RStudio](https://www.rstudio.com/) - environment for R programming
* [Avogadro](https://avogadro.cc/) - static molecular structure visualization
* [Octave](https://www.gnu.org/software/octave/) - free alternative to MATLAB
* [Mercury](https://www.ccdc.cam.ac.uk/Community/csd-community/freemercury/) - molecule/crystal visualization software that can also count bonds/angles/dihedrals and calculate the BFDH morphology
* [Anaconda](https://www.anaconda.com/distribution/) - powerful software manager for Python
