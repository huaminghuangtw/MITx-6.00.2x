### Introduction

In this problem set you will practice designing a simulation and implementing a program that uses classes.

As with previous problem sets, please don't be discouraged by the apparent length of this assignment. There is quite a bit to read and understand, but most of the problems do not involve writing much code.

  
### Getting Started

**Download and save**

[pset2.zip](https://prod-edxapp.edx-cdn.org/assets/courseware/v1/5ac75dd1b33a9b97132c0b1b24e65324/asset-v1:MITx+6.00.2x+3T2018a+type@asset+block/pset2.zip): A zip file of all the files you need, including:

> 1. ps2.py, a skeleton of the solution.
> 2. ps2_visualize.py, code to help you visualize the robot's movement (an optional - but cool! - part of this problem set).
> 3. ps2_verify_movement35.pyc, precompiled module for Python 3.5 that assists with the visualization code. In ps2.py you will uncomment this out if you have Python 3.5.
> 4. ps2_verify_movement36.pyc, precompiled module for Python 3.6 that assists with the visualization code. In ps2.py you will uncomment this out if you have Python 3.6.

For precompiled module for Python 3.7 (or newer), please visit: [Richard-B-UK/MITx-6.00.2x-version-files-for-Python-3.5---3.9](https://github.com/Richard-B-UK/MITx-6.00.2x-version-files-for-Python-3.5---3.9)


### REVIEW OBJECT ORIENTED PROGRAMMING AND CLASSES

This and future problem sets will require you to know OOP. If you need a refresher, please visit these links and make sure you are familiar with these topics.

* Implementing [new classes and their attributes](https://greenteapress.com/thinkpython2/html/thinkpython2016.html).
* Understanding [class methods](https://greenteapress.com/thinkpython2/html/thinkpython2018.html).
* Understanding [inheritance](https://greenteapress.com/thinkpython2/html/thinkpython2019.html).
* Telling the difference between a class and an instance of that class - recall that a *class* is a blueprint of an object, whilst an *instance* is a single, unique unit of a class.
* Utilizing libraries as black boxes.


**Note**: If you want to use numpy arrays, you should add the following lines at the beginning of your code for the grader:

```python
import os
os.environ["OPENBLAS_NUM_THREADS"] = "1"
```

Then, do `import numpy as np` and use `np.METHOD_NAME` in your code.
