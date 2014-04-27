from setuptools import setup

setup(
    name='MARKr',
    version='1.0',
    long_description=__doc__,
    packages=['project'],
    include_package_data=True,
    zip_safe=False,
    dependency_links=['http://pypi.python.org/packages/source/F/Flask/Flask-0.10.1.tar.gz'],
    install_requires=[
        'Flask', 
        'requests', 
        'SQLAlchemy', 
        'Flask-SQLAlchemy', 
        'MySQL-python', 
        'fabric'
    ]
   
) 