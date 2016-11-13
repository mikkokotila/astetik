#! /usr/bin/env python
#
import os
# temporarily redirect config directory to prevent matplotlib importing
# testing that for writeable directory which results in sandbox error in
# certain easy_install versions
os.environ["MPLCONFIGDIR"] = "."

DESCRIPTION = "Pretty data visualization and reporting library"
LONG_DESCRIPTION = """\

Pretty provides a very high level overlay on Seaborn and matplotlib.
It is a data visualization library for data exploration, and for 
telling captivating stories with data. Unlike any other visualization
library, Pretty is specifically made for day-to-day use by data 
scientists and reduces learning curve compared to similar solutions 
significantly. 

"""

DISTNAME = 'pretty'
MAINTAINER = 'Mikko Kotila'
MAINTAINER_EMAIL = 'mailme@mikkokotila.com'
URL = 'http://mikkokotila.com'
LICENSE = 'MIT'
DOWNLOAD_URL = 'https://github.com/mikkokotila/pretty'
VERSION = '0.9.2'

try:
    from setuptools import setup
    _has_setuptools = True
except ImportError:
    from distutils.core import setup

def check_dependencies():
    install_requires = []

    try:
        import numpy
    except ImportError:
        install_requires.append('numpy')
    try:
        import seaborn
    except ImportError:
        install_requires.append('seaborn')
    try:
        import matplotlib
    except ImportError:
        install_requires.append('matplotlib')
    try:
        import pandas
    except ImportError:
        install_requires.append('pandas')
    try:
        import IPython
    except ImportError:
        install_requires.append('IPython')
    try:
        import statsmodels
    except ImportError:
        install_requires.append('statsmodels')
    try:
        import patsy
    except ImportError:
        install_requires.append('patsy')

    return install_requires

if __name__ == "__main__":

    install_requires = check_dependencies()

    setup(name=DISTNAME,
        author=MAINTAINER,
        author_email=MAINTAINER_EMAIL,
        maintainer=MAINTAINER,
        maintainer_email=MAINTAINER_EMAIL,
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        license=LICENSE,
        url=URL,
        version=VERSION,
        download_url=DOWNLOAD_URL,
        install_requires=install_requires,
        packages=['pretty'],
        classifiers=[
                     'Intended Audience :: Science/Research',
                     'Programming Language :: Python :: 2.7',
                     'Operating System :: POSIX',
                     'Operating System :: Unix',
                     'Operating System :: MacOS'],
          )