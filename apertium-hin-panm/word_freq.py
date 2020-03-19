
def freq(str): 
  
    # break the string into list of words 
    str_list = str.split() 
  
    # gives set of unique words 
    unique_words = sorted(set(str_list)) 
      
    for words in sorted(unique_words) : 
        print('Frequency of ', words , 'is :', str_list.count(words)) 
    
# driver code 
if __name__ == "__main__": 
    with open("test_pan.txt", "r") as f:
        data = f.read().replace('\n', '')
        str = data
      
        # calling the freq function 
        freq(str) 