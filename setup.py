from setuptools import find_packages, setup
from typing import List


def get_requirements() -> List[str]:
    """
    This function will return the list of requirements 
    from requirements.txt file
    """

    req_list: List[str] = []

    try:
        with open("requirements.txt", "r") as req_file:
            lines = req_file.readlines()
            for line in lines:
                req = line.strip()
                # ignore empty lines and editable installs
                if req and req != "-e .":
                    req_list.append(req)
    except FileNotFoundError:
        print("No requirements.txt file found.")

    return req_list


setup(
    name="network_security_system",
    version="0.1.0",
    author="Oday Najad",
    author_email="oday.najad@lau.edu",
    packages=find_packages(),
    install_requires=get_requirements(),
)
