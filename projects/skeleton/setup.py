try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My project',
    'author': 'Adam Szymanowski',
    'url': 'URL to get it at',
    'download_url': 'Where to download it.',
    'author_email': 'adam.szym@yahoo.pl',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'name': 'projectname'
}

setup(**config)