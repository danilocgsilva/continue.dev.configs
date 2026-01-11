from setuptools import setup, find_packages

setup(
    name="continue_dev_configs",
    version="0.1",
    packages=find_packages(),
    install_requires=[
    ],
    author="Danilo Silva",
    author_email="contact@danilocgsilva.me",
    description="Facilitates the generation of local configuration yaml for Continue.dev",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/danilocgsilva/continue.dev.configs",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={"console_scripts": ["continue_dev_configs=continue_dev_configs.__main__:main"]},
)
