wget -O glove.840B.300d.zip http://nlp.stanford.edu/data/glove.840B.300d.zip
unzip glove.840B.300d.zip
python glove2tar.py --glove-path glove.840B.300d.txt --out-path glove.840B.300d.tar
