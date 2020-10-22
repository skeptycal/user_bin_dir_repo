#! /usr/bin/env python
# coding: utf-8

package_name="repo"

import os
import importlib
from setuptools import setup, find_packages

package = importlib.import_module('_' + package_name + '.main')

def read(*path):
    basepath = os.path.abspath(os.path.dirname(__file__))
    return open(os.path.join(basepath, *path)).read()

def main():
    install_requires = [
        'requests',
        'configobj', # r/w configuration files, preserving order & comments
        ]
    setup(
        name=package_name,
        version=package.__version__,
        description=package.__doc__,
        install_requires=install_requires,
        long_description=read('README.rst') + '\n\n' + read('CHANGELOG'),
        url='https://bitbucket.org/anthon_van_der_neut/' + package_name,
        author='Anthon van der Neut',
        author_email='a.van.der.neut@ruamel.eu',
        #license='MIT License',
        #py_modules=[package_name],
        packages=find_packages(exclude=['test*']),
        entry_points= {'console_scripts': ['{pn} = _{pn}.main:main'.format(pn=package_name)]},
        classifiers=['Development Status :: 3 - Alpha',
            'Environment :: Console',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: Software Development :: Version Control',
            'Topic :: Utilities',
        ]
    )

if __name__ == '__main__':
    main()