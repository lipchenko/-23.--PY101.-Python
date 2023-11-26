money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

while money_capital >= 0:
 budget = salary + money_capital  # Бюджет текущего месяца

 if spend > budget:
    break  # Прерываем цикл, если траты превышают бюджет

 money_capital -= spend - salary
    spend *= (1 + increase)
    months += 1

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

print("Количество месяцев, которое можно протянуть без долгов:", months)
