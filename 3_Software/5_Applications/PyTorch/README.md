## Word-level language modeling RNN
### Introduction
This example trains a **language module** which can be used by a **NLP**(**Natural Language Processing**) processor. It takes Wikitext-2 dataset and uses nn.RNN module to process the training, the trained model can then be used by the generate script to generate new text.
* https://github.com/pytorch/examples/tree/master/word_language_model

### Run example steps:
```
(pytorch-build) $ git clone https://github.com/pytorch/examples.git
(pytorch-build) $ cd examples/word_language_model
(pytorch-build) $ python main.py --cuda --emsize 650 --nhid 650 --dropout 0.5 --epochs 40 --tied # 40 epoches, 141 minutes
(pytorch-build) $ python generate.py --cuda --words 100
| Generated 0/100 words
```
### Result
```
(pytorch-build) $ cat generated.txt
to the present of stabilized fountains , because they did not do so by the time they did contribute to
the personal structure . Additionally , the rate of the entire event was often survives at projects of homes .
<eos> The work records different as of 2009 . The front music guides erected all the style of several "
<unk> " and " <unk> " <unk> ( proper water ) . In 2007 , Pflueger created the " More
coded balanced " at this point and recorded a primary event played in a US 2 , which was the
```
### Reference
* https://github.com/pytorch/examples

### Demo Video:
> TODO
