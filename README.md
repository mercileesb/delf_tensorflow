# DELF: DEep Local Features


This project is wrapper of [DELF Tensorflow code](https://github.com/tensorflow/models/tree/master/research/delf) (introduced
in the paper ["Large-Scale Image Retrieval with Attentive Deep Local Features"](https://arxiv.org/abs/1612.06321)) and
[DELF_Enhanced](https://github.com/insikk/delf_enhanced).

A simple application is also illustrated, where two images containing the same landmark can be matched to each other, to obtain local image correspondences.

When I extract Large scale Image, such as 4K image above, Original code has OOM problem, So I modified image size and batch processing to add some lines simply.




## Installation

Please follow [these instructions](INSTALL_INSTRUCTIONS.md) to properly install the DELF library.



## DELF extraction

```bash
# From tensorflow/models/research/delf/delf/python/examples/
python extract_features.py \
  --config_path delf_config_example.pbtxt \
  --list_images_path list_images.txt \
  --output_dir data/oxford5k_features \
  --batch_size 10
```

If you setup properly, it is easy to extract code.


## Acknowledgement

```
"Large-Scale Image Retrieval with Attentive Deep Local Features",
Hyeonwoo Noh, Andre Araujo, Jack Sim, Tobias Weyand, Bohyung Han,
Proc. ICCV'17
```

## Reference

You can find nice examples below page !

* [DELF_Enhanced](https://github.com/insikk/delf_enhanced)


