# https://en.wikipedia.org/wiki/Shannon%E2%80%93Fano_coding
# https://www.youtube.com/watch?v=B3y0RsVCyrw
# https://www.youtube.com/watch?v=9XVEgZM6QoY&list=PLiqLGdpbmTW0vTp-V-5Rr9c3KzCvCg4HQ&index=6




class BinaryTree:
    def __init__(self,root):
        self.root = root
        self.position = root 
    def go_right(self):
        self.position = self.position.right
        return self.position.right
    def go_left(self):
        self.position = self.position.left
        return self.position.left
    def go_up(self):
        if self.position.parent == None:
            return None
        self.position = self.position.parent
        return self.position.parent
    def get_position(self):
        return self.position
    def set_position(self,node):
        self.position = node
        return self.position



class node:
    def __init__(self,value,parent=None):
        self.right = None
        self.left = None
        self.parent = parent
        self.value = value
    def add_right(self,node):
        self.right = node
    def add_left(self,node):
        self.left = node
    def delete_right(self):
        self.right = None
    def delete_left(self):
        self.left = None


def main():
    message = input("Enter your message: ")
    # get the unique characters from the sequence
    character_count={}
    unique_characters = set(message)
    for character in unique_characters:
        # get the probability  from the input message
        character_count[character] = message.count(character)
    
    # sort characters by probability
    character_count = dict(sorted(character_count.items(),key=lambda x:x[1],reverse=True))
    ordered_characters = list(character_count.keys())

    # now we are going to start and build up our tree

    # initialize a root node for the tree
    root_node = node(sum(list(character_count.values())))


    # initialize a tree object
    tree = BinaryTree(root_node)
    tree = build_tree(character_count,ordered_characters,tree)
    tree.set_position(root_node)
    encoding_alphabet = create_encoding(tree,"")
    print(encoding_alphabet)

     
# provided a binary tree and an encoding alphabet dictionary (which will serve as a way of saving result since we are doing this recursively)
# traverse the tree and save the encoding for each letter
# encoding_alphabet is default to an empty dictionary so that we can save the result of the recursive call
# i have also used a encoded_so_far variable to keep track of the current encoding so that we can save the result of the recursive call
# since this method of encoding works that each time we go right we add 1 to the sequence and each time we go left we add 0 to the sequence
def create_encoding(tree,encoded_so_far,encoding_alphabet = {}):
    # we will prefer the right on every branch
    # if we have a leaf node, we will save the letter in the encoding_alphabet
    # meaning if the node on the right has a value of type string meaning it is the end of that branch no more going down

    if type(tree.get_position().right.value) == str:
        # since we have gone to the right we have to add 1 to the sequence
        encoding_alphabet[tree.get_position().right.value] = encoded_so_far + '1'
    # if the value of the right is an integer meaning we can go deeper we go there first
    else:
        current_position = tree.get_position()
        tree.go_right()
        create_encoding(tree,encoded_so_far + '1',encoding_alphabet)
        tree.set_position(current_position)
    # now that we are done with the right branch we will go to the left
    if type(tree.get_position().left.value) == str :
        # since we have gone to the left we have to add 0 to the sequence
        encoding_alphabet[tree.get_position().left.value] = encoded_so_far + '0'
    # if the value of the left is an integer meaning we can go deeper we go there first
    else:
        current_position = tree.get_position()
        tree.go_left()
        create_encoding(tree,encoded_so_far + '0',encoding_alphabet)


    return encoding_alphabet



def build_tree(character_count,ordered_characters,tree):
        binary_tree = tree
        # find best way to divide theset
        # the best way is defined as the way that produces two sets that have the
        # closest sum of probabilities to each other
        divide_index = check_best_divide(list(character_count.values()))
        # print(divide_index)
        # print(ordered_characters)
        # print(character_count)
        # divide the set into two parts


        left_set = {}
        for i in range(divide_index+1):
            left_set[ordered_characters[i]] = character_count[ordered_characters[i]]

        right_set = {}
        for i in range(divide_index+1,len(ordered_characters)):
            right_set[ordered_characters[i]] = character_count[ordered_characters[i]]


        current_position = binary_tree.get_position()

        if len(left_set) == 1:
            binary_tree.position.add_left(node(str(list(left_set.keys())[0]),parent=binary_tree.position))
        else:

            # add left node
            binary_tree.position.add_left(node(sum(list(character_count.values())[:divide_index+1]),parent=binary_tree.position))
            # go to that newly created node and start building the tree from there
            binary_tree.go_left()
            # create the left branch
            build_tree(left_set,ordered_characters[:divide_index+1],binary_tree)
            
        if len(right_set) == 1:
            binary_tree.position.add_right(node(str(list(right_set.keys())[0]),parent=binary_tree.position))
        else:

            # add right node
            # after finishing the left branch we go up one level and start building the right branch
            binary_tree.set_position(current_position)
            binary_tree.position.add_right(node(sum(list(character_count.values())[divide_index+1:]),parent=binary_tree.position))
            binary_tree.go_right()
            # create the right branch
            build_tree(right_set,ordered_characters[divide_index+1:],binary_tree)


        return binary_tree






def check_best_divide(count_list):
    # i initialized it to -1 so that any division index value will be bigger than it
    # hence it will always be replaced with a better value
    best_index_so_far = None
    best_gap_so_far = None
    for i in range(len(count_list)):

        # left items sum
        left_sum = sum(count_list[:i+1])
        # right items sum
        right_sum = sum(count_list[i+1:])
        # get the gap between the two sets
        gap = abs(left_sum - right_sum)

        # if the gap so far is not initilzed yet or it it bigger than the value for this
        # iteration then we will update the best index and gap
        if best_gap_so_far is None or gap < best_gap_so_far:
            best_index_so_far = i
            best_gap_so_far = gap
        else:
            continue

    return best_index_so_far







if __name__ == "__main__":
    main()
