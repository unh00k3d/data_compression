import sys



def look_for_match(search_buffer,lookahead):

    run_length=0
    offset = 0
    i = 0
    # note that i have used while loop rather than a for loop 
    # because i needed to be able to update the length that we are checking against 
    # which in our case is the length of the search buffer
    # this is needed because in some cases lzss and lz77 allow for the offset to smaller than the run and encoding still works because
    # we are contantly updating the search buffer which in return becomes longer and provided a new reference

# check for characters in the search buffer
    while i < len(search_buffer):
        # if there is a match between a character in the search buffer and the first character in the lookahead
        # then we want to start a run looking if the next character of each matches
        if search_buffer[i] == lookahead[0]:
            # set the offset
            offset = len(search_buffer) - i
            # 
            j = i
            while (j < len(search_buffer)) and (j - i < len(lookahead)):
                if search_buffer[j] == lookahead[j-i]:
                    search_buffer += search_buffer[j]
                    run_length += 1
                    j+=1
                else:
                    break
            

        # this is the main difference between lz77 and lzss
        # lzss does not allow for run_length less than 3 because it is not efficient

        # if a match was found then stop looking for other matches and return that
        if run_length > 2:
            break
        else:
            run_length=0
            offset=0
            break

        i+=1

    return run_length,offset
                
    
def lzss_encoder(message,search_buffer_length,lookahead_length):
    """
    an lzss encoder
    """

    cursor = 0
    run_length=0
    offset = 0


    while cursor<len(message):

        # check if we are out of bounds
        if cursor+lookahead_length >= len(message):
            lookahead = message[cursor:]
        else:
            lookahead = message[cursor:cursor+lookahead_length]

        if cursor-search_buffer_length < 0:
            search_buffer = message[:cursor]

        else:
            search_buffer = message[cursor-search_buffer_length:cursor]



        run_length,offset = look_for_match(search_buffer,lookahead)

        # ordering of the cursor and output matters
        if run_length > 0:
            output = (1,-offset,run_length)
            cursor += run_length
        else:
            output = (0,message[cursor])
            cursor += 1

        print(output)

def main():
    message = input("Enter a message: ")
    search_buffer=  int(input("Buffer: "))
    lookahead = int(input("Lookahead: "))
    lzss_encoder(message, search_buffer, lookahead)


if __name__ == "__main__":
    main()