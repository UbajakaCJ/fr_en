import gradio as gr
import numpy as np
from transformers import pipeline

pipe = pipeline("translation", model="t5-base")

def translate(text):
    return pipe(text)[0]["translation_text"]

with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column():
            french = gr.Textbox(label="French text")
            translate_btn = gr.Button(value="Translate")
        with gr.Column():
            english = gr.Textbox(label="English text")
            
    translate_btn.click(translate, inputs=french, outputs=english)
    examples = gr.Examples(examples=["Quel age as-tu?", "Dix-neuf"],
                           inputs=[french])
    
demo.launch()