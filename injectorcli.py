"""
This class handles the parsing of the cli arguments.

Comment:
    Sometime in the future I can see having a lot of arguments
    that will need to handled in various ways which is why
    I have this as it's own class right now.
"""

import argparse

class InjectorCLI(object):
    def __init__(self):
        parser = argparse.ArgumentParser(description = 'PowerMTA Injector')
        parser.add_argument('-l', '--list', required = True, help = 'The email list to inject', metavar = 'email_list.txt')
        parser.add_argument('-c', '--creative', required = True, help = 'The creative to send', metavar = 'example-creative')
        self.args = parser.parse_args()
