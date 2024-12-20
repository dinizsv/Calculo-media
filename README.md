# Cálculo da Média dos Valores Obtidos de Arquivo Compactado.

# Descrição
Este script tem como objetivo realizar cálculos de média de valores obtidos de uma base de dados `data.txt` compactada em arquivo `.zip`. Sua construção foi realizada utilizando Python.


## Autor
Everton Diniz Silva

## Data de Criação
30/11/2024

## Versão

1.0

## Instrução de Instalação.

### Pré-Requisitos.
Para executar o script `main.py`, será necessário que o ambiente tenha os seguintes pré-requisitos:

- `Python 3.11.3` ou superior.
Verifique a versão do python utilizando o seguinte comando no terminal ou prompt de comando.

```bash
python --version
```

### Biblioteca Necessária.
Este script utiliza as seguintes bibliotecas:

- `zipfile`: Para manipulação de arquivos ZIP.
- `pathlib`: Para trabalhar com caminhos de arquivos e diretórios.
- `numpy`: Para calcular a média dos números extraídos dos dados.

As bibliotecas `zipfile` e `pathlib` são nativas do python, porém, a biblioteca 
`numpy` deve ser instalada caso não exista. 
Instale através do terminal utilizando o seguinte script:

```bash
pip install numpy
```

## Instrução de Uso:

- Certifique-se de ter o arquivo `.zip` contendo o arquivo `data.txt` dentro do diretório `base_dados` do projeto.
- Execute o script `main.py` em seu ambiente Python.
- O script irá descompactar o arquivo ZIP, ler o conteúdo do arquivo `data.txt`, processar os dados, calcular a média e exibir os resultados no terminal.


## Estrutura do Código:
### - Importação das Bibliotecas:

```bash
import zipfile
from pathlib import Path
import numpy as np

```
O código utiliza três bibliotecas essenciais:

- `zipfile`: Para manipulação de arquivos ZIP.
- `pathlib`: Para trabalhar com caminhos de arquivos e diretórios.
- `numpy`: Para calcular a média dos números extraídos dos dados.

### - Variaveis Utilizadas:

```bash
#Variáveis Globais:
ListaDeDados = []
DadosIncompatíveis = []

```
- `ListaDeDados` é uma variável do tipo lista que irá armazenar todos os dados obtidos do tipo númerico.
- `DadosIncompatíveis`é uma variável que armazena outros dados que são incompatíveis para os cálculos da média.

### Caminho de Arquivos e Pasta:

```bash
#Definir caminho da pasta e do arquivo:
CaminhoArquivo = Path(__file__).parent /'base_dados'/'Arquivo.zip'
CaminhoPasta = Path(__file__).parent /'base_dados'

```
Esta estrutura define o caminho exato onde estão localizados os arquivos e pastas utilizados para análise dos dados.

- `CaminhoArquivo` variável que determina o caminho do arquivo `.zip`
- `CaminhoPasta` variável armazena o caminho da pasta onde deverá estar o arquivo `.zip`

### Função decompactar_dado(): 

```bash
#Função para descompactar arquivo e obter dados: 
def decompactar_dado():

    #Decompactar arquivo .zip:
    with zipfile.ZipFile(f'{CaminhoArquivo}', 'r') as ArquivoZip:    
        arquivos = ArquivoZip.namelist()
        
        #Interar sobre os arquivos existente e selecionar o arquivo de interesse:
        for arquivo in arquivos:

            if arquivo ==  'data.txt':
                DadosTxt = arquivo
            
                #Abrir dados disponiveis em arquivo txt:
                DadosEmBytes = ArquivoZip.read(DadosTxt)

                #formatar e listar dados:
                DadosForm = DadosEmBytes.decode("utf-8").split(" ")

                return DadosForm   

            else:
                print(f'Arquivo "data.txt" não foi encontrado em: " {CaminhoPasta} "')  
                return 'ARQUIVO NÃO ENCONTRADO' 
           
```
- O código descompacta o arquivo `.zip` localizado na pasta `base_dados` e, caso encontre o arquivo `data.txt`, ele formata os dados através da variável `DadosForm` e, em seguida, retorna-os na chamada da função.

- Caso o código não encontre o arquivo `data.txt` será exibida a seguinte mensagem no terminal:

```bash
Arquivo "data.txt" não foi encontrado em: "NOME DA PASTA DE ORIGEM DO ARQUIVO"
```


### Função listar_dados(dado):

```bash
#Função para obter lista com os dados formatados e calcular a média dos valores obtidos: 
def listar_dados(dado):

    #Interar sobre os dados obtidos e acrescentar em uma lista no fomato numérico inteiro:
    for d in dado:
        #Atribuir dado numérico em lista:
        if d.isnumeric():
            ListaDeDados.append(int(d))

        #Dados incompatíveis:
        else:
            DadosIncompatíveis.append(d)  

    #Calcular média dos valores da lista:
    MédiaDados = f'{np.mean(ListaDeDados).tolist():.6f}'
   
    #Retornar resultados da função:
    return MédiaDados, len(ListaDeDados), DadosIncompatíveis  
```
- O código realiza uma interação sobre todos os dados que estão contidos na variável de formato lista `dado`, em seguida avalia se o dado em questão 
é do formato numérico. Se verdadeiro, o valor é convertido e acrescentado a `ListaDeDados`, caso contrário, acrescenta o mesmo a lista `DadosIncompatíveis`.

- Após processar todos os dados, é calculada a média dos valores na lista `ListaDeDados` usando a função `np.mean()` da biblioteca `numpy`.

- O valor da média é formatado com três casa decimais e a função retorna a média dos dados formatados, total de dados presentes na `ListaDeDados` e a lista de
 dados incompatíveis. 


 ## Execução das Funções e Apresentação dos Resultados:

 ```bash
#Chamadas das funções: 

DadoForm = decompactar_dado()

if DadoForm != 'ARQUIVO NÃO ENCONTRADO':

    media = listar_dados(DadoForm)

    #Apresentação dos resultados:

    texto = 'Calculo da média dos valores obtido atravéz do arquivo data.txt:'

    print(f'{"-"*len(texto)}{"-"*5}')
    print(f'\n{texto}\n')
    print(f'Total de valores existente: {media[1]} ')
    print(f'Média calculada: {media[0]} ')
    print(f'Dados incompativeis para os calculos: {media[2]}\n')
    print(f'{"-"*len(texto)}{"-"*5}')

 ```

 - A função `decompactar_dado()` é chamada e atrelada a variável `DadoForm`, em
 seguida, é avaliado a resposta desta chamada. Caso seja diferente de "ARQUIVO NÃO ENCONTRADO" o script continua a execução chamando a função `listar_dados(DadoForm)` passando a variável `DadoForm`. Em seguida apresenta os resultados :

 ```bash
---------------------------------------------------------------------

Calculo da média dos valores obtido atravéz do arquivo data.txt:

Total de valores existente: 2999995 
Média calculada: 500.625930 
Dados incompativeis para os calculos: ['a', 'b', 'u', 'x', 'e', '']

---------------------------------------------------------------------
 ```

# Conclusão
Este script foi desenvolvido com o objetivo de descompactar e processar um arquivo de texto `data.txt` dentro de um arquivo `.zip`. O código calcula a média dos números contidos no arquivo e lida com dados inválidos de forma eficaz.
É uma solução simples e eficiente para manipulação e cálculo de dados numéricos extraídos de arquivos compactados.