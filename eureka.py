
# |  ||
# || |_


infinite = True

def eureka():
	firstchoice = input("#  How may I be of assistance? ").lower()
	if (firstchoice == "molarmass"):
		print()
		print()
		molmasscalc(False)
	elif (firstchoice == "tips"):
		print()
		print()
		tipcalc()
	elif (firstchoice == "ph"):
		print()
		print()
		phcalc()
	elif (firstchoice == "molarity"):
		print()
		print()
		molarity()
	elif (firstchoice == "help" or firstchoice == "?"):
		print()
		print()
		helpfunction()
		# explains all functions
	elif (firstchoice == "exit"):
		secondchoice = input("#  Do you need anything else before I shut down? ")
		if (secondchoice[0] == "n"):
			print("#  Ok. See you later!")
			print()
			print("* Session terminated by USER *")
			global infinite
			infinite = False
			molmasscalc(True)
		else:
			print()
			print()
			print()
			eureka()
	else:
		print("#  I'm sorry, but I do not understand that command.")
		print()
		print()
		print()
		eureka()

# # # # # # # # # # # # # # # # # # # # # # # # # # #

def eureka_two(firstchoice):
	if (firstchoice == "exit"):
		secondchoice = input("#  Do you need anything else before I shut down? ")
		if (secondchoice[0] == "n"):
			print("#  Ok. See you later!")
			print()
			print("* Session terminated by USER *")
			global infinite
			infinite = False
			molmasscalc(True)
		else:
			print()
			print("#  An error occured. Rebooting...  ")
			print()
			print()
			print()
			start()
	else:
		print("#  I'm sorry, but I do not understand that command.")
		print()
		print()
		print()
		eureka()

# # # # # # # # # # # # # # # # # # # # # # # # # # #

def molmasscalc(temp):
	totalmass = 0
	x = False
	if (temp == True):
		# no u
		x = True
	else:
		print("M O L A R   M A S S   C A L C U L A T O R")
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
                   "hs": 277, "hassium": 277
                    }

		while x == False:
			print
			molecule = input("Enter an element: ").lower()
			if (molecule == "exit"):
				print("# Exiting program...")
				print()
				print()
				print()
				eureka()
			else:
				molecule = float(atomicMass[molecule])
				numofmol = input("How many moles/atoms? ")
				if (numofmol == "exit"):
					print("# Exiting program...")
					print()
					print()
					print()
					eureka()
				else:
					numofmol = float(numofmol)
					checker = input("Would you like to add another element? ").lower()
					if (checker == "exit"):
						print("# Exiting program...")
						print()
						print()
						print()
						eureka()
					else:
						if (checker[0] == "y" or checker == "true"):
							temp = molecule * numofmol
							totalmass += temp
						else:
							temp = molecule * numofmol
							totalmass += temp
							x = True
							print("Mass: " + str(totalmass) + "g.")
							print()
							print()
							print()
							eureka()

# # # # # # # # # # # # # # # # # # # # # # # # # # #

def tipcalc():
	print("T I P   C A L C U L A T O R")
	print()
	amount = input("Total amount: ")
	if (amount == "exit"):
		print("# Exiting program...")
		print()
		print()
		print()
		eureka()
	else:
		checking = input("$" + str(float(amount)) + " was your total. Is that correct? ").lower()
		if (checking == "exit"):
			print("# Exiting program...")
			print()
			print()
			print()
			eureka()
		else:
			if (checking[0] == "y" or checking == "True" or checking == "true"):
				# all good
				print("* Value approved *")
				print()
				print("! 20% Tip !")
				calculatepercent(float(amount), 2)
				print()
				print("! 18% Tip !")
				calculatepercent(float(amount), 1.8)
				print()
				print("! 15% Tip !")
				calculatepercent(float(amount), 1.5)
				print()
				print("! 10% Tip !")
				calculatepercent(float(amount), 1)
				print()
				print()
				print()
				eureka()
			else:
				#no bueno
				print("* Value not approved *")
				print()
				to_restart = input("Would you like to input a new value? ")
				if (to_restart[0] == "y"):
					tipcalc()
				else:
					print()
					print()
					print()
					eureka()


