import os.path
import sys

from SIC_Simulator.sic_configuration import SIC_DEFAULT_WORKING_DIRECTORY
from SIC_Utilities.sic_constants import SIC_ASSEMBLY_LISTING_FILE_EXTENSION
from SIC_Utilities.sic_messaging import print_error, print_status

class SICAssemblyListingParserError(Exception):
    pass


# This function reads an assembly list file (*.lst).
# It processes each line of code one at a time.
# It parses out the memory address and stores it with
# the corresponding line of code in a line of code dictionary.
# It returns a list containing all the parsed line of code
# dictionaries.
def sic_assembly_listing_parser(assembly_listing_file):
    parsed_listing_dict_list = []

    start_found = False
    end_found = False

    for line_of_listing in assembly_listing_file:
        memory_address = line_of_listing[:4]
        unparsed_line_of_listing = line_of_listing[:-1]

        # Check for empty line in assembly listing file
        if line_of_listing.isspace():
            # Close assembly file and throw exception
            assembly_listing_file.close()

            # ERROR
            raise SICAssemblyListingParserError("Assembly listing cannot contain blank lines")

        if not start_found:
            if line_of_listing[19:28].rstrip() == "START":
                start_found = True
            else:
                # Close assembly file and throw exception
                assembly_listing_file.close()

                # ERROR
                raise SICAssemblyListingParserError("START must be the first opcode in the in assembly listing file")
        else:
            if line_of_listing[19:28].rstrip() == "END":
                # Close assembly listing file, print status message, and exit program
                assembly_listing_file.close()

                return parsed_listing_dict_list
            else:
                parsed_listing_dict = {memory_address: unparsed_line_of_listing}

                parsed_listing_dict_list.append(parsed_listing_dict)

    if not end_found:
        # Close assembly file and throw exception
        assembly_listing_file.close()

        # ERROR
        raise SICAssemblyListingParserError("END was not found in assembly listing file")


# TEST BED
# assembly_listing_file_name = "ReadWrite"
#
# assembly_listing_file_path = (SIC_DEFAULT_WORKING_DIRECTORY +
#                               assembly_listing_file_name +
#                               "." +
#                               SIC_ASSEMBLY_LISTING_FILE_EXTENSION)
#
# parsed_listing_dict_list = sic_assembly_listing_parser(assembly_listing_file_path)
#
# for line in parsed_listing_dict_list:
#     print(line)
