from pathlib import Path

path = Path('10_ArchivosExcepciones/pi.txt')
contents = path.read_text()
print(contents)