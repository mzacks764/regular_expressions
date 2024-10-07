import re

def main():
    test_str = input("Text: ")
    print(count(test_str))

def count(test_str):
    pattern =  r'\bum\b'        # \b checks for a word boundary before and after the um
    result = re.findall(pattern,test_str,re.IGNORECASE)  # re.Ignorecase ignores case of letters u m in pattern
    #print(result)
    return len(result)      # result is a list of each occurence of pattern; len counts the items in result.


if __name__ == '__main__':
    main()
    