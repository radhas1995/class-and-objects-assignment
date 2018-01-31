class ipaddr():
    def __init__(self,oct_a,oct_b,oct_c,oct_d,subnet):
            self.a = oct_a
            self.b = oct_b
            self.c = oct_c
            self.d = oct_d
            self.netmask = subnet
    def __str__(self):
        return(str(self.a)+"."+str(self.b)+"."+str(self.c)+"."+str(self.d))
print(ipaddr(10,2,3,4,24))

