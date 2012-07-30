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
        parser.add_argument('-c', '--campaign', required = True, help = 'The campaign to send', metavar = 'example-campaign')
        parser.add_argument('-s', '--hostname', required = False, help = 'The hostname or IP address of the PMTA server to inject to. If this option is omited it defaults to 127.0.0.1', metavar = '127.0.0.1')
        parser.add_argument('-p', '--port', required = False, help = 'The port the PMTA server is listening on. If this option is omited it defaults to 25', metavar = '25')
        self.args = parser.parse_args()
