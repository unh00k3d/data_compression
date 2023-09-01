# https://www.youtube.com/playlist?list=PLE125425EC837021F
# https://www.youtube.com/watch?v=BQxerK9-Rbs&list=PLiqLGdpbmTW0vTp-V-5Rr9c3KzCvCg4HQ&index=21
# https://www.youtube.com/watch?v=4yYgRAHtDLk
# https://en.wikipedia.org/wiki/Arithmetic_coding

# this is probably the most sophisticated coding algorithm since it requires a little bit more thinking also we have to make sure that we don't mess up the floating point percision
# because machines are nutoriously bad at floating point numbers and being precise so we have to make sure the put that into consideration while we
# implement this algorithm


# for the sake of simplicity our probability distribution will be based on the message meaning we are going to see it as i.i.d. 
# simply put we are going to count each character in the message and then we are going to divide it by the length of the message


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

    print(f"ordered_characters: {ordered_characters}")
    print(f"ordered_probabilities: {ordered_probabilities}")


    # define initial lower and upper bounds
    a = 0
    b = 1

    c_j = lambda j : sum(ordered_probabilities[:j])
    i = 0
    while i < len(message) :
        print(f'a: {a}')
        print(f'b: {b}')

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
        print(f'character: {message[i]}')
        print(f'character_index: {character_index}')

        print(f"c_j(character_index+1) : {c_j(character_index+1)}")
        print(f"c_j(character_index) : {c_j(character_index)}")


        # current windows or interval length
        w = b - a
        print(f"w: {w}")
        # update b to be the new value
        b  = a + w * c_j(character_index+1)
        # update a to be the new value
        a  = a + w * c_j(character_index)

        # check if this is the termination character 
        if message[i] == EOF_character:
            break
        else:
            i += 1


 

    print((a+b)/2)










if __name__ == '__main__':
    main()