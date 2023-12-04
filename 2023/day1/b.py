from string import digits

def replace_text_digits(string: str):
    digit_to_text =  {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
    }
    for i in range(len(string)):
        for key, value in digit_to_text.items():
            if string[i] == value[0]:
                len_str = len(value)
                if string[i : (i + len_str)] == value:
                    # Using recursion here we repeat the process on the string
                    string = string.replace(value, str(key))
                    return replace_text_digits(string)
    return string

with open("input.txt", "r") as reader:
    calibration_list = []
    for line in reader:
        line = replace_text_digits(line)
        calibration = ""
        for char in line:
            if char in digits:
                calibration += char
                for char in reversed(line):
                    if char in digits:
                        calibration += char
                        break
                break 
        calibration_list.append(int(calibration))
    print(calibration_list)
    print(sum(calibration_list))