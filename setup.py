# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name='autoeq',
    version='1.2.5',
    author='Jaakko Pasanen',
    packages=['autoeq'],
    scripts=[],
    url='https://github.com/jaakkopasanen/autoeq-pkg',
    licence='MIT Licence',
    description='Tool for equalizing headphones',
    platforms=['any'],
    keywords=['headphones', 'equalization'],
    install_requires=[
        'Pillow~=7.2.0',
        'matplotlib~=3.3.3',
        'pandas~=1.2.0',
        'scipy~=1.5.4',
        'numpy~=1.19.5',
        'tensorflow~=2.4.0',
        'tabulate~=0.8.5',
        'soundfile~=0.10.2'
    ]
)
