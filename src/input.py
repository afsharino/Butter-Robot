import time

def read_input(read_type:int=1) -> list:
    # Read from file
    if read_type == 1:
        with open("test/input1.txt", 'r') as file:
            input_matrix = file.readlines()
            
        # Extract number of rows and Columns from file
        n_rows = int(input_matrix[0].strip("\n")[0])
        n_columns = int(input_matrix[0].strip("\n")[2])
        del input_matrix[0]
        
        # Extract gameplay matrix from file
        matrix = [line.strip('\n').split() for line in input_matrix]
        
        return matrix
    
    # Read from command line  
    elif read_type == 2:
        while True:
            print("Enter matrix Below:\n")
            input_matrix = input()
            try:
                n_rows = int(input_matrix[0])
                n_columns = int(input_matrix[2:4])
                input_matrix = input_matrix[5:]

                matrix = []
                input_matrix = input_matrix.split()
                for i in range(n_rows):
                    row = []
                    for j in range(n_columns):
                        row.append(input_matrix[j])
                    input_matrix = input_matrix[n_columns:]
                    matrix.append(row)
                
                return matrix
            except:
                print("Wrong input for matrix!")
    else:
        return []
    
def get_input():
    while True:
        print("Enter 1 to read from file.") 
        print("Enter 2 to enter matrix.")
        
        try:
            user_choice = int(input("[1]/2? "))
            matrix = read_input(user_choice)
            if matrix == []:
                print("Wrong input, just enter 1 or two!")
                time.sleep(2)
            else:
                break  
        except:
            print("Please enter valid integer number!") 
            time.sleep(2)
            
    return matrix