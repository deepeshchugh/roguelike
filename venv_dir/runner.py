
import os
 
def list_files_recursive(path='.'):
    entry_list = []
    extra_list = []
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            extra_list = extra_list + list_files_recursive(full_path)
        elif full_path.endswith(".py"):
            if "\\Lib\\" not in full_path:
                entry_list.append(("roguelike" + full_path[1:]).replace('\\','/'))
    return entry_list + extra_list

file_list = list_files_recursive()
for file in file_list:
    print("\\lstinputlisting[caption=" + file.replace("_", "{\\textunderscore}") + ",language=Python, breaklines=true]{final_report/src/" + file +"}")
