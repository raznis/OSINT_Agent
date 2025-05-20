#!/usr/bin/env python
import os
import sys
import warnings

from datetime import datetime

from investigators.crew import Investigators

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# Create output directory if it doesn't exist
os.makedirs('output', exist_ok=True)

def run():
    """
    Run the crew.
    """
    # inputs = {
    #     'target': 'Raz Nissim',
    #     'affiliations': 'Ben Gurion University, General Motors',
    #     # 'current_year': str(datetime.now().year)
    # }

    # inputs = {
    #     'target': 'Avraham Hirschson',
    #     'affiliations': 'Israeli government, Israeli Knesset, Histadrut',
    #     # 'current_year': str(datetime.now().year)
    # }

    # inputs = {
    #     'target': 'Igal Nissim',
    #     'affiliations': 'Comverse, Verint',
    #     # 'current_year': str(datetime.now().year)
    # }

    # inputs = {
    #     'target': 'Yeela Harel',
    #     'affiliations': 'Israel Ministry of Justice, ThetaRay, Bank Of Israel',
    #     # 'current_year': str(datetime.now().year)
    # }

    # inputs = {
    #     'target': 'Yehuda Harel',
    #     'affiliations': 'Hapoalim Bank',
    #     # 'current_year': str(datetime.now().year)
    # }

    inputs = {
        'target': 'Bar Mittelman',
        'affiliations': 'Bitin, crypto',
        # 'current_year': str(datetime.now().year)
    }

    try:
        Investigators().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


