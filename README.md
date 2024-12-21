# BlazePose Experimentation

This was a final project in the course 50.035 Computer Vision, Singapore University of Technology and Design. This project had four contributors - Sarang, Vy Dinh, Rachel Leow and myself (Ryan Wang). My main contributions include adapting the original blazepose model, experimenting with extra layers, and experimenting with CBAM modules.

Review the full report [here](/Project_BlazePose.pdf).

**Theme: Design Track - healthcare**

Initial project idea: Utilizing human pose estimation models to determine whether someone is exercising correctly

Background: Human pose estimation, a subfield of computer vision, involves the task of localizing and identifying human body joints in an image or video sequence. This technology has seen significant advancements in recent years, driven by improvements in deep learning algorithms and the availability of large-scale datasets. Our group wishes to use this existing technology to help people exercise better by tracking landmarks on their body to determine whether their posture is correct when doing a particular exercise. 

This task is a complex computer vision task because the problem deals with object occlusion, lighting conditions, body position and different clothing. Our group will be using GoogleMediaPipe which uses the BlazePose model for 3D pose estimation. By identifying key landmarks on the body, such as the shoulders, elbows, wrists, hips, knees, and ankles, we can assess the correctness of an individual's posture while performing various exercises.

Another challenge would be processing images in real time as we have to process frames very quickly determining the landmark positions per frame and providing real time feedback. 

The following link is the blazepose research paper:  https://arxiv.org/abs/2006.10204. 

## Implementation

This is an experimental adaptation of BlazePose in Tensorflow from [alishsuper/BlazePose-Implementation](https://github.com/alishsuper/BlazePose-Implementation?tab=readme-ov-file). 

### Setup

1. Install required libraries:
    ```
    python -m venv .venv
    .venv\Scripts\activate
    python -m pip install -r requirements.txt
    ```

2. Run `python test.py`. The keypoint predictions will be shown in the `/results` folder.

### Train/finetune model

In `config.py`, modify `use_existing_model_weights = 0`. Then refer to `README_OG.md`.


### Video processing from trained model
After training the model, in `config.py` modify the `input_video_path` and `output_video_path` parameters.
Run `video_processor.py` 

## Train
1. Pre-train the heatmap branch and the regression branch.
  run `python train.py`.

## Test
1. Set `select_model` to the model you would like to test in config.py.

2. Run `python test.py`.

## Test All
Running `python test_all.py` will load all the models and display PCK results as well as the latency results

## Test Performance Comparison

### PCK Performance
Base Model PCK: 0.58
Extra Model PCK: 0.39
CBAM Model PCK: 0.021
VIT Model PCK: 0.42
Heatmap Model PCK: 0.44

### Latency Performance (ms)
Base Model Latency: 116
Extra Model Latency: 290
CBAM Model Latency: 124
VIT Model Latency: 117
Heatmap Model Latency: 93


## Reference

```tex
@article{Bazarevsky2020BlazePoseOR,
  title={BlazePose: On-device Real-time Body Pose tracking},
  author={Valentin Bazarevsky and I. Grishchenko and K. Raveendran and Tyler Lixuan Zhu and Fangfang Zhang and M. Grundmann},
  journal={ArXiv},
  year={2020},
  volume={abs/2006.10204}
}
```

