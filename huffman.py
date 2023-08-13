
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
    def __init__(self,key,value,parent=None):

        self.right = None
        self.left = None
        self.parent = parent
        self.value = value
        self.key= key
# this function was added so that we can build the tree from the bottom up
# as it is the case wiht huffman encoding
    def add_parent(self,node):
        self.parent = node
    def add_right(self,node):
        self.right = node
    def add_left(self,node):
        self.left = node
    def delete_right(self):
        self.right = None
    def delete_left(self):
        self.left = None







def build_tree(nodes):
    minimum_frequency_node = nodes[-1]
    second_minimum_frequency_node = nodes[-2]

    parent_node = node(key=(minimum_frequency_node.key + second_minimum_frequency_node.key),value=(minimum_frequency_node.value + second_minimum_frequency_node.value))
    parent_node.add_left(second_minimum_frequency_node)
    parent_node.add_right(minimum_frequency_node)

    del nodes[-1]
    # after deleting the minimum the second minimum will be the new minimum
    del nodes[-1]

    if len(nodes) == 0:
        return parent_node
    else:
        nodes.append(parent_node)
        nodes = sorted(nodes,key=lambda x: x.value,reverse=True)
        return build_tree(nodes)
# provided a binary tree and an encoding alphabet dictionary (which will serve as a way of saving result since we are doing this recursively)
# traverse the tree and save the encoding for each letter
# encoding_alphabet is default to an empty dictionary so that we can save the result of the recursive call
# i have also used a encoded_so_far variable to keep track of the current encoding so that we can save the result of the recursive call
# since this method of encoding works that each time we go right we add 1 to the sequence and each time we go left we add 0 to the sequence
def create_encoding(tree,encoded_so_far,encoding_alphabet = {}):
    # we will prefer the right on every branch
    # if we have a leaf node, we will save the letter in the encoding_alphabet
    # meaning if the node on the right has a value of type string meaning it is the end of that branch no more going down

    if len(tree.get_position().right.key) == 1:
        # since we have gone to the right we have to add 1 to the sequence
        encoding_alphabet[tree.get_position().right.key] = encoded_so_far + '1'
    # if the value of the right is an integer meaning we can go deeper we go there first
    else:
        current_position = tree.get_position()
        tree.go_right()
        create_encoding(tree,encoded_so_far + '1',encoding_alphabet)
        tree.set_position(current_position)
    # now that we are done with the right branch we will go to the left
    if len(tree.get_position().left.key) == 1 :
        # since we have gone to the left we have to add 0 to the sequence
        encoding_alphabet[tree.get_position().left.key] = encoded_so_far + '0'
    # if the value of the left is an integer meaning we can go deeper we go there first
    else:
        current_position = tree.get_position()
        tree.go_left()
        create_encoding(tree,encoded_so_far + '0',encoding_alphabet)


    return encoding_alphabet





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



    nodes =[]


    # create a node for each character and sort by value
    for character,count in character_count.items():
        nodes.append(node(key = character,value= count))
    
    # sort the nodes by value
    nodes = sorted(nodes,key=lambda x:x.value,reverse=True)

    # create a binary tree from the nodes
    root_node = build_tree(nodes)
    # create a tree
    tree = BinaryTree(root = root_node)

    # create an encoding alphabet dictionary
    encoding_alphabet = create_encoding(tree,encoded_so_far = '')
    return encoding_alphabet
    
    

    




if __name__ == "__main__":
    main()