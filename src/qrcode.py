import helper
import txtdata
import copy

class QRCode:
    """
    A class that contains information about a qr code
    and is able to compare with other QR codes and check
    the error correction capability of the QR code
    
    Attributes:
    last_update_date: a dictionary representing the last
    updated date of the QR code (dict)
    
    owner: the owner of the QR code (str)
    
    data: the QR code itself (TxtData)
    
    error_correction: error correction capability of the
    QR code (float)
    
    """

#3.1
    def __init__(self, file_path,
                 last_update_date = '00/00/0000',
                 owner = 'Default Owner',
                 error_correction = 0.0):
        """
        Initialializes a QRCode object based on
        inputed data
        
        Parameters:
            file_path: name of file (str)
            
            last_update_date: last updated date of QR code (str)
            
            owner: owner of QR code (str)
            
            error_correction: error correction capability of the
            QR code (float)
            
        Returns:
            None: This method does not return anything
        
        Examples:
        >>> my_qrcode = QRCode("qrcode_binary.txt",
        "01/09/2024", "Vivian", 0.1)
        >>> my_qrcode.last_update_date['Day']
        '01'
        >>> my_qrcode.last_update_date['Month']
        '09'
        >>> my_qrcode.last_update_date['Year']
        '2024'
        >>> my_qrcode.owner
        'Vivian'
        >>> my_qrcode.error_correction
        0.1
        
        >>> new = QRCode("text.txt",
        "16/02/2005", "Theo", 2.0 )
        >>> new.last_update_date['Day']
        '16'
        >>> new.last_update_date['Month']
        '02'
        >>> new.last_update_date['Year']
        '2005'
        >>> new.owner
        'Theo'
        >>> new.error_correction
        2.0
        
        >>> new = QRCode("text.txt",
        "06/02/2000", "Bob", 1.0 )
        >>> new.last_update_date['Day']
        '06'
        >>> new.last_update_date['Month']
        '02'
        >>> new.last_update_date['Year']
        '2000'
        >>> new.owner
        'Bob'
        >>> new.error_correction
        1.0
        
        """
        
        self.data = txtdata.TxtData(helper.get_data(file_path))
        #txtdata. since imported txtdata

        self.last_update_date = helper.convert_date(
            last_update_date)
        #imported helper
        
        self.owner = owner
        self.error_correction = error_correction

#3.2
    def __str__(self):
        """
        Returns a string of a wanted format informing
        how the details regarding the QR code file
        
        Parameters:
            None: This method does not have any parameters
            
        Returns:
            'The QR code was created by OWNER and last
            updated in LAST UPDATE YEAR.
            The details regarding the QR code
            file are as follows:
            This TxtData object has ROWS rows and
            COLS columns.' (str)
        
        Examples:
        >>> my_qrcode = QRCode("qrcode_binary.txt",
        "01/09/2024", "Vivian", 0.1)
        >>> print(my_qrcode)
        The QR code was created by Vivian and last updated in 2024.
        The details regarding the QR code file are as follows:
        This TxtData object has 33 rows and 33 columns.
        
        >>> new = QRCode("binary.txt",
        "09/09/2005", "Leo", 2.0)
        >>> print(new)
        The QR code was created by Leo and last updated in 2005.
        The details regarding the QR code file are as follows:
        This TxtData object has 2 rows and 2 columns.
        
        >>> new = QRCode("binary.txt",
        "09/19/2015", "Ana", 1.0)
        >>> print(new)
        The QR code was created by Leo and last updated in 2015.
        The details regarding the QR code file are as follows:
        This TxtData object has 3 rows and 3 columns.
        
        """
        return ("The QR code was created by "+str(self.owner)+
                " and last updated in "
                +str(self.last_update_date['Year'])+
                ".\nThe details regarding the QR code file"+
                " are as follows:\nThis TxtData object has "
                +str(self.data.rows)+" rows and "+str(self.data.cols)+
                " columns.")

#3.3
    def equals(self, another_qrcode):
        """
        Returns a boolean indicating whether the inputed
        QR code and the original QR code are the same
        
        Parameters:
            another_qrcode: the other qr code (QRCode)
            
        Returns:
            Boolean: True if the two QRCodes are the same,
            False otherwise
        
        Examples:
        >>> my_qrcode = QRCode("qrcode_binary.txt",
        "01/09/2024", "Vivian", 0.1)
        >>> my_qrcode_copy = QRCode("qrcode_binary_copy.txt",
        "01/09/2022", "Xuanpu", 0.1)
        >>> my_qrcode.equals(my_qrcode_copy)
        True
        
        >>> qrcode1 = QRCode("binary.txt",
        "03/09/2024", "Roy", 0.9)
        >>> qrcode2 = QRCode("different.txt",
        "08/09/2002", "Boy", 1.0)
        >>> my_qrcode.equals(my_qrcode_copy)
        False
        
        >>> qrcode1 = QRCode("binary.txt",
        "02/02/2012", "Jessica", 0.3)
        >>> qrcode2 = QRCode("binary_copy.txt",
        "02/02/2012", "Hannah", 0.3)
        >>> my_qrcode.equals(my_qrcode_copy)
        True
        
        """

        return (self.data.data == another_qrcode.data.data and
            self.error_correction == another_qrcode.error_correction)
            
        
#3.4
    def is_corrupted(self, precise_qrcode):
        """
        Returns whether the self object is corrupted based on
        the inputed precise qr code
        
        Parameters:
            precise_qrcode: the inputed qr code (QRCode)
            
        Returns:
            Boolean: True if the self object is corrupted,
            else False
        
        Examples:
        >>> my_qrcode = QRCode("qrcode_binary.txt",
        "01/09/2024", "Vivian", 0.1)
        >>> my_c_qrcode = QRCode("qrcode_binary_c.txt",
        "01/09/2000", "Vivian", 0.1)
        >>> my_c_qrcode.is_corrupted(my_qrcode)
        True
        
        >>> qrcode1 = QRCode("binary.txt",
        "02/02/2012", "Jessica", 0.3)
        >>> qrcode2 = QRCode("binary_copy.txt",
        "02/02/2012", "Hannah", 0.3)
        >>> my_qrcode.is_corrupted(my_qrcode_copy)
        True
        
        >>> qrcode1 = QRCode("binary.txt",
        "03/09/2024", "Roy", 0.9)
        >>> qrcode2 = QRCode("different.txt",
        "08/09/2002", "Boy", 1.0)
        >>> my_qrcode.is_corrupted(my_qrcode_copy)
        False
        
        """

        return not self.data.approximately_equals(
            precise_qrcode.data, self.error_correction) 

            #not since check for not approximately equal
