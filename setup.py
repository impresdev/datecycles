from setuptools import setup, find_packages

setup(
    name='datecycles',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'datecycles=datecycles.cli:main',
        ],
    },
    install_requires=[
        # Add your dependencies here, for example:
        'python-dateutil',
    ],
)
