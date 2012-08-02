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
File: mailmergesmtp.py
Date: 8-01-2012

Comment:
   This class interactes with the libpmta shared library to inject email
   into pmta over SMTP with mailmerge capabilities. 
"""
import time

from port25.submitter.message import Message, PmtaMessageError
from port25.submitter.recipient import Recipient, PmtaRecipientError
from port25.submitter.connection import Connection, PmtaConnectionError
from port25 import PmtaError

class MailMergeSMTP(object):
    def __init__(self, use_from, campaign_object, smtp_server_hostname = '127.0.0.1', smtp_server_port = '25'): 

        if use_from == None:
            self.__use_from = True
        else:
            self.__use_from = False

        self.__smtp_server_hostname = smtp_server_hostname
        self.__smtp_server_port = smtp_server_port
        self.__campaign_handler = campaign_object

    def Inject(self, address):
        try:
            print 'Connecting to %s on port %s' % (self.__smtp_server_hostname, self.__smtp_server_port)
            from_address = self.__campaign_handler.GetFrom()

            if self.__use_from == True:
                from_parts = from_address.split('@') 
                redirect_domain = from_parts[1]
            else:
                redirect_domain = self.__campaign_handler.GetDomain()

                if redirect_domain == None:
                    raise ValueError('The domains file can not be empty')

            rcpt = Recipient(address)
            rcpt.defineVariable('to', address)
            rcpt.defineVariable('friendlyfrom', self.__campaign_handler.GetFriendlyFrom())
            rcpt.defineVariable('from', from_address)
            rcpt.defineVariable('subject', self.__campaign_handler.GetSubject())
            rcpt.defineVariable('date', time.strftime("%a, %d %b %Y %H:%M:%S %z", time.gmtime()))
            rcpt.defineVariable('*parts', '1')
            rcpt.defineVariable('rdomain', redirect_domain)

            email = Message(from_address)

            email.addRecipient(rcpt)
            email.addMergeData(self.__campaign_handler.GetBody())

            conn = Connection(str(self.__smtp_server_hostname), int(self.__smtp_server_port))
            conn.submit(email)

        except PmtaError as e:
            print 'Connecting to %s on port %s' % (self.__smtp_server_hostname, self.__smtp_server_port)
            print e
