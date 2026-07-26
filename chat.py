import flask
import requests
import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import CSVLoader
from langchain_core.runnables import RunnablePassthrough
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from utils.evolution import EvolutionAPI


load_dotenv()
app = flask.Flask(__name__)
client = ChatGroq(model="llama-3.1-8b-instant")  
e = EvolutionAPI()
loader = CSVLoader(file_path='Q&A_Ecommerce.csv')

# Lazy loading dos embeddings para evitar travamento do debugger
embeddings = None
documents = None
vector_store = None
retrival = None

def initialize_embeddings():
    """Inicializa embeddings e vector store sob demanda"""
    global embeddings, documents, vector_store, retrival
    if embeddings is None:
        print("Carregando embeddings...")
        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        print("Carregando documentos...")
        documents = loader.load()
        print("Criando vector store...")
        vector_store = FAISS.from_documents(documents, embeddings)
        retrival = vector_store.as_retriever()
        print("Embeddings carregados com sucesso!")

llm = ChatGroq(model="llama-3.1-8b-instant", api_key=os.getenv("GROQ_API_KEY"))  

template = "Você é um atendente virtual de uma loja de e-commerce. Responda às perguntas dos clientes com base nas informações disponíveis. contexto: {context} pergunta: {pergunta}"
prompt = ChatPromptTemplate.from_template(template)

def get_chain():
    """Retorna a chain, inicializando embeddings se necessário"""
    initialize_embeddings()
    return (
         {"context": retrival, "pergunta": RunnablePassthrough()}
         | prompt
         | llm 
    ) 



@app.route('/webhook', methods=['POST'])
def webhook():
     remoteAmigo = 'Coloque o número que servirá pra teste aqui'
     data = flask.request.json  
     instance = data['instance']
     apikey = data['apikey']
     sender_number = data ['data']['key']['remoteJid'].split('@')[0]
     chain = get_chain()  # Inicializa embeddings se necessário
     message = chain.invoke(data['data']['message']['conversation'])
     if sender_number == remoteAmigo:
          e.enviar_mensagem(instance, apikey, sender_number, message.content)
          return flask.jsonify(message.content)
     
if __name__ == '__main__':
    app.run(port=5000)