from setuptools import setup, find_packages

setup(name='Greater than, equal, or less Library',
      version='0.1',
      url='https://github.com/vinaynv3/Ormuco/tree/master/Greater%20than%2C%20equal%2C%20or%20less%20Library',
      license='MIT',
      author='Vinaynv3',
      author_email='vinaynv987@gmail.com',
      description='Add static script_dir() method to Path',
      packages=find_packages(exclude=['tests']),
      long_description=open('README.md').read(),
      zip_safe=False)