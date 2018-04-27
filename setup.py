#!/usr/bin/env python
"""Script to load defaults to database and install the packages."""
import atexit
import subprocess as sp

from setuptools.command.install import install
from distutils.cmd import Command

from setuptools import find_packages, setup


class Migrate(Command):
    """Migrate the database and create sample users."""
    description = 'Makemigrations for PoPe models.' 

    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        cmds = [
            './manage.py makemigrations users',
        ]
        sp.call('./manage.py migrate --noinput'.split())
        for cmd in cmds:
            sp.call(cmd.split())


setup(
    name='pope',
    version='0.1',
    install_requires=[
        'celery==4.1.0',
        'coreapi==2.3.1',
        'django==1.11',
        'django-cors-headers<2.2',
        'django-filter==1.0.4,<1.1',
        'django-rest-auth<1',
        'djangorestframework==3.7.7',
        'elasticsearch<5.5',
        'elasticsearch-dsl>=5.0.0,<6.0.0',
        'markdown<=2.6',
        'Pillow<4.3',
        'psycopg2<2.8',
        'pycryptodomex<3.5',
        'requests<2.19',
        'watson-developer-cloud==1.0.2',
    ],
    extras_require={
        'dev': ['flake8', 'astroid==1.5.3', 'rednose<1.3',
                'django-nose', 'coverage']
    },
    packages=find_packages(),
    scripts=['manage.py'],
    author='CPA - Bay Area',
    author_email='fabricasoftwares@gmail.com',
    url='https://github.com/cpa-bayarea/pope',
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
        'install': Migrate,
    }
)
