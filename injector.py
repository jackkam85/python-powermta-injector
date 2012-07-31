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
        injector = MailMergeSMTP(campaigns_handler, cli_parser.args.hostname, cli_parser.args.port)
    else:
        injector = MailMergeSMTP(campaigns_handler)

    while True:
        address = list_handler.GetAddress()
        """
        print 'from: ' + campaigns_handler.GetFrom()
        print 'ff: ' + campaigns_handler.GetFriendlyFrom()
        print 'subject: ' + campaigns_handler.GetSubject()
        print 'body: ' + campaigns_handler.GetBody()
        """
        if address == None:
            break

        injector.Inject(address)


except IOError as e:
    print e.strerror

except ValueError as e:
    print e
