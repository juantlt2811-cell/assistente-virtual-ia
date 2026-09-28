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

current_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(current_dir, '..', 'data', 'Q&A_Ecommerce.csv')

current_dir = os.path.dirname(os.path.abspath(__file__))
dotenv_path = os.path.join(current_dir, '..', '.env')
load_dotenv(dotenv_path=dotenv_path)
app = flask.Flask(__name__)
client = ChatGroq(model="openai/gpt-oss-20b")
e = EvolutionAPI()
loader = CSVLoader(file_path=csv_path)
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    print("❌ ATENÇÃO: GROQ_API_KEY não foi encontrada! Verifique o arquivo .env na raiz.")
else:
    print("✅ Chave da Groq carregada com sucesso!")

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

llm = ChatGroq(model="openai/gpt-oss-20b", api_key=os.getenv("GROQ_API_KEY"))  

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

@app.route('/teste', methods=['POST'])
def teste():
    # Tenta pegar o JSON de forma segura
    data = flask.request.get_json(silent=True)
    
    if not data or 'pergunta' not in data:
        return flask.jsonify({
            "erro": "Formato inválido. Envie um JSON no formato: {\"pergunta\": \"Sua dúvida aqui\"}"
        }), 400
        
    pergunta = data.get('pergunta', '')
    
    try:
        chain = get_chain()
        message = chain.invoke(pergunta)
        return flask.jsonify({
            "pergunta": pergunta,
            "resposta": message.content
        })
    except Exception as e:
        return flask.jsonify({"erro": str(e)}), 500

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