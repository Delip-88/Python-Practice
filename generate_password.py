import string
import random


s1 = string.ascii_letters
s2 = string.digits
s3 = string.punctuation
# print(new_str)
list_s1 = list(s1)
list_s2 = list(s2)
list_s3 = list(s3)

random.shuffle(list_s1)
random.shuffle(list_s2)
random.shuffle(list_s3)

new_list = [
    random.choice(list_s1),
    random.choice(list_s2),
    random.choice(list_s3),
]
new_list.extend(random.choices(list_s1 + list_s2 +list_s3,k=7))

# print(new_list)
random.shuffle(new_list)

random_password = ''.join(new_list)
print(random_password)
