from setuptools import setup

requirements = []

version = '0.1.0'

if not version:
    raise RuntimeError('version is not set')

with open('README.md') as f:
    readme = f.read()

setup(name='dbapi',
      author='Decorater',
      author_email='seandhunt_7@yahoo.com',
      url='https://github.com/AraHaan/dbapi',
      bugtrack_url='https://github.com/AraHaan/dbapi/issues',
      version=version,
      packages=['dbapi'],
      license='MIT',
      description='Discord Bots API for Discord Bots.',
      long_description=readme,
      maintainer_email='seandhunt_7@yahoo.com',
      download_url='https://github.com/AraHaan/dbapi',
      include_package_data=True,
      install_requires=requirements,
      platforms='Any',
      classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Other Audience',
        'Intended Audience :: Science/Research',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Telecommunications Industry',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
      ]
)
