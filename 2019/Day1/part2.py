def calculate_fuel(mass):
    fuel = 0
    while True:
        tmpfuel = (int(int(mass)/3)) - 2
        if tmpfuel <= 0:
            return fuel
        else:
            fuel += tmpfuel
            mass = tmpfuel


if __name__ == '__main__':
    total_fuel = 0

    with open('day1.txt', 'r') as f:
        for line in f:
            line = line.strip()
            total_fuel += calculate_fuel(line)

    print(total_fuel)
