"""
This class handles loading the creatives.

Comment:
    Yes, this is a simple class and probably won't
    change much, but I don't want to shove this in
    another class such as the actual injector, because
    of possible code duplication. I plan on having 
    different injectors that do different things. 
    For example one that supports mail merge over smtp,
    mail merge via file pickup, custom mail merge over
    smtp that supports bcc (pmta won't do a true bcc with
    its built in mail merge and it won't support bcc via
    file pick up even with BMSTP)
"""

from glob import glob

class Creatives(object):
    def __init__(self, creative_directory):
        self.__creative_directory = creative_directory
        self.__froms_counter = 0
        self.__friendly_from_counter = 0
        self.__subjects_counter = 0
        self.__bodies_counter = 0

        self.LoadFroms__()
        self.LoadFriendlyFroms__()
        self.LoadSubjects__()
        self.LoadBodies__()

    def LoadFroms__(self):
        try:
            with open('creatives/' + self.__creative_directory + '/froms') as fh:
                self.__froms = [line.strip() for line in fh.readlines()]

                if len(self.__froms) <= 0:
                    fh.close()
                    raise ValueError('The froms file is empty.')

                fh.close()
        except IOError as e:
            e.strerror = 'Froms file doesn\'t exist for the creative %s' % (creative)
            raise e

    def LoadFriendlyFroms__(self):
        try:
            with open('creatives/' + self.__creative_directory + "/friendly_froms") as fh:
                self.__friendly_froms = [line.strip() for line in fh.readlines()]

                if len(self.__friendly_froms) <= 0:
                    fh.close()
                    raise ValueError('The friendly froms file is empyty')

                fh.close()
        except IOError as e:
            e.strerror = 'Domains file doesn\'t exist for the creative %s' % (creative)
            raise e

    def LoadSubjects__(self):
        try:
            with open('creatives/' + self.__creative_directory + '/subjects') as fh:
                self.__subjects = [line.strip() for line in fh.readlines()]
                fh.close()
        except IOError as e:
            e.strerror = 'Subjects file doesn\'t exist for the creative %s' % (creative)
            raise e
    def LoadBodies__(self):
        try:
            self.__bodies = []
            body_files = glob('creatives/' + self.__creative_directory + '/bodies/*')

            for current_body in body_files:
                with open(current_body) as fh:
                    self.__bodies.append(fh.read())
                    fh.close()
        except IOError as e:
            e.strerror = 'Body file doesn\'t exist for the creative %s' % (creative)
            raise e

