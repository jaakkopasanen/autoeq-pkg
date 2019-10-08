# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name='AutoEQ',
    version='1.0.0',
    author='Jaakko Pasanen',
    packages=['autoeq'],
    scripts=[],
    url='https://github.com/jaakkopasanen/autoeq-pkg',
    licence='MIT Licence',
    description='Tool for equalizing headphones',
    platforms=['any'],
    keywords=['mongodb', 'mongoengine'],
    install_requires=[
        'Pillow',
        'matplotlib',
        'pandas',
        'scipy',
        'numpy',
        'tensorflow(<1.15.0)',
        'tabulate',
        'gevent',
        'soundfile'
    ]
)
