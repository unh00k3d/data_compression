# https://www.youtube.com/playlist?list=PLE125425EC837021F
# https://www.youtube.com/watch?v=BQxerK9-Rbs&list=PLiqLGdpbmTW0vTp-V-5Rr9c3KzCvCg4HQ&index=21
# https://www.youtube.com/watch?v=4yYgRAHtDLk
# https://en.wikipedia.org/wiki/Arithmetic_coding

# this is probably the most sophisticated coding algorithm since it requires a little bit more thinking also we have to make sure that we don't mess up the floating point percision
# because machines are nutoriously bad at floating point numbers and being precise so we have to make sure the put that into consideration while we
# implement this algorithm


# --------------
# note that this code is the infinite percision version of the algorithm and it doesn't not take into account float point percision 
# for the more usable version integer-arithmetic.py will be the better choice
# --------------


# for the sake of simplicity our probability distribution will be based on the message meaning we are going to see it as i.i.d. 
# simply put we are going to count each character in the message and then we are going to divide it by the length of the message

from math import log2,ceil


# probability function 
p = lambda character_count,length: round(character_count/length,ndigits=5)


def main():


    # get the message to be encoded
    message = input("Enter the message: ")

    # get the EOF character
    EOF_character = input("Enter the EOF character: ")

    # ask the user if they want to set the probability by themselves
    set_probability = input("Do you want to set the probability of each character? (y/n): ")
    



    # get the probability of each character in the message
    character_probability ={}
    # get the unique characters from the sequence
    unique_characters = set(message)
    for character in unique_characters:
        # prompt the user to set the probability of each character
        # if they have to chose to do so
        if set_probability=='y':
            probability  = float(input(f"what is the probability of {character}: "))
            character_probability[character] = probability
        # else decide the probability based on the message and the number of occurances of that character in the message
        elif set_probability == 'n':
            character_probability[character] = p(message.count(character),len(message))
    # sort characters by probability
    character_probability = dict(sorted(character_probability.items(),key=lambda x:x[1],reverse=True))
    # will be working with these lists because it is better than working with dicts
    ordered_characters = list(character_probability.keys())
    # will be working with these lists because it is better than working with dicts
    ordered_probabilities= list(character_probability.values())

    # print(f"ordered_characters: {ordered_characters}")
    # print(f"ordered_probabilities: {ordered_probabilities}")


    # define initial lower and upper bounds
    a = 0
    b = 1

    c_j = lambda j : sum(ordered_probabilities[:j])
    i = 0
    while i < len(message) :
        # this is based on the visual interpetation of the algorithm
        # we are going to say well we want to go (n) windows up so that we expand the (n+1) then what we will do is take whatever the current windows size
        # is and then we will multiply the that with the sum of the (n) windows' probabilities so that we move that many windows ahead
        # and for b we want to tell it to start from the origin a and go one more windows meaning if we are going to tell 'a' to move (n) windows up
        # we want to tell 'b' to move (n+1) windows up 
        # note that we have to update b before updating 'a' that is because 'b' is calculated based on the original 'a' value so we have to calculate it first
        # and then update 'a'


        # for the c_j function it will just say well we want to move (n) windows up and it will give us the sum of probabilities

        # get the current character's index so that we can use it to determine how many windows we want to go up 
        character_index = ordered_characters.index(message[i])
        # print(f'character: {message[i]}')
        # print(f'character_index: {character_index}')

        # print(f"c_j(character_index+1) : {c_j(character_index+1)}")
        # print(f"c_j(character_index) : {c_j(character_index)}")


        # current windows or interval length
        w = b - a
        # print(f"w: {w}")
        # update b to be the new value
        b  = a + w * c_j(character_index+1)
        # update a to be the new value
        a  = a + w * c_j(character_index)
        # print(f"a: {a}")
        # print(f"b: {b}")

        # check if this is the termination character 
        if message[i] == EOF_character:
            break
        else:
            i += 1


 

    # after calculating the interval we want to encode it 
    # you can transmit it as it is or do whatever you want but to the more formal way is to use dyadic fraction so that we represent things in binary
    # first we find t = log2(1/l)  l is the length of the interval
    # then we find the number x such that ( a <= x/2^t < b ) this inequality holds
    # if we find two solutions we use the even one
    # lastly we calculate r to be r = x / (2^t) then we convert this fraction to binary and we can transmit the part that comes after the decimal point
    # so for 0.1 we transmit 1 ...

    t = ceil(log2(1/(b-a)))
    numbers = int(2**t * b) - int(2**t * a)
    if numbers == 2:
        if int(2**t * b) % 2 == 0:
            x = int(2**t * b)
        else:
            x = int(2**t * a) + 1
    elif numbers == 1:
        x = int(2**t * b)

    r = x / (2**t)
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"t: {t}")
    print(f"x: {x}")
    print(f"r: {r}")
    # 32 is the percision of the binary representation
    print(f"code to be transmitted : {fraction_to_binary(r,t)}")







def fraction_to_binary(fraction,percision):
    # convert the fraction to binary
    integral_part = int(fraction)
    fractional_part = fraction - integral_part
    integral_part_binary = bin(integral_part).replace('0b','')

    # then we will convert fractional part to binary
    fractional_part_binary = ""
    for i in range(percision):
        fractional_part *= 2
        if fractional_part >= 1:
            fractional_part_binary += "1"
            fractional_part -= 1
        else:
            fractional_part_binary += "0"
    return integral_part_binary + '.' + fractional_part_binary








if __name__ == '__main__':
    main()