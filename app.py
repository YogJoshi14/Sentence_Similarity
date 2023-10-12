import gradio as gr
from flask import Flask, request, jsonify, render_template
from sentence_transformers import SentenceTransformer, util
import os
from part_a import inference
app = Flask(__name__)


@app.route('/', methods=['POST'])
def calculate_similarity():
    try:
        data = request.get_json()
        text1 = data["text1"]
        text2 = data["text2"]

        similarity_score = inference(text1,text2)

        # Prepare the response body
        response_body = {"similarity score": similarity_score}

        return jsonify(response_body), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


with gr.Blocks() as demo:
    gr.Markdown(
    """
    # Sentence Similarity Calculator
    Start typing below to see the output.
    """)
    txt = gr.Textbox(label="Input 1", lines=2)
    txt_2 = gr.Textbox(label="Input 2")
    txt_3 = gr.Textbox(value="", label="Output")
    btn = gr.Button(value="Submit")
    btn.click(inference, inputs=[txt, txt_2], outputs=[txt_3])


# @app.route("/")
# def gradio_interface():
#     return render_template("gradio.html", iface=demo.launch(share=True))

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port= 8080)
    # demo.launch()
    
