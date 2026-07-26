# Chatbot de FAQ para E-commerce (Python)

Um chatbot de perguntas frequentes (FAQ) simulando o atendimento de um e-commerce.

## Qual foi a ideia?

O objetivo principal deste projeto foi desenvolver minhas habilidades de programação em Python, entregando uma aplicação interessante e funcional para um trabalho da faculdade.

Durante a pesquisa de viabilidade, encontrei um [tutorial do AntonnyMendonca2 no YouTube](https://youtu.be/eVnCa5wuwdU?si=cM-ohL9EmMCtOgh8), que serviu como base estrutural. A partir dele, consegui adaptar e implementar exatamente o que eu precisava para a apresentação do projeto.

---

## O que absorvi desse projeto?

Mais do que apenas escrever código, este projeto foi uma grande escola sobre planejamento, ferramentas e visão de mercado. Abaixo, compartilho os principais desafios e aprendizados práticos.

### 1. Pesquisa vs. Tentativa e Erro

- **Gerenciamento de Tokens e Custos:** No início, sofri bastante com o esgotamento rápido de tokens da IA, o que dificultava os testes. Aprendi na prática que sair codando na "tentativa e erro" não funciona. É essencial pesquisar e analisar previamente quais APIs oferecem o melhor custo-benefício. Saber planejar evita o desperdício de recursos e tempo.
- **Bugs Inesperados no WhatsApp:** Como faltou um planejamento mais profundo inicialmente, acabei enfrentando um vazamento de mensagens. O bot, que estava rodando no meu número pessoal para testes, acabou lendo mensagens de grupos e respondendo tanto nos grupos quanto no privado das pessoas.
  - _Como resolvi:_ Configurei a Evolution API para ignorar grupos e fiz um ajuste provisório no código para que o bot respondesse apenas a um número específico. Reconheço que foi uma medida paliativa (um "band-aid" no código), mas me ensinou a importância de prever o escopo da aplicação.

**A lição que fica:** Ter uma visão limpa e estratégica antes de começar é o que permite transformar um simples projeto de faculdade em uma solução real, escalável e relevante para o portfólio.

### 2. O Ecossistema e Novas Ferramentas

Como eu estava apenas no meu terceiro semestre, este projeto marcou meu primeiro contato com tecnologias que são padrão na indústria, como:

- **Docker:** Entendi na prática por que a conteinerização é tão vital.
- **Redis & Caching:** Descobri a necessidade do uso de cache para gerenciar o estado da conversa (memória de curto prazo) e aliviar queries pesadas.
- **Evolution API:** Compreendi como integrar sistemas de mensageria com o código.

Ver todas essas peças funcionando juntas me abriu os olhos. A partir desse projeto, parei de apenas "usar coisas prontas" e passei a estudar o _porquê_ e _como_ as ferramentas funcionam por trás dos panos.

### 3. Python vs. Ferramentas No-Code/Low-Code

Ao finalizar a aplicação, cheguei a uma conclusão muito importante sobre arquitetura de soluções: para um projeto real de mercado focado apenas na entrega rápida deste tipo de chatbot, utilizar uma ferramenta como o **n8n** teria sido um caminho muito mais simples, prático e lógico.

No entanto, me forcei a construir tudo na "unha" com **Python** pelo desafio técnico e pela experiência de aprendizado — o que valeu muito a pena. Hoje, tenho a consciência necessária para escolher a ferramenta certa dependendo do prazo e do objetivo de negócio.
