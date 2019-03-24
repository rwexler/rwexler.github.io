---
layout: post
title:  "gzip in parallel using pigz"
date:   2019-03-24
categories: gzip parallel pigz
---

If you are running MD simulations, then this is the post for you. It can sometimes be a nightmare to compress MD trajectories because they can be so large, like multiple GBs (or maybe even TBs if you're working with gigantic systems). Up until now, I have found myself deleting MD trajectors but saving a restart file so that I can regenerate the data if I need to do further processing. This can be somewhat of a drag so I went searching for a way to compress MD trajectories in parallel. That's when I came across [pigz](https://zlib.net/pigz/). If you already know how to make a `tar.gz` file, then it is really easy to use pigz. For example, the pigz command corresponding to

`tar zcvf <filename>.tar.gz <filename/directory_name/etc>`

is

`tar cvf - <filename/directory_name/etc> | pigz -n <number_cores> <filename>.tar.gz`

Enjoy!
