#  in data compression entropy is a measure of the average information content of a data set.
#  in another words it is kind of a measure of how much information is actually in the data
#  so when we think about it we actually only need this information bit we don't need the extra bits
#  that surround it so the basic idea of any compression is to strip out these excess stuff and only keep the information we need
#  and entropy works kind of as a measure or a limit to how much we can compress 
#  this is why compression varies from data set to another



#  the general formula for entropy is:
#  we have a function P(n) that takes an n whether that be an character or a sequence or characters and it outputs
#  the probability of that n by dividing its occurences by the total number
#  and then we add up P(n) * log2(P(n)) for each character in the dataset to get the entropy


# in information theory information is defined by the unpredictablity of the data
# so if the information carried is unlikely then it carries more information rather than a message that carries 
# a likely outcome or a predicted one because that is less valuable in terms of information
# entropy is a measure of how much information is actually in the data with this definition of information
# for instance casting a die has a higher entropy than a coin because the die has more outcomes hence it is less predictable
# which means it carries information that is more valuable in terms of information
# note that because we using probability and logarithm the output will be in negative so we are going to take the absolute value of the answer


#  ----------------------
#  1. check the entropy of a string of characters
#  ----------------------

# https://www.youtube.com/watch?v=M5c_RFKVkko


import math

characters = {}
input_string=input("enter a string to calculate its entropy: ")

# find the probability of each character in the string when needed
p = lambda n : characters[n]/len(input_string)


for char in input_string:
    if char in list(characters.keys()):
        characters[char]+=1
    else:
        characters[char]=1
entropy = 0
for char in list(characters.keys()):
    entropy += p(char) * math.log2(p(char))

entropy = abs(entropy)
print(f"entropy of the string is {entropy}")

    


