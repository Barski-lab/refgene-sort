from setuptools import setup, find_packages
import os

setup(
    name='refgene-sort',
    description='refGene sort utility',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    version='v0.0.1',
    url='https://github.com/Barski-lab/refgene-sort',
    download_url=('https://github.com/Barski-lab/refgene-sort'),
    author='Michael Kotliar',
    author_email='misha.kotliar@gmail.com',
    license = 'Apache 2.0',
    packages=find_packages(),
    package_data={'refgene_sort': ['*.sql']},
    install_requires=[
        'argparse'
    ],
    zip_safe=False,
    entry_points={
        'console_scripts': [
            "refgene-sort=refgene_sort.main:main"
        ]
    }
)