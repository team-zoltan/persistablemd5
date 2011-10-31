import os
from setuptools import setup, find_packages

version = '0.0.2'
README = os.path.join(os.path.dirname(__file__), 'README.rst')
long_description = open(README).read() + '\n\n'

if __name__ == '__main__':
    setup(
        name='persistablemd5',
        version=version,
        description=('Adds get- and setstate methods to hashlib.md5'),
        long_description=long_description,
        author='Team Zoltan',
        author_email='zoltan@spideroak.com',
        url='https://github.com/team-zoltan/persistablemd5',
        license='MIT',
        classifiers=[
            "Intended Audience :: Developers",
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python",
            "Topic :: Software Development :: Libraries :: Python Modules",
        ],
        packages=find_packages(),
        test_suite='persistablemd5.test',
        tests_require=['mock'],
    )
