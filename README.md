# interactive-argparse
Turn your [argparse](https://docs.python.org/2/howto/argparse.html)-parser into an interactive session, prompting the user for the defined arguments.

## Example run
```bash
$ ./example.py
A random string: a value here
One of these values (legal values are legal1, legal2): legal
legal1  legal2
One of these values (legal values are legal1, legal2): legal1
Some integer: a
>>> Error: Value has to be <type 'int'>
Some integer: 10
Some other integer: 101
Resulting arguments namespace: Namespace(a4=101, argument_one='a value here', argument_three=10, argument_two='legal1')
```
