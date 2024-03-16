class faculty:
    def __init__(self,f_name,dpartment,f_id):
        self.f_name=f_name
        self.dpartment=dpartment
        self.f_id=f_id
    def print_info(self):
        print("faculty info=",self.f_name,self.dpartment,self.f_id)
ob=faculty("suji","IT",1201)
ob.print_info()
class cse(faculty):
    pass
ob=cse("prakash","computer science",1120)
ob.print_info()
