from SIC_Utilities.sic_constants import HEX_TO_BIN_DICT, BIN_TO_HEX_DICT

NUMBER_OF_HEX_DIGITS = 6
NUMBER_OF_BIN_DIGITS = 24


class RegisterContentsError(Exception):
    pass


class SICRegisterModel:
    def __init__(self):
        self.hex_string = "------"
        self.bin_string = "------------------------"

    def hex_to_bin(self, hex_string):
        bin_string = ""

        for hex_digit in hex_string:
            bin_string += HEX_TO_BIN_DICT[hex_digit]

        print("bin_string:", bin_string)

        return bin_string

    def set_hex_string(self, hex_string):
        # Make sure hex_string contains all capital characters
        hex_string = hex_string.upper()

        # Error check for length and hex digits
        error_found = False
        if len(hex_string) != NUMBER_OF_HEX_DIGITS:
            error_found = True

        for digit in hex_string:
            if digit not in HEX_TO_BIN_DICT:
                error_found = True

        if error_found:
            raise RegisterContentsError

        # hex_string is OK, set the value
        self.hex_string = hex_string

        # Set self.register_bin_string
        self.bin_string = self.hex_to_bin(hex_string)

    def get_hex_string(self):
        return self.hex_string

    def bin_to_hex(self, bin_string):
        hex_string = ""
        # Register holds 24 bits
        # range(START, STOP, STEP)
        for index in range(0, 24, 4):
            hex_string += BIN_TO_HEX_DICT[bin_string[index:index + 4]]

        return hex_string

    def set_bin_string(self, bin_string):
        # Error check for length and hex digits
        error_found = False
        if len(bin_string) != NUMBER_OF_BIN_DIGITS:
            error_found = True

        for digit in bin_string:
            if digit != "0" and digit != "1":
                error_found = True

        if error_found:
            raise RegisterContentsError

        # bin_string is OK, set the value
        self.bin_string = bin_string

        # Set self.register_hex_string
        # Convert bin_string to hex
        self.hex_string = self.bin_to_hex(bin_string)

    def get_bin_string(self):
        return self.bin_string


# TEST BED
register_a = SICRegisterModel()
# register_a.set_hex_string("01FDeK")
register_a.set_bin_string("111111111000000011111111")
# register_a.hex_to_bin(register_a.bin_to_hex("001110111111110000011110"))
# register_a.hex_to_bin("01DEF3")
print("bin:", register_a.get_bin_string())
print("hex:", register_a.get_hex_string())
register_a.set_hex_string("f180ff")
print("bin:", register_a.get_bin_string())
print("hex:", register_a.get_hex_string())
register_x = SICRegisterModel()
register_l = SICRegisterModel()
register_pc = SICRegisterModel()
register_sw = SICRegisterModel()
