
import gradio as gr

def processar_dados(texto, numero, imagem, lista_texto, cor, opcoes):
    texto_revertido = texto[::-1]
    dobro_numero = numero * 2
    mensagem_imagem = 'Imagem recebida!' if imagem is not None else 'Não ha imagem recebida'

    lista_processada = [[item] for item in lista_texto.splitlines()] if lista_texto else []

    return(
        texto_revertido,
        dobro_numero,
        mensagem_imagem,
        lista_processada,
        f'Cor selecionada: {cor}',
        opcoes
    )

iface = gr.Interface(
    fn=processar_dados,
    inputs=[
        gr.Textbox(label='Texto', placeholder='Digite um texto aqui...'),
        gr.Slider(minimum=0, maximum=100, label='Numero', value=0),
        gr.Image(type='pil', label='Imagem'),
        gr.Textbox(label='Lista de itens', lines=4, placeholder='Item1\nItem2'),
        gr.ColorPicker(label='Escolha uma cor'),
        gr.CheckboxGroup(
            choices=['Opção 1', 'Opção 2', 'Opção 3'],
            label='Escolha suas opções'
        )
    ],
    outputs=[
        gr.Textbox(label='Texto revertido'),
        gr.Number(label='Dobro do numero'),
        gr.Textbox(label='Status da imagem'),
        gr.Dataframe(headers=['Itens'], label='Itens da lista'),
        gr.Textbox(label='Cor selecionada'),
        gr.Textbox(label='Opções selecionadas')
    ],
    title='Verificador de entrada e saída',
    description='Insira um texto, um numero, uma imagem e uma lista de itens, uma cor e opções para ver como a entrada é processada'
)

iface.launch()
