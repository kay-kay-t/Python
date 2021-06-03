# http://pypi.org
# to install pip: in terminal - pip instal ....

import requests
response = requests.get("http://google.com")
print(response)

# pip install pipenv -  to create virtual enviroment
# pipenv shell
# pipenv graph - to see dependencies
# To publish pip:
# pip install setuptools wheel twine
# python setup.py sdist bdist_wheel
# twine upload dist/*

# docstring """ One line description.

# A more detailed explanaition.
# """

# pydoc utility
# pydoc ... < -- (module, like math)
