# Criando um Sistema Bancário com Python
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

