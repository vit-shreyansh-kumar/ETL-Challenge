from setuptools import find_packages, setup
from package import Package


try:
    setup(
        version="1.0",
        author="Shreyansh Kumar",
        author_email="shreyansh.kumar2012@vitalum.ac.in",
        packages=find_packages(),
        include_package_data=True,
        cmdclass={
            "package": Package
        }
    )
except Exception as e:
    msg = e
    print("Error occurred:",msg)