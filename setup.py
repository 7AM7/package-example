
from setuptools import setup, find_packages

setup(
    name='cluc-am7',
    version='0.0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='An example python package',
    long_description=open('README.txt').read(),
    install_requires=['numpy'],
    url='https://github.com/7AM7/python-package-example',
    author='AM7',
    author_email='myemail@example.com',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
