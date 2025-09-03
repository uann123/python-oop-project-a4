import helper
import copy


class TxtData:
    """
    A class that contains information about a file and
    turns it into data based on a nested list
    to save as a qr code
    
    Attributes:
    data: a nested list of integer
    representing the data (list)
    
    rows: number of rows in data (int)
    
    cols: number of columns in data (int)
    
    """
    
#2.1
    def __init__(self, data):
        """
        Initialializes a TxtData object based on
        inputed data
        
        Parameters:
            data: 2D nested list inputed (list)
            
        Returns:
            None: This method does not return anything
        
        Examples:
        >>> example = [[1,2,3],[4,5,6]]
        >>> ex = TxtData(example)
        >>> ex.rows
        2
        >>> ex.cols
        3
        
        >>> list1 = [[1,1,1],[2,2,2],[0,0,0]]
        >>> txt_list = TxtData(lst1)
        >>> txt_list.rows
        3
        >>> txt_list.cols
        3
        
        >>> list2 = [[1,1],[2,2]]
        >>> txt_list2 = TxtData(lst2)
        >>> txt_list2.rows
        2
        >>> txt_list2.cols
        2
        
        """
        
        self.data = copy.deepcopy(data)
        self.rows = len(self.data)
        self.cols = len(self.data[0])

#2.2
    def __str__(self):
        """
        Returns a string of a certain format informing
        how many rows and colums the TxtData object has
        
        Parameters:
            None: This method does not have any parameters
            
        Returns:
            "This TxtData object has "+str(self.rows)+
            " rows and " + str(self.cols)+ " columns."
            (str)
        
        Examples:
        >>> my_list_simple = [[1,2,3],[4,5,6]]
        >>> my_txt_simple = TxtData(my_list_simple)
        >>> print(my_list_simple)
        This TxtData object has 2 rows and 3 columns.
        
        >>> example = [[0,0,0],[9,9,9],[1,3,5]]
        >>> ex = TxtData(example)
        >>> print(ex)
        This TxtData object has 3 rows and 3 columns.
        
        >>> example = [[0,0],[3,5]]
        >>> ex = TxtData(example)
        >>> print(ex)
        This TxtData object has 2 rows and 2 columns.
        
        """
        
        return ("This TxtData object has "+str(self.rows)+
              " rows and " + str(self.cols)+ " columns.")

#2.3
    def get_pixels(self):
        """
        Returns an integer indicating the total number of
        pixels in data
        
        Parameters:
            None: This method does not take an explicit input
            
        Returns:
            self.rows * self.cols (int)
        
        Examples:
        >>> my_list_simple = [[1,2,3],[4,5,6]]
        >>> my_txt_simple = TxtData(my_list_simple)
        >>> my_txt_simple.get_pixels()
        6
        
        >>> example = [[7,3,8],[8,1,6],[1,3,5]]
        >>> ex = TxtData(example)
        >>> ex.get_pixels()
        9
        
        >>> example = [[1,9],[3,5]]
        >>> ex = TxtData(example)
        >>> ex.get_pixels()
        4
        
        """
        
        return self.rows * self.cols

#2.4
    def get_data_at(self, row, col):
        """
        Returns an integer indicating the value in data
        at the inputed position and a ValueError should be
        raised instead in case where the position inputed
        is out of bound 
        
        Parameters:
            row: the row of the wanted position (int)
            col: the column of the wanted position (int)
            
        Returns:
            self.data[i][j] = the position (int)
        
        Examples:
        >>> my_list_simple = [[1,2,3],[4,5,6]]
        >>> my_txt_simple = TxtData(my_list_simple)
        >>> my_txt_simple.get_data_at(0,0)
        1
        
        >>> example = [[7,7,8],[8,6,9],[7,3,8]]
        >>> ex = TxtData(example)
        >>> ex.get_data_at(0,2)
        8
        
        >>> example = [[1,100],[30,50]]
        >>> ex = TxtData(example)
        >>> ex.get_data_at(10,10)
        Traceback (most recent call last):
        ValueError: Index out of bound!
        
        """
        
        if 0 <= row < self.rows and 0 <= col < self.cols:
            #check if inputed row and col out of range
            
            for i in range(len(self.data)):
                #index for the rows
                for j in range(len(self.data[0])):
                    #index for the col
                    
                        return self.data[i][j]
                        
        else:
            raise ValueError("Index out of bound!")

