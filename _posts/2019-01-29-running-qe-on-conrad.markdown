---
layout: post
title:  "Running Quantum Espresso on Conrad"
date:   2019-01-29
categories: qe
---
Today, I figured out that there is a working `pw.x` executable for Quantum Espresso on the DoD machine Conrad. It is located in `/app/espresso/6.3-intel/bin`. All you need is a PBS script with an execution line like

```
aprun -n 32 /app/espresso/6.3-intel/bin/pw.x < qe.in > qe.out
```

Also, you need to do `module load intel` prior to submitting the job. You can either add a line in your `.bashrc` or place it in the PBS script. Enjoy!
