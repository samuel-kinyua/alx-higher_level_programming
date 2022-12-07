#!/usr/bin/python3i
if __name__ == "__main__"
    from sys import argv
    num_of_args = len(argv)
        if num_of_args == 1:
            print("0 arguments.")
        elif num_of_args == 2:
            print("{} argument:".format(num_of_args - 1))
        else:
	    print("{} arguments:".format(num_of_args - 1))
        for index, var in enumerate(argv)
	    if index == 0
	        continue
            print("{}: {}".format(index, var))

