def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count(file_contents)
        letter_count(file_contents)
#function created to count words, takes a string        
def word_count(string):
    words = string.split()
    count = 0
    for word in words:
        count += 1
    print("---Begin report of books/frankenstein.txt---")
    print(f"{count} words found in the document")
#function to create dictionary to count iterations of characters in text
def letter_count(string):
    character_count = {}
    char_list = []
    lower_case = string.lower()
    for char in lower_case:
        if char.isalpha() == True: #if char is a letter iterate, else ignore
            character_count[char] = character_count.get(char, 0) + 1
    for char in character_count: #for each char in the dictionary, add to new dict and then append dict to list
        char_dict = {'name':char, 'num':character_count[char]}
        char_list.append(char_dict)
    char_list.sort(reverse=True, key=sort) #call sort function 
    for dict in char_list: #for every dictionary in the list, access name and num
        print(f"The {dict['name']} character was found {dict['num']} times")
#function to sort dictionary in numerical order, received from letter_count function
def sort(item):
    return item['num']





if __name__ == '__main__':
    main()
    
    