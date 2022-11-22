name = " Zed A. Shaw"
age = 35 # not False
height = round (74 * 2.54) # cms
weight = round (180 * 0.453592) # kgs round floating
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} cms tall.")
print(f"He's {weight} kgs heavy.")
print(f"Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = round (age + height + weight)
print(f"If I add {age}, {height}, and {weight} I get {total}.")
