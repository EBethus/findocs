# findocs


Fazer instalacao dos pacotes
```
sudo apt install tesseract-ocr
sudo apt install tesseract-ocr-por
```

Descarregar a data de treino da rede neuronal
https://github.com/tesseract-ocr/tessdata/blob/main/por.traineddata

Mover a rede
```
sudo mv eng.traineddata /usr/local/share/tessdata/
```

Instalar dependencias
```
pip3 install pytesseract
```