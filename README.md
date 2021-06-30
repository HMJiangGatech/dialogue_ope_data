# Dialogue Off-Policy Evaluation Data

> This repo contains experience data as well as usage of pre-trained agents for dialogue off-policy evaluation. 

## What is dialogue off-policy evaluation?

**Dialogue Off-Policy Evaluation (OPE)** is the task of estimating human evaluation scores for dialogue systems without real interaction between human and dialogue systems. 

## Why we need experience data for OPE?

OPE is usually done with experience data, which is the historical conversations between human and dialogue systems. The dialogue systems used for collecting experience data are also called behavior models/behavior agents. 

Note that the experience data can be *different* from the *training data*, which usually contains only high-quality human-to-human conversations. As the human-to-human conversations does not cover failure modes of dialogue systems, they are not appropriate for OPE. 


## What's in this repo?

This repo contains experience data for two tasks: [Convai2](https://parl.ai/projects/convai2/) and [AirDialogue](https://github.com/google/airdialogue). 

### ConvAI2 / Persona Chat

This is a chit-chat task. We mainly use the pre-trained dialogue agents from the [Controllable Dialogue](https://github.com/facebookresearch/ParlAI/tree/controllable_dialogue_archive/projects/controllable_dialogue) project. See [convai2/README.md](convai2/README.md) for details.


### AirDialogue

This is a goal-oriented task. We trained transformer based models and ask human evaluator to chat with these models to generate experience data. The model is trained using this [code base](https://github.com/google-research/google-research/tree/master/dialogue_ope/airdialogue_model_transformer). See [airdialogue/README.md](airdialogue/README.md) for details.

## Reference


Please cite the following papers, if you are using our data.
```
@article{jiang2021towards,
  title={Towards Automatic Evaluation of Dialog Systems: A Model-Free Off-Policy Evaluation Approach},
  author={Jiang, Haoming and Dai, Bo and Yang, Mengjiao and Zhao, Tuo and Wei, Wei},
  journal={arXiv preprint arXiv:2102.10242},
  year={2021}
}
@article{dinan2019second,
  title={The second conversational intelligence challenge (convai2)},
  author={Dinan, Emily and Logacheva, Varvara and Malykh, Valentin and Miller, Alexander and Shuster, Kurt and Urbanek, Jack and Kiela, Douwe and Szlam, Arthur and Serban, Iulian and Lowe, Ryan and others},
  journal={arXiv preprint arXiv:1902.00098},
  year={2019}
}
@inproceedings{see2019what,
  author={Abigail See and Stephen Roller and Douwe Kiela and Jason Weston},
  booktitle={North American Chapter of the Association for Computational Linguistics (NAACL)},
  title={What makes a good conversation? How controllable attributes affect human judgments},
  url={https://arxiv.org/abs/1902.08654},
  year={2019},
}
@inproceedings{wei2018airdialogue,
  title={Airdialogue: An environment for goal-oriented dialogue research},
  author={Wei, Wei and Le, Quoc and Dai, Andrew and Li, Jia},
  booktitle={Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},
  pages={3844--3854},
  year={2018}
}
```
