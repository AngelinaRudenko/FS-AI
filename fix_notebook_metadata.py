import json

# Read the notebook
notebook_path = r'c:\Programming\FS-AI\src\flight-price-prediciton.ipynb'

with open(notebook_path, 'r', encoding='utf-8') as f:
    notebook = json.load(f)

# Fix the metadata.widgets structure
# The widgets content should be inside a "state" key
if 'widgets' in notebook.get('metadata', {}):
    widgets_content = notebook['metadata']['widgets']
    # Wrap the current content in a 'state' key
    notebook['metadata']['widgets'] = {
        'state': widgets_content
    }
    print("Fixed: Wrapped widgets content in 'state' key")
else:
    print("No widgets metadata found")

# Save the fixed notebook
with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=1, ensure_ascii=False)

print(f"Notebook saved: {notebook_path}")
print("The notebook should now open correctly on GitHub!")
