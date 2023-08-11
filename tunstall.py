# probability function 
p = lambda character_count,length: round(character_count/length,ndigits=5)



def main():
    message = input("Enter a message: ")

    # get the bit length to determine the number of iteration if any
    try:
        bit_length= int(input("Enter the bit length of the message: "))
    except ValueError:
        print("Bit length must be an integer")
        return
    



    # since set doesn't allow duplicates we can use to get the characters in the message
    unique_characters = set(message)
    # get the count of each character in the message
    character_probabilty = {}
    # the count of each character this is used to calculate probability
    for character in unique_characters:
        character_probabilty[character] = p(message.count(character),len(message))

    # order according to the count of each as if ordering with respect to probability
    character_probabilty = dict(sorted(character_probabilty.items(),key=lambda x:x[1],reverse=True))

    # calculate the iteration count (K) according to the following inequality : N + K(N - 1) <= 2 ^ n
    # K --> number of iterations
    # N --> number of unique characters in the message
    # n --> bit length of the message
    # we are going to take the integer part of the division
    iterations=( 2 ** bit_length - len( unique_characters ) ) // ( len( unique_characters ) - 1  )

    # sequence probabilty list 
    # this is the dictionary that we will be adding to sequences to so the we don't messup with the original dictionary
    sequence_probabilty = character_probabilty.copy()
    # iterate as many times as the number of iterations
    for i in range(iterations):
        sequence_probabilty = dict(sorted(sequence_probabilty.items(),key=lambda x:x[1],reverse=True))
        # get the highest probability character and its probability
        highest_character,highest_probabilty=list(sequence_probabilty.items())[0]
        # iterate over all the other characters and generate new sequences
        for character in list(character_probabilty.keys()):
            # calculate the new probability of the new sequence
            new_sequence = highest_character+character
            new_probability = round( highest_probabilty*character_probabilty[character],ndigits=3 )
            # add the new sequence to the dictionary
            sequence_probabilty[new_sequence] = new_probability
        # remove the character from the dictionary
        del sequence_probabilty[highest_character]


    # after generating all the sequences we want to get the encoding alphabet
    encoding_alphabet = {}
    for i in range(len(list(sequence_probabilty.keys()))):
        
        codeword = bin(i)[2:]
        if len(codeword)<bit_length:
            codeword = '0'*(bit_length-len(codeword))+codeword
        encoding_alphabet[list(sequence_probabilty.keys())[i]] = codeword


    print(encoding_alphabet)

if __name__ == '__main__':  
    main()