
# Currenct Conversion Program
with open('currency.txt','r') as f:
    lines = f.readlines()

new_list = []
for line in lines:
    parsed = line.strip().split('\t')
    parsed.pop()
    new_list.append(parsed)

def convert_value(country_index_no,curr):
    user_choosen_country_index = int(country_index_no-1)
    user_np_amount = float(curr)
    for index,element in enumerate(new_list):
        # print(index,element)
        if index == user_choosen_country_index:
            return print(f"The converted amount in {new_list[index][0]} and Amount is {round(float(new_list[index][1]) * user_np_amount,2)}")



country_name = [sublist[0] for sublist in new_list if len(sublist) > 0]
# print(country_name)

print("Country_Currencty Names :")
for index,country_currency in enumerate(country_name,start=1):
    print(f"{index}. {country_currency}")

try:
    user_input =int(input(f"Choose a currency to convert : (1-11)"))
    if user_input > 0  and user_input <12:
        try:
            user_currency = float(input("Enter amount in Nepali currency (NPR):"))
            # print(user_input,user_currency)
            convert_value(user_input, user_currency)
            
        except ValueError:
            print("Please enter a valid number for the currency amount. ")
    else:
        print("Please enter a valid number within the range.")
except ValueError :
    print("Please enter a valid number for the country selection.")
