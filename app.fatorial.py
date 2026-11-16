import gradio as gr
import math

def fatorial(num):
    if num < 0:
        return 'Fatorial não definido para numeros negativos'
    return str(math.factorial(int(num)))

iface = gr.Interface(
    fn=fatorial,
    inputs='number',
    outputs='text',
    title='Calculadora de Fatorial',
    description='Insira um numero para obter o fatorial'
)

iface.launch()
