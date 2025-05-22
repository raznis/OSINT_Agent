#!/bin/bash


    if [ -d "output" ]; then
        rm -rf output
        echo "Cleaned main output directory"
    else
        echo "Main output directory does not exist"
    fi

    # Clear investigators output directory
    if [ -d "investigators/output" ]; then
        rm -rf investigators/output
        echo "Cleaned investigators output directory"
    else
        echo "Investigators output directory does not exist"
    fi

    rm -rf search_results_*
    echo "Output directories and search logs are cleaned"
