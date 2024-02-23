
# when installing requirements.txt file, since it has -e . it look for setup.py file 
# it opens setup.py file, execute, automatically set all folders within US_Visa folder as local packages since they have __init__ constructor; it helps importing local packages, modules

from setuptools import setup, find_packages

setup(
    name="US_Visa",
    version="0.0.0",
    author="Malleswari",
    author_email="malleswari.gelli@gmail.com",
    packages=find_packages()
)