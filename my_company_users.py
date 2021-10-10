company_name = input()

companies_employee_id_dict = {}

while not company_name == 'End':
    company, employee_id = company_name.split(' -> ')
    if company not in companies_employee_id_dict:
        companies_employee_id_dict[company] = [employee_id]
    else:
        if employee_id not in companies_employee_id_dict[company]:
            companies_employee_id_dict[company].append(employee_id)
    company_name = input()

companies_employee_id_dict = dict(sorted(companies_employee_id_dict.items(), key=lambda x: x[0]))
for key, value in companies_employee_id_dict.items():
    print(key)
    for name in value:
        print(f'-- {name}')
