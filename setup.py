import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-sweetcaptcha',
    version='0.2',
    packages=['sweetcaptcha'],
    include_package_data=True,
    license='BSD License',
    description='A simple Django sweetcaptcha field/form app.',
    long_description=README,
    url='http://github.com/jordij/django-sweetcaptcha',
    author='Jordi J. Tablada',
    author_email='hi@jordijoan.me',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)

