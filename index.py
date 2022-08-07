# OCR
import pytesseract
# Para recorrido do diretorio
import os
#Para salvar no banco de dados
import sqlite3

#Imagens
from PIL import Image
import pytesseract

directory = 'imagens';

# Python program to find MD5 hash value of a file
import hashlib

def hashFile(filename):
  with open(filename,"rb") as f:
    bytes = f.read() # read file as bytes
    readable_hash = hashlib.sha1(bytes).hexdigest();
    return readable_hash

conn = sqlite3.connect('data.db3')
cursor = conn.cursor()

for dirname in os.listdir(directory):
  dir = os.path.join(directory, dirname)
  # checking if it is a file
  if os.path.isdir(dir):
    for filename in os.listdir(dir):
      f = os.path.join(dir, filename)
      if not os.path.isfile(f):
        print(f)
        continue

      cursor.execute("SELECT Count() FROM {0} where filename = '{1}'".format('quotes', f))
      count = cursor.fetchone()[0]
      if (count > 0):
        print('processado {0}'.format(f))
        continue

      hash = hashFile(f)
      cursor.execute("SELECT Count() FROM {0} where checksum = '{1}'".format('quotes', hash))
      count = cursor.fetchone()[0]
      if (count > 0):
        print('Repeat iamges {0} - {1}'.format(f, hash))
        continue

      img = Image.open(f) # Abre 
      img.load()
      text = pytesseract.image_to_string(img, lang='por') # Extrae o texto
      print("Processando {0} - {1}".format(count, f))
      # inserindo dados na tabela
      try:
        cursor.execute(
          "INSERT INTO quotes (checksum, filename, content) VALUES (?,?,?)",
          (hash, f, text)
        )
        conn.commit()
      except sqlite3.IntegrityError as err:
        print(hash + " " + f)

conn.close()