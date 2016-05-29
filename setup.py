import os
import io
from setuptools import setup, find_packages

def read(*parts):
    with io.open(os.path.join(os.path.dirname(__file__), *parts)) as f:
        return f.read()

setup(
    name='django-yandexmoney-notice',
    url='http://github.com/nikicat/yandex_money_http_notifications_django',

    description='Django support for Yandex.Money HTTP notifications',
    long_description=read('README.md'),
    license='GNU GPLv3',

    author='Lev Tonkikh',
    author_email='leonst998@gmail.com',
    maintainer='Nikolay Bryskin',
    maintainer_email='nbryskin@gmail.com',

    packages=find_packages(),
    package_data={'': ['fixtures/*.yaml']},
    zip_safe=False,

    install_requires=[
        'PyYAML',
        'python-dateutil',
    ],

    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3) License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
