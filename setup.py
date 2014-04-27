from setuptools import setup

setup(
    name='MARKr',
    version='1.0',
    long_description=__doc__,
    packages=['project'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask', 
        'requests', 
        'SQLAlchemy', 
        'Flask-SQLAlchemy', 
        'MySQL-python', 
        'fabric'
    ]
) 