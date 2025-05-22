import gradio as gr
from investigators.src.investigators.crew import Investigators

def investigate(target_name, affiliations, progress=gr.Progress()):
    inputs = {
        'target': target_name,
        'affiliations': affiliations,
    # 'current_year': str(datetime.now().year)
    }
    progress(0.1, desc=f"Created AI Crew and launched investigation of {target_name}..")
    try:
        investigators = Investigators(progress)
        crew_output = investigators.crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")
    
    return crew_output.raw


def clear_inputs():
    return "", ""
    
with gr.Blocks() as view:
    gr.Markdown("# OSINT Investigator")
    gr.Markdown("#### Enter the name of your target and their affiliations (to make search easier), and get a AML Risk assessment based on their public information.")
    with gr.Row(equal_height=True):
        with gr.Column(scale=3):
            name_input = gr.Textbox(label="Target name:")
            affiliation_input = gr.Textbox(label="Target Affiliations (comma separated):")
            with gr.Row():
                clear_btn = gr.Button("Clear")
                submit_btn = gr.Button("Investigate")
        with gr.Column(scale=1):
            img1 = gr.Image("images/logo1.png", show_download_button=False, show_fullscreen_button=False, show_label=False, show_share_button=False)
        
    
    with gr.Row():
        output = gr.Markdown(label="Risk Assessment Report:", container=True, show_copy_button=True, min_height=50)
    
    submit_btn.click(
        fn=investigate, 
        inputs=[name_input, affiliation_input],
        outputs=output
    )
    
    clear_btn.click(
        fn=clear_inputs,
        inputs=[],
        outputs=[name_input, affiliation_input]
    )
    gr.Examples(
        examples=[["Raz Nissim", "Ben Gurion University, General Motors"],
                  ["Mohammed Mosharref Hossain", "Albany"], 
                  ["Giovanni Cazzetta", "Montreal"],
                  ["Willy Bokonga", "Congo"],
                  ["Avraham Hirshzon", "Israel, Politician"],
            ],
        inputs=[name_input, affiliation_input]
    )

view.launch(inbrowser=True)