# A module is a file that contains some pythin code

from folder.subfolder import file
import name_of_the_file
from name_of_the_file import function, function

function()

# Or

name_of_the_file.function()

# If you add __init__.py file in a folder, python treats that folder
as a package with couple modules

# Absolute import
file.function()

# # Relative import
# from ..subfolder import file
# file.function()
