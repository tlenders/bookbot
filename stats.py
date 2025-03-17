def get_num_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_count = {}
    text = text.lower() 
    
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    return char_count

def sort_on(dict):
 
    sorted_list = []
    for key, value in dict.items():
        if key.isalpha():
            sorted_list.append({"character": key, "count": value})
    sorted_list.sort(key=lambda x: x["count"], reverse=True)
    return sorted_list
        
    