import time

class batteryBank:
    def __init__(self, line :str):
        self.numberArray = [int(number) for number in line]
        self.numberArrayReverse = self.numberArray[::-1]
        self.joltage1 = self.calculateJoltage1()
        self.joltage2 = self.calculateJoltage2()

    def calculateJoltage1(self):
        
        pos1 = 0 #dezimalstelle
        pos2 = 0
        jol = 0
        # length = self.numberArray.length()

        for index, number in enumerate(self.numberArray):
            if index == len(self.numberArray) - 1:
                # print(f"Dies ist die letzte Zahl: {number}")
                if pos2 < number:
                    pos2 = number
            else: # wenn nicht die letzte Zahl
                if pos1 < number:
                    pos1 = number
                    pos2 = 0 # rest pos2 if 1 is set again
                elif pos2 < number:
                    pos2 = number

        jol = pos1 * 10 + pos2
        print(f"V1: {self.numberArray} > {jol}")
        return jol

    def calculateJoltage2(self):
        jol = 0
        numberOfBatteries = 12
        selectedBatteries = [0] * numberOfBatteries
        currentBattery = numberOfBatteries
        pointer = 0
        for index, batteries in enumerate(selectedBatteries):
            for index2, number in enumerate(self.numberArray):
                
                if index2 < (len(self.numberArray)-numberOfBatteries+index+1):
                    # print(f"index2={index2} number {number}")
                    if index2 >= pointer:    
                        if number > selectedBatteries[index]:
                            selectedBatteries[index] = number
                            pointer = index2+1
                            # print(f"  index: {index} pointer: {pointer}")
                    
            # print("----------")
        print(f"V2, Selected: {selectedBatteries}")

        for index, batteries in enumerate(selectedBatteries):
            jol += 10**(numberOfBatteries-index-1)*selectedBatteries[index]
        
        print(f"V2: {self.numberArray} > {jol}")
        return jol

    def getMaxJoltage1(self):
        return self.joltage1

    def getMaxJoltage2(self):
        return self.joltage2

# Program:
def process_file(file_path):
    
    combinedMaxJoltage1 = 0
    combinedMaxJoltage2 = 0

    try:
        # Öffnen und Lesen der Datei zeilenweise
        with open(file_path, 'r') as file:
            '''
            first_line = next(file)
            L = first_line.strip()
            bb = batteryBank(L)
            combinedMaxJoltage1 += bb.getMaxJoltage1()
            combinedMaxJoltage2 += bb.getMaxJoltage2()

            '''
            for line in file:
                # Bereinigen der Zeile (Entfernen von Leerzeichen und Zeilenumbrüchen)
                L = line.strip()

                # Überspringen von leeren Zeilen
                if not L:
                    continue

                bb = batteryBank(L)
                combinedMaxJoltage1 += bb.getMaxJoltage1()
                combinedMaxJoltage2 += bb.getMaxJoltage2()
            
    except FileNotFoundError:
        print(f"Fehler: Die Datei '{file_path}' wurde nicht gefunden.")
        return -1 # Rückgabe eines Fehlercodes
    except Exception as e:
        print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")
        return -1
    return [combinedMaxJoltage1, combinedMaxJoltage2]


start_time = time.perf_counter()
final_result1, final_result2 = process_file("input.txt")
# final_result1, final_result2  = process_file("input_demo.txt")
end_time = time.perf_counter()
print(f"Maximum Joltage Part 1: {final_result1}")
print(f"Maximum Joltage Part 2: {final_result2}")
print(f"Time to find solution: {end_time-start_time}")