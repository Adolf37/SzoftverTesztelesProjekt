from employee_manager import EmployeeManager
import datetime
from employee import Employee
from relations_manager import RelationsManager

rm = RelationsManager()
print(f"All team members: {rm.get_all_employees()}")
everybody = rm.get_all_employees()

em = EmployeeManager(rm)
#print(em.calculate_salary(everybody[1]))

def test_salaryNotTeamLeaderHireDate_10_10_1998_BaseSalary1000():
    #Make sure the returned value is 3000$ (1000$ + 20 X 100$)
    outputHireDate = False
    outputBaseSalary = False
    finalOutput = False
    date = datetime.date(1998,10,10)
    for i in everybody:
        if rm.get_team_members(i) == None:
            #print("Nem team leader",i.first_name)
            hireDate = i.hire_date
            if hireDate == date:
                outputHireDate = True
                if i.base_salary == 1000:
                    outputBaseSalary = True

        
    if outputBaseSalary == outputHireDate == True:
        finalOutput = True
    
    assert finalOutput == True, "No person who match the requirments"
