months = {
    1: "January", 
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

w_day = {
    0: 4,
    1: 5,
    2: 6,
    3: 7,
    4: 1,
    5: 2,
    6: 3
}
# draw function

def print_head(year, month):
    print("\t",year,"\t",months[month],"\t")

def print_line():
    for _ in range(35):
        print("-",end="")
    print("")

def print_day():
    print(" Sun",end="  ")
    print("Mon",end="  ")
    print("Tue",end="  ")
    print("Wed",end="  ")
    print("Thu",end="  ")
    print("Fri",end="  ")
    print("Sat")

def draw_date(year, month):
    rows, cols = 6, 7
    matrix = [[" " for _ in range(cols)] for _ in range(rows)]
    d = get_days(year)
    day = d[month]
    index_r = month_first_day(year, month) - 1
    index_c = month_first_day(year, month) - 1
    for i in range(day):
        matrix[index_r//7][index_c] = i+1
        index_c = (index_c + 1)%7
        index_r = index_r + 1
    for i in range(rows):
        for j in range(cols):
            print(f"{str(matrix[i][j]):>3}", end="  ")
        print("")
        
# tool function

def is_leap_year(year):
    if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def dayx(year):
    if(is_leap_year(year)):
        return 366
    return 365

def get_days(year):
    d = {
        1: 31, 2: 28, 3: 31, 4: 30,
        5: 31, 6: 30, 7: 31, 8: 31,
        9: 30, 10: 31, 11: 30, 12: 31
    }
    if is_leap_year(year):
        d[2] = 29
    return d    

# core function
def number_days(year, month):
    c_year = 1800
    day = 0
    while(c_year!=year):
        day += dayx(c_year)
        c_year = c_year+1
    d = get_days(c_year)
    for i in range(1, month):
        day+=d[i]
    return day

def month_first_day(year, month):
    day = number_days(year,month)
    return w_day[day%7]


def main():
    year = int(input("请输入年份,大于1800"))
    month = int(input("请输入月份"))
    print_head(year,month)
    print_line()
    print_day()
    draw_date(year, month)

if __name__ == "__main__":
    main()
