# Markhus Dammar
# 10/14/19
# This program is demonstrating lists, loops, and functions with the Bakery Entry Project


# init
cookie_list = []
candy_list = []


def cookies():
    for cookie in range(1, 7):
        sales = int((input(f"What are the cookie sales for Month {cookie}? > ")))
        cookie_list.append(sales)
        print(f"The cookie sale for Month {cookie} is {sales}")
        if cookie > 7:
            break


def candies():
    for candy in range(1, 7):
        sales2 = int((input(f"What are the candy sales for Month {candy}? > ")))
        print(f"The candy sale for Month {candy} is {sales2}")
        candy_list.append(sales2)
        if candy > 7:
            break


def avg_cookies():
    print(f"The average cookie sales was {avg1}")


def avg_candies():
    print(f"The average candy sales was {avg2}")


def max_cookie():
    cookie_list.sort()
    print("The highest cookie sale was:", cookie_list[-1])


def max_candy():
    candy_list.sort()
    print("The highest candy sale was:", candy_list[-1])


def min_cookie():
    cookie_list.sort()
    print("The lowest cookie sale was:", cookie_list[:1])


def min_candy():
    candy_list.sort()
    print("The lowest candy sale was:", candy_list[:1])


# execute: calls functions in sets
# /start
cookies()
candies()
input("Press ENTER/RETURN to view the compiled data")
print("Here is the list of cookies sales", cookie_list)
print("")
input("Press ENTER/RETURN")
print("Here is the list of candy sales", candy_list)
print("")
input("Press ENTER/RETURN")
print("")
# Lines 70 through 73 calculate the total and average it out.
total_cookies = int((cookie_list[0] + cookie_list[1] + cookie_list[2] + cookie_list[3] + cookie_list[4] + cookie_list[5]))
avg1 = (int(total_cookies) / 6) # Cookie Average
total_candies = int((candy_list[0] + candy_list[1] + candy_list[2] + candy_list[3] + candy_list[4] + candy_list[5]))
avg2 = (int(total_candies) / 6) # Candy Average
# displays the averages
avg_cookies()
avg_candies()
print("")
input("Press ENTER/RETURN")
# Reveals the Maximums
max_cookie()
max_candy()
print("")
input("Press ENTER/RETURN")
# Reveals the minimums
min_cookie()
min_candy()
print("")
input("Press ENTER/RETURN")
# conclusion
if avg1 < avg2:  # This is the if statement that determines what is mot popular.
    print("Candy is the most popular item we sell.")
else:
    print("Cookies are the most popular items we sell")
# Thanks for reading.
