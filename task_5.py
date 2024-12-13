name = "Dolgova Polina Evgenevna"
print(name)
upper_case_list = [ord(symbol) for symbol in name.upper()]
print(upper_case_list)
lower_case_list = [ord(symbol) for symbol in name.lower()]
print(lower_case_list)

sum_upper = sum(upper_case_list)
print(f"Сумма кодов ASCII в верхнем списке: {sum_upper}")

sum_lower = sum(lower_case_list)
print(f"Сумма кодов ASCII в нижнем списке: {sum_lower}")