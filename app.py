from pdf_reader import extraire_texte
from llm import poser_question


texte = extraire_texte("documents/rapport.pdf")

print("Document chargé.")
print("Pose tes questions ou écris 'q' pour quitter.\n")

while True:
    question = input("Question : ").strip()

    if question.lower() == "q":
        print("Fin du programme.")
        break

    if not question:
        print("Écris une question.\n")
        continue

    reponse = poser_question(texte, question)

    print("\nRéponse de Gemini :")
    print(reponse)
    print()