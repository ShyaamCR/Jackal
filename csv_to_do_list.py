import csv
from validator_collection import validators,checkers
import datetime

def main():
    
    date_check(v_Due = input("Due By: "))

#Variable declarition
# v_Entry_Date = datetime.date.today().strftime("%d-%b-%Y")
# v_Summary = input("Summary: ")
# v_Priority = input("Priority: ")

# v_Pert_Completion = input("Percentage completion: ")
# v_Status = input("Status: ")


# header = ['S.No','Date','Task Description','Priority','Due Date','Status','%_completion','Due in Days']

def date_check(date_value):
    if checkers.is_date(date_value, minimum=datetime.date.today().strftime("%d-%b-%Y")):
        pass
    else:
        return print('please input the value in the DD-MMM-YYYY date format')


if __name__ == "__main__":
    main()