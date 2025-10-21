import re
import os

input_file = r"C:\Users\natha\Documents\chess1_ULTRA_CLEAN.pgn"
output_file = r"C:\Users\natha\Documents\chess1_FINAL_ANALYSIS.pgn"

# Caractères illégaux à remplacer par un X
ILLEGAL_CHARS_PATTERN = re.compile(r'[?/\\*:|"<>\[\]\(\)\{\}.]')

def clean_pgn_tags(input_path, output_path):
    print(f"Lecture du fichier : {input_path}")
    with open(input_path, 'r', encoding='utf-8') as infile:
        content = infile.read()

# Dans C:\Users\natha\Chess-Tactic-Finder\clean_tags.py

def replace_illegal_chars(match):
    tag_name = match.group(1)
    tag_value = match.group(2)
    cleaned_value = tag_value  # Valeur par défaut

    # Nettoyage : Remplacer les caractères illégaux uniquement dans les balises
    if tag_name.lower() in ['white', 'black', 'event', 'site', 'date']:
        # Nettoyage agressif de tous les caractères illégaux pour Windows
        cleaned_value = ILLEGAL_CHARS_PATTERN.sub('X', tag_value).strip()
        
        # S'il reste une valeur vide ou une valeur purement illégale, mettez une valeur par défaut sûre
        if not cleaned_value or cleaned_value.strip('X0') == '':
            if tag_name.lower() == 'date':
                cleaned_value = '20250101' # Format date sans points
            else:
                cleaned_value = 'Inconnu'
    
    return f'[{tag_name} "{cleaned_value}"]'

    # Remplacez les balises PGN
    cleaned_content = re.sub(r'\[(\w+)\s+"(.*?)"\]', replace_illegal_chars, content, flags=re.DOTALL)

    print(f"Écriture du fichier nettoyé : {output_path}")
    with open(output_path, 'w', encoding='utf-8') as outfile:
        outfile.write(cleaned_content)
    print("Nettoyage terminé. Prêt pour l'analyse.")

if __name__ == "__main__":
    clean_pgn_tags(input_file, output_file)
