import re
import sys

if __name__ == '__main__':

    n_command = int(input())

    my_list = []

    command_pattern = "[a-z]+"
    index_pattern = "(\d+) (\d+)"
    integer = "\d+"

    for i in range(n_command):
        command = input()
        command_function = re.match(command_pattern, command).group()
        
        if command_function == "insert":
            re_result = re.search(index_pattern, command)
            my_list.insert(int(re_result.group(1)), int(re_result.group(2)))
        
        elif command_function == "print":
            print(my_list)

        elif command_function == "remove":
            re_result = re.search(integer, command)
            my_list.remove(int(re_result.group(0)))
            
        elif command_function == "append":
            re_result = re.search(integer, command)
            my_list.append(int(re_result.group(0)))
            
        elif command_function == "sort":
            my_list.sort()
        
        elif command_function == "pop":
            my_list.pop()
            
        elif command_function == "reverse":
            my_list.reverse()
            
        else:
            sys.exit("Invalid Input")

