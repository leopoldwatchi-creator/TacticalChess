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

    def replace_illegal_chars(match):
        tag_name = match.group(1)
        tag_value = match.group(2)
        
        # Remplacement universel : nettoie tous les caractères illégaux, même pour les balises inconnues
        cleaned_value = ILLEGAL_CHARS_PATTERN.sub('X', tag_value).strip()
        
        # Si la valeur est vide après nettoyage, mettez une valeur par défaut
        if not cleaned_value:
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
