from typing import Any, Dict, List, Tuple, Optional, Callable
from datetime import date

### Functions for input parsing

def parse_string_not_empty(user_input: str) -> Tuple[Optional[Any], bool, str]:
    ''' Function that verify the input string is not empty'''
    if len(user_input) > 0:
        return user_input, True, ''
    else:
        return None, False, 'String length must be > 0'

def parse_int(user_input: str):
    ''' Function that verify the input is an int'''
    try:
        res = int(user_input)
        return res, True, ''
    except ValueError:
        return None, False, f'{user_input} is not a valid integer'


def parse_date(user_input: str):
    '''Function that verify the input is a valid date'''
    try:
        day, month, year = user_input.split('/')
        res = date(int(year), int(month), int(day))
        return res, True, ''
    except ValueError:
        return None, False, f'{user_input} is not a valid date'



### Functions for input validation

def validate_date_format(parsed_date: date):
    '''Function that verify if the date format is dd/mm/yyyy'''
    if len(str(parsed_date.year)) == 4:
        res = parsed_date
        return res, True, ''
    else:
        return None, False, 'Date should be in the format dd/mm/yyyy'

def no_validation(user_input):
    '''Function that do no validation when this is not needed'''
    res = user_input
    return res, True, ''


### Global Function Parse & Validate

def parse_and_validate(explanation: str,
                       parse: Callable[[str], Tuple[Optional[Any], bool, str]],
                       validate: Callable[[Any], Tuple[Any, bool, str]]):
    is_valid, error_message = False, None
    final_result = None
    while not is_valid:
        user_input = input(explanation)
        validatable_result, is_valid, error_message = parse(user_input)
        if is_valid:
            final_result, is_valid, error_message = validate(validatable_result)
        if not is_valid:
            print(error_message)

    return final_result


if __name__ == '__main__':

    date_explanation = 'Renseignez un date : '
    result = parse_and_validate(explanation=date_explanation, parse=parse_date,validate=validate_date_format)
    result2 = parse_and_validate(explanation=date_explanation, parse=parse_date, validate=no_validation)
    print(result2)