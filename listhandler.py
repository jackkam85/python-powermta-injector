"""
This class handles processing the email list for the injector.

Comment:
    Eventually the injector will be multi-threaded and support
    bcc and other options. That is why the list processing is 
    split into a different class.
"""

class ListHandler(object):
    def __init__(self, listname):
        try:
            with open('lists/' + listname) as fh: 
               self.__list = [line.strip() for line in fh.readlines()]
               fh.close()
        except IOError as e:
            e.strerror = 'The list %s doesn\'t exist' % (listname)
            raise e


    def GetAddress(self):
        if (len(self.__list) > 0):
            address = self.__list[0]
            del self.__list[0]
            return address
        else:
            return None


