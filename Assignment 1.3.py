
# coding: utf-8

# In[16]:

firstName = input("Enter first name?")
print(firstName)
lastName = input("Enter last name?")
print(lastName)
fNameLen=len(firstName)
lNameLen=len(lastName)
print(str(fNameLen) + ";" + str(lNameLen))
fNameRev = ""
lNameRev = ""
while fNameLen>0:
   fNameRev += firstName[fNameLen-1]
   fNameLen = fNameLen-1
   #print (fNameLen)
#print (fNameRev)
while lNameLen>0:
   lNameRev += lastName[lNameLen-1]
   lNameLen = lNameLen-1
   #print (lNameLen)
#print (lNameRev)
print(fNameRev + " " + lNameRev)


# In[ ]:



