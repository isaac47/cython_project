# Import libraries
import numpy
import setuptools
from Cython.Build import cythonize
import Cython.Compiler.Options

Cython.Compiler.Options.annotate = True

# Compile Cython files
setuptools.setup(name='preprocess', ext_modules=cythonize("preprocessor_v1.pyx", annotate=True),
                 include_dirs=[numpy.get_include()])