#2.5
    def pretty_save(self, file_name):
        """
        Returns nothing but rather converts the data
        of the inputed file to a prettier form so that it
        can be scanned as a qr code
        
        Parameters:
            file_name: name of the file (str)
            
        Returns:
            None: this method does not return anything
        
        Examples:
        >>> my_list = get_data("qrcode_binary.txt")
        >>> my_txt = TxtData(my_list)
        >>> my_txt.pretty_save("qrcode_pretty.txt")
        
        >>> data_list = get_data("list.txt")
        >>> save_data = TxtData(data_list)
        >>> save_data.pretty_save("pretty.txt")
        
        >>> data = get_data("list_binary.txt")
        >>> save = TxtData(data)
        >>> save.pretty_save("prettier.txt")
        
        """

        fobj = open(file_name, 'w')
        #open for writing
        
        for row in self.data:
            new_char = []
            #new list for each row
            
            for i in row:
                if i == 1:
                    i = chr(0x2588)*2
                    new_char.append(i)
                    #change i into black blocks and append
                
                elif i == 0:
                    i = '  '
                    new_char.append(i)
                    #change i into space char and append
            
            pretty_qr = ''.join(new_char) #join list
            fobj.write(pretty_qr + '\n')
            #add new line after each row
        
        fobj.close()

#2.6
    def equals(self, another_data):
        """
        Returns a boolean indicating if the inputed data and
        the original data are equal
        
        Parameters:
            another_data: data of another TxtData object
            (TxtData)
            
        Returns:
            Boolean: True if the two TxtData objects are equal,
            else False 
        
        Examples:
        >>> my_list_simple = [[1,2,3],[4,5,6]]
        >>> my_txt_simple_1 = TxtData(my_list_simple)
        >>> my_txt_simple_2 = TxtData(my_list_simple)
        >>> my_txt_simple_1.equals(my_txt_simple_2)
        True
        
        >>> list1 = [[1,0,0],[0,1,0]]
        >>> txt1 = TxtData(list1)
        >>> list2 = [[0,0,0],[0,1,1]]
        >>> txt2 = TxtData(list2)
        >>> txt1.equals(txt2)
        False
        
        >>> list1 = [[1,1,1],[0,0,0]]
        >>> txt1 = TxtData(list1)
        >>> txt2 = TxtData(list1)
        >>> txt1.equals(txt2)
        True
        
        """

        return another_data.data == self.data

#2.7
    def approximately_equals(self, another_data, precision):
        """
        Returns a boolean indicating if the two TxtData objects
        are approximately equal
        
        Parameters:
            another_data: data of another TxtData object
            (TxtData)
            precision: the input precision (float)
            
        Returns:
            Boolean: True if the two TxtData objects are
            approximately equal, else False 
        
        Examples:
        >>> my_list_simple_1 = [[1,2,3],[4,5,6]]
        >>> my_list_simple_2 = [[1,2,3],[7,8,9]]
        >>> my_txt_simple_1 = TxtData(my_list_simple_1)
        >>> my_txt_simple_2 = TxtData(my_list_simple_2)
        >>> my_txt_simple_1.equals(my_txt_simple_2)
        False
        >>> my_txt_simple_1.approximately_equals(my_txt_simple_2, 0.5)
        True
        
        >>> list1 = [[1,6,7],[8,4,9]]
        >>> txt1 = TxtData(list1)
        >>> list2 = [[9,6,7],[8,4,1]]
        >>> txt2 = TxtData(list2)
        >>> txt1.equals(txt2)
        False
        >>> txt1.approximately_equals(txt2, 3)
        True
        
        >>> list1 = [[7,8,19],[0,1,0]]
        >>> txt1 = TxtData(list1)
        >>> txt2 = TxtData(list1)
        >>> txt1.equals(txt2)
        True
        >>> txt1.approximately_equals(txt2, 0.1)
        True
        
        """
        
        incon_val = 0
        #number of inconsistent values initialized
        
        total_val = self.get_pixels()
        #total number of values with earlier function
        
        for i in range(len(self.data)):
            #find index for rows
            
            for j in range(len(self.data[0])):
                #find index for col
                
                if self.data[i][j] != another_data.data[i][j]:
                    #if character not equal
                    
                    incon_val += 1
            
        
        incon_rate = incon_val/total_val
        #find inconsistent rate
        
        return incon_rate <= precision
