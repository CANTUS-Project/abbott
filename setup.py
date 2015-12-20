#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#--------------------------------------------------------------------------------------------------
# Program Name:           abbot
# Program Description:    HTTP Server for the CANTUS Database
#
# Filename:               setup.py
# Purpose:                Configuration for installation with setuptools.
#
# Copyright (C) 2015 Christopher Antila
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#--------------------------------------------------------------------------------------------------
'''
Configuration for installation with setuptools.
'''

from setuptools import setup, Command
import abbot  # for __version__


class PyTest(Command):
    user_options = []
    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import subprocess
        import sys
        errno = subprocess.call([sys.executable, 'runtests.py'])
        raise SystemExit(errno)


setup(
    name = 'Abbot',
    version = abbot.__version__,
    packages = ['abbot', 'tests'],

    install_requires = [
        'pysolr-tornado',
        'systemdream==0.0.2',
        'tornado>=4,<5',
    ],
    tests_require = ['pytest'],

    scripts = ['packaging/start_abbot', 'runtests.py'],
    cmdclass = {'test': PyTest},

    # metadata for upload to PyPI
    author = 'Christopher Antila',
    author_email = 'christopher@antila.ca',
    description = 'HTTP Server for the CANTUS Database',
    license = 'AGPLv3+',
    keywords = 'database',
    url = 'http://cantusdatabase.org/',
    # TODO: long_description, download_url, classifiers, etc.
)
