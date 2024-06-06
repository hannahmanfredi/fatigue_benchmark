# Fatigue Benchmark

Using the IEMOCAP dataset, I intend to fine-tune an existing (likely Wav2Vec) model to classify audio with a level of fatigue rating.

## Datasets

- [IEMOCAP dataset](https://sail.usc.edu/iemocap/)

## Things to Explore

## Weekly Objectives

- Week 1:

  - Find dataset to establish benchmark
  - Init project repo

- Week 2:

  - Get a high level understanding of how the Wav2Vec works
  - Research physiological cues for fatigue in conversation
  - Scan the dataset and understand what I'm working with
  - Explore the data in a Jupyter Notebook
  - Do some audio classification tutorials: [Audio-Classification-on-Keyword-Spotting.ipynb - Colaboratory](https://colab.research.google.com/github/huggingface/notebooks/blob/main/examples/audio_classification.ipynb)
  - Review [Audio Classification Guide](https://huggingface.co/docs/transformers/en/tasks/audio_classification)
  - complete [Speech Recognition with Wav2Vec2 — Torchaudio 2.2.0 documentation](https://pytorch.org/audio/stable/tutorials/speech_recognition_pipeline_tutorial.html)
  - This is overkill: [Google Colab](https://colab.research.google.com/github/m3hrdadfi/soxan/blob/main/notebooks/Emotion_recognition_in_Greek_speech_using_Wav2Vec2.ipynb)

- Week 3:
  Establish a benchmark

- Week 4:
  Build a simple UI / think about how I am going to test this

## Resources

- [Audio Classification](https://huggingface.co/docs/transformers/en/tasks/audio_classification)
- [Search Audio Emotion Classification Models - Hugging Face](https://huggingface.co/models?pipeline_tag=audio-classification&sort=downloads&search=emotion)

## Models

- [Wav2Vec](https://ai.meta.com/research/impact/wav2vec/#how-it-works)
- [Wav2Vec2 Model on Hugging Face](https://huggingface.co/docs/transformers/en/model_doc/wav2vec2)
  - [facebook/wav2vec2-base · Hugging Face](https://huggingface.co/facebook/wav2vec2-base)
    - Do not use: [facebook/wav2vec2-base-960h · Hugging Face](https://huggingface.co/facebook/wav2vec2-base-960h) even though it looks the same but better [it's actually already fine-tuned](https://huggingface.co/facebook/wav2vec2-base-960h/discussions/3#62e7a0b7ae8b00c198ba1dbe)
- [ehcalabres/wav2vec2-lg-xlsr-en-speech-emotion-recognition · Hugging Face](https://huggingface.co/ehcalabres/wav2vec2-lg-xlsr-en-speech-emotion-recognition)

## Additional Datasets to Explore

- [ravdess Dataset - Hugging Face](https://huggingface.co/datasets/narad/ravdess)
- [Toronto emotional speech set (TESS) - Kaggle](https://www.kaggle.com/datasets/ejlok1/toronto-emotional-speech-set-tess)
- [RAVDESS Emotional speech audio - Kaggle](https://www.kaggle.com/datasets/uwrfkaggler/ravdess-emotional-speech-audio)

## Tutorials

- Linked from hugging face task doc: [Audio Classification on Keyword Spotting - Colab](https://colab.research.google.com/github/huggingface/notebooks/blob/main/examples/audio_classification.ipynb)
  - [transformers/examples/pytorch/audio-classification at main · huggingface/transformers](https://github.com/huggingface/transformers/tree/main/examples/pytorch/audio-classification)
- Linked from model card: [Fine-Tune Wav2Vec2 for English ASR Notebook - Colaboratory](https://colab.research.google.com/drive/1FjTsqbYKphl9kL-eILgUc-bl4zVThL8F?usp=sharing)
  - [Fine-Tune Wav2Vec2 for English ASR in Hugging Face with 🤗 Transformers](https://huggingface.co/blog/fine-tune-wav2vec2-english)
- [Speech Recognition with Wav2Vec2 — Torchaudio 2.2.0 documentation](https://pytorch.org/audio/stable/tutorials/speech_recognition_pipeline_tutorial.html)
- [Greek Emotion Recogntion Wav2Vec2](https://colab.research.google.com/github/m3hrdadfi/soxan/blob/main/notebooks/Emotion_recognition_in_Greek_speech_using_Wav2Vec2.ipynb)

## Deployment

- [Deploy Automatic Speech Recogntion with Hugging Face's Transformers & Amazon SageMaker](https://www.philschmid.de/automatic-speech-recognition-sagemaker)
