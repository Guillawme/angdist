from setuptools import setup
from os import path

# Get the long description from the README file
here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding = 'utf-8') as f:
    readme = f.read()

setup(
    name = 'angdist',
    version = '1.3',

    description = 'Plot the 2D histogram of Euler angles covered by a set of cryo-EM particles',
    long_description = readme,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/Guillawme/angdist',

    author = 'Guillaume Gaullier',
    author_email = 'contact@gaullier.org',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Visualization',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Environment :: Console',
        'Natural Language :: English'
    ],
    keywords = 'cryo-EM Euler angle histogram visualization',

    py_modules = ["angdist"],

    python_requires = '>=3.9.7',
    install_requires = [
        'click>=8.0.3',
        'matplotlib>=3.4.3',
        'starfile>=0.4.9'
    ],

    entry_points = {
        'console_scripts': [
            'angdist=angdist:cli'
        ]
    },

    project_urls = {
        'Bug Reports': 'https://github.com/Guillawme/angdist/issues',
        'Source': 'https://github.com/Guillawme/angdist'
    }
)
