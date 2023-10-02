''' one boy is having 1 lakh in his bank acc rate of interst is 12% per ann
 in the 5th month he is withdrawing 25000rupees inoder to give gift to his loved one 
in the 9th month 10000rs is has added from his 2th loved one and end of the year
 how much of money he is having in his bank acc. '''
# Initial principal amount
principal = 100000  # 1 lakh

# Annual interest rate
annual_interest_rate = 0.12  # 12%

# Number of months in a year
months_in_year = 12

# Withdrawal and deposit details
withdrawal_month = 5
withdrawal_amount = 25000
deposit_month = 9
deposit_amount = 10000

# Calculate monthly interest rate
monthly_interest_rate = annual_interest_rate / months_in_year

# Calculate the balance at the end of each month
for month in range(1, months_in_year + 1):
    # Apply interest
    principal += principal * monthly_interest_rate
    
    # Check if this is the withdrawal month
    if month == withdrawal_month:
        principal -= withdrawal_amount
    
    # Check if this is the deposit month
    if month == deposit_month:
        principal += deposit_amount

# The final balance at the end of the year
final_balance = principal

print("Total money by year end:", round(final_balance, 2))
