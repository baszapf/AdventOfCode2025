import re
import time

class dial:
    def __init__(self, startingPosition):
        # Position muss im Bereich 0-99 sein
        self.currentPosition = startingPosition % 100 
        self.numberOfClicks = 0

    def rotate (self, turningPrompt):
        match = re.fullmatch(r'[LR](\d+)', turningPrompt)
        
        if match:
            turningVector = 1 # R
            if turningPrompt[0].upper() == 'L':
                turningVector = -1

            # Extrahiert die Zahl direkt aus der Match-Gruppe
            turningSteps = int(match.group(1)) 

            self.updatePosition(turningVector, turningSteps)
        else:
            print(f"Warnung: Ungültige Zeichenkette gefunden: {turningPrompt}")
        
        #print(f"turningPrompt: {turningPrompt}, Pos: {self.currentPosition}, Clicks: {self.numberOfClicks}")
        #print("-----------------------------------")
        return self.currentPosition

    def getResult(self):
        return self.numberOfClicks


    def updatePosition(self, turningVector, turningSteps):

        # Berechnung des Abstands zum Nullpunkt
        distanceToZero = 100-self.currentPosition
        if turningVector == -1:
            distanceToZero = self.currentPosition
        elif self.currentPosition == 0:
            distanceToZero = 0
        # print(f"distanceToZero: {distanceToZero} ({turningVector})")
        
        # Wenn Drehung genau auf den Nullpunkt ohne zus. Nulldurchgänge        
        if turningSteps == distanceToZero:
            # print("Case: turningSteps == distanceToZero")
            self.currentPosition = 0
            self.numberOfClicks += 1

        # Wenn kein Nulldurchgang
        elif turningSteps < distanceToZero:
            # print("Case: turningSteps < distanceToZero")
            self.currentPosition = self.currentPosition + turningVector * turningSteps

        else: # Wenn 1 oder mehr Nulldurchgänge (bei turningSteps > distanceToZero)
            # print("Case: turningSteps > distanceToZero")
            clicksCount = 0

            clicksCount += (turningSteps-distanceToZero)//100
            
            if self.currentPosition!=0:
                clicksCount += 1

            absolutePosition = self.currentPosition + turningVector * turningSteps
            self.currentPosition = absolutePosition%100
            # print(f"absolutePosition: {absolutePosition}")

            self.numberOfClicks += clicksCount
                    
        return self.currentPosition

# Program:
def process_file(file_path):
    """
    Verarbeitet eine Datei gemäß dem bereitgestellten Pseudocode.

    Args:
        file_path (str): Der Pfad zur zu lesenden Textdatei.

    Returns:
        int: Der berechnete resultCode.
    """
    secretEntranceDial = dial(50) # Startposition 50

    try:
        # Öffnen und Lesen der Datei zeilenweise
        with open(file_path, 'r') as file:
            for line in file:
                # Bereinigen der Zeile (Entfernen von Leerzeichen und Zeilenumbrüchen)
                L = line.strip()

                # Überspringen von leeren Zeilen
                if not L:
                    continue

                secretEntranceDial.rotate(L)
    except FileNotFoundError:
        print(f"Fehler: Die Datei '{file_path}' wurde nicht gefunden.")
        return -1 # Rückgabe eines Fehlercodes
    except Exception as e:
        print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")
        return -1
    return secretEntranceDial.getResult()

start_time = time.perf_counter()
final_result = process_file("input.txt") # Correct result 6379
# final_result = process_file("inputTestCase.txt")
end_time = time.perf_counter()
print(f"Number of clicks: {final_result}")
print(f"Time to find solution: {end_time-start_time}")