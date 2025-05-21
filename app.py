import gradio as gr
from investigators.src.investigators.crew import Investigators

def investigate(target_name, affiliations):
    inputs = {
        'target': target_name,
        'affiliations': affiliations,
    # 'current_year': str(datetime.now().year)
    }

    try:
        crew_output = Investigators().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")
    
    return crew_output.raw

view = gr.Interface(
    fn=investigate,
    inputs=[
        gr.Textbox(label="Target name:"),
        gr.Textbox(label="Target Affiliations (comma separated):")],
    outputs=[gr.Markdown(label="Risk Assessment Report:")],
    flagging_mode="never",
    examples=[
        ["Raz Nissim", "Ben Gurion University, General Motors"],
    ],
    title="OSINT Investigator",
    description="Enter the name of your target and their affiliations (to make search easier), and get a AML Risk assessment based on their public information.",)
view.launch(inbrowser=True)
