try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'My Project',
	'author': 'Karl Byas',
	'url': 'URL to get it at.',
	'download_url': 'https://github.com/karlbyas/repo',
	'author_email': 'karlbyas@studiokb.net',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['NAME'],
	'scripts': [],
	'name': 'projectname'
}

setup(**config)
