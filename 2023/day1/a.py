# Left and Right pointer -- First instance of number of each line creates 2 digit number
# Sum all lines

f = open('input.txt', 'r')
lines = f.read().split("\n")
f.close()

def extract_calibration_values(document):
    total_sum = 0
    
    # Iterate through each line in the document
    for line in document:
        # Extract the first and last digits from the line
        first_digit = next(char for char in line if char.isdigit())
        last_digit = next(char for char in reversed(line) if char.isdigit())
        
        # Combine the first and last digits to form a two-digit number
        calibration_value = int(first_digit + last_digit)
        
        # Add the calibration value to the total sum
        total_sum += calibration_value
    
    print( total_sum)




extract_calibration_values(lines)