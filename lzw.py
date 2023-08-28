# https://www.youtube.com/watch?v=PPnLA3XkT7I&list=PLiqLGdpbmTW0vTp-V-5Rr9c3KzCvCg4HQ&index=19
# https://www.geeksforgeeks.org/lzw-lempel-ziv-welch-compression-technique/


# this function take a letter and returns a list that contains all the indexes of the entry that starts with that letter
def get_first_letter_matching_indexes(entry,letter):
    result = []
    for i in range(len(entry)):
        if entry[i][0] == letter:
            result.append(i)
    return result



def main():
    # get a message
    message = input("Enter a message: ")


    # unique characters from the message
    unique_characters = sorted(set(message))

    
    # initialize the entry
    entry = []
    for character in unique_characters:
        entry.append(character)


    

    # got through each letter
    # note that i prefer using while loop instead of a for loop because i can change the the index variable according to the situation
    i = 0
    while i < len(message):
        # the search algorithm will go like this:
        #   we will look for any entry that starts with the same letter as the current letter
        #   if we find any entry that starts with the same letter then we will get the index of that entry
        #   then we will pick the longest match of characters for most optimal encoding 
        #   and then we will add that to the entry alongside with the next character in order to form a new sequence
        #   and then we will add that to the entry and continue the process
        #   if we do not find any entry that starts with the same letter then we will just add the current letter to the entry and continue the process

        # to store the best run length so far
        best_run_so_far = 0
        
        # to store the index of the best entry so far
        best_index_so_far = None




        for index in get_first_letter_matching_indexes(entry,message[i]):


            run_length = 0
            # now we start expanding those indexes if possible

            # this is necessary for us to be able to determine the best match for optimal encoding

            # note that we are using the min function to make sure that we don't go out of bounds 
            # so we are going to go with the smaller of both which in most cases will be the entry index length but 
            # for the end of the file sometimes this might not be the case so yeah
            for j in range(i,i+min(len(entry[index]),len(message[i:]))):
                if message[j] == entry[index][j-i]:
                    run_length += 1
                else:
                    break

            if run_length > best_run_so_far:
                best_run_so_far = run_length
                best_index_so_far = index

        # after we are done with the search algorithm we will add the new results to the entry and output the 
        # encoding to the user
        print(best_index_so_far)

        # if this is the last character of the message after we encode the match then 
        # do not add 1 to not go out of bounds

        
        i += best_run_so_far
        if i == len(message):
            break
            
        # add the new sequence to the entry

        new_entry = entry[best_index_so_far] + message[i]
        entry.append(new_entry)
    print(entry)

# abracadabrarabarabara



if __name__ == "__main__":
    main()



