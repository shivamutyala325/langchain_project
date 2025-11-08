from setuptools import setup,find_packages

def find_requirements(path="./requirements.txt"):
    with open(path) as f:
        requirements=f.read().splitlines()

    return requirements



setup(

    name="langchain_project",
    version="0.0.1",
    description="it is a sample library build on langchain",
    author="shiva mutyala",
    author_email="shivamutyala325@gmail.com",
    packages=find_packages(where="src"),
    package_dir={"":"src"},
    install_requires=find_requirements()


)



