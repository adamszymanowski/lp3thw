try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Automated Testing',
    'author': 'Adam Szymanowski',
    'url': 'URL to get it at',
    'download_url': 'Where to download it.',
    'author_email': 'adam.szym@yahoo.pl',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['Ex 47'],
    'name': 'Exercise 47'
}

setup(**config)