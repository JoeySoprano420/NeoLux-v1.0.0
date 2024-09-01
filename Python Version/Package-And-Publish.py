import os
import subprocess

def package_project():
    """
    Creates a distribution package for NeoLux.
    """
    subprocess.run(["python", "setup.py", "sdist", "bdist_wheel"], check=True)

def publish_project():
    """
    Publishes the package to PyPI.
    """
    subprocess.run(["twine", "upload", "dist/*"], check=True)

def main():
    """
    Main function to package and publish the project.
    """
    package_project()
    publish_project()

if __name__ == '__main__':
    main()
