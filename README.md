# RetinaFace

<style>
    .gallery {
        display: grid;
        grid-template-columns: repeat(6, 1fr); /* 6 列 */
        grid-gap: 10px;
    }
    .gallery img {
        width: 100%;
        height: auto;
    }
    .gallery-caption {
        text-align: center;
        margin-top: 5px;
    }
</style>


  <style>
      .gallery1 {
          display: grid;
          grid-template-columns: repeat(3, 1fr); /* 每行显示 3 张图片 */
          grid-gap: 10px;
      }
      .gallery img {
          width: 100%;
          height: auto;
      }
      .gallery-caption {
          text-align: center;
          margin-top: 5px;
      }
  </style>

RetinaFace is a deep learning based cutting-edge facial detector for Python coming with facial landmarks. Its detection performance is amazing even in the crowd as shown in the following illustration.

RetinaFace is the face detection module of [insightface](https://github.com/deepinsight/insightface) project. The original implementation is mainly based on mxnet. Then, its tensorflow based [re-implementation](https://github.com/StanislasBertrand/RetinaFace-tf2) is published by [Stanislas Bertrand](https://github.com/StanislasBertrand). So, this repo is heavily inspired from the study of Stanislas Bertrand. Its source code is simplified and it is transformed to pip compatible but the main structure of the reference model and its pre-trained weights are same.

<p align="center"><img src="./tests/outputs/result.png" width="90%" height="90%">
<br><em>Second grade Chinese class</em>
</p>

<body>
    <div class="gallery">
        <!-- 添加 28 张图片 -->
        <img src="./tests/outputs/faces/test/face_0.png" alt="图片1">
        <img src="./tests/outputs/faces/test/face_1.png" alt="图片2">
        <img src="./tests/outputs/faces/test/face_2.png" alt="图片3">
        <img src="./tests/outputs/faces/test/face_3.png" alt="图片4">
        <img src="./tests/outputs/faces/test/face_4.png" alt="图片5">
        <img src="./tests/outputs/faces/test/face_5.png" alt="图片6">
        <img src="./tests/outputs/faces/test/face_6.png" alt="图片7">
        <img src="./tests/outputs/faces/test/face_7.png" alt="图片8">
        <img src="./tests/outputs/faces/test/face_8.png" alt="图片9">
        <img src="./tests/outputs/faces/test/face_9.png" alt="图片10">
        <img src="./tests/outputs/faces/test/face_10.png" alt="图片11">
        <img src="./tests/outputs/faces/test/face_11.png" alt="图片12">
        <img src="./tests/outputs/faces/test/face_12.png" alt="图片13">
        <img src="./tests/outputs/faces/test/face_13.png" alt="图片14">
        <img src="./tests/outputs/faces/test/face_14.png" alt="图片15">
        <img src="./tests/outputs/faces/test/face_15.png" alt="图片16">
        <img src="./tests/outputs/faces/test/face_16.png" alt="图片17">
        <img src="./tests/outputs/faces/test/face_17.png" alt="图片18">
        <img src="./tests/outputs/faces/test/face_18.png" alt="图片19">
        <img src="./tests/outputs/faces/test/face_19.png" alt="图片20">
        <img src="./tests/outputs/faces/test/face_20.png" alt="图片21">
        <img src="./tests/outputs/faces/test/face_21.png" alt="图片22">
        <img src="./tests/outputs/faces/test/face_22.png" alt="图片23">
        <img src="./tests/outputs/faces/test/face_23.png" alt="图片24">
        <img src="./tests/outputs/faces/test/face_24.png" alt="图片25">
        <img src="./tests/outputs/faces/test/face_25.png" alt="图片26">
        <img src="./tests/outputs/faces/test/face_26.png" alt="图片27">
        <img src="./tests/outputs/faces/test/face_27.png" alt="图片28">
        <img src="./tests/outputs/faces/test/face_28.png" alt="图片28">
    </div>
    <p class="gallery-caption"><em>Pull up pictures of faces</em></p>
</body>

<body>
    <div class="gallery1">
        <!-- 添加 28 张图片 -->
        <img src="./tests/outputs/cmp/face_0_00.png" alt="图片1">
        <img src="./tests/outputs/cmp/face_1_00.png" alt="图片2">
        <img src="./tests/outputs/cmp/face_2_00.png" alt="图片3">
        <img src="./tests/outputs/cmp/face_3_00.png" alt="图片4">
        <img src="./tests/outputs/cmp/face_4_00.png" alt="图片5">
        <img src="./tests/outputs/cmp/face_5_00.png" alt="图片6">
        <img src="./tests/outputs/cmp/face_6_00.png" alt="图片7">
        <img src="./tests/outputs/cmp/face_7_00.png" alt="图片8">
        <img src="./tests/outputs/cmp/face_8_00.png" alt="图片9">
        <img src="./tests/outputs/cmp/face_9_00.png" alt="图片10">
        <img src="./tests/outputs/cmp/face_10_00.png" alt="图片11">
        <img src="./tests/outputs/cmp/face_11_00.png" alt="图片12">
        <img src="./tests/outputs/cmp/face_12_00.png" alt="图片13">
        <img src="./tests/outputs/cmp/face_13_00.png" alt="图片14">
        <img src="./tests/outputs/cmp/face_14_00.png" alt="图片15">
        <img src="./tests/outputs/cmp/face_15_00.png" alt="图片16">
        <img src="./tests/outputs/cmp/face_16_00.png" alt="图片17">
        <img src="./tests/outputs/cmp/face_17_00.png" alt="图片18">
        <img src="./tests/outputs/cmp/face_18_00.png" alt="图片19">
        <img src="./tests/outputs/cmp/face_19_00.png" alt="图片20">
        <img src="./tests/outputs/cmp/face_20_00.png" alt="图片21">
        <img src="./tests/outputs/cmp/face_21_00.png" alt="图片22">
        <img src="./tests/outputs/cmp/face_22_00.png" alt="图片23">
        <img src="./tests/outputs/cmp/face_23_00.png" alt="图片24">
        <img src="./tests/outputs/cmp/face_24_00.png" alt="图片25">
        <img src="./tests/outputs/cmp/face_25_00.png" alt="图片26">
        <img src="./tests/outputs/cmp/face_26_00.png" alt="图片27">
        <img src="./tests/outputs/cmp/face_28_00.png" alt="图片28">
    </div>
    <p class="gallery-caption"><em>Pull up pictures of faces</em></p>
</body>


## Installation [![PyPI](https://img.shields.io/pypi/v/retina-face.svg)](https://pypi.org/project/retina-face/) [![Conda](https://img.shields.io/conda/vn/conda-forge/retina-face.svg)](https://anaconda.org/conda-forge/retina-face)

The easiest way to install retinaface is to download it from [PyPI](https://pypi.org/project/retina-face/). It's going to install the library itself and its prerequisites as well.

```shell
$ pip install retina-face
```

RetinaFace is also available at [`Conda`](https://anaconda.org/conda-forge/retina-face). You can alternatively install the package via conda.

```shell
$ conda install -c conda-forge retina-face
```

Then, you will be able to import the library and use its functionalities.

```python
from retinaface import RetinaFace
```

**Face Detection** - [`Demo`](https://youtu.be/Wm1DucuQk70)

RetinaFace offers a face detection function. It expects an exact path of an image as input.

```python
resp = RetinaFace.detect_faces("img1.jpg")
```

Then, it will return the facial area coordinates and some landmarks (eyes, nose and mouth) with a confidence score.

```json
{
    "face_1": {
        "score": 0.9993440508842468,
        "facial_area": [155, 81, 434, 443],
        "landmarks": {
          "right_eye": [257.82974, 209.64787],
          "left_eye": [374.93427, 251.78687],
          "nose": [303.4773, 299.91144],
          "mouth_right": [228.37329, 338.73193],
          "mouth_left": [320.21982, 374.58798]
        }
  }
}
```


## Acknowledgements

This work is mainly based on the [insightface](https://github.com/deepinsight/insightface) project and [retinaface](https://arxiv.org/pdf/1905.00641.pdf) paper; and it is heavily inspired from the re-implementation of [retinaface-tf2](https://github.com/StanislasBertrand/RetinaFace-tf2) by [Stanislas Bertrand](https://github.com/StanislasBertrand). Finally, Bertrand's [implemenation](https://github.com/StanislasBertrand/RetinaFace-tf2/blob/master/rcnn/cython/cpu_nms.pyx) uses [Fast R-CNN](https://arxiv.org/abs/1504.08083) written by [Ross Girshick](https://github.com/rbgirshick/fast-rcnn) in the background. All of those reference studies are licensed under MIT license.

## Citation

If you are using RetinaFace in your research, please consider to cite its [original research paper](https://arxiv.org/abs/1905.00641). Besides, if you are using this re-implementation of retinaface, please consider to cite the following research papers as well. Here are examples of BibTeX entries:

```BibTeX
@inproceedings{serengil2020lightface,
  title        = {LightFace: A Hybrid Deep Face Recognition Framework},
  author       = {Serengil, Sefik Ilkin and Ozpinar, Alper},
  booktitle    = {2020 Innovations in Intelligent Systems and Applications Conference (ASYU)},
  pages        = {23-27},
  year         = {2020},
  doi          = {10.1109/ASYU50717.2020.9259802},
  url          = {https://doi.org/10.1109/ASYU50717.2020.9259802},
  organization = {IEEE}
}
```

```BibTeX
@inproceedings{serengil2021lightface,
  title        = {HyperExtended LightFace: A Facial Attribute Analysis Framework},
  author       = {Serengil, Sefik Ilkin and Ozpinar, Alper},
  booktitle    = {2021 International Conference on Engineering and Emerging Technologies (ICEET)},
  pages        = {1-4},
  year         = {2021},
  doi          = {10.1109/ICEET53442.2021.9659697},
  url          = {https://doi.org/10.1109/ICEET53442.2021.9659697},
  organization = {IEEE}
}
```

Finally, if you use this RetinaFace re-implementation in your GitHub projects, please add retina-face dependency in the requirements.txt.

## Licence

This project is licensed under the MIT License - see [`LICENSE`](https://github.com/serengil/retinaface/blob/master/LICENSE) for more details.
