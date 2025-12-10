import re

def process_file(file_path):
    """
    Verarbeitet eine Datei gemäß dem bereitgestellten Pseudocode.

    Args:
        file_path (str): Der Pfad zur zu lesenden Textdatei.

    Returns:
        int: Der berechnete resultCode.
    """
    
    # Initialisierung der Variablen
    resultCode = 0
    pos = 50

    try:
        # Öffnen und Lesen der Datei zeilenweise
        with open(file_path, 'r') as file:
            for line in file:
                # Bereinigen der Zeile (Entfernen von Leerzeichen und Zeilenumbrüchen)
                L = line.strip()
                # print(L + " Position: " + str(pos))

                # Überspringen von leeren Zeilen
                if not L:
                    continue

                # 1. wert.op bestimmen (R -> 1, L -> -1)
                first_char = L[0].upper()
                if first_char == 'R':
                    wert_op = 1
                elif first_char == 'L':
                    wert_op = -1
                else:
                    # Optional: Zeilen ignorieren, die nicht mit R oder L beginnen
                    # print(f"Warnung: Ungültige Zeile übersprungen: {L}")
                    continue

                # 2. wert.val extrahieren (Integer-Zahl im String)
                # re.search sucht nach der ersten Sequenz von einer oder mehreren Ziffern (\d+)
                match = re.search(r'(\d+)', L)
                if match:
                    # Die gefundene Zahl als Integer konvertieren
                    wert_val = int(match.group(1))
                else:
                    # Optional: Zeilen überspringen, wenn keine Zahl gefunden wird
                    # print(f"Warnung: Keine Zahl in Zeile gefunden: {L}")
                    continue
                
                # 3. Modulo-Operation: wert.val %= 100
                wert_val %= 100
                
                # 4. pos aktualisieren: pos = pos + wert.op * wert.val
                pos += wert_op * wert_val
                
                # 5. Randbedingungen für pos prüfen
                if pos < 0:
                    pos += 100
                elif pos > 99:
                    pos -=100
                if pos == 0:
                    resultCode += 1
                    
        return resultCode

    except FileNotFoundError:
        print(f"Fehler: Die Datei '{file_path}' wurde nicht gefunden.")
        return -1 # Rückgabe eines Fehlercodes
    except Exception as e:
        print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")
        return -1

final_result = process_file("day1TestCase.txt")
print(f"Der finale resultCode ist: {final_result}")