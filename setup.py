# -*- python -*-
#
#       Copyright CIRAD - INRAE
#
#       File author(s):
#
#       File contributor(s):
#
#       Distributed under the Cecill-C License.
#       See accompanying file LICENSE.txt or copy at
#           http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html
#
#       OpenAlea WebSite : http://openalea.gforge.inria.fr
#
# ==============================================================================
"""
"""
# ==============================================================================
from setuptools import setup, find_packages
# ==============================================================================

setup(
    name="gafam",
    version="1.0",
    description="Growing AgroForestry with Apple in Mediterranean climate",
    long_description="Analysis of Growing AgroForestry with Apple in Mediterranean climate",

    author="* Christophe Pradal\n"
           "* Francesco Reyes\n",

    author_email="* christophe.pradal@cirad.fr\n",
    maintainer="",
    maintainer_email="",

    url="https://github.com/openalea/gafam",
    license="Cecill-C",
    keywords='openalea, apple tree, MTG, analysis, agroforestery',

    # package installation
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    package_data={"": ["*.txt"]},
    zip_safe=False,
    )
