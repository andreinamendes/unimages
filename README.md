# Repositório Unimages

Repositório voltado a todas as informações do projeto da disciplina de Engenharia de Software ministrada pelo professor Camilo Almendra.

Equipe:  
[Andreina Mendes](https://github.com/andreinamendes)  
[Elano Nunes](https://github.com/elanonc)  
[João Victor Aquino](https://github.com/jvac99)  
[Mariana Oliveira](https://github.com/marianaoliveira1)  
[Roberto Coutinho](https://github.com/RobertoCoutinho)

## Detalhes do projeto escolhido

No contexto social vigente, a internet conta com inúmeros bancos, não somente de imagens, como também vetores, templates e outros inúmeros elementos associados ao design. Contudo, muitas vezes encontram-se limitações pela necessidade de assinar um plano do site ou pagar pelo produto para ter acesso ao que deseja, o que pode não ser possível considerando a realidade socioeconômica de muitos alunos. Pensando nisso, nota-se que há uma necessidade de um banco de imagem que esteja disponível para alunos, mas que mantenha o suporte financeiro para os artistas parceiros.

O sistema escolhido como projeto final, denominado Unimages, é a criação de um banco de imagens que possa auxiliar estudantes, onde os mesmos terão acesso ao conteúdo pago após uma comprovação de sua relação com a instituição.

Para  mais detalhes sobre o projeto fica a disposição o [Documento de Visão](https://github.com/andreinamendes/unimages/blob/main/docs/Unimages.pdf), contendo a descrição da problemática, personas, requisitos e etc.

## Especificação de requisitos

Os requisitos foram organizados na ferramenta de gerenciamento de tarefas Trello. Abaixo segue o link do quadro criado, e nele, especificado cada história de usuário com seus respectivos testes.

Link: <https://trello.com/invite/b/7JqyV2FX/0ca68abd02cd901cf91ca74aa6979426/unimages>

### Requisitos Funcionais

- [Hist-1] Como usuário comum, eu gostaria de realizar um cadastro no sistema
- [Hist-2] Como usuário comum, eu gostaria de realizar login
- [Hist-3] Como usuário comum, eu gostaria de realizar logout
- [Hist-4] Como usuário comum, eu gostaria de visualizar as fotos disponíveis
- [Hist-5] Como usuário comum, eu gostaria de saber o preço de uma imagem
- [Hist-6] Como usuário comum, eu gostaria de ver as resoluções disponíveis para uma imagem
- [Hist-7] Como usuário comum, eu gostaria de ver se uma imagem é gratuita
- [Hist-8] Como usuário comum, eu gostaria de ver quais planos estão disponíveis
- [Hist-9] Como usuário comum, eu gostaria de ver o perfil de outros usuários
- [Hist-10] Como criador de conteúdo, eu gostaria de realizar o upload de uma imagem no sistema
- [Hist-11] Como criador de conteúdo, eu gostaria de inserir os dados equivalentes a uma imagem associada a minha conta
- [Hist-12] Como criador de conteúdo, eu gostaria de atualizar os dados equivalentes a uma imagem associada a minha conta
- [Hist-13] Como criador de conteúdo, eu gostaria de remover uma imagem  associada a minha conta do sistema
- [Hist-14] Como usuário comum, eu gostaria de compartilhar imagens gratuitas
- [Hist-15] Como usuário comum, eu gostaria de baixar imagens gratuitas
- [Hist-16] Como usuário comum, eu gostaria de buscar por usuários
- [Hist-17] Como usuário comum, eu gostaria de filtrar as imagens por categoria
- [Hist-18] Como usuário comum, eu gostaria de filtrar as imagens por nome
- [Hist-19] Como usuário comum, eu gostaria de filtrar as imagens por formato
- [Hist-20] Como usuário comum, eu gostaria de filtrar as imagens por descrição
- [Hist-21] Como usuário comum, eu gostaria de marcar uma imagem como favorito
- [Hist-22] Como usuário, comum, eu gostaria de demarcar uma imagem dos meus favoritos
- [Hist-23] Como usuário comum, eu gostaria de realizar uma assinatura premium
- [Hist-24] Como usuário comum, gostaria de realizar uma assinatura de um plano universitário por meio da confirmação de vínculo institucional
- [Hist-25] Como usuário assinante, eu gostaria de cancelar a minha assinatura
- [Hist-26] Como usuário assinante, eu gostaria de mudar a forma de pagamento da minha assinatura
- [Hist-27] Como usuário assinante, eu gostaria de alterar a minha assinatura vigente
- [Hist-28] Como usuário assinante, eu gostaria de renovar a minha assinatura vigente
- [Hist-29] Como usuário assinante, eu gostaria de cancelar a minha assinatura
- [Hist-30] Como aluno assinante, eu gostaria de renovar minha assinatura com os meus dados acadêmicos

### Requisitos Não-Funcionais

- Usabilidade
  - [RNF-1] Como usuário comum, gostaria que o sistema se adaptasse aos diferentes dispositivos que eu possa utilizar para acessar.
- Desempenho
  - [RNF-2] Como usuário comum, eu gostaria de realizar o que estiver dentro da minha necessidade atual ao acessar o sistema.
  - [RNF-3] Como usuário comum, eu gostaria que o sistema não tivesse travamentos.
  - [RNF-4] Como usuário com um, eu gostaria que o sistema não demorasse muito para executar o que quero.
- Segurança
  - [RNF-5] Como usuário comum, eu gostaria de ter os meus dados de acesso seguros.
  - [RNF-6] Como usuário comum, eu gostaria de ter os meus dados de pagamentos seguros.
  - [RNF-7] Como usuário comum, eu gostaria de ter as minhas imagens com direitos autorais reservados, seguras.
- Disponibilidade
  - [RNF-8] Como usuário comum, gostaria de ter acesso às contas de outros usuários para usar como inspiração sempre que eu quiser.
  - [RNF-9] Como usuário comum, gostaria de poder acessar os dados referentes à compra das minhas imagens sempre que eu quiser.
  - [RNF-10] Como usuário comum, gostaria de poder acessar a listagem de imagens sempre que eu precisar.

## Modelagem Entidade Relacionamento

Os requisitos especificados anteriormente assim como os dados padrão para usuários utilizados no desenvolvimento de softwares foram considerados para o desenvolvimento do Modelo Entidade Relacionamento especificado abaixo.  
O mesmo contém a listagem dos atributos assim como seus valores e se são chaves primárias, estrangeiras ou os dois. As ligações estão especificadas por setas diferenciadas representando assim as ligações (1, n), (n, 1) e (n, n).

![](https://github.com/andreinamendes/unimages/blob/main/docs/ModeloER.jpeg)
<<<<<<< HEAD

## Desenvolvimento da Aplicação

### Tecnologias utilizadas

- Front-End
  - HTML, CSS e JS
- Back-End
  - Django, python
- Banco de dados
  - SQLite

### Histórias de usuário desenvolvidas

- Simples

  - [Hist-1] Como usuário comum, eu gostaria de realizar um cadastro no sistema
  - [Hist-2] Como usuário comum, eu gostaria de realizar login
  - [Hist-3] Como usuário comum, eu gostaria de realizar logout
  
- Definidas como obrigatórias a serem implementadas

  - [Hist-4] Como usuário comum, eu gostaria de visualizar as fotos disponíveis
  - [Hist-8] Como usuário comum, eu gostaria de ver quais planos estão disponíveis
  - [Hist-10] Como criador de conteúdo, eu gostaria de realizar o upload de uma imagem no sistema
  - [Hist-11] Como criador de conteúdo, eu gostaria de inserir os dados equivalentes a uma imagem associada a minha conta
  - [Hist-17] Como usuário comum, eu gostaria de filtrar as imagens por categoria
  - [Hist-21] Como usuário comum, eu gostaria de marcar uma imagem como favorito
  - [Hist-22] Como usuário, comum, eu gostaria de demarcar uma imagem dos meus favoritos
  - [Hist-23] Como usuário comum, eu gostaria de realizar uma assinatura premium
  - [Hist-24] Como usuário comum, gostaria de realizar uma assinatura de um plano universitário por meio da confirmação de vínculo institucional*
  - [Hist-27] Como usuário assinante, eu gostaria de alterar a minha assinatura vigente
=======
>>>>>>> 934a83b9a9756f445af5e3ddcf744a4a25824309
