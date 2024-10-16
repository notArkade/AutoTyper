import pyautogui
import time

def autotype_code(code):
    # Give some time to switch to the target window or tab
    time.sleep(5)  # Adjust the delay as needed
    
    # Type the code
    pyautogui.typewrite(code, interval=0.0)

def main():
    # Read the code from a text file
    with open("code.txt", "r") as file:
        code_to_type = "\n".join(line.strip() for line in file.readlines())    
    # Call the autotype function with the code to type
    autotype_code(code_to_type)

if __name__ == "__main__":
    main()
 