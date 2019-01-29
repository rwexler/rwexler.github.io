---
layout: post
title:  "Compiling LAMMPS on Koehr"
date:   2019-01-28 
categories: compiling lammps
---
Today, I was able to successfully compile LAMMPS on DoD machine Koehr. First, I used `mpicc` as my C++ compiler. Then, I manually pointed the makefile to Intel's MPI libraries using the following three lines of code:

```
MPI_INC =       -I/app/intel/parallel_studio_xe_2018_update1/impi/2018.1.163/intel64/include
MPI_PATH =      -L/app/intel/parallel_studio_xe_2018_update1/impi/2018.1.163/intel64/lib
MPI_LIB =
```

Finally, I manually pointed the makefile to the FFTW3 library as follows :

```
FFT_INC =       -I/app/COST/fftw3/3.3.5/intel/include
FFT_PATH =      -L/app/COST/fftw3/3.3.5/intel/lib
FFT_LIB =       -lfftw3
```

That's all she wrote! Of course, I executed make in parallel as `make -j 48 <Makefile suffix>`. Next, I'm going to test this recipe on other DoD computers.

P.S. It is necessary to load the modules `costinit`, `fftw3/intel/3.3.5`, and `compiler/intelmpi/18.0.1.163` prior to running LAMMPS. I added two lines in my `.bashrc` to take care of this. This can also be done in your PBS script.
