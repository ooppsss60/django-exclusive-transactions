from setuptools import setup, find_packages


setup(
    name="django-exclusive-transactions",
    version="0.0.1",
    packages=find_packages(),

    # author="",
    # author_email="",
    # description="",
    # long_description=open("README.md").read(),
    url="https://github.com/ooppsss60/django-exclusive-transactions",
    include_package_data=True,
    install_requires=[
        "Django >= 1.8",
    ],
    zip_safe=True,
)