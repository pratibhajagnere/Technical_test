'''

I apologize for code with less comments because I had limited time to put all the functionalities.
But I have tried to keep the code as readable as possible by following naming convention to depict the usage.

'''



i = 0 # for UID creation
ownerdict = {}
petdict = {}

def get_id():
    global i
    i += 1
    return i

class General:

    def __init__(self, name, birthday):
        self.id = get_id()
        self.name = name
        self.birthday = birthday

    def UpdateName(self, name):
        self.name = name

    def UpdateBDay(self, bday):
        self.birthday = bday

class Owner(General):

    def __init__(self, first, last, birthday):
        global ownerdict
        General.__init__(self, first, birthday)
        self.lastname = last
        self.doglist = []
        self.catlist = []
        ownerdict[self.id] = self

    def __str__(self):
        return self.name + " " + self.lastname

    def ReadOwner(self):

        owner = ownerdict[self.id]
        print(owner, owner.birthday, owner.doglist, owner.catlist)


    def DeleteOwner(self):

        global ownerdict, petdict
        owner = ownerdict[self.id]
        del ownerdict[self.id]
        for id in owner.doglist+owner.catlist:
            del petdict[id]

        print("Deleted", owner)


    def AddPet(self, pet_type, petid):
        '''
        Add new pet in petlist of pwner
        :param pet_type: type of pet, Dog or Cat
        :param petid: Unique ID of pet
        :return: None
        '''
        if pet_type == 'Dog':
            self.doglist.append(petid)
        else:
            self.catlist.append(petid)

    def AllDogs(self):

        return [ petdict[petid] for petid in self.doglist]

    def AllCats(self):

        return [petdict[petid] for petid in self.catlist]

    def AllPetsCount(self):
        return len(self.AllCats()+ self.AllDogs())


    def UpdateLastName(self, lname):
        '''
        Update last name of Pwner
        :param lname: New last name
        :return: None
        '''
        self.lastname = lname


    def RemovePet(self,pet_type, petid):
        '''
        Remove a pet from petlist
        :param pet_type: Dog or Cat
        :param petid: ID of pet
        :return:
        '''
        if pet_type == 'Dog':
            self.doglist.remove(petid)
        else:
            self.catlist.remove(petid)


class Pet(General):

    def __init__(self, pet_type, first, birthday, ownerid):

        if pet_type not in ['Dog', 'Cat']:
            print("Invalid pet, only Dog or Cat is allowed")
        else:
            global petdict
            self.pet_type = pet_type
            General.__init__(self,first, birthday)
            self.ownerid = ownerid
            owner = ownerdict[ownerid]
            owner.AddPet(pet_type, self.id)

            petdict[self.id] = self


    def UpdateOwner(self,new_ownerid):
        '''
        Change the owner of pet
        :param new_ownerid: ID of new owner
        :return: None
        '''
        owner = ownerdict[new_ownerid]
        owner.AddPet(self.pet_type, self.id)
        old_owner = ownerdict[self.ownerid]
        old_owner.RemovePet(self.pet_type, self.id)
        self.ownerid = new_ownerid

    def GetOwner(self):
        return self.ownerid

    def __str__(self):
        return self.name


    def ReadPet(self):

        '''
        Print details of self
        :return: None
        '''
        pet = petdict[self.id]
        print(pet, pet.pet_type, pet.birthday)

    def DeletePet(self):

        '''

        Delete self from petdict and owner's petlist
        :return: None

        '''
        global petdict
        pet = petdict[self.id]
        del petdict[self.id]
        owner = ownerdict[pet.ownerid]
        if pet.pet_type == 'Dog': owner.doglist.remove(pet.id)
        else: owner.catlist.remove(pet.id)
        print("Deleted", pet)


def ListAllOwners():

    '''
    Generate list of all Owners with their details
    '''

    print("List of all owners")
    for key in ownerdict:
        if ownerdict[key].ReadOwner():
            print(ownerdict[key].ReadOwner())


Owner("A", "Ben", "30-11-2017")
Owner("B", "Cathy", "30-1-2007")
Owner("D", "Tom", "10-11-2001")

Pet("Dog","gen","21-11-2002",3)
Pet("Dog","genna","21-11-2002",3)
Pet("Dog","hen","12-11-2002",2)
Pet("Cat","heena","12-1-2012",2)


ListAllOwners()

