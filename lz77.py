import sys



def look_for_match(search_buffer,lookahead):

    run_length=0
    offset = 0
    i = 0
    while i < len(search_buffer):
        if search_buffer[i] == lookahead[0]:
            offset = len(search_buffer) - i
            j = i
            while (j < len(search_buffer)) and (j - i < len(lookahead)):
                if search_buffer[j] == lookahead[j-i]:
                    search_buffer += search_buffer[j]
                    run_length += 1
                    j+=1
                else:
                    break
            
        if run_length > 0:
            break

        i+=1

    return run_length,offset
                
    
def lz77_encoder(message,search_buffer_length,lookahead_length):
    """
    an lz77 encoder
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
            cursor += run_length +1
        else:
            cursor += 1


        if cursor >= len(message):
            output = (run_length,offset,message[-1])
            print(output)
            break
        output = (run_length,offset,message[cursor - 1 ])
        print(output)


def lz77_decoder(encoded_text,search_buffer,lookahead):
    """
    an lz77 decoder
    """
    pass



def main():
    if len(sys.argv) == 2:
        if sys.argv[1] == "-e":            
            message = input("Enter a message: ")
            search_buffer=  int(input("Buffer: "))
            lookahead = int(input("Lookahead: "))
            lz77_encoder(message, search_buffer, lookahead)
        elif sys.argv[1] == "-d":
            encoded_text = input("Enter an encoded message: ")
            search_buffer=  int(input("Buffer: "))
            lookahead = int(input("Lookahead: "))
            lz77_decoder(encoded_text, search_buffer, lookahead)

        else:
            print("error happened")
            return

    else:
        print("useage: python lz77.py <mode(e,d)>")
        return



if __name__ == "__main__":
    main()