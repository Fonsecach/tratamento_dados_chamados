import re

import pandas as pd
import streamlit as st

st.title('Tratamento da planilha de chamados')
st.write(
    '''Você pode usar esse script para limpar as tags HTML que estão presentes
     na coluna Detalhamento planilha de chamados.'''
)

uploaded_file = st.file_uploader(
    'Insira a planilha de chamados', type=['xlsx']
)

if uploaded_file is not None:
    st.write('Arquivo carregado com sucesso.')

    try:
        df = pd.read_excel(uploaded_file)

        if 'Detalhamento' not in df.columns:
            st.error('Erro: A coluna "Detalhamento" não existe na planilha.')
        else:
            df['Detalhamento'] = df['Detalhamento'].apply(
                lambda x: re.sub('<[^>]+>', '', str(x)) if pd.notna(x) else x
            )

            output_filename = 'helpdesk_tratado.xlsx'
            df.to_excel(output_filename, index=False)

            with open(output_filename, 'rb') as file:
                st.download_button(
                    label='Baixar planilha processada',
                    data=file,
                    file_name=output_filename,
                    mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                )

            st.success(f'Arquivo {output_filename} gerado com sucesso!')

    except Exception as e:
        st.error(f'Erro ao processar o arquivo: {str(e)}')
else:
    st.write('Nenhum arquivo carregado.')
