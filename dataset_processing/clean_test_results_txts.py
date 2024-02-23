import os
import re

def clean_test_results_txts(input_folder_path, output_folder_path):
    os.makedirs(output_folder_path, exist_ok=True)
    
    heading_pattern = re.compile(r"Model = (.*)\nChunk Size = (.*)\nChunk Overlap = (.*)\nReranking on = (.*)\n", re.MULTILINE)
    qa_pattern = re.compile(r"QUESTION:\s*\n\s*(.*?)\s*\n\s*CONTEXT:\s*\n(.*?)\s*\n\s*ANSWER:\s*\n\s*(.*?)\s*\n\s*INFERENCE TIME:\s*\n\s*([\d.]+)( seconds)?", re.DOTALL)
    
    for file_name in os.listdir(input_folder_path):
        if file_name.endswith('.txt'):
            input_file_path = os.path.join(input_folder_path, file_name)
            output_file_path = os.path.join(output_folder_path, file_name)
            
            with open(input_file_path, 'r', encoding='utf-8') as infile, open(output_file_path, 'w', encoding='utf-8') as outfile:
                text = infile.read()
                
                heading_match = heading_pattern.search(text)
                if heading_match:
                    outfile.write(heading_match.group(0) + "\n\n\n")
                
                matches = qa_pattern.findall(text)

                for match in matches:
                    question, _, answer, time, unit = match
                    time = float(time)
                    
                    #special case with old formatting of inference time
                    if not unit:
                        time = time * 60
                    time = str(round(time))
                    outfile.write("QUESTION: " + question.strip() + "\n")
                    outfile.write("ANSWER: " + answer.strip() + "\n")
                    outfile.write("INFERENCE_TIME: " + time.strip() + " seconds\n")
                    outfile.write("SCORE: /10\n")
                    outfile.write("\n\n")

input_folder_path = './model_test_results_precleaned'
output_folder_path = './model_test_results_cleaned'

clean_test_results_txts(input_folder_path, output_folder_path)
