        current_value = romVal[roman_string[i]]
        previous_value = romVal[roman_string[i-1]]

        if previous_value >= current_value:
            value_int += previous_value
        else:
            value_int -= previous_value

    return value_int
