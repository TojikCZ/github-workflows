"""Setup.py for testing github workflows."""

from setuptools import setup  # type: ignore

setup(
    name="github-workflows",
    version="0.0.1",
    description="Test github workflows",
    author="Tom",
    author_email="tojik@tojik.cz",
    maintainer="Tom",
    maintainer_email="tojik@tojik.cz",
    url="https://github.com/TojikCZ/github-workflows",
    packages=["pylintable"],
    license="AGPLv3",
    license_files=[],
    long_description="Test github workflows, lorem ipsum dolor",
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Programming Language :: Python :: 3 :: Only",
    ],
    python_requires=">=3.9",
    entry_points={'console_scripts': ['pylintable = pylintable.pylintable:print_hi']})

