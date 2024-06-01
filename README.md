# Criando um Sistema Bancário com Python

## Versão I
Nessa primeira versão do desafio devemos implementar apenas três operações: depósito saque e extrato.

### Operação de depósito 
No sistema, deve ser possível depositar valores positivos para uma conta bancária.
Nesta primeira versão vamos nos preocupar apenas com um usuário. 
Dessa forma não precisamos nos preocupar em identificar qual é o número de agência e conta bancária.
Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.

### Operação de saque 
O sistema deve permitir realizar três saques diários com limite máximo de R$ 500 por saque.
Ccaso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro. 
Todos os saques devem ser armazenados em uma variável e exibidas na operação de extrato.

### Operação de extrato 
Essa operação deve listar todos os depósitos de saques realizados na conta.
No fim da listagem, deve ser exibido o saldo atual da conta.
Se o extrato estiver em branco exibir uma mensagem informando que não foram realizadas movimentações.
Os valores devem ser exibidos utilizando o formato **R$ xxxx.xx**

### Considerações
Utilizei a importação da biblioteca "os", para permitir realizar a limpeza na tela entre cada movimentação de depósito, saque ou visualização do extrato.
Após cada movimentação, sendo ela efetuada com sucesso ou apresentando algum erro, o usuário deve acionar a tecla "ENTER" para prosseguir até o menu novamente. Isso permite ao usuário verificar se sua movimentação ocorreu normalmente ou se houve algum erro.


## Versão II
Para a segunda versão, criei um novo arquivo para comparação com a primeira versão. 

Nesse novo arquivo ainda temos as opções do Menu da versão I e a adição de novas opções de nível superior:

    - Cadastrar Cliente
    - Listar Clientes
    - Excluir Cliente 
    - Cadastrar Conta Corrente
    - Listar Contas Correntes
    - Excluir Conta Correte

Foram criadas mais funcionalidades para melhorar a experiência e o aprendizado com funções em Python.


Utilizando a modularização, implementei as funções no arquivo chamado "operacoes.py" e as configurações das variáveis com escopo global, foram realocadas para o arquivo "config.py".
Para que os dados dos clientes não fossem apagados após o encerramento da aplicação, realizei a persistência dos dados em um arquivo de extensão "clientes_contas.json", sendo essa extensão de arquivo muito utilizada para o registro de informações na web.

Tenho conciência que este arquivo não deve ser adicionado ao meu reposótirio por se tratar de dados sensíveis. Ao executar o programa, o arquivo será criado sem dados e você mesmo poderá criar dados fictícios para verificar as funcionalidades do programa.

## Versão III
Para o segundo desafio, a missão é atualizar a implementação do sistema bancário, para armazenar os dados de clientes e contas bancárias em objetos ao invés de dicionários.
Após concluir a modelagem das classes e a criação dos métodos, atualizei os métodos que tratam as opções do menu, para funcionarem com as classes modeladas.

