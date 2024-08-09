from setuptools import setup, find_packages

setup(
    name='shared-orm-library',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    description='A shared ORM library for Django projects',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Kamal Sharma',
    author_email='kamalsharma.git@gmail.com',
    license='MIT',
    python_requires='>=3.6',
    install_requires=[
        'Django>=3.2',
    ],
)
