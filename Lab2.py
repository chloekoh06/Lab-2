import statistics


def display_main_menu():
    print("Enter some numbers seperated by commas (e.g. 5,67,32)")


def get_user_input():
    usr_str = input()
    str_list = usr_str.split(',')
    number_list = [float(x) for x in str_list]
    return number_list


def calc_average(number_list):
    total = 0
    for number in number_list:
        total = total + number
    amt = len(number_list)
    avg = total / amt
    return avg


def find_min_max(number_list):
    minmaxium = min(number_list), max(number_list)
    return minmaxium


def sort_temperature(number_list):
    number_list.sort()
    return number_list


def calc_median_temperature(number_list):
    m = statistics.median(number_list)
    return m


def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    print(num_list)
    average = calc_average(num_list)
    print(average)
    minmax = find_min_max(num_list)
    print(minmax)
    sort = sort_temperature(num_list)
    print(sort)
    median = calc_median_temperature(num_list)
    print(median)


if __name__ == "__main__":
    main()