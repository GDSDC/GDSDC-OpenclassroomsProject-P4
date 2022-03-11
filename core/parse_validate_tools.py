from typing import Any, Tuple, Optional, Callable
from datetime import datetime
from core.model import Sex, ControleDuTemps


# Functions for input parsing


def parse_string_not_empty(user_input: str) -> Tuple[Optional[Any], bool, str]:
    """Function that verify the input string is not empty"""
    if len(user_input) > 0:
        return user_input, True, ''
    else:
        return None, False, 'Votre entrée doit contenir au moins 1 caractère.'


def parse_int(user_input: str):
    """Function that verify the input is an int"""
    try:
        res = int(user_input)
        return res, True, ''
    except ValueError:
        return None, False, f"{user_input} n'est pas un entier valide."


def parse_float(user_input: str):
    """Function that verify the input is a float"""
    try:
        res = float(user_input)
        return res, True, ''
    except ValueError:
        return None, False, f"{user_input} n'est pas un entier décimal valide."


def parse_date(user_input: str):
    """Function that verify the input is a valid date"""
    try:
        day, month, year = user_input.split('/')
        res = datetime(int(year), int(month), int(day))
        return res, True, ''
    except ValueError:
        return None, False, f"{user_input} n'est pas un date valide."


# Functions for input validation


def validate_date_format(parsed_date: datetime):
    """Function that verify if the date format is dd/mm/yyyy"""
    if len(str(parsed_date.year)) == 4:
        res = parsed_date
        return res, True, ''
    else:
        return None, False, 'La date doit être au format jj/mm/aaaa'


def validate_integer_interval(parsed_int: int, interval: Tuple[int, int]):
    """Function that verify if the integer is in the interval"""
    res = parsed_int
    if (parsed_int >= interval[0]) and (parsed_int <= interval[1]):
        return res, True, ''
    else:
        return (
            None,
            False,
            f"{parsed_int} n'est pas compris entre {interval[0]} et {interval[1]}.",
        )


def validate_integer_positive(parsed_int: int):
    """Function that verify if the integer is positive"""
    res = parsed_int
    if parsed_int > 0:
        return res, True, ''
    else:
        return None, False, f"{parsed_int} n'est pas un entier positif."


def validate_controle_du_temps(user_input: str):
    """Function that verify if user_input is in Controle_du_temps(Enum)"""
    try:
        res = ControleDuTemps(user_input)
        return res, True, ''
    except ValueError:
        exemple_controle_du_temps = [
            controle_du_temps.value for controle_du_temps in ControleDuTemps
        ]
        return (
            None,
            False,
            f'"{user_input}" n\'est pas un choix de contrôle du temps valide. '
            f'Veuillez choisir un élément dans la liste {exemple_controle_du_temps}.',
        )


def validate_sexe(user_input: str):
    """Function that verify if user_input is in Sex(Enum)"""
    try:
        res = Sex(user_input)
        return res, True, ''
    except ValueError:
        exemple_sexe = [sexe.value for sexe in Sex]
        return (
            None,
            False,
            f'"{user_input}" n\'est pas un choix de sexe valide. '
            f'Veuillez choisir un élément dans la liste {exemple_sexe}.',
        )


def validate_actor_key(user_input: Any):
    """Function that verify if user_input is an int or str 'terminer' """
    if user_input == 'terminer':
        res = user_input
        return res, True, ''
    else:
        try:
            res = int(user_input)
            return res, True, ''
        except ValueError:
            return (
                None,
                False,
                f'"{user_input}" n\'est pas un choix valide. Veuillez choisir un entier ou le mot "terminer".',
            )


def no_validation(user_input):
    """Function that do no validation when this is not needed"""
    res = user_input
    return res, True, ''


# Global Function Parse & Validate


def parse_and_validate(
        explanation: str,
        parse: Callable[[str], Tuple[Optional[Any], bool, str]],
        validate: Callable[[Any], Tuple[Any, bool, str]] = no_validation,
):
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
    pass
