#Virtual Adept Name Checker program
#Made by KorumakTheBroBot aka. TheMemeKing aka. Ya Boi Skinny Penis aka. Merlyn the Wizard

while True:
    name = input('Enter your handle: ')

#initalises total and adds the little bars 
#the f makes a formatted string, the \n mkaes it go to the new line b4 printing the rest
    total = 0
    print(f"\nProcessing: '{name}'")
    print("=" * 30)

# this checks the handle and sorts for digits and letters
    for c in name.upper():
     if c.isdigit(): 
        val = int(c)
        print(f"'{c}' (digit) → {val}")
     else: 
        val = ord(c) - ord('A') + 1
        print(f"'{c}' (letter) → {val}")
    
     total += val

    print(f"\nTotal sum: {total}")

# this takes the sum of total and makes in into a digit <= 9
    if total > 9:
        original_total = total
        while total > 9:
            digits = [int(d) for d in str(total)]
            total = sum(digits)
            print(f"Reduced: {original_total} → {total}")
            original_total = total

    print(f"Final number: {total}")

# this gets the decimal
    divided_value = total / 3
    print(f"\n{total} /3 = {divided_value:.3f}")

# this declares the range for the essences
    start = 0.33
    end = 3.00
    increments = 9
    step = (end - start) / (increments - 1)

    ranges = []
    for i in range(increments):
        lower = start + i * step
        upper = lower + step if i < increments - 1 else end
        ranges.append((lower, upper))

    range_index = None
    for i, (lower, upper) in enumerate(ranges):
        if lower <= divided_value <= upper:
            range_index = i + 1
            break

    # this checks the index against the categories of essence and finds a match
    if range_index == 1:
        category = "Primordial"
    elif 2 <= range_index <= 4:
        category = "Pattern"
    elif 5 <= range_index <= 7:
        category = "Dynamic"
    elif 8 <= range_index <= 9:
        category = "Questing"
    else:
        category = "man fuck you"
        #it says this because i don't really know how you'd trigger it
        #i tested it by trying to mix in non-alphanumeric symbols and it sorta just,,, worked?
        #if someone finds out how to trigger this, i congratulate you, and if it was by sheer accident then man
        #you might need to rethink that name

    print(f"\nResult: {divided_value:.3f} falls into Range {range_index}")
    print(f"Category: {category}")
    #idk how to make the response appear below the damn brackets, but it works fine, im going to bed
    again = input("\nEnter another handle? (y/N) ")
    if again != 'y':
        print("===DEACTIVATING PROGRAM===")
        print("===Made by D3v1l===")
        break
        #d3v1l is the handle of my virtual adept character, Eddie DiAngelo (see what i did there) 
        #i also made a program to run the fibonacci sequence to a certain amount of places for him
        #that's a pretty simple project, i'd recommend it if you're bored, its like 10 lines of code
