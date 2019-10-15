try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'ex47',
	'author': 'Karl Byas',
	'url': 'ttps://github.com/karlbyas/lpthw',
	'download_url': 'https://github.com/karlbyas/repo',
	'author_email': 'karlbyas@studiokb.net',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['ex47'],
	'scripts': [],
	'name': 'ex47'
}

setup(**config)
