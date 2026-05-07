ages = [25, 30, '40', 'not_available', 20, -5]

def calculate_average_age(age_list):
    total = 0
    count = 0
    for age in age_list:
        total += age
        count += 1

    return total / count

print(calculate_average_age(ages))

