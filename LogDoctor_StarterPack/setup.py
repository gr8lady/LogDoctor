from setuptools import setup, find_packages

setup(
    name='logdoctor',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'logdoctor=logdoctor.main:cli'
        ]
    },
    install_requires=[
        'pandas',
        'transformers',
        'rich'
    ]
)
