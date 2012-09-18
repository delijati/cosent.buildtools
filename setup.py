from setuptools import setup, find_packages

version = '0.3'

# http://pypi.python.org/pypi?%3Aaction=list_classifiers
setup(name='cosent.buildtools',
      version=version,
      description="Release scripts",
      long_description=open('README.rst').read(),
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GPL License',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: POSIX',
          'Programming Language :: Python :: 2',
      ],
      keywords='python git buildout',
      author='Guido Stevens',
      author_email='guido.stevens@cosent.net',
      url='http://cosent.nl',
      license='GPL',
      packages=find_packages(),
      namespace_packages=['cosent'],
      test_suite='cosent.buildtools.tests',
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'jarn.mkrelease',
      ],
      entry_points={
          'console_scripts': ['bumpversion=cosent.buildtools.bumpversion:main',
                              'buildtool=cosent.buildtools.buildtool:main']
      },
      )
