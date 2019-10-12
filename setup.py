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
    keywords=['headphones', 'equalization'],
    install_requires=[
        'Pillow~=6.2.0',
        'matplotlib~=3.1.1',
        'pandas~=0.25.1',
        'scipy~=1.3.1',
        'numpy~=1.17.2',
        'tensorflow~=2.0.0',
        'tabulate~=0.8.5',
        'soundfile~=0.10.2'
    ]
)
