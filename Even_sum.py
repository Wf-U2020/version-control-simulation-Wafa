sum_even_for = 0

for number in range(1, 51):
    if number % 2 == 0:
        sum_even_for += number

print(f"The sum of even numbers from 1 to 50 is {sum_even_for}.")


# Sum of even numbers from 1 to 50 using a while loop

sum_even_while = 0
number = 1

while number <= 50:
    if number % 2 == 0:
        sum_even_while += number
    number += 1

print(f"The sum of even numbers from 1 to 50 is {sum_even_while}.")

#The sum of even numbers from 1 to 50 is 650.
#The sum of even numbers from 1 to 50 is 650.

#Both the for loop and while loop produce the same result, which is 650. The for loop is clearer because it automatically handles 
# the iteration through the range of numbers, making the code shorter and easier to read. The while loop requires manually updating the 
# counter variable, which can make the code slightly more complex.