
# **PyttoExcel**

Um aplicativo desenvolvido em **Python** utilizando a biblioteca **Flet**, que permite criar e gerenciar planilhas de forma simples e eficiente. O projeto inclui funcionalidades como geração de planilhas, armazenamento em diretórios organizados, e envio direto para o usuário.

## **Sumário**
- [Funcionalidades](#funcionalidades)
- [Pré-requisitos](#pré-requisitos)
- [Como Executar](#como-executar)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)


## **Funcionalidades**
- Interface intuitiva para geração de planilhas personalizadas.
- Organização automática das planilhas em diretórios.
- Suporte para envio das planilhas diretamente ao usuário.
- Compatibilidade multiplataforma (Windows, MacOS, Linux).
- Modo de desenvolvimento com "hot reload" utilizando Flet.

## **Pré-requisitos**
Antes de começar, certifique-se de ter os seguintes itens instalados em sua máquina:
- **Python 3.7 ou superior**
- **Pip** (gerenciador de pacotes do Python)
- **Flet** (instalado via pip)
- Editor de texto ou IDE (recomendado: **Visual Studio Code**)

## **Como Executar**
Siga os passos abaixo para executar o projeto:

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/pyttoexcel.git
   cd pyttoexcel
   ```

2. **Instale as dependências**:
   ```bash
   pip install flet
   ```

3. **Execute o aplicativo**:
   ```bash
   flet run lib/main.py -d -r
   ```

4. O aplicativo será aberto no navegador ou como uma janela independente.

## **Estrutura do Projeto**
```plaintext
pyttoexcel/
├── lib/
│   ├── main.py         # Arquivo principal do aplicativo
│   ├── tela.py         # Gerenciamento da interface do usuário
│   ├── computador.py   # Objeto computador
│   └── __pycache__/    # Arquivos cache gerados automaticamente
├── README.md           # Documentação do projeto
├── requirements.txt    # Dependências do projeto
└── .gitignore          # Arquivos e pastas ignorados pelo Git
```

## **Tecnologias Utilizadas**
- **Python**: Linguagem principal do projeto.
- **Flet**: Biblioteca para criação de interfaces gráficas.


# **InventoryXcel**
**by José Guilherme Neves**

Para o primeiro "run" do app, deve-se definir no arquivo `main` o diretório do dispositivo onde o programa está sendo executado, possibilitando rodar tanto em **PC** quanto em **Android**.

### **Como rodar o código**

- Para rodar o app no seu computador, use:
  ```bash
  flet run lib/main.py
  ```

- Para gerar o código QR e rodar no **Android**, use:
  ```bash
  flet run --android
  ```

- Para gerar o **APK** do app, use:
  ```bash
  flet build apk
  ```
