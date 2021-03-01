# TODO: Use fast-bert library to make this more streamlined
#   If that fails (hardware constraints), may need to abandon BERT and try
#   this problem using just scikit-learn

import os as _os
import logging as _logging
import torch as _torch
from datetime import datetime as _date
from fast_bert.data_cls import BertDataBunch as _BertDataBunch
from fast_bert.learner_cls import BertLearner as _BertLearner
from fast_bert.metrics import accuracy as _accuracy

DEFAULT_DATA_DIR = _os.path.join(
    _os.path.dirname(_os.path.dirname(__file__)),
    'classification_data'
)

def train(data_location: str = DEFAULT_DATA_DIR,
          output_path: str = None) -> _BertLearner:

    if output_path is None:
        output_path = _os.path.join(
            _os.path.dirname(DEFAULT_DATA_DIR),
            'training_output',
            'classification',
            _date.now().strftime("%Y%m%d%H%M%S") + '_' + 'model'
        )
    _os.mkdir(output_path)

    # TODO: this could be parsed from classification_labels.csv
    possible_labels = ['title', 'ingredient', 'instruction', 'other']

    databunch = _BertDataBunch(data_location, data_location,
                              tokenizer='bert-base-uncased',
                              train_file='classification_train.csv',
                              val_file='classification_test.csv',
                              label_file='classification_labels.csv',
                              text_col='text',
                              label_col=possible_labels,
                              batch_size_per_gpu=16,
                              max_seq_length=512,
                              multi_gpu=True,
                              multi_label=True,
                              model_type='bert')

    logger = _logging.getLogger()
    device_cpu = _torch.device("cpu")
    metrics = [{'name': 'accuracy', 'function': _accuracy}]
    learner = _BertLearner.from_pretrained_model(
                            databunch,
                            pretrained_path='bert-base-uncased',
                            metrics=metrics,
                            device=device_cpu,
                            logger=logger,
                            output_dir=output_path,
                            finetuned_wgts_path=None,
                            warmup_steps=500,
                            multi_gpu=True,
                            is_fp16=True,
                            multi_label=True,
                            logging_steps=50)
    
    # learner.lr_find(start_lr=1e-6)
    # learner.plot()
    learner.fit(epochs=6, lr=6e-5)
    return learner


def save(classifier: _BertLearner):
    classifier.save_model()


def load():
    raise NotImplementedError