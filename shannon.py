# https://en.wikipedia.org/wiki/Shannon_coding
# https://indepth.dev/posts/1019/the-simple-math-behind-decimal-binary-conversion-algorithms
# https://www.youtube.com/watch?v=q1ig6rSt8T4

import math

message = input("Enter your message: ")


# probability function 
p = lambda character_count,length: round(character_count/length,ndigits=5)

def main():
    # get the probability of each character in the message

    character_probability ={}
    # get the unique characters from the sequence
    unique_characters = set(message)
    for character in unique_characters:
        # get the probability  from the input message
        character_probability[character] = p(message.count(character),len(message))

    # sort characters by probability
    character_probability = dict(sorted(character_probability.items(),key=lambda x:x[1],reverse=True))
    ordered_characters = list(character_probability.keys())

    # now we are going to calculate the cumulative probability of each character
    cumelative_probability = {}
    for i in range(len(ordered_characters)):
        cumelative_probability[ordered_characters[i]] = sum(list(character_probability.values())[:i])


    # nex we want to calculate how many digits we will be taking from the binary representation
    # we will take the log base 2 of the probability of each character and multiply by -1 and then 
    # use the ceil function to round up the next integer

    encoding_alphabet= {}
    for character in unique_characters:
        # get the percision or in other words the l(i) which correspond to the length of the encoding of this
        # character

        percision_needed = math.ceil(math.log2(1/character_probability[character]))
        # the binary fraction with the percision calculated before
        binary_fraction = fraction_to_binary(fraction = cumelative_probability[character],percision = percision_needed)
        # write that the encode alphabet for this character is the binary fraction
        encoding_alphabet[character] = binary_fraction[2:]

        # this is just to produce a more elegant output and it is not necessary for the algorithm to work
        encoding_alphabet= dict(sorted(encoding_alphabet.items(),key=lambda x:len(x[1])))
        
    for key,value in encoding_alphabet.items():
        print(key,value)









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


    



if __name__ == "__main__":
    main()

    

