# Assistente Virtual com Inteligência Artificial para E-commerce

Protótipo de assistente inteligente desenvolvido em Python utilizando arquitetura RAG (Retrieval-Augmented Generation) para automatizar o atendimento de suporte de lojas virtuais.

---

## 1. Documentação (Visão Geral)
* **Objetivo:** Automatizar o atendimento de primeira linha de um e-commerce, respondendo dúvidas frequentes de clientes (prazos, trocas, pagamentos) com agilidade e precisão.
* **Público-alvo:** Consumidores finais de lojas virtuais e operadores de atendimento.
* **Comportamento Esperado:** Cordial, direto, estritamente baseado em dados confiáveis (sem alucinações) e capaz de orientar a pessoa usuária para os próximos passos.

## 2. Base de Conhecimento
Os dados estruturados utilizados pelo assistente encontram-se na pasta `data/`:
* `data/Q&A_Ecommerce.csv`: Arquivo contendo as perguntas frequentes e respostas oficiais da loja virtual, indexadas para busca semântica.

## 3. Prompts e Diretrizes
As instruções de sistema configuradas no pipeline orientam o comportamento da IA via Groq:
> *"Você é um atendente virtual de uma loja de e-commerce. Responda às perguntas dos clientes com base nas informações disponíveis. contexto: {context} pergunta: {pergunta}"*

O modelo é instruído a se basear exclusivamente no contexto recuperado e a admitir quando não possuir informação suficiente.

## 4. Aplicação Funcional
O código-fonte está estruturado no diretório `src/`:
* `src/chat.py`: Aplicação Flask contendo o pipeline de RAG (LangChain + FAISS + HuggingFace Embeddings) e rotas de teste/webhook.
* `src/utils/evolution.py`: Módulo de integração com a Evolution API para disparo de mensagens via WhatsApp[cite: 4].

### Como rodar o projeto localmente:
1. Clone o repositório e instale as dependências:
   ```bash
   pip install -r requirements.txt