def swap_case(s):
    result = ""
    
    for character in s:
        if character.isupper():
            result += character.lower()
        else:
            result += character.upper()
    return result
	
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
	
	
