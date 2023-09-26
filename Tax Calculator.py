# https://listentotaxman.com/  as reference


# need
# money from
# employer - gross pay
# self-employed or contract work
# state benefit
# rental income
# interest on savings

class User():
    name = ""
    persAllowance = 0
    taxReduction = 0

user1 = User()

# Adding all potential incomes sources
# 
print("Income from employment (enter 0 or more): ")
answer = input()
if answer.isdecimal():
    income = float(answer)


print("Income from self-employemnt or any other service (enter 0 or more):")
tmp = float(input())
income+= tmp



print("Bereavement Allowance (enter 0 or more):")
tmp = float(input())
income+= tmp

print("Carer's Allowance (enter 0 or more):")
tmp = float(input())
income+= tmp

print("Employment and Support Allowance ESA (enter 0 or more):")
tmp = float(input())
income+= tmp

print("Incapacity benefit, ignoring the first 29 weeks (enter 0 or more):")
tmp = float(input())
income+= tmp

print("Job seekers allowance (enter 0 or more):")
tmp = float(input())
income+= tmp

print("Pensions paid by the Industrial Death Benefit scheme (enter 0 or more):")
tmp = float(input())
income+= tmp

print("State pension (enter 0 or more):")
tmp = float(input())
income+= tmp

print("Widowed Parent’s Allowance (enter 0 or more):")
tmp = float(input())
income+= tmp

print("Income from rental (enter 0 or more):")
tmp = float(input())
if (income < 7500):

income+= tmp

if (income > 100000):
    if (income > 125140):
        user1.persAllowance = 0
    else:
        print("This is complicated ...")


#Calculating personal allowance
#
# Default:
user1.persAllowance = 12570
# Adjustig for marriage allowance 
print("Are you tranferrring some of your personal allowance to your married partner? (y/n)")
answer = input()
if (answer == 'y'):
    user1.persAllowance = user1.persAllowance - 1260
else:
    print("Is your married partner tranferring some of their pers allowance to you? (y/n)")
    answer = input()
    if (answer == 'y'):
        user1.taxReduction+=252
# Adjusting for blind person allowance
print("Enter your blind person allowance")
answer = float(input())
user1.persAllowance = user1.persAllowance + 2870









