# Function to check loan eligibility
def check_loan_eligibility():
    # Input monthly salary and loan amount
    monthly_salary = float(input("Enter Monthly Salary: "))
    loan_amount = float(input("Enter Loan Amount Requested: "))

    # Eligibility criteria
    max_loan_amount = 10 * monthly_salary

    if loan_amount <= max_loan_amount:
        print("Customer Eligible")
        # Input months to pay
        months_to_pay = int(input("Enter Months to Pay: "))
        # Calculate total payment with 10% interest
        total_payment = loan_amount * 1.10  # Adding 10% interest
        monthly_payment = total_payment / months_to_pay
        print(f"Monthly Payment: {monthly_payment:.2f}")
    else:
        print("Not Eligible")

# Call the function
check_loan_eligibility()