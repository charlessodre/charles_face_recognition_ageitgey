# Reconhecimento Facial usando o modulo face_recognition

<p> O objetivo deste projeto é realizar alguns estudos/testes na área de visão computacional, especialmente em reconhecimento facial. </p>

<p> Nesse estudo vamos utilizar o modulo face_recognition para realizar alguns testes de reconhecimento facial.</p>

<p> O módulo e os exemplos utilizados neste estudo estão disponíveis no github do criador: </p>

<p> https://github.com/ageitgey/face_recognition</p>

## Informação sobre os arquivos:

<p> <b>face_recognition_min_draw_box.py </b> -  Esse programa realiza o reconhecimento dos rostos nas imagens que estão no diretório  “source_img/unknown” e salva a imagem, com os rostos identificados, no diretório “source_img/output”. Ele executa em batch o reconhecimento dos rostos . </p>

<p>  <b>face_recognition_webcam.py </b> - Esse programa realiza o reconhecimento dos rostos identificados na Webcam. Ele pode salvar as imagens, se necessário.</p>

<p>  <b>helper.py </b> - Funções de suporte diversas.</p>

<p> Obs.: Os programas  <b>face_recognition_min_draw_box.py</b>  e  <b>face_recognition_webcam.py</b>  são independentes. Eles podem ser executados separadamente. </p>

## Estrutura dos diretórios:

<p> <b>source_img/known_people </b>- Neste diretório ficam as imagens das pessoas conhecidas. A imagem deve conter somente o rosto da pessoa (um rosto). O nome do arquivo da imagem deve ser o nome da pessoa seguido do caractere "#". Todo o texto que estiver antes do "#" será o nome utilizado para a classificação do rosto.</p>
<p> Exemplo de nomes de arquivos válidos: </p>
	<p> <b>charles#.jpeg</b></p>
	<p> <b>charles_sodre#.jpeg</b></p>
	<p> <b>charles_sodre#_001.jpeg</b></p>



<p> <b>source_img/unknown </b>- Neste diretório ficam as imagens dos rostos desconhecidos. A imagem pode conter vários rostos, pois será verificado se existe algum rosto conhecido (informado no diretório source_img/known_people).</p>


<p> <b>source_img/output </b>- Neste diretório será salva a imagem informando se reconheceu ou não o rosto. Os rostos que não possuírem um retângulo significa que o algoritmo não identificou como um rosto válido.</p>

## Exemplo de faces reconhecidas:

![Exemplo de faces reconhecidas](exemplo.gif)



