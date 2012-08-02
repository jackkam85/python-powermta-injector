"""
This class handles loading the campaigns.

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

class Campaigns(object):
    def __init__(self, campaign_directory):
        self.__campaign_directory = campaign_directory
        self.__froms_counter = 0
        self.__friendly_from_counter = 0
        self.__subjects_counter = 0
        self.__bodies_counter = 0
        self.__domains_counter = 0

        self.LoadFroms__()
        self.LoadFriendlyFroms__()
        self.LoadSubjects__()
        self.LoadBodies__()
        self.LoadDomains__()

    def GetFrom(self):
        if self.__froms_counter == len(self.__froms):
            self.__froms_counter = 0

        from_address = self.__froms[self.__froms_counter]
        self.__froms_counter += 1

        return from_address

    def GetFriendlyFrom(self):
        if self.__friendly_from_counter == len(self.__friendly_froms):
            self.__friendly_from_counter = 0

        friendly_from = self.__friendly_froms[self.__friendly_from_counter]
        self.__friendly_from_counter += 1

        return friendly_from

    def GetSubject(self):
        if self.__subjects_counter == len(self.__subjects):
            self.__subjects_counter = 0

        subject = self.__subjects[self.__subjects_counter]
        self.__subjects_counter += 1

        return subject

    def GetBody(self):
        if self.__bodies_counter == len(self.__bodies):
            self.__bodies_counter = 0

        body = self.__bodies[self.__bodies_counter]
        self.__bodies_counter += 1

        return body

    def GetDomain(self):
        if len(self.__domains) <= 0:
            return None

        if self.__domains_counter == len(self.__domains):
            self.__domains_counter = 0

        domain = self.__domains[self.__domains_counter]
        self.__domains_counter += 1

        return domain

    def LoadFroms__(self):
        try:
            with open('campaigns/' + self.__campaign_directory + '/froms') as fh:
                self.__froms = [line.strip() for line in fh.readlines()]

                if len(self.__froms) <= 0:
                    fh.close()
                    raise ValueError('The froms file is empty.')

                fh.close()
        except IOError as e:
            e.strerror = 'Froms file doesn\'t exist for the campaign %s' % (campaign)
            raise e

    def LoadFriendlyFroms__(self):
        try:
            with open('campaigns/' + self.__campaign_directory + "/friendly_froms") as fh:
                self.__friendly_froms = [line.strip() for line in fh.readlines()]

                if len(self.__friendly_froms) <= 0:
                    fh.close()
                    raise ValueError('The friendly froms file is empyty')

                fh.close()
        except IOError as e:
            e.strerror = 'Domains file doesn\'t exist for the campaign %s' % (campaign)
            raise e

    def LoadSubjects__(self):
        try:
            with open('campaigns/' + self.__campaign_directory + '/subjects') as fh:
                self.__subjects = [line.strip() for line in fh.readlines()]

                if len(self.__subjects) <= 0:
                    fh.close()
                    raise ValueError('The subjects field is empty')

                fh.close()
        except IOError as e:
            e.strerror = 'Subjects file doesn\'t exist for the campaign %s' % (campaign)
            raise e

    def LoadBodies__(self):
        try:
            self.__bodies = []
            body_files = glob('campaigns/' + self.__campaign_directory + '/bodies/*')

            if len(body_files) <= 0:
                raise ValueError('No email body files found')

            for current_body in body_files:
                with open(current_body) as fh:
                    self.__bodies.append(fh.read())
                    fh.close()
        except IOError as e:
            e.strerror = 'Body file doesn\'t exist for the campaign %s' % (campaign)
            raise e

    """
        An exception isn't raised here on purpose, because the domains file isn't 
        required. It's an option file that will allow you to use redirect domains
        in your campaign and requires you to set a cli option. If the CLI option is 
        set and this is empty an exception will be raise later in the program.
    """
    def LoadDomains__(self):
        try:
            with open('campaigns/' + self.__campaign_directory + '/domains') as fh:
                self.__domains = [line.strip() for line in fh.readlines()]
                fh.close()

        except IOError as e:
            pass
