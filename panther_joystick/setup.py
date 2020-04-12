## ! DO NOT MANUALLY INVOKE THIS setup.py, USE CATKIN INSTEAD

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

from io import open
# Launch command
from os import path
import re

here = path.abspath(path.dirname(__file__))
project_homepage = "https://github.com/rpanther/panther_hardware"

# with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
#     requirements = f.read().splitlines()

# Get the long description from the README file
with open(path.join(here, '../README.md'), encoding='utf-8') as f:
    long_description = f.read()

# fetch values from package.xml
setup_args = generate_distutils_setup(
    packages=['panther_joystick'],
    package_dir={'': 'scripts'},
    author_email="raffaello@rnext.it",
    description="Joystick manager for Panther. Tools to control leds, audio and roboteq controller.",
    license='MIT',
    long_description=long_description,
    long_description_content_type="text/markdown",
    download_url=(project_homepage + "/archive/master.zip"),
    project_urls={
        "How To": (project_homepage + "/tree/master/docs"),
        "Examples": (project_homepage + "/tree/master/examples"),
        "Bug Reports": (project_homepage + "/issues"),
        "Source": (project_homepage + "/tree/master")
    },
    # install_requires=requirements,
    )

setup(**setup_args)
