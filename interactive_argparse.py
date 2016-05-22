#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Override `raw_input` with proper readline functionality
import readline

# Add tab completion to readline
readline.parse_and_bind('tab: complete')


# Main method for the interactive argument prompting
def interactive_argument_resolver(parser):
    input_strings = []
    # Iterate through all arguments in the parser
    for action in [a for a in parser.__dict__['_actions'] if a.nargs is not 0]:
        # Use the rightmost defined flag
        flag = action.option_strings[-1]

        # Iterate until input value is accepted
        while True:
            # Set an auto completer if choices are defined
            if action.choices:
                readline.set_completer(_make_autocompleter(action.choices))
            # Clear the auto completer otherwise
            else:
                readline.set_completer(_make_autocompleter(['']))

            # Prompt user for an input value
            value = raw_input(_prompt(action))

            # If user input is blank and there is a default value defined, use the default value
            if not value and action.default:
                value = action.default
                break
            # If user input validates
            if _value_validates(action, value):
                break

        # Add flag and value to resulting list of arguments
        input_strings.append(flag)
        input_strings.append(value)

    return parser.parse_args(input_strings)


def _value_validates(action, value):
    def error_message(message):
        return '>>> Error: {}'.format(message)

    # If choices exist, the value must be one of them
    if action.choices:
        return value in action.choices

    try:
        # Try parsing the value as the specified argument type
        action.type(value)
        return True
    except ValueError:
        print(error_message('Value has to be {}'.format(action.type)))
        return False
    except Exception as e:
        print(error_message(e.message))
        return False


# Creates an auto completer based on a list of possible choices
def _make_autocompleter(choices):
    def reduce_to_probable_choices(user_input):
        return [choice for choice in choices if choice.startswith(user_input)]

    def complete(user_input, state):
        probable_choices = reduce_to_probable_choices(user_input)
        return probable_choices[state]

    return complete


# Creates a prompt string
def _prompt(action):
    help_text = action.help
    choices = action.choices
    default = action.default
    prompt = help_text
    if choices:
        prompt += ' (legal values are {})'.format(', '.join(choices))
    if default:
        prompt += ' [{}]'.format(default)
    return prompt + ': '
