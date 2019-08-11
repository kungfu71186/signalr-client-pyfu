import io
from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with io.open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
   long_description = f.read()

setup(
    name='signalr-client-pyfu',
    version='0.0.7.1',
    description='Simple SignalR client for Python',
    long_description=long_description,
    url='https://github.com/kungfu71186/signalr-client-pyfu',
    author='Kungfu',
    author_email='none@none.com',
    license='Apache',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='signalr',
    packages=find_packages(),
    install_requires=['gevent', 'websocket-client', 'sseclient', 'requests']
)
