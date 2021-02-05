# formatting numbers for Fourteen IP Comms v2

# read the data into the script
with open('Numbers.txt') as edit_numbers:
    numbers_contents = edit_numbers.read()
    numbers_contents = numbers_contents.split('\n')

# creates a list of the numbers to edit
number_list = []

for number in numbers_contents:
    number_list.append(number)


# stores the country code for the numbers
cc = input("What is the country code of these numbers?")


# formatting the numbers ready for the doc
formatted_numbers = [] 
for num in number_list:
    prefix = num[0:len(cc)]
    ddi = num[len(cc):]
    complete_num = "+" + prefix + "-" + ddi
    formatted_numbers.append(complete_num)


# modifying the current doc with the new formatted data
with open('Numbers.txt', 'w') as gen_file:
    for item in formatted_numbers:
        gen_file.write('%s\n' % item)