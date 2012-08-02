#!/usr/bin/python
"""
Copyright (c) 2012, William Betts
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met: 

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer. 
2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution. 
3. Redistributions of source code must reproduce the author lines at the top 
   of the original files. You may add to them (i.e. mention you modified the 
   file), but you may not subtract from them.
4. If redistributed in binary form you may not strip the author lines from any
   files before compiling.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

The views and conclusions contained in the software and documentation are those
of the authors and should not be interpreted as representing official policies, 
either expressed or implied, of the FreeBSD Project.

Author: William Betts
File: injector.py
Date: 8-01-2012

Comment:
    This is the file that is actually ran to inject email into powermta.
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
