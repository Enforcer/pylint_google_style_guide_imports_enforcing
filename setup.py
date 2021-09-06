from setuptools import setup

with open('README.rst') as readme_file:
    long_description = readme_file.read()

setup(
  name = 'pylint_google_style_guide_imports_enforcing',
  packages = ['pylint_google_style_guide_imports_enforcing'],
  version = '1.1.0',
  description = 'Plugin for PyLint that checks if we import only modules or packages. Direct imports of classes, functions and constants are forbidden',
  long_description = long_description,
  author = 'Sebastian Buczyński',
  author_email = 'nnplaya@gmail.com',
  url = 'https://github.com/Enforcer/pylint_google_style_guide_imports_enforcing',
  download_url = 'https://github.com/Enforcer/pylint_google_style_guide_imports_enforcing/archive/1.1.0.tar.gz',
  keywords = ['pylint', 'google style guide', 'imports'],
  classifiers = [],
  include_package_data=True
)
