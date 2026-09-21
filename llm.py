import os

from dotenv import load_dotenv
from google import genai


load_dotenv()

cle_api = os.getenv("GEMINI_API_KEY")

if not cle_api:
    raise RuntimeError("La clé GEMINI_API_KEY est absente du fichier .env.")

client = genai.Client(api_key=cle_api)


def poser_question(texte_document: str, question: str) -> str:
    prompt = f"""
Tu es un assistant spécialisé dans l'analyse de documents financiers.

Réponds uniquement à partir du document fourni.
Si la réponse n'apparaît pas dans le document, indique :
"Cette information n'est pas présente dans le document."

DOCUMENT :
{texte_document}

QUESTION :
{question}
"""

    reponse = client.interactions.create(
        model="gemini-3.8-flash",
        input=prompt
    )

    return reponse.output_text