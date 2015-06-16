from setuptools import setup

setup(
    name='msw',
    version='0.1',
    description='A Python wrapper for the Magic Seaweed Marine Forecast API.',
    url='https://github.com/hhubbell/python-msw',
    author='Harry Hubbell',
    install_requires=['requests'],
    packages=[
        'msw',
        'msw.spots',
        'msw.spots.africa',
        'msw.spots.asia',
        'msw.spots.australasia',
        'msw.spots.caribbean',
        'msw.spots.central_america',
        'msw.spots.europe',
        'msw.spots.indian_ocean',
        'msw.spots.indonesia',
        'msw.spots.middle_east',
        'msw.spots.north_america',
        'msw.spots.pacific_ocean',
        'msw.spots.south_america'
    ]
)
