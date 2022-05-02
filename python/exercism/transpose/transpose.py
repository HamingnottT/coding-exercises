def transpose(lines):

    # The brute force way is to concatenate characters for each list index
    # And collect these concatenations into a new list

    # Copy of the list
    

    old_line = ''
    new_line = ''
    
    for line in lines:
        new_line = line
        old_line = new_line
        

    print(new_line)
    print(old_line)
    
    for i in lines:
        for n in range(len(i)):
            try:
                print(i[n])
                
            except IndexError:
                break

transpose(["Hello", "World"])