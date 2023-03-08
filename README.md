# UWO Physics &amp; Astronomy Python Course
Python course designed for grad students of the Physics &amp; Astronomy department at the University of Western Ontario.

## Course overview

### Lecture 1
* Print statement (Hello world!) → running with Ctrl+B
* Comments
* Variables and types (duck typing):
    * ints, floats (+, -, *, /, //, **, %, round function)
    * Multiple assignments
    * Strings
        * Adding strings
        * Accessing individual chars
        * Selecting a range of chars
        * Modifying strings - immutable!
        * len function
        * Repetition by multiplying
    * Converting one type to another
* Lists - universal containers!
    * append, pop, indexing, insert, remove
    * Reversing a list
    * Unpacking elements to variables
    * Multidimensional lists
    * Nested lists
    * range statement
    * map statement
    * join to string

### Lecture 2
* While loops
* If statements
* For loops
* File input/output
* Hands on example
* Homework - lists, loops

### Lecture 3
* File I/O continued
* os and shutil libraries - handling files, directories
* Task - batch file renaming (inspired by a problem from real life)
* Homework - batch file sorting

### Lecture 4
* Functions
* Programming style and style guides
* Handling and visualizing data 1
    * Numpy ("numerical Python")
    * Matplotlib - basics plots
* Task 1 - function for loading data from text files
* Task 2 - load data from a file and plot it
* Homework - handling time

### Lecture 5
* Advanced plotting in matplotlib
* Advanced data manipulation in numpy
* Sampling univariate and multivariate probability distributions
* Plotting histograms
* Sorting arrays
* Plotting images
* Plotting higher dimensionality data

### Lecture 6
* linear regression with least squares, RANSAC and Theil-Sen estimator (and their comparison)
* minimization: BFGS, Nelder-Mead and basin-hopping
* fitting nonlinear models

### Lecture 7
* integrating ODEs
* spline interpolation
* Fourier transform
* filters for signal processing
* wavelets
* detecting a low-frequency signal (determine it's exact occurrence in time and duration) in data abundant with high-frequency noise

### Lecture 8
* generators
* object oriented programming (basics, operator overloading, inheritance)
* list comprehension
* dictionaries
* sets

### Lecture 9
* parallel programming (multiprocessing, pool of workers, universal function for parallelization)
* exceptions (i.e. error handling)
* decorators
* regular expressions

### Lecture 10
* astroquery - querying astronomical databases and plotting data (we will have fun with SDSS data and color magnitude diagrams of globular clusters)
* a short word on dependencies
* Cython - converting slow Python code to C

### Homeworks
Homework solutions are available upon request.


## Installing Python on your computer

There are two approaches to installing Python packages:

### a) Installing Python Anaconda

Python Anaconda is a software package which contains Python + most used Python libraries. In all probability, is has all libraries you may ever need. To install Python Anaconda go here: https://www.anaconda.com/download and be careful to select the Python 3 version. 
If you are using Sublime on Linux, you might have to change an environment variable which will tell Sublime which installation of Python to use. Please see the section “Installing Sublime on your computer” below which will explain how to install Sublime Text 3 as well.

### b) Installing everything from scratch

This is probably a more difficult route, but this will give you a greater knowledge and flexibility when it comes to managing your Python libraries.  This is what I always do, as I like to have a better control over my Python installation.
The thing is, I cannot give universal instructions how to install Python and all its packages on your computer, as it depends on the operating system you are using.  What I can do is give you a list of things you’ll need, and let you google how to install them and get them working – there are plenty of resources online.
We are using Python 3.x (I recommend installing Python with the highest ‘x’ you can find, i.e. the latest version).

1. Python 3

1. Python libraries:
    1. Numpy (when installing on Windows, be sure to get the MKL package as well)
    1. Matplotlib
    1. Scipy (if the installation is failing on Linux, you are probably missing a few dependencies)
    1. Sci-kit learn
    1. Jupyter notebook
    1. Cython (this one may be tricky to get working on Windows if you don’t have Visual Studio installed, you will have to install an external C compiler and play with a few configuration files, but there are instructions online how to get it to work)
    1. astroquery



## Installing Sublime on your computer
If you want to install Sublime as well, go to this website: https://www.sublimetext.com/3 download and install it.

To install Sublime Anaconda, which will make your life easier, do this:

1. Open Sublime
2. Go to Tools->Command Palette
3. A new text box will open, start writing inside "Install Package Control", when that appears as an option, press Enter and it will install Package Control, i.e. the functionality to add more external packages.
4. Go to Tools->Command Palette again, start typing "Install Package" and press Enter when "Package Control: Install package" appears.
5. You will be presented with a list of packages to install.
6. Write "Anaconda" in the text box and install the first package on the list - Anaconda for Python.

Once this package is installed, Sublime will have Python auto-completion, code linting, etc. It will also try to tell you that you need to write your code according to the default Python coding style known as PEP8, as it will surround all code which does not conform to that standard in white boxes. This can be a bit annoying, and can be disabled if you do the following:

1. Open Sublime and go to ```Preferences -> Package settings -> Anaconda -> Settings - User``` (here: https://s27.postimg.org/). An empty file called "Anaconda.sublime-settings" will open.
2. Write inside it:
```
{
	"pep8": false,
}
```
3. Save the file. This will remove the white boxes.
