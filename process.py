log_file = open("um-server-01.txt")


def sales_reports(log_file):    #declare a function that takes in a parameter
    for line in log_file:       #loops over the list
        line = line.rstrip()    # remove white space
        day = line[0:3]         #check the first 3 letters
        if day == "Mon":        # if the day is equal to Monday
            print(line)         # if match, print the entire line


sales_reports(log_file)         # calling the abnove function
