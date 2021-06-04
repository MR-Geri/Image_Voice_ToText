from setuptools import setup, find_packages
from os.path import join, dirname
from ImageVoiceToText import __version__

setup(
    name='Image_Voice_ToText',
    version=__version__,
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    install_requires=[
        'opencv-python~=4.5.2.52',
        'pytesseract~=0.3.7',
        'imutils~=0.5.4'
    ]
)
