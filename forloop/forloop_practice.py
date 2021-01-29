business_list = [1500, 2542, 2001, 3500, 5300, 5555, 17000, 21000, 15001]

total_taxes = 0

for single_income in business_list:

    if single_income >= 1 and single_income <= 2000:
        tax = single_income * 0.05
    elif single_income >= 2001 and single_income <= 5000:
        tax = single_income * 0.10
    elif single_income >= 5001 and single_income <= 15000:
        tax = single_income * 0.15
    else:
        tax = single_income * 0.17
 


    net_income = single_income - tax
    income_after_healthcare_reduction = net_income * 0.98
    print(f"taxes taken out {round(tax, 2)}")
    print(f"income after healthcare reduction: {round(income_after_healthcare_reduction, 2)} ")
    print("\n")
    total_taxes = total_taxes + tax

print(f" total of taxes {round(total_taxes, 2)}")