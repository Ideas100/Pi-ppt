from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), 'r') as f:
    long_description = f.read()

setup(
    name='pippt',
    version='2.0.0',
    description='A simple presentation module',
    author='Pravin Raghul',
    author_email='pravinraghul@gmail.com',
    url='https://github.com/Ideas100/Pi-ppt',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    classifiers= [
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8'
    ],
    packages=['pippt'],
    py_modules=['pippt.script.pippt_script'],
    package_data={'pippt': ['data/*.dat']},
    entry_points={
        'console_scripts': ['pi-ppt = pippt.script.pippt_script:main'],
    },
    install_requires=['Pillow']
)
