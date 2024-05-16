import time

# Define the initial color values
color_list = [[255,0,0]]

# Loop to cycle through colors
while True:
    # Increment green from 0 to 255 (Red to Yellow)
    while color_list[0][1] < 255:
        color_list[0][1] += 1
        print(color_list)
        time.sleep(0.01)
    
    # Increment blue from 0 to 255 (Yellow to Green)
    while color_list[0][2] < 255:
        color_list[0][2] += 1
        print(color_list)
        time.sleep(0.01)
    
    # Decrement red from 255 to 0 (Green to Cyan)
    while color_list[0][0] > 0:
        color_list[0][0] -= 1
        print(color_list)
        time.sleep(0.01)
    
    # Increment green from 255 to 0 (Cyan to Blue)
    while color_list[0][1] > 0:
        color_list[0][1] -= 1
        print(color_list)
        time.sleep(0.01)
    
    # Increment blue from 255 to 0 (Blue to Magenta)
    while color_list[0][2] > 0:
        color_list[0][2] -= 1
        print(color_list)
        time.sleep(0.01)
    
    # Increment red from 0 to 255 (Magenta to Red)
    while color_list[0][0] < 255:
        color_list[0][0] += 1
        print(color_list)
        time.sleep(0.01)

"""color_list[0][1] += 1
print(color_list[0])"""