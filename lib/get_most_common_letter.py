def get_most_common_letter(text):
    counter = {}
    for char in text:
        if char != " ":
            counter[char] = counter.get(char, 0) + 1
    letter = sorted(counter.items(), key=lambda item: item[1])[-1][0]
    # print(counter)
    return letter


print(f"""
Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
Expected: o
Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
""")


# sorting the key-value pairs based on the keys --> print(sorted(counter.items(), key=lambda item: item[0]))
# sorting the key-value pairs based on the values --> print(sorted(counter.items(), key=lambda item: item[1]))