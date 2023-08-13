# https://en.wikipedia.org/wiki/Canonical_Huffman_code

# https://www.youtube.com/watch?v=yXM4wq_arB0&list=PLiqLGdpbmTW0vTp-V-5Rr9c3KzCvCg4HQ&index=12



# the basic idea for this is that we use the huffman coding or the huffman tree or whatever in order to be able to find the most optimal bit length
# for each character in the message
# then what we do it we order by bit length first in ascending order and second by alphabetical order
# this ensures that both the encoder and decoder can agree on the order without transmiting that data
# this makes for a more efficient way
# next we assign as many 0's to the first character as the bit length of the character
# after that we start increment one by one and converting the number to binary while truncating the left 0's
# the next step is to add as many 0's to the right of the binary character as necessary to keep the same bit length
# 
# the main benefits are that we are using the most optimal bit length however we are cutting down the amount of data that the
# encoder needs to transmit to the decoder in order for the decoder to be able to decode the message
# simply by ordering them by bit length and alphabetical order
# and then incrementing one by one and the thing that is common between both is that we don't need to transmit them they are a standard
import huffman

def main():
    # get the encoding alphabet
    encoding_alphabet = huffman.main()


    # sort first by codeword length second by alphabetical order
    encoding_alphabet = dict(sorted(encoding_alphabet.items(),key=lambda x:(len(x[1]),x[0])))


    canonicil(encoding_alphabet=encoding_alphabet)

    # 



# we will suppose that the alphabet given is already sorted by codeword length and then by alphabetical order
def canonicil(encoding_alphabet):



    # index variable to keep track of the current character
    # i have done it this way because this make it easier to grab the key value pair
    i = 1
    canonicil_alphabet = {}
    for character,codeword in encoding_alphabet.items():
        if i==1:

            canonicil_alphabet[character] = '0' * len(codeword)
        else:

            canonicil_alphabet[character] = bin(i).replace('0b','') + ('0' * (len(codeword)-len(bin(i).replace('0b',''))))

        i += 1
        
    print(encoding_alphabet)
    print(canonicil_alphabet)


if __name__ == "__main__":
    main()

