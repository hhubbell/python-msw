from setuptools import setup

setup(
    name='msw',
    version='0.1',
    description='A Python wrapper for the Magic Seaweed Marine Forecast API.',
    url='https://github.com/hhubbell/python-msw',
    author='Harry Hubbell',
    install_requires=[
        'requests'
    ]
    packages=['msw']
)
