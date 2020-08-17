import os

search = "document"
replace = "file"
type_filter = ".py"
 
dir_content = os.listdir('.')
docs = [doc for doc in dir_content if os.path.isfile(doc)]
renamed = 0

print(f"{len(docs)} of {len(dir_content)} elements are files.")

for doc in docs:

    doc_name, filetype = os.path.splitext(doc)

    if filetype == type_filter:
             
        if search in doc_name:
            new_name = doc_name.replace(search, replace) + filetype
            os.rename(doc, new_name)
            renamed += 1
            print(f"Renamed file {doc} to {new_name}")

print(f"Renamed {renamed} of {len(docs)}")