#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
"""

import io, sys, os
from shutil import rmtree

from setuptools import find_packages, setup, Command

__THISDIR = os.path.dirname(__file__)

PACKNAME            = 'test_huggin' # this package...
PACKURL             = 'https://github.com/gjacopo/test-huggin'
DESCRIPTION         = 'transformers for dummies'
VERSION             = None

REQUIRES_PYTHON = '>=3.6.0'

REQUIRED = [
    'numpy', 'pandas', 'transformers''
]

EXTRAS = {
}

class UploadCommand(Command):
 
    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds…')
            rmtree(os.path.join(__THISDIR, 'dist'))
        except OSError:
            pass

        self.status('Building Source and Wheel (universal) distribution…')
        os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))

        self.status('Uploading the package to PyPI via Twine…')
        os.system('twine upload dist/*')

        self.status('Pushing git tags…')
        os.system('git tag v{0}'.format(about['__version__']))
        os.system('git push --tags')
        
        sys.exit()


setup(
    name =                              PACKNAME,
    description =                       DESCRIPTION,
    python_requires =                   REQUIRES_PYTHON,
    url =                               PACKURL,
    packages =                          find_packages(exclude=('tests','notebooks')),
    install_requires =                  REQUIRED,
    extras_require =                    EXTRAS,
    include_package_data =              True,
    license =                           'EUPL',
    classifiers =                       [
                                        'Programming Language :: Python',
                                        'Programming Language :: Python :: 3',
                                        'Programming Language :: Python :: 3.6',
                                        'Topic :: Database'
                                        ],
    cmdclass =                          {
                                        'upload': UploadCommand,
                                        },
)
