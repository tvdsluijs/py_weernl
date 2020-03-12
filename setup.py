from setuptools import setup, find_packages


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='py_weernl',
      version='0.3.2',
      description='Python WeerLive data parser',
      long_description=readme(),
      long_description_content_type="text/markdown",
      url='https://github.com/tvdsluijs/py_weernl',
      author='Theo van der Sluijs',
      author_email='theo@vandersluijs.nl',
      keywords='weather Netherlands Live',
      packages=find_packages(),
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
      ],
      zip_safe=False)
