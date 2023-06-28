import json
import subprocess
import re


# Leitura do arquivo settings.json
f = open('./settings.json', 'r')
files_settings = json.load(f)




#1. Escrever arquivos da pasta informada para o arquivo output.txt

download_path = "D:\\Downloads"

with open('./download-path-list.txt', 'w') as file:
    result = subprocess.run(["ls", download_path],  stdout=file, text=True)




# 2. Ler linhas do arquivo download-path.txt e formatá-las pro Python


directory_array = ["Documents", "Videos", "Music","Image"]

with open('./download-path-list.txt', 'r') as file:
    
    for raw_text in file:  # while e < 5:
        
        new_text = re.sub(r'\n', "", raw_text)
        inline_file_name = new_text

        temp_text = inline_file_name.split('.')
        extension_file = temp_text[-1]
        

# Comparação e execução de comandos no subprocesso 

        for workDirectory in directory_array:
            
            for i in range(len(files_settings[workDirectory]["extensoes"])):
                extensions = files_settings[workDirectory]["extensoes"][i]

                if extension_file == extensions:
                    #Processement above
                    print(f'\'{inline_file_name}\' matches with .{extensions} from \'{workDirectory}\'')
                    

                    source_path = f"{download_path}\\{inline_file_name}"
                    target_path = files_settings[workDirectory]["path"]  # o problema tá no path
                    

                    command1 = ["pwd"]
                    command2 =  ["cd", "/d", "d:\\"]
                    join_operator = ["&&"]            

                    
                    move_fileSrc_toTarget = ["move", source_path, target_path]
                    
                    # print(move_fileSrc_toTarget)
                    # print(f"move {source_path} {target_path}")
                    
                    
                    child_process = subprocess.run(move_fileSrc_toTarget, shell=True, stderr=subprocess.PIPE)
                    
                    if child_process !=0:
                        print(f"O comando para o arquivo \'{inline_file_name}\'não pôde ser efetuado pelos seguintes motivos:")
                        print("  - Leitura do arquivo não foi feita corretamente. Tente renomeá-lo para algo mais simples.")
                        print("  - O arquivo encontra-se duplicado com a pasta do destino.")
                    
                    

                    print("\n")
                    break
                
                else:
                    continue