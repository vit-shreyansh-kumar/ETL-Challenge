from setuptools import find_packages, setup
from package import Package


try:
    setup(
        name = "Test",
        version="1.0",
        author="Shreyansh Kumar",
        url="https://github.com/vit-shreyansh-kumar/ETL-Challenge.git",
        author_email="shreyansh.kumar2012@vitalum.ac.in",
        packages= 'Test',
        include_package_data=True,
        zip_safe=False
    )
except Exception as e:
    msg = e
    print("Error occurred:",msg)