# Meta regras

O projeto tem objetivo de automatizar um pipeline de aprendizagem de máquina e gerar regras que expliquem o comportamento do modelo diante dos dados de entrada, ajudando a identificar padrões nos dados de entrada que levam a erros de predição do modelo.

## Fluxo da solução

<img width="729" height="799" alt="image" src="https://github.com/user-attachments/assets/59d32f80-1128-4ceb-9982-167f9056810b" />

# Estrutura do Algoritmo

📦 projeto
├── class/
│   └── (lógica do backend)
│
├── pyhard/
│   └── (testes do PyHard)
│
└── resours/dataset/
    └── (dados de entrada)
│
└── main.py                # Arquivo principal de execução

## Diagrama de classes

foto aqui

- **input_data:** Automatiza o ETL: leitura dos dados, análise exploratória, limpeza e abre uma janela com alguns gráficos para demonstrar os dados processados.
- **
