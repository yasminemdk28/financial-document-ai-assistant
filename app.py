from pdf_reader import extraire_texte
from llm import poser_question


texte = extraire_texte("documents/rapport.pdf")

question = input("Pose une question sur le document : ")

reponse = poser_question(texte, question)

print("\nRéponse de Gemini :")
print(reponse)