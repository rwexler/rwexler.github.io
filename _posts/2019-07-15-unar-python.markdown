---
layout: post
title: "Unzipping files into folders with the same name in Linux"
date:   2019-07-15
categories: unzip Python Linux
---

Here is a little Python script that unzips files into folders with the same name in Linux. Take, for example, the file `test.zip`. If it contains a number of files and you unzip using `unzip test.zip` on Linux, then they will all be decompressed into your present working directory. If you wanted the files to go into a folder bearing the prefix of zip file, i.e. `test`, then you'd have to write a shell script...until now! Just because, I wrote a python script that does the same thing using `unar`. Now, `unar` can do this for one file but not for several, e.g. as defined using a wildcar `*.zip`. My script, called `unzipr` (because every Python script needs a fancy name), does just this. Please feel free to use and pass along if you find it helpful!

```python
import sys
import os

filenames = sys.argv[1:]
for filename in filenames :
    os.system("unar -d {}".format(filename))
```

If you create an alias, i.e. add `alias unzipr="python <path-to-unzipr>/unzipr.py"` in your `.bashrc`, then you can unzip individual or multiple files seamlessly by executing `unzipr *.zip` on your command line. Happy zipping!
