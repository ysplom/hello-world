<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8"/>
    <title>Canvas tutorial</title>
    <script type="text/javascript">
      function draw() {
        var canvas = document.getElementById('tutorial');
        if (canvas.getContext) {
          var ctx = canvas.getContext('2d');
        }
      }
    </script>
    <style type="text/css">
      canvas { border: 1px solid black; }
    </style>
  </head>
  <body onload="draw();">
    <canvas id="tutorial" width="150" height="150">

//В данном изображении, эта функция берет фрагмент из изображения, в виде прямоугольника, левый верхний угол которого -  (sx, sy), ширина и высота -  sWidth и sHeight и рисует  в  canvas, располагая его в точке  (dx, dy) и изменяя его размер на указанные величины в  dWidth и dHeight
drawImage(image, sx, sy, sWidth, sHeight, dx, dy, dWidth, dHeight)

    </canvas>
  </body>
</html>
