#!user/bin/python

print('Please enter a family role (example: brother, sister, mom, or dad)');
name = raw_input(); #have to use raw input since were using python 2.7
if name == "Brother": 
    print('Your brother is Nick!');
elif name == "Sister":
    print('Your sister is Nina!');
elif name == "Mom":
    print('Your mother is Dawna!');
elif name == "Dad":
    print('Your father is Joachim or JZ!');
else:
    print('I dont know who that is.');
print('That is all');
