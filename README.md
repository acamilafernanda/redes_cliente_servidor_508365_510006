# redes_cliente_servidor_508365_510006
Trabalho de Redes de Computadores sobre utilização de Socket, utilizando Python.

Camila Fernanda - 508365 
Mayronn Gomes - 510006

O trabalho possuí duas aplicações: "Cliente" e "Servidor" que se comunicam, onde o cliente faz uma requisição de conexão com o servidor, e ao ser aceito, passa um dado para o mesmo. O servidor, ao receber o valor, realiza uma verificação com este e retorna uma resposta. Após receber a resposta, o cliente fecha a conexão e por fim o servidor fecha também. 

Cliente: 
  O cliente realiza 10 conexões, controladas por meio de um laço de repetição "while".
  A cada conexão, é gerado um número aleatório que pode possuir de 1 até 30 casas decimais.
  O cliente envia o número gerado para o servidor.
  Em seguida, recebe a resposta do servidor e imprime uma mensagem baseada na resposta
  Após isso, o cliente encerra a conexão e dorme por 10 segundas até a próxima interação.

Servidor: 
  O servidor abre uma conexão que atenderá a 10 clientes.
  Se inicia um laço de repetição "while" que receberá a requisição dos clientes individualmente a cada repetição
  Após receber a requisição de conexão, o servidor recebe o valor passado pelo cliente
  Em seguida faz uma verficiação:
    Se o valor possuir mais de 10 casas decimais, o servidor retorna o número em formato de string
    Caso contrário, o servidor verifica e retorna se o valor é ímpar ou par.
  Após receber as dez conexões e responder a todas, o servidor encerra a conexão.
  
  

