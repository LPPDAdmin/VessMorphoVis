####################################################################################################
# Copyright (c) 2019 - 2020, EPFL / Blue Brain Project
# Author(s): Marwan Abdellah <marwan.abdellah@epfl.ch>
#
# This file is part of VessMorphoVis <https://github.com/BlueBrain/VessMorphoVis>
#
# This program is free software: you can redistribute it and/or modify it under the terms of the
# GNU General Public License as published by the Free Software Foundation, version 3 of the License.
#
# This Blender-based tool is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
# PURPOSE.  See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with this program.
# If not, see <http://www.gnu.org/licenses/>.
####################################################################################################


####################################################################################################
# @write_string_to_file
####################################################################################################
def write_string_to_file(string,
                         file_path):
    """Write a string to a file

    :param string:
        A string to be written to the file.
    :param file_path:
        The output path of the file.
    """

    # Open the file
    file_handle = open(file_path, 'w')

    # Write the string
    file_handle.write(string)

    # Close the file
    file_handle.close()


####################################################################################################
# @write_list_string_to_file
####################################################################################################
def write_list_string_to_file(list_strings,
                              file_path):
    """Write a string to a file

    :param list_strings:
        A string list to be written to the file.
    :param file_path:
        The output path of the file.
    """

    # Open the file
    file_handle = open(file_path, 'w')

    # Write the strings
    for string in list_strings:
        file_handle.write(string + '\n')

    # Close the file
    file_handle.close()


####################################################################################################
# @write_distribution_to_file
####################################################################################################
def write_distribution_to_file(distribution,
                               file_path):
    """Write a string to a file

    :param distribution:
        A list containing analysis distribution.
    :param file_path:
        The output path of the file.
    """

    # Open the file
    file_handle = open(file_path, 'w')

    # Write the strings
    for element in distribution:
        file_handle.write(str(element) + '\n')

    # Close the file
    file_handle.close()
