from setuptools import setup, find_packages
from typing import List

# Define the editable install marker
HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    Reads a requirements file and returns a cleaned list of dependencies.
    """
    requirements = []

    try:
        with open(file_path, "r") as file_obj:
            # Read lines and strip newline characters
            requirements = [req.strip() for req in file_obj.readlines()]

        # Remove '-e .' if it exists in the list
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    except FileNotFoundError:
        print(f"Warning: {file_path} not found. No dependencies loaded.")

    return requirements

# Setup project metadata
setup(
    name="mlproject",
    version="0.0.1",
    author="astrooinaut",
    author_email="rooi860@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)