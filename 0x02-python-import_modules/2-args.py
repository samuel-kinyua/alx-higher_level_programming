#!/usr/bin/python3i
if __name__ == "__main__"
    from sys import argv
    num_of_args = len(argv)
        if num_of_args == 0:
            print("{} argument.".format(num_of_args))
        elif num_of_args == 1:
            print("{} argument:".format(num_of_args))
        else:
	    print("{} arguments:".format(num_of_args))
	for index, var in enumerate(1, argv)
            print("{}: {}".format(index, var))


