# Reconhecimento Facial usando o modulo face_recognition

<p> O objetivo deste projeto é realizar alguns estudos/testes na área de visão computacional, especialmente em reconhecimento facial. </p>

<p> Nesse estudo vamos utilizar o modulo face_recognition para realizar alguns testes de reconhecimento facial.</p>

<p> O módulo e os exemplos utilizados neste estudo estão disponíveis no github do criador: </p>

<p> https://github.com/ageitgey/face_recognition</p>

## Informação sobre os arquivos:

<p> face_recognition_min_draw_box.py -  Esse programa realiza o reconhecimento dos rostos nas imagens que estão no diretório  “source_img/unknown” e salva a imagem com os rostos identificados no diretório “source_img/output”.</p>

<p> face_recognition_webcam.py - Esse programa realiza o reconhecimento dos rostos identificados na Webcam. Ele pode salvar as imagens, se necessário.</p>

<p> helper.py - Funções de suporte diversas.</p>

## Estrutura dos diretórios:

<p> source_img/known_people - Neste diretório ficam as imagens das pessoas conhecidas. A imagem deve conter somente o rosto da pessoa (um rosto). O nome do arquivo da imagem deve ser o nome da pessoa seguido do caractere "#". Todo o texto que estiver antes do "#" será o nome utilizado para a classificação do rosto.</p>
<p> Exemplo nome do arquivo válidos: </p>
	<p> charles#.jpeg</p>
	<p> charles_sodre#.jpeg</p>
	<p> charles_sodre#_001.jpeg</p>



<p> source_img/unknown - Neste diretório ficam as imagens das pessoas desconhecidas. A imagem pode conter vários rostos, pois será verificado se existe algum rosto conhecido (informado no diretório source_img/known_people).</p>


<p> source_img/output - Neste diretório é onde será salva a imagem informando se reconheceu ou não o rosto. Os rostos que não possuírem um retângulo significa que o não foi identificado como um rosto.</p>

## Exemplo de faces reconhecidas:

![Exemplo de faces reconhecidas](exemplo.gif)



