#Find if the second string is rotation of first string or not
def areRotations(self,s1,s2):
        if(len(s1)!=len(s2)):
            return 0;
        tmp=s1+s1;
        if(tmp.count(s2)): # Here I am checking if the 2 times of first has substring of second string
            return 1;
        else :
            return 0;
