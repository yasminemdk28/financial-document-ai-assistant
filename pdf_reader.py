from pathlib import Path
from pypdf import PdfReader


def extraire_texte(chemin_pdf: str) -> str:
    fichier = Path(chemin_pdf)

    if not fichier.exists():
        raise FileNotFoundError(f"Le fichier {fichier} est introuvable.")

    lecteur = PdfReader(fichier)
    texte_pages = []

    for page in lecteur.pages:
        texte = page.extract_text()

        if texte:
            texte_pages.append(texte)

    return "\n".join(texte_pages)


if __name__ == "__main__":
    texte = extraire_texte("documents/rapport.pdf")
    print(texte[:2000])