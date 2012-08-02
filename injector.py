#!/usr/bin/python
"""
This is the actual file that glues all the classes to gather
and preforms the actual injection.
"""

import sys

from injectorcli import InjectorCLI
from campaigns import Campaigns
from listhandler import ListHandler
from mailmergesmtp import MailMergeSMTP

cli_parser = InjectorCLI()
try:
    campaigns_handler = Campaigns(cli_parser.args.campaign)
    list_handler = ListHandler(cli_parser.args.list)

    if cli_parser.args.hostname != None and cli_parser.args.port != None:
        injector = MailMergeSMTP(cli_parser.args.use_from_as_redirect, campaigns_handler, cli_parser.args.hostname, cli_parser.args.port)
    else:
        injector = MailMergeSMTP(cli_parser.args.use_from_as_redirect, campaigns_handler)

    while True:
        address = list_handler.GetAddress()

        if address == None:
            break

        injector.Inject(address)

except IOError as e:
    print e.strerror

except ValueError as e:
    print e
