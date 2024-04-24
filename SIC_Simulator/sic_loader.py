from SIC_Simulator.sic_memory_model import initialize_memory
from SIC_Utilities.sic_converter import hex_string_to_dec


# This function will initialize the memory model and
# then load program object code into the memory model
def load_program_object_code(parsed_object_code_dict_list):
    memory_model_dict = initialize_memory()

    # Load object code into memory model
    for parsed_object_code_dict in parsed_object_code_dict_list:
        if parsed_object_code_dict["record_type"] == "text":
            address_hex_string = parsed_object_code_dict["start_address"]
            address_dec = hex_string_to_dec(address_hex_string)
            byte_list = parsed_object_code_dict["byte_list"]

            for byte in byte_list:
                memory_model_dict[address_dec] = byte
                address_dec += 1

    return memory_model_dict
