#!/usr/bin/env python
"""Script to load defaults to database and install the packages."""
import atexit
import subprocess as sp

from setuptools.command.install import install
from distutils.cmd import Command

from setuptools import find_packages, setup

APPS = [
    'users',
    'geographic',
    'organizations',
    'services',
]


class Migrate(Command):
    """Migrate the database and create sample users."""
    description = 'Makemigrations for PoPe models.'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        for app in APPS:
            sp.call('./manage.py makemigrations {}'.format(app).split())
        sp.call('./manage.py migrate --noinput'.split())


class LoadFixtures(Command):
    """Load fixtures from all apps to the database."""
    description = 'Populate database with default data.'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        fixtures = [
            'geographic/fixtures/administrative_areas.json'
        ]
        for data in fixtures:
            sp.call('./manage.py loaddata {}'.format(data).split())


setup(
    name='pope',
    version='1.0',
    install_requires=[
        'django>=2.1.5',
        'django-compressor==2.2',
        'markdown<=2.6',
        'Pillow<4.3',
        'requests>=2.20',
        'djangorestframework==3.8.2',
        'django-filter>=1.0.1',
        'coreapi>=1.32',
        'pygments',
        'django-cors-headers>=2.4.0',
        'gunicorn'
    ],
    extras_require={
        'dev': ['flake8', 'astroid==1.5.3', 'rednose<1.3',
                'django-nose', 'coverage']
    },
    packages=find_packages(),
    scripts=['manage.py'],
    author='CPA - Bay Area',
    author_email='fabricasoftwares@gmail.com',
    url='https://www.bayareacpa.com.br',
    entry_points={
        'console_scripts': [
            'pope=manage:main'
        ]
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.6',
    ],
    cmdclass={
        'migrate': Migrate,
        'loaddb': LoadFixtures
    }
)
