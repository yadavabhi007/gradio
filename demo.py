import gradio as gr

def greet(name, intensity):
    return "Hello " * intensity + name + "!"

# demo = gr.Interface(
#     fn=greet,
#     inputs=["text", "slider"],
#     outputs=["text"],
# )

demo = gr.Interface(
    fn=greet,
    inputs=[gr.Textbox(lines=5, placeholder='Write your name'), "slider"],
    outputs=["text"],
    description='This is Demo',
    examples=[['Abhi', 5], ['Abhishek', 6]],
    css="""
        body {background-color: red;}
    """,
    #theme="light"
)

demo.launch(auth=('Abhi', '1234'))
