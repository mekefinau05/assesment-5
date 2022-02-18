log_file = open("um-server-01.txt")


def sales_reports(log_file):    #define some report in the log_file
    for line in log_file:       #loops on every row in the log_file
        line = line.rstrip()    # remove white space in the row
        day = line[0:3]         #include all the dtat from the row
        if day == "Tue":        # if the day is equal to Tuesday
            print(line)         # console log the result on line


sales_reports(log_file)         #
