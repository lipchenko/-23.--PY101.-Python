numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

total_sum = sum(number for number in numbers if number is not None)

count = len(numbers)

mean_number = total_sum / count

numbers = [mean_number if number is None else number for number in numbers]

print("Измененный список:", numbers)


