import io
import sys
import tqdm
import pickle
import tarfile
import argparse
import numpy as np


parser = argparse.ArgumentParser()
parser.add_argument("--glove-path", required=True)
parser.add_argument("--out-path", required=True)


def write_file(tf, name, write_fn):
    bio = io.BytesIO()
    write_fn(bio)
    data = bio.getvalue()
    info = tarfile.TarInfo(name)
    info.size = len(data)
    tf.addfile(info, io.BytesIO(data))


def load_glove(path):
    data = {}
    with open(path, "r") as f:
        for line in tqdm.tqdm(f, desc="reading glove"):
            tokens = line.split()
            word = " ".join(tokens[:-300])
            vec = np.array([float(v) for v in tokens[-300:]])
            data[word] = vec
    return data


def write_tar(glove, path):
    words = list(glove.keys())
    vocab = {w: i for i, w in enumerate(words)}
    array = np.stack([glove[w] for w in words])
    with tarfile.TarFile(path, mode="w") as f:
        write_file(f, "vocab.pkl", lambda s: pickle.dump(vocab, s))
        write_file(f, "array.npy", lambda s: np.save(s, array))


if __name__ == "__main__":
    args = parser.parse_args()
    glove = load_glove(args.glove_path)
    write_tar(glove, args.out_path)
