import pymem
import pymem.process
import pyautogui
import time

# Addresses for current HP and full HP
current_hp_address = 0x0990E840
full_hp_address = 0x28B54BAC

# Function to read the current HP and full HP
def read_hp(pm):
    current_hp = pm.read_int(current_hp_address)  # Reading current HP from memory
    full_hp = pm.read_int(full_hp_address)  # Reading full HP from memory
    return current_hp, full_hp

# Function to heal by pressing F5 if HP is lower than 90%
def heal_if_needed(pm):
    current_hp, full_hp = read_hp(pm)
    
    # Calculate the percentage of HP
    hp_percentage = (current_hp / full_hp) * 100
    
    print(f"Current HP: {current_hp}/{full_hp} ({hp_percentage:.2f}%)")
    
    # Check if HP is below 90%, then press F5 to heal
    if hp_percentage < 90:
        print("HP is below 90%, healing now...")
        pyautogui.press('f9')  # Simulate pressing F5 to heal

# Main loop to continuously monitor the HP and heal when needed
def main():
    # Attach to the game process
    pm = pymem.Pymem("Game.exe")  # Replace with the correct process name

    while True:
        heal_if_needed(pm)
        time.sleep(1)  # Check every 5 seconds

if __name__ == "__main__":
    main()
