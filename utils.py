def main():
    active = True
    while active:
        print("\n- UTILS -\n"
              "[1] Tip Calculator\n"
              "[2] Caesar Cipher\n"
              "[3] Molar Mass Calculator\n"
              "[4] Exit")
        choice = input("# ")

        if choice == "1":
            print("\n- Tip Calculator -")
            amount = float(input("Total cost: "))
            tipCalculator(amount, 2)    # 20%
            tipCalculator(amount, 1.5)  # 15%
            tipCalculator(amount, 1)    # 10%

        elif choice == "2":
            print("\n- Caesar Cipher -")
            caesar()

        elif choice == "3":
            print("\n- Molar Mass Calculator -")
            molar_mass()

        elif choice == "4":
            print("\nGoodbye!")
            active = False

################################################################################


def tipCalculator(amount, mult):
    tip = amount / 10  # makes it easier to convert percentages
    tip = round(tip * mult, 2)  # calculate tip amount
    total = round(tip + amount, 2)  # calculate total amount
    mult = int(mult * 10)  # fixes visuals

    print(str(mult) + "% Tip: $" + str(tip) + " | Total: $" + str(total))

################################# ^ Choice 1 ^ #################################


def caesar():
    invalid_method = True
    invalid_num = True
    method = input("Encode or Decode: ").lower()

    while invalid_method == True:
        if (method[0] == "d" or method[0] == "e"):
            invalid_method = False
        else:
            method = input("Please enter a valid choice: ").lower()

    message = input("Enter your message: ").lower()
    key = int(input("Enter the key number (1-26): "))

    while invalid_num == True:
        if (key <= 0 or key > 26):
            key = int(input('Please enter a valid number: '))
        else:
            invalid_num = False

    if method[0] == "d":
        key = -key
    coded = ""
    for char in message:
        if char.isalpha():
            num = ord(char)
            num += key
            if num > ord("z"):
                num -= 26
            elif num < ord("a"):
                num += 26
            coded += chr(num)
        else:
            coded += char
    print("Your encoded message: " + str(coded))

################################# ^ Choice 2 ^ #################################


