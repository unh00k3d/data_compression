# this function take a letter and returns a list that contains all the indexes of the entry that starts with that letter
def get_first_letter_matching_indexes(entry,letter):
    for i in range(1,len(entry)):
        if entry[i][0] == letter:
            # i have used yield which is a way of returning a value without stopping the funciton from executing
            # such that the function returns a value but then goes on and continue 
            # this helps because we can call the function from the declaration of the for loop and it will iterat over the indexes we want
            # note that we could have simply made a list and returned that and that is also ok
            yield i



def main():

    # get the message from the user
    message  = input("Enter a message: ")
    # the entry that saves sequences that were seen previously
    entry = [None]

    # got through each letter
    # note that i prefer using while loop instead of a for loop because i can change the the index variable according to the situation
    i = 0
    while i < len(message):
        # the search algorithm will go like this:
        #   we will look for any entry that starts with the same letter as the current letter
        #   if so then we will extend this search and look if there is a match between the next two letters
        #   then we will check for the best match so far in terms of length
        #   if the new match is longer meaning it is better for use to use since it compresses more
        #   then update the best lenght so far to the current length
        #   else we will just ignore this one and go on with the next one

        # to store the best run length so far
        best_run_so_far = 0
        
        # to store the index of the best entry so far
        best_index_so_far = None
        for index in get_first_letter_matching_indexes(entry,message[i]):
            run_length = 0
            # now we start expanding those indexes if possible

            # note that we are using the min function to make sure that we don't go out of bounds 
            # so we are going to go with the smaller of both which in most cases will be the entry index length but 
            # for the end of the file sometimes this might not be the case so yeah
            for j in range(i,i+min(len(entry[index]),len(message[i:]))):
                if message[j] == entry[index][j-i]:
                    run_length += 1
                else:
                    break



# abracadabrarabarabara
            if run_length > best_run_so_far:
                best_run_so_far = run_length
                best_index_so_far = index
        
        # if there are no matches in the first place we just encode it as it is

        if best_index_so_far == None:
            entry.append(message[i])
            print((0,message[i]))
            i+=1

        # else if there is a match we will encode it as follows
        # we will encode the best match as an index in a list and then we will encode the letter that is after it 
        # then we will add this new sequence to the entry

        else:

            # if it is the last character in the message then just output the index and the last letter of that sequnce
            if i + best_run_so_far == len(message):
                print((best_index_so_far,"EOF"))
                entry.append(message[i:i+best_run_so_far])
                break

            # else if this is not the end of the characters then output the index and the letter that is after it
            else:
                print((best_index_so_far,message[i+best_run_so_far]))
                entry.append(message[i:i+best_run_so_far+1])
                i+=best_run_so_far+1


    # print the entry of the encoder
    print(entry)

            

        



if __name__ == "__main__":
    main()