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
