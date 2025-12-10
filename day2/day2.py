import time
import re

# Since the young Elf was just doing silly patterns, you can find the invalid IDs by looking for any ID which is made only of some sequence of digits repeated twice. So, 55 (5 twice), 6464 (64 twice), and 123123 (123 twice) would all be invalid IDs.

# Examples:
# - 11-22 has two invalid IDs, 11 and 22.
# - 95-115 has one invalid ID, 99.
# - 998-1012 has one invalid ID, 1010.
# - 1188511880-1188511890 has one invalid ID, 1188511885.
# - 222220-222224 has one invalid ID, 222222.
# - 1698522-1698528 contains no invalid IDs.
# - 446443-446449 has one invalid ID, 446446.
# - 38593856-38593862 has one invalid ID, 38593859.
# - The rest of the ranges contain no invalid IDs.

# Adding up all the invalid IDs in this example produces 1227775554.
# What do you get if you add up all of the invalid IDs?

class GiftShop:
	def __init__(self, file_path: str):
	# Position muss im Bereich 0-99 sein
		self.speicherArrayPart1 = []
		self.speicherArrayPart2 = []
		self.file_path = file_path
		self.processFile()

	def processFile(self):	
		try:
			with open(self.file_path, 'r') as file:
				content = file.read().strip()
				ranges = content.split(',')

				for range_str in ranges:
					range_str = range_str.strip()
					if '-' in range_str:
						# Zerlegen des Bereichs anhand des Bindestrichs "-"
						start_str, end_str = range_str.split('-')
						# Konvertierung in Integer
						start = int(start_str.strip())
						end = int(end_str.strip())

						if start > end:
							print(f"Warnung: Startwert ({start}) ist größer als Endwert ({end}) in {range_str}. Überspringe.")
							continue

						for number in range(start, end + 1):
							self.patternCheckPart1(number)
							self.patternCheckPart2(number)

		except ValueError:
			print(f"Fehler: Konnte {range_str} nicht in gültige Zahlen konvertieren.")
		except Exception as e:
			print(f"Ein unerwarteter Fehler ist aufgetreten: {e} bei {range_str}")
		# else:
		#	print(f"Warnung: Ungültiges Bereichsformat gefunden: {range_str}. Überspringe.")
		print("Verarbeitung abgeschlossen.")


	def patternCheckPart1(self, number: int): #Your puzzle answer was 16793817782.
		number_str = str(number)
		length = len(number_str)

		if length%2 == 0:
			half_length = length//2
			snippet1 = number_str[:half_length]
			snippet2 = number_str[half_length:]
			if snippet1 == snippet2:
				self.speicherArrayPart1.append(number)

	def patternCheckPart2(self, number: int):
		number_str = str(number)
		# (Gruppe 1: Das Muster) gefolgt von (\1: die Rückreferenz) plus ( + : mindestens einmal)
		pattern = r"^(\d+)\1+$"
		# re.fullmatch prüft, ob der GESAMTE String übereinstimmt.
		if re.fullmatch(pattern, number_str):
			self.speicherArrayPart2.append(number)

	def getSumOfIds(self, part: int):
		sumOfIds = 0
		if part==1:	
			for number in self.speicherArrayPart1:
				sumOfIds += number
		else: #part 2
			for number in self.speicherArrayPart2:
				sumOfIds += number
		return sumOfIds

# <<< END class GiftShop

# Run the program
start_time = time.perf_counter()

#NorthPoleGiftShop = GiftShop("input_demo.txt")
NorthPoleGiftShop = GiftShop("input.txt") 

finalResult1 = NorthPoleGiftShop.getSumOfIds(1)
finalResult2 = NorthPoleGiftShop.getSumOfIds(2)
end_time = time.perf_counter()

print(f"Die Summe aller erfassten IDs Teil 1 {finalResult1}")
print(f"Die Summe aller erfassten IDs Teil 2 {finalResult2}")
print(f"Durchlaufzeit des Programms {end_time-start_time}")