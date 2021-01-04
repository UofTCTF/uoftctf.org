import os

path = "/home/rfaccount/ctf/uoftctf.org/content/posts/write-ups/picoCTF"


dirname = [f for f in os.listdir(path) if not f.endswith("py")]

md_file_path = []
for i in dirname:
    print([f for f in os.listdir(os.path.join(path, i)) if f.endswith(".md")])
    md_file_path.extend([os.path.join(os.path.join(path, i), f) for f in os.listdir(os.path.join(path, i)) if f.endswith(".md")])

print(md_file_path)

for mdpath in md_file_path:
    with open(mdpath, 'r') as f:
        print(f.readlines())
