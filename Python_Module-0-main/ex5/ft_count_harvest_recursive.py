def ft_recursive(days, count=1):
    print(f"Day {count}")
    if (count < days):
        ft_recursive(days, (count + 1))


def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    if (days > 0):
        ft_recursive(days)
