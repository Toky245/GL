import fitz
import re

def analyze_pdf(file_path):  
    total_masculin = 0
    total_feminin = 0
    niveaux_instruction = {"Primaire": 0, "Secondaire 1er Cycle": 0, "Secondaire 2nd Cycle": 0, 
                           "Licence": 0, "Master": 0, "Doctorat": 0, "Autre": 0}
    
   
    age_counts = {}

    with fitz.open(file_path) as doc:
        for page_num in range(doc.page_count):
            page = doc[page_num]
            text = page.get_text()

          
            total_masculin += text.count("Masculin")
            total_feminin += text.count("Féminin")

            for niveau in niveaux_instruction.keys():
                niveaux_instruction[niveau] += text.count(niveau)

            for line in text.split('\n'):
                if "Q03 : Age" in line:
                    parts = line.split("Q03 : Age")
                    if len(parts) > 1:
                        age_info = parts[1].strip()

                        age_info = re.sub(r"\(.*?\)", "", age_info).strip()

                        if "-" in age_info:
                            age_range = age_info + " ans"
                        else:
                            age_range = age_info + " ans"
                        
                        if age_range in age_counts:
                            age_counts[age_range] += 1
                        else:
                            age_counts[age_range] = 1

    print("Total Masculin:", total_masculin)
    print("Total Féminin:", total_feminin)
    print("Niveaux d'instruction:", niveaux_instruction)
    print("Occurrences d'âges (Q03) :", age_counts)


analyze_pdf("/home/dazai/Documents/script_extract/sodapdf-converted.pdf")
