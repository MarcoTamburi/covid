import os
import glob
import nbformat
from deep_translator import GoogleTranslator

translator = GoogleTranslator(source="it", target="en")

def translate_text(text: str) -> str:
    if not text.strip():
        return text
    # Traduci mantenendo le newlines (deep-translator regge abbastanza bene)
    return translator.translate(text)

for path in glob.glob("**/*.ipynb", recursive=True):
    nb = nbformat.read(path, as_version=4)

    changed = False
    for cell in nb.cells:
        if cell.cell_type == "markdown":
            original = cell.source
            translated = translate_text(original)
            if translated and translated != original:
                cell.source = translated
                changed = True

    if changed:
        backup = path + ".bak"
        if not os.path.exists(backup):
            os.rename(path, backup)
        nbformat.write(nb, path)
        print(f"Tradotto: {path} (backup: {backup})")
    else:
        print(f"Nessun cambiamento: {path}")