def calculatepercent(amount, multiple):
	new_amount = amount / 10
	new_amount = float(round(new_amount * multiple, 2))
	print("Tip: $" + str(new_amount))
	new_total = new_amount + amount
	new_total = float(round(new_total, 2))
	print("Total: $" + str(new_total))

# # # # # # # # # # # # # # # # # # # # # # # # # # #

def helpfunction():
	print("A V A I L A B L E   P R O G R A M S")
	print()
	print("[molarmass] : Molar Mass Calculator")
	print()
	print("     [tips] : Restaurant Tip Calculator")
	print()
	print("       [ph] : pH/pOH Calculator")
	print()
	print(" [molarity] : Molarity Calculator")
	print()
	print()
	print()
	eureka()

# # # # # # # # # # # # # # # # # # # # # # # # # # #

def phcalc():
	import math
	print("P H / P O H   C A L C U L A T O R")
	print()
	acid_base_con = input("Enter the concentration of the acid or base: ")
	if (acid_base_con == "exit"):
		print("# Exiting program...")
		print()
		print()
		print()
		eureka()
	else:
		checking = input(str(float(acid_base_con)) + " is the concentration. Is that correct? ").lower()
		if (checking == "exit"):
			print("# Exiting program...")
			print()
			print()
			print()
			eureka()
		else:
			if (checking[0] == "y" or checking == "True" or checking == "true"):
				# all good
				print("* Value approved *")
				acid_base_con = float(acid_base_con)
				pH_pOH = math.log(acid_base_con, 10) * -1
				pH_pOH = "%.2f" % pH_pOH
				print()
				print("The pH/pOH is " + str(pH_pOH))
				print()
				print()
				print()
				eureka()
			else:
				#no bueno
				print("* Value not approved *")
				print()
				to_restart = input("Would you like to input a new pH? ").lower()
				if (to_restart[0] == "y"):
					phcalc()
				else:
					print()
					print()
					print()
					eureka()

# # # # # # # # # # # # # # # # # # # # # # # # # # #

def molarity():
    print("M O L A R I T Y   C A L C U L A T O R")
    print()
    pH_pOH = input("Enter the pH or pOH of an acid/base: ")
    if (pH_pOH == "exit"):
        print("# Exiting program...")
        print()
        print()
        print()
        eureka()
    else:
        checking = input(str(float(pH_pOH)) +
     	                    " is your pH/pOH. Is that correct? ").lower()
        if (checking == "exit"):
            print("# Exiting program...")
            print()
            print()
            print()
            eureka()
        else:
            if (checking[0] == "y" or checking == "True" or checking == "true" or checking == "yes"):
         	   # all good
                print("* Value approved *")
                print()
                pH_pOH = float(pH_pOH)
                acid_base_con = 10**(pH_pOH * -1)
                acid_base_con = '%.2e' % acid_base_con
                print("The concentration (molarity) of the acid/base is " + str(acid_base_con))
                print()
                print()
                print()
                eureka()
            else:
                #no bueno
                print("* Value not approved *")
                print()
                to_restart = input("Would you like to input a new pH/pOH? ").lower()
                if (to_restart[0] == "y"):
                    phcalc()
                else:
                    print()
                    print()
                    print()
                    eureka()

# # # # # # # # # # # # # # # # # # # # # # # # # # #

def start():
    print("#  Welcome to E.U.R.E.K.A.")
    print()
    allowed_people = [3000048, 3000043, 3000027, 3000078, 3000014, 0]
    global infinite
    if infinite == True:
        while infinite == True:
            allowed = False
            while allowed == False:
                val = input("#  Please Scan a Valid ID: ")
                x = len(allowed_people)
                while x > 0:
                    try:
                        if int(val) == allowed_people[x-1]:
                            allowed = True
                            x = 0
                        x = x - 1
                    except:
                        allowed = False
                        x = 0
                if allowed == False:
                    if val == "exit":
                        eureka_two("exit")
                        break
                    else:
                        print()
                        print("#  Access denied.")
                        print()
                        break
                if allowed == True:
                    print()
                    print("#  Permission granted.")
                    print()
                    print()
                    print()
                    eureka()
    else:
        eureka()

start()
