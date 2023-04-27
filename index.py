pip install gradio requests
import gradio as gr

def sum(num1,num2):
  return num1+num2
def sub(num1,num2):
  return num1-num2
inp1=gr.inputs.Number(label="Enter 1st Number:")
inp2=gr.inputs.Number(label="Enter 2nd Number:")
out1=gr.outputs.Textbox(label="Result")
out2=gr.outputs.Textbox(label="Result")

A=gr.Interface(fn=sum,inputs=[inp1,inp2],outputs=out1)
B=gr.Interface(fn=sub,inputs=[inp1,inp2],outputs=out2)
A.launch()
B.launch()