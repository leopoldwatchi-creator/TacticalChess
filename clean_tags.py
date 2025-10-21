import re
import os

# Configuration des chemins
# ASSUREZ-VOUS QUE LE NOM DU FICHIER PGN EST CORRECT
input_file = r"C:\Users\natha\Documents\chess1_ULTRA_CLEAN.pgn"
output_file = r"C:\Users\natha\Documents\chess1_FINAL_ANALYSIS.pgn"

# Caractères illégaux pour Windows (et PGN mal formé)
ILLEGAL_CHARS_PATTERN = re.compile(r'[?/\\*:|"<>\[\]\(\)\{\}.]')

def clean_pgn_tags(input_path, output_path):
    print(f"Lecture du fichier : {input_path}")
    with open(input_path, 'r', encoding='utf-8') as infile:
        content = infile.read()

    # Nettoyage : Remplacer les caractères illégaux uniquement dans les balises
    # Une balise PGN commence par [ et contient deux chaînes entre guillemets
    def replace_illegal_chars(match):
        tag_name = match.group(1)
        tag_value = match.group(2)
        # Remplacement des caractères illégaux par un simple tiret ou une lettre
        # On remplace les '?' ou '.' par un 'X' pour les noms, et par '0' pour les dates
        if tag_name.lower() in ['white', 'black', 'event', 'site']:
            cleaned_value = ILLEGAL_CHARS_PATTERN.sub('X', tag_value).strip()
            if not cleaned_value:
                cleaned_value = 'Inconnu'
        elif tag_name.lower() == 'date':
            cleaned_value = ILLEGAL_CHARS_PATTERN.sub('0', tag_value).strip()
            if cleaned_value.startswith('00'):
                 cleaned_value = '2025.01.01' # Date par défaut valide

        return f'[{tag_name} "{cleaned_value}"]'

    # Le regex cherche toutes les balises [Nom "Valeur"]
    cleaned_content = re.sub(r'\[(\w+)\s+"(.*?)"\]', replace_illegal_chars, content, flags=re.DOTALL)

    # Assurez-vous qu'il y a au moins une balise de résultat à la fin de chaque partie
    # (Pour aider pgn-extract à reconnaître la fin de partie si nécessaire)
    cleaned_content = re.sub(r'(]\s*)(1-0|0-1|1/2-1/2|\*)', r'\1\n\n\2', cleaned_content)


    print(f"Écriture du fichier nettoyé : {output_path}")
    with open(output_path, 'w', encoding='utf-8') as outfile:
        outfile.write(cleaned_content)
    print("Nettoyage terminé. Prêt pour l'analyse.")


if __name__ == "__main__":
    # --- VERIFIEZ LE CHEMIN ET LE NOM DE VOTRE FICHIER PGN ENTRÉE ---
    clean_pgn_tags(input_file, output_file)
