# Experimental Framework for NLU Generation #

## Getting Started ##

Setting up the environment:

1. Clone this repository recursively: `git clone https://github.com/kaniblu/ludus-jluva --recursive && cd ludus-jluva`

1. Download and setup GloVe: `cd datasets/glove && bash setup.sh && cd ../..`

1. Install required packages: `pip install -r requirements.txt && pip install -r codebase/requirements.txt`

1. (Optional) Install additional packages as specified in `codebase/README.md` if required.

1. Setup environments: `export PATH=$(pwd)/scripts:${PATH}`

1. Create instance directory: `mkdir instances`


Creating and running an experimental instance:

1. Create an experimental instance from the archetype: `instance-create jluva atis-jluva`

1. Set dataset: `config-set atis-jluva data dataset atis -w`

1. Train a generative model: `instance-run atis-jluva train`

1. Generate NLU corpus using the trained model: `instance-run atis-jluva generate --eidx 97`


The generated corpus (utterances + intents + slot labels) is saved under `instances/atis-jluva/(word.txt|intent.txt|label.txt)`, 
which can be used to train language understanding models with improved performances.
