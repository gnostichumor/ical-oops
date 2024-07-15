from setuptools import setup, find_packages

setup(
    name='ical-oops',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'ical-oops=ical_oops.cli:main',
        ],
    },
    install_requires=[],
    author='Matthew Preston',
    author_email='gnostichumor+ical-oops@gmail.com',
    description='A simple CLI to update iCal files with STATUS:CANCELLED for each event.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/gnostichumor/ical-oops',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)