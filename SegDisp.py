from machine import Pin

DIGIT_PATTERNS = {
    0: (1, 1, 1, 1, 1, 1, 0),
    1: (0, 1, 1, 0, 0, 0, 0),
    2: (1, 1, 0, 1, 1, 0, 1),
    3: (1, 1, 1, 1, 0, 0, 1),
    4: (0, 1, 1, 0, 0, 1, 1),
    5: (1, 0, 1, 1, 0, 1, 1),
    6: (1, 0, 1, 1, 1, 1, 1),
    7: (1, 1, 1, 0, 0, 0, 0),
    8: (1, 1, 1, 1, 1, 1, 1),
    9: (1, 1, 1, 1, 0, 1, 1),
}

LETTERS_PATTERNS = {
    'A': (1, 1, 1, 0, 1, 1, 1),
    'B': (0, 0, 1, 1, 1, 1, 1),
    'C': (1, 0, 0, 1, 1, 1, 0),
    'D': (0, 1, 1, 1, 1, 0, 1),
    'E': (1, 0, 0, 1, 1, 1, 1),
    'F': (1, 0, 0, 0, 1, 1, 1),
    'O': (1, 1, 1, 1, 1, 1, 0), 
    'S': (1, 0, 1, 1, 0, 1, 1),
    'P': (1, 1, 0, 0, 1, 1, 1),
    'N': (0, 1, 1, 0, 1, 1, 0),
    'o': (0, 0, 1, 1, 1, 0, 1), 
    'n': (0, 0, 1, 0, 1, 0, 1),
}


def write_digit(pins, digit):
    pattern = DIGIT_PATTERNS.get(digit, DIGIT_PATTERNS[0])
    for pin, value in zip(pins, pattern):
        pin.value(value)

def write_letter(pins, letter):
    pattern = LETTERS_PATTERNS.get(letter, LETTERS_PATTERNS.get(letter.upper(), (0, 0, 0, 0, 0, 0, 0)))
    for pin, value in zip(pins, pattern):
        pin.value(value)


def display_distance(segments, distance):
    try:
        number = int(distance)
    except (TypeError, ValueError):
        number = 0

    if number < 0:
        number = 0
    elif number > 999:
        number = 999

    hundreds = number // 100
    tens = (number // 10) % 10
    ones = number % 10

    write_digit(segments[0], hundreds)
    write_digit(segments[1], tens)
    write_digit(segments[2], ones)

def display_message(segments, message):
    message = (message + "   ")[:3] 
    for i, char in enumerate(message):
        if char == ' ':
            for pin in segments[i]:
                pin.value(0)
        elif char.isdigit():
            write_digit(segments[i], int(char))
        else:
            write_letter(segments[i], char)

def show_startup_message(segments):
    display_message(segments, 'on')

def show_stop_message(segments):
    display_message(segments, 'OFF')