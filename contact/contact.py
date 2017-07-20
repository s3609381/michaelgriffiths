class Contact(object):

    def __init__(self):

        self.profile = {}
        self.profilecomplete = True

    def setphone(self, phone):

        if len(phone) > 0:
            self.profile['phone'] = str(phone)

    def getphone(self):
        return self.profile['phone']

    def setemail(self, email):
        if len(email) > 0:
            self.profile['email'] = str(email)

    def getemail(self):
        return self.profile['email']

    def setlocation(self, location):
        if len(location) > 0:
            self.profile['location'] = str(location)

    def getlocation(self):
        return self.profile['location']

    def printdetails(self):

        for record in self.profile:
            if len(record) == 0:
                print("Sorry! you havent finished your profile " + record.key + "has not been set!")
                self.profilecomplete = False
                return

        if self.profilecomplete:
            print("****Contact Details****")
            print("M: " + self.profile['phone'])
            print("E: " + self.profile['email'])
            print("L: " + self.profile['location'])



