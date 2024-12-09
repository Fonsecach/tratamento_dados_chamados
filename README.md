# Tratamento de Dados Helpdesk

## Descrição

Este aplicativo Streamlit permite limpar tags HTML da coluna "Detalhamento" em uma planilha de chamados do helpdesk. O script remove todas as tags HTML, deixando apenas o texto puro.

## Requisitos

- Python 3.13 ou superior
- Dependências listadas no arquivo `pyproject.toml`

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/tratamento-dados-helpdesk.git
cd tratamento-dados-helpdesk
```

2. Configure um ambiente virtual (opcional, mas recomendado):
```bash
uv venv
```

3. Instale as dependências usando `uv`:
```bash
uv sync
```

## Uso

Execute o aplicativo Streamlit:
```bash
uv run streamlit run tratamento.py
```

### Como Usar

1. Abra o aplicativo no navegador
2. Faça upload de um arquivo Excel (.xlsx)
3. O aplicativo processará automaticamente a coluna "Detalhamento"
4. Baixe o arquivo processado com tags HTML removidas

## Funcionalidades

- Remove todas as tags HTML da coluna "Detalhamento"
- Preserva o conteúdo textual original
- Gera um novo arquivo Excel limpo

## Tarefas de Desenvolvimento

Utilize as tarefas definidas no `pyproject.toml`:

- Verificar lint:
```bash
vu run task lint
```

- Formatar código:
```bash
uv run task format
```

- Executar aplicação:
```bash
uv run task run
```

## Dependências

- pandas
- streamlit
- openpyxl

## Deploy

O deploy foi feito com a cloud publica do Streamlit, você pode acessar em:

https://tratamentodadoschamados-c3zcni7hrszwrjsc5njhvp.streamlit.app/



