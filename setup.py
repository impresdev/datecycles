from setuptools import setup, find_packages

setup(
    name='datecycles',
    version='0.1.1',
    description='A Python package designed for generating a series of dates based on specific cycle periods.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/impresdev/datecycles',
    author='impresdev',
    author_email='dev@impresario.net.au',
    license='MIT',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'datecycles=datecycles.cli:main',
        ],
    },
    install_requires=[
        'python-dateutil',
    ],
)
