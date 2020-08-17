import os
import argparse

parser = argparse.ArgumentParser(description="Batch rename files in directory")

parser.add_argument("search", type=str, help="Text to be replaced")
parser.add_argument("replace", type=str, help="Replacement text")
parser.add_argument(
    "--path",
    type=str,
    default=".",
    help="Directory path that contains the to be renamed files"
)
parser.add_argument(
    "--filetype",
    type=str,
    default=None,
    help="Only files with the given type will be renamed (e.g. .txt)"
)

args = parser.parse_args()
print(args)

search = args.search
replace = args.replace
type_filter = args.filetype
path = args.path

print(f"Renaming files at path {path}")
 
dir_content = os.listdir(path)
path_dir_content = [os.path.join(path, doc) for doc in dir_content]
docs = [doc for doc in path_dir_content if os.path.isfile(doc)]
renamed = 0

print(f"{len(docs)} of {len(dir_content)} elements are files.")

for doc in docs:

    full_doc_path, filetype = os.path.splitext(doc)
    doc_path = os.path.dirname(full_doc_path)
    doc_name = os.path.basename(full_doc_path)


    if filetype == type_filter or type_filter is None:
             
        if search in doc_name:
            new_doc_name = doc_name.replace(search, replace)
            new_doc_path = os.path.join(doc_path, new_doc_name) + filetype
            os.rename(doc, new_doc_path)
            renamed += 1
            print(f"Renamed file {doc} to {new_doc_path}")

print(f"Renamed {renamed} of {len(docs)}")