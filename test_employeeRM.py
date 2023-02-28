from relations_manager import RelationsManager
import datetime

rm = RelationsManager()
#print(f"All team members: {rm.get_all_employees()}")
everybody = rm.get_all_employees()
print(everybody)

#team_members = rm.get_team_members(everybody[0])


def test_johnDoeBirthDate_31_01_1970():
    output = False
    nameTest = "John Doe"
    birthDateTest = datetime.date(1970, 1, 31)
    for i in everybody:
        fullName = i.first_name + ' ' +  i.last_name
        birthDate = i.birth_date
        if fullName == nameTest and birthDate == birthDateTest:
            output = True

    assert output == True

def test_John_DoeTeamMembers_Myrta_Torkelson_and_Jettie_Lynch():
    myrtaAndJettieId = []
    johnTeamMembersId = []
    for i in everybody:
        fullName = i.first_name + ' ' +  i.last_name
        if fullName == "John Doe":
            #print(rm.get_team_members(i))
            johnTeamMembersId = rm.get_team_members(i)
    
    for i in everybody:
        fullName = i.first_name + ' ' +  i.last_name
        if fullName == "Myrta Torkelson" or fullName == "Jettie Lynch":
            myrtaAndJettieId.append(i.id)
    
    if myrtaAndJettieId == johnTeamMembersId:
        output = True
    else:
        output = False
    
    assert output == True


def test_tomasAndreNotJohnDoeTeamMember():
    #Tomas Andre is not John Doe’s team member => output= True
    johnTeamMembersId = []
    tomasAndreId = None
    for i in everybody:
        fullName = i.first_name + ' ' +  i.last_name
        if fullName == "John Doe":
            #print(rm.get_team_members(i))
            johnTeamMembersId = rm.get_team_members(i)
        if fullName == "Tomas Andre":
            tomasAndreId = i.id
    if tomasAndreId in johnTeamMembersId:
        output = False
    else:
        output = True
    
    assert output == True

def test_GretchenWatfordBaseSalary4000():
    baseSalary = 4000
    for i in everybody:
        fullName = i.first_name + " " + i.last_name
        if fullName == "Gretchen Watford":
            gretchenWatfordSalary = i.base_salary
    
    assert baseSalary == gretchenWatfordSalary

def test_TomasAndreNotTeamLeader():
    output = None
    for i in everybody:
        
        fullName = i.first_name + " " + i.last_name
        #print(f'Team members lekerese({fullName}):')
        #print(rm.get_team_members(i))
        if fullName == "Tomas Andre":
            output = rm.is_leader(i)
            #print(rm.get_team_members(i))
    assert output == False
    
def test_JudeOvercashNotStored():
    output = True
    for i in everybody:
        fullName = i.first_name + " " + i.last_name
        if fullName == "Jude Overcash":
            output = False
    assert output == True
