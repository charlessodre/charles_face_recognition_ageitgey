# Reconhecimento Facial usando o modulo face_recognition

O objetivo deste projeto é realizar alguns estudos/testes na área de visão computacional, especialmente em reconhecimento facial. 

Nesse estudo vamos utilizar o modulo face_recognition para realizar alguns testes de reconhecimento facial utilizando esta biblioteca.<br>

O módulo e os exemplos utilizados neste estudo estão disponíveis no github do criador: <br/>

https://github.com/ageitgey/face_recognition

## Informação sobre os arquivos:

face_recognize_min_draw_box.py -  Esse programa realiza o reconhecimento dos rostos  nas imagens que estão no diretório  “source_img/unknown” e salva a imagem com os rostos identificados no diretório “source_img/output”. <br/>
face_recognize_webcam.py - Esse programa realiza o reconhecimento dos rostos identificados na Webcam. Ele não salva as imagens.<br>
helper.py - Funções de suporte diversas.<br/>

## Estrutura dos diretórios:

source_img/known_people - Neste diretório ficam as imagens das pessoas conhecidas. A imagem deve conter somente o rosto da pessoa (um rosto). O nome do arquivo da imagem deve ser o nome da pessoa seguido do caractere "#". Todo o texto que estiver antes do "#" será o nome utilizado para a classificação do rosto.<br>
Exemplo nome do arquivo.: 
	charles#.jpeg
	charles_sodre#.jpeg
	charles_sodre#_001.jpeg

<br/>

source_img/unknown - Neste diretório ficam as imagens das pessoas desconhecidas. A imagem pode conter vários rostos, pois verificar se existe algum rosto conhecido (informado no diretório source_img/known_people).<br/>


source_img/output - Neste diretório é onde será salva a imagem informando se reconheceu ou não o rosto. Os rostos que não possuírem um retângulo significa que o não foi identificado como um rosto.<br/>

