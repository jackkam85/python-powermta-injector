import time

from port25.submitter.message import Message, PmtaMessageError
from port25.submitter.recipient import Recipient, PmtaRecipientError
from port25.submitter.connection import Connection, PmtaConnectionError
from port25 import PmtaError

class MailMergeSMTP(object):
    def __init__(self, campaign_object, smtp_server_hostname = '127.0.0.1', smtp_server_port = '25'): 
        self.__smtp_server_hostname = smtp_server_hostname
        self.__smtp_server_port = smtp_server_port
        self.__campaign_handler = campaign_object


    def Inject(self, address):
        try:
            print 'Connecting to %s on port %s' % (self.__smtp_server_hostname, self.__smtp_server_port)
            from_address = self.__campaign_handler.GetFrom()

            rcpt = Recipient(address)
            rcpt.defineVariable('to', address)
            rcpt.defineVariable('friendlyfrom', self.__campaign_handler.GetFriendlyFrom())
            rcpt.defineVariable('from', from_address)
            rcpt.defineVariable('subject', self.__campaign_handler.GetSubject())
            rcpt.defineVariable('date', time.strftime("%a, %d %b %Y %H:%M:%S %z", time.gmtime()))
            rcpt.defineVariable('*parts', '1')

            email = Message(from_address)

            email.addRecipient(rcpt)
            email.addMergeData(self.__campaign_handler.GetBody())

            conn = Connection(str(self.__smtp_server_hostname), int(self.__smtp_server_port))
            conn.submit(email)

        except PmtaError as e:
            print 'Connecting to %s on port %s' % (self.__smtp_server_hostname, self.__smtp_server_port)
            print e

        except Exception as e:
            print e.args
