
# refer to this video for more information on this topic
# https://www.youtube.com/watch?v=SkrLnr-KVOE&list=PLiqLGdpbmTW0vTp-V-5Rr9c3KzCvCg4HQ&index=3

# the sardinas-patterson algorithm is a way for us to determine whether and encoding scheme is uniqely decodable or not
# meaning when we encode this text and decode it it should losslessly output the same message and nothing else
# this means that we hvae to have an encoding sequence of which cannot be understood differently by different decoders hence losing or not being able to recover the 
# original message




# this is the encoding sequence that we will be using to encode the message and we want to test if it is as a good one

# return true if there are duplicates
check_duplicates=lambda sequence : True if len(sequence)!=len(set(sequence)) else False


def main():
    encoding_sequence = ['010','0100','0010','20','21','22']
    # check for duplicates
    while True:
        if not check_duplicates(encoding_sequence):
            # get dangling suffixes
            dangling_suffixes=check_prefixes(encoding_sequence)
            if len(dangling_suffixes)!=0:
                # add the dangling suffix to the encoding sequence and repeat the process
                for suffix in dangling_suffixes:
                    encoding_sequence.append(suffix)
                continue
            else:
                print("the encoding sequence is unique")
                break
        else:
            print("the encoding sequence is not unique")
            break


def check_prefixes(sequence):
    dangling_suffixes=[]
    # loop through each element and check it against the element after it 
    # if it is a prefix then save the dangling suffix
    for i in range(len(sequence)):
        for j in range(i+1,len(sequence)):
            moving_code=sequence[i]
            code_to_check_against=sequence[j]
            if len(moving_code)<len(code_to_check_against):
                # if it is a prefix then save the dangling suffix
                if code_to_check_against.startswith(moving_code):
                    dangling_suffix= code_to_check_against[len(moving_code):]
                    dangling_suffixes.append(dangling_suffix)
                else:
                    continue
            else:
                # if it is a prefix then save the dangling suffix
                if moving_code.startswith(code_to_check_against):
                    dangling_suffix=moving_code[len(code_to_check_against):]
                    dangling_suffixes.append(dangling_suffix)
                    
    return dangling_suffixes
                

if __name__=="__main__":
    main()