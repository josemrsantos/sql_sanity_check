# Deployment
This document is only intended to be a guide on how to deploy the SQLSanityCheck module. It is not intended to be a 
guide on how to deploy the SQLSanityCheck package both in github and in PyPi.

## How to create a new version of the package in github
1. Make sure you have the latest version of the code in your local repository.
2. Make sure you have the latest version of the code in the remote repository.
3. Make sure that the new version number is in the setup.py and in the __init__.py files.
4. Update the CHANGELOG.md file with the new version number and the changes that were made.
5. Commit the changes to the remote repository.
6. Tag the new version with the following command: `git tag -a v0.1.0 -m "Version 0.1.0"`.
7. Push the tag to the remote repository with the following command: `git push origin v0.1.0`.
8. In GitHub go to the releases tab and create a new release with the same tag name.

This should be enough to create a new version of the package in GitHub as long as you have the necessary permissions.

## How to deploy the package to PyPi
1. Make sure you have the latest version of the code in your local repository.
2. Build distribution files: `python setup.py sdist bdist_wheel`.
3. Upload to PyPI: `twine upload dist/*`.

This should work as long as you have the necessary permissions to upload to PyPi (a .pypirc file with the necessary 
credentials).
