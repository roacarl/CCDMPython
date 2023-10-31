#sting
a = "Apple"

#list
course = ["CCIT", "CCDM"]

#tuple
'''tupledemo = (2004202307, "Carl Roa")

print(type(a))

print(type(course))

print(type(tupledemo))
'''
      
#Dictionary
#Create a dictionary and call this Staff
#It should contain the details:
#Id: 1102, Name: Shirly Komogy, Role: IT Trainer
# Phone: 3267424


'''staff = {"ID":1102, "Name": "Shirly", "Role": "IT Trainer", "Phone":3267424 }
print(staff)


#2 Access the role of this staff by using key

print(staff["Role"])

'''


# Exercise1 - Q1
#Create an object to hold data. Call it CEIT courses....#use Dictionary

'''CEITCourses= {1001:"CCLSA",1002:"CCIT", 113:"CCDM",1004:"CCNS"}
print(CEITCourses)
'''
# Question2
# Create another object to hold all related permenant data for schools in UPNG. Call it UPNGschools. #Using Tuple

'''UPNGSchools =(["SOL,120"],["SHSS,90"],["SMHS,150"],["SNPS,100"],["SBPP,200"])
print(UPNGSchools)
'''
# Question3
#Create an Object to hold this temporary data for staff. this should contain only the id,Name and role.

'''staffJT = [223,"John Tambu", "Payroll Officer"]
print(staffJT)

staffJm = [332, "Jimmy masin", "Auditor"]
print(staffJm)
'''
#... Jimmy got a promotion to be the Senior Auditor. Update the role.
'''staffJm [2]= "Senior Auditor"
print(staffJm)
'''
# Use the type fuction to confirm that the objects you created are the correct type.
'''print(type(CEITCourses))
print(type(UPNGSchools))
print(type(staffJm))
'''
