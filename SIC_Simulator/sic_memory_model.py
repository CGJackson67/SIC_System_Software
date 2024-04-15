from SIC_Utilities.sic_constants import BYTES_IN_MEMORY
from SIC_Utilities.sic_converter import dec_to_memory_address_hex_string


EMPTY_BYTE = "--"
SMALL_SEPARATOR = " "  # One space
LARGE_SEPARATOR = "   "  # Three spaces
BYTES_PER_GROUP = 4
BYTES_PER_ROW = 16
ROWS_IN_MEMORY_DUMP = BYTES_IN_MEMORY // BYTES_PER_ROW


class SICAddressOutOfRangeError(Exception):
    pass


def initialize_memory():
    # Create an empty dictionary to model memory
    # and then load dictionary with empty bytes
    memory_model_dict = {}

    for byte_address_dec in range(BYTES_IN_MEMORY):
        memory_model_dict[byte_address_dec] = EMPTY_BYTE

    return memory_model_dict


def dump_memory(memory_model_dict):
    # Rows 0 through 2048 (32767 / 16)
    for row in range(ROWS_IN_MEMORY_DUMP):
        # Memory Row Format:
        # ADDR   MEMORY CONTENTS
        # XXXX   -- -- -- --   -- -- -- --   -- -- -- --   -- -- -- --

        # Create memory_row_string and initialize it
        # with a byte address as a 4-digit hex number
        memory_row_string = dec_to_memory_address_hex_string(row * BYTES_PER_ROW)

        # 0 through 15
        for byte_column in range(BYTES_PER_ROW):
            # Calculate byte address
            byte_address_dec = row * BYTES_PER_ROW + byte_column

            if byte_address_dec % BYTES_PER_GROUP == 0:
                memory_row_string += LARGE_SEPARATOR + memory_model_dict[byte_address_dec]
            else:
                memory_row_string += SMALL_SEPARATOR + memory_model_dict[byte_address_dec]

        print(memory_row_string)


# TEST BED
memory_model_dict = initialize_memory()

dump_memory(memory_model_dict)
