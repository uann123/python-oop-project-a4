#1.1

def convert_date(date_str):
    """
    Returns a dictionary with "Day", "Month" and "Year"
    as keys and strings as values with an inputed
    date string
    
    Parameters:
        date_str: the inputed date string (str)
        
    Returns:
        dictionary: a dictionary with "Day", "Month" and
        "Year" as keys and strings as values (dict)
    
    Examples:
    >>> convert_date("09/01/2024")
    {'Day': '09', 'Month': '01', 'Year': '2024'}
    
    >>> convert_date("08/08/2021")
    {'Day': '08', 'Month': '08', 'Year': '2021'}
    
    >>> convert_date("0/01/202")
    Traceback (most recent call last):
    ValueError:Input format incorrect!
    
    """
    
    parts_dict = date_str.split("/")
    #split into 3 parts
    
    if (len(parts_dict) !=3 or len(parts_dict[0]) != 2 or
        len(parts_dict[1]) != 2 or len(parts_dict[2])!= 4):
        # if date_str cannot be seperated into 3 parts
        #if any of the parts doesn't have the right length
        #then raise ValueError
        
        raise ValueError("Input format incorrect!")
    
    else:
        dictionary = {"Day": parts_dict[0], "Month": parts_dict[1],
                  "Year": parts_dict[2]}
        #create dictionary
        
    return dictionary

#1.2
def get_data(file_path):
    """
    Returns a nested list of integers representing the data
    in the file based on an inputed file_path
    
    Parameters:
        file_path: the inputed name of the file (str)
        
    Returns:
        empty_list: list of the integers representing
        the data(list)
    
    Examples:
    >>> get_data("small_data.txt")
    [[0,1],[1,0]]
    
    >>> get_data([0,0],[9,0])
    Traceback (most recent call last):
    ValueError: File should contain only 0s and 1s!
    
    >>> convert_date([1,2],[3,4])
    Traceback (most recent call last):
    ValueError: File should contain only 0s and 1s!
    
    """
    
    fobj = open(file_path, 'r') #read the file
    empty_list = []
    
    for i in fobj:
        
        line = i.strip('\n') #strip newline
        lists = [] #new empty list
        
        for j in line:
            try:
                j = int(j) #convert to integer the values
                lists.append(j) #add to list
                
                if j not in [0,1]:
                    raise ValueError("File should contain"+
                                         " only 0s and 1s!")
                
            except ValueError:
                raise ValueError("File should contain"+
                                         " only 0s and 1s!")
            #if one of the character cannot be changed into
            #an integer
            
        empty_list.append(lists) #nested list
            
    fobj.close()  
            
    return empty_list
