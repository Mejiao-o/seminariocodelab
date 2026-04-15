Ola esta es una prueba de cosas no se aaaaaaaa
echo "# asd" >> README.md
git init
git add README.md # . para añadir todo
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Mejiao-o/asd.git
git push -u origin main

cd "C:\Users\Computers Lab 19\Desktop\proyectoFinal\seminariocodelab\customModel\model_out"
yolo task=classify mode=train model=yolov8n-cls.pt data={C:\Users\Computers Lab 19\Desktop\proyectoFinal\seminariocodelab\customModel\dataSet} epochs=20 imgsz=256