def molar_mass():
    totalmass = 0
    working = True

    atomicMass = {0: 0,
                  "h": 1.008, "hydrogen": 1.008,
                  "he": 4.0026, "helium": 4.0026,
                  "li": 4.0026, "lithium": 4.0026,
                  "be": 9.0122, "beryllium": 9.0122,
                  "b": 10.81, "boron": 10.81,
                  "c": 12.011, "carbon": 12.011,
                  "n": 14.007, "nitrogen": 14.007,
                  "o": 15.999, "oxygen": 15.999,
                  "f": 18.998, "fluorine": 18.998,
                  "ne": 20.180, "neon": 20.180,
                  "na": 22.990, "sodium": 22.990,
                  "mg": 24.305, "magnesium": 24.305,
                  "al": 26.892, "aluminum": 26.892,
                  "si": 28.085, "silicon": 28.085,
                  "p": 30.974, "phosphorus": 30.974,
                  "s": 32.06, "sulfur": 32.06,
                  "cl": 35.45, "chlorine": 35.45,
                  "ar": 39.948, "argon": 39.948,
                  "k": 39.098, "potassium": 39.098,
                  "ca": 40.078, "calcium": 40.078,
                  "sc": 44.956, "scandium": 44.956,
                  "ti": 47.867, "titanium": 47.867,
                  "v": 50.942, "vanadium": 50.942,
                  "cr": 51.996, "chromium": 51.996,
                  "mn": 54.938, "manganese": 54.938,
                  "fe": 55.845, "iron": 55.845,
                  "co": 58.933, "cobalt": 58.933,
                  "ni": 58.693, "nickel": 58.693,
                  "cu": 63.546, "copper": 63.546,
                  "zn": 65.38, "zinc": 65.38,
                  "ga": 69.723, "gallium": 69.723,
                  "ge": 72.630, "germanium": 72.630,
                  "as": 74.922, "arsenic": 74.922,
                  "se": 78.971, "selenium": 78.971,
                  "br": 79.904, "bromine": 79.904,
                  "kr": 83.798, "krypton": 83.798,
                  "rb": 85.468, "rubidium": 85.468,
                  "sr": 87.62, "strontium": 87.62,
                  "y": 88.906, "yittrium": 88.906,
                  "zr": 91.224, "zirconium": 91.224,
                  "nb": 92.906, "niobium": 92.906,
                  "mo": 95.95, "molybdenum": 95.95,
                  "tc": 98, "technetium": 98,
                  "ru": 101.07, "ruthenium": 101.07,
                  "rh": 102.91, "rhodium": 102.91,
                  "pd": 106.42, "palladium": 106.42,
                  "ag": 107.87, "silver": 107.87,
                  "cd": 112.41, "cadmium": 112.41,
                  "in": 114.82, "indium": 114.82,
                  "sn": 118.71, "tin": 118.71,
                  "sb": 121.76, "antimony": 121.76,
                  "te": 127.6, "tellurium": 127.6,
                  "i": 126.9, "iodine": 126.9,
                  "xe": 131.29, "xenon": 131.29,
                  "cs": 132.9055, "cesium": 132.9055,
                  "ba": 137.327, "barium": 137.327,
                  "la": 138.9055, "lanthanum": 138.9055,
                  "ce": 140.116, "cerium": 140.116,
                  "pr": 140.9077, "praseodymium": 140.9077,
                  "nd": 144.24, "neodymium": 144.24,
                  "pm": 145, "promethium": 145,
                  "sm": 150.36, "samarium": 150.36,
                  "eu": 151.964, "europium": 151.964,
                  "gd": 157.25, "gadolinium": 157.25,
                  "tb": 158.9253, "terbium": 158.9253,
                  "dy": 162.5, "dysprosium": 162.5,
                  "ho": 164.9303, "holmium": 164.9303,
                  "er": 167.259, "erbium": 167.259,
                  "tm": 168.9342, "thulium": 168.934,
                  "yb": 173.04, "ytterbium": 173.04,
                  "lu": 174.967, "lutetium": 174.967,
                  "hf": 178.49, "hafnium": 178.49,
                  "ta": 180.9479, "tantalum": 180.9479,
                  "w": 183.84, "tungsten": 183.84,
                  "re": 186.207, "rhenium": 186.207,
                  "os": 190.23, "osmium": 190.23,
                  "ir": 192.217, "iridium": 192.217,
                  "pt": 195.078, "platinum": 195.078,
                  "au": 196.9665, "gold": 196.9665,
                  "hg": 200.59, "mercury": 200.59,
                  "tl": 204.3833, "thallium": 204.3833,
                  "pb": 207.2, "lead": 207.2,
                  "bi": 208.9804, "bismuth": 208.9804,
                  "po": 209, "polonium": 209,
                  "at": 210, "astatine": 210,
                  "rn": 222, "radon": 222,
                  "fr": 223, "francium": 223,
                  "ra": 226, "radium": 226,
                  "ac": 227, "actinium": 227,
                  "pa": 231.0359, "protactinium": 231.0359,
                  "th": 232.0381, "thorium": 232.0381,
                  "np": 237, "neptunium": 237,
                  "u": 238.0289, "uranium": 238.0289,
                  "am": 243, "americium": 243,
                  "pu": 244, "plutonium": 244,
                  "cm": 247, "curium": 247,
                  "bk": 247, "berkelium": 247,
                  "cf": 251, "californium": 251,
                  "es": 252, "einsteinium": 252,
                  "fm": 257, "fermium": 257,
                  "md": 258, "mendelevium": 258,
                  "no": 259, "nobelium": 259,
                  "rf": 261, "rutherfordium": 261,
                  "lr": 262, "lawrencium": 262,
                  "db": 262, "dubnium": 262,
                  "bh": 264, "bohrium": 264,
                  "sg": 266, "seaborgium": 266,
                  "mt": 268, "mertnerium": 268,
                  "rg": 272, "roentgenium": 272,
                  "hs": 277, "hassium": 277}

    while working == True:
        molecule = input("Enter an element: ").lower()
        molecule_mass = float(atomicMass[molecule])
        num_of_mol = float(input("How many moles/atoms? "))
        checker = input("Would you like to add another element? ").lower()
        if (checker[0] == "y"):
            temp = molecule_mass * num_of_mol
            totalmass += temp
        else:
            temp = molecule_mass * num_of_mol
            totalmass += temp
            print("Mass: " + str(round(totalmass, 10)) + "g")
            working = False

################################# ^ Choice 3 ^ #################################


main()
