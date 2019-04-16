---
layout: post
title:  "Generating thermal profiles for LAMMPS simulations"
date:   2019-03-25
categories: thermal profile lammps
---

This notebook generates thermal profiles for LAMMPS simulations. All you need to do is define the temperatures then the notebook will generate an NVT equilibration phase (10K steps), NPT equilibration phase (40K steps, P = 1.01325 bar), and NPT sampling step (40K steps, P = 1.01325 bar) for each temperature. Should be easy to make modifications. Please feel free to do so. If you'd like me to include your updates, then please shoot me an email with your notebook or Python script.


```python
# loads numpy
import numpy as np
```


```python
# define temperatures
temps = np.arange(10, 30, 10)
temps
```




    array([10, 20])




```python
# generate thermal profile
k = 1
for temp in temps :
    for i in range(3) :
        if i == 0 :
            # nvt equilibration
            print("fix {} all nvt temp {} {} 1.0".format(k, temp, temp))
            print("run 10000")
            print("unfix {}".format(k))
            print("")
        elif i == 1 :
            # npt equilibration
            print("fix {} all npt temp {} {} 1.0 aniso 1.01325 1.01325 5.0".format(k, temp, temp))
            print("run 40000")
            print("unfix {}".format(k))
            print("")
        else :
            # npt sampling
            print("fix {} all npt temp {} {} 1.0 aniso 1.01325 1.01325 5.0".format(k, temp, temp))
            print("dump {} all custom 200 dump{:03d}.xyz x y z".format(k, temp))
            print("dump_modify {} sort id".format(k))
            print("run 40000")
            print("write_restart BST.restart{:03d}".format(temp))
            print("undump {}".format(k))
            print("unfix {}".format(k))
            print("")
        k += 1
```

    fix 1 all nvt temp 10 10 1.0
    run 10000
    unfix 1
    
    fix 2 all npt temp 10 10 1.0 aniso 1.01325 1.01325 5.0
    run 40000
    unfix 2
    
    fix 3 all npt temp 10 10 1.0 aniso 1.01325 1.01325 5.0
    dump 3 all custom 200 dump010.xyz x y z
    dump_modify 3 sort id
    run 40000
    write_restart BST.restart010
    undump 3
    unfix 3
    
    fix 4 all nvt temp 20 20 1.0
    run 10000
    unfix 4
    
    fix 5 all npt temp 20 20 1.0 aniso 1.01325 1.01325 5.0
    run 40000
    unfix 5
    
    fix 6 all npt temp 20 20 1.0 aniso 1.01325 1.01325 5.0
    dump 6 all custom 200 dump020.xyz x y z
    dump_modify 6 sort id
    run 40000
    write_restart BST.restart020
    undump 6
    unfix 6
    

