## Getting Started ##

### Setting up the environment ###

Clone this repository recursively:

`git clone https://github.com/kaniblu/ludus-jluva --recursive && cd ludus-jluva`

Download and setup GloVe: 

`cd datasets/glove && bash setup.sh && cd ../..`

Install required packages: 

`pip install -r requirements.txt && pip install -r codebase/requirements.txt`

(Optional) Install additional packages as specified in `codebase/README.md` if required.

Setup environments: 

`export PATH=$(pwd)/scripts:${PATH}`

Create the instance directory: 

`mkdir instances`


### Creating and running an experimental instance ###

Create an experimental instance from the archetype: 

`instance-create jluva atis-jluva`

Configure the dataset option in the instance: 

`config-set atis-jluva data dataset atis -w`

Train a generative model: 

`instance-run atis-jluva train`

Generate NLU corpus using the trained model: 

`instance-run atis-jluva generate --eidx 97`


After above steps, the synthetic corpus (utterances + intents + slot labels) will be generated under `instances/atis-jluva` with the filenames `word.txt`, `intent.txt`, and `label.txt`. 
Such corpus improves LU performances when used to augment the existing corpus for training supervised LU models.
