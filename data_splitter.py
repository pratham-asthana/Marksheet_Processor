import os
import random
import shutil

def split_dataset(dataset_dir: str,
                  output_dir: str,
                  train_ratio: float = 0.8,
                  seed: int = 42):
    """
    Splits a YOLO-style dataset into train/test.

    Parameters
    ----------
    dataset_dir : str
        Path to your original dataset folder, containing:
           - images/
           - labels/
           - classes.txt
           - notes.json
    output_dir : str
        Path where the train/ & test/ folders will be created.
    train_ratio : float
        Fraction of data to use for training (e.g. 0.8 → 80% train, 20% test).
    seed : int
        Random seed for reproducibility.
    """

    imgs_dir   = os.path.join(dataset_dir, 'images')
    lbls_dir   = os.path.join(dataset_dir, 'labels')
    filenames = [f for f in os.listdir(imgs_dir)
                 if os.path.isfile(os.path.join(imgs_dir, f))]
    random.seed(seed)
    random.shuffle(filenames)

    split_idx   = int(len(filenames) * train_ratio)
    train_files = filenames[:split_idx]
    test_files  = filenames[split_idx:]

    for split in ('train', 'test'):
        for sub in ('images', 'labels'):
            os.makedirs(os.path.join(output_dir, split, sub), exist_ok=True)

    def _copy(split_files, split_name):
        for img_fn in split_files:
            base, _ = os.path.splitext(img_fn)
            src_img = os.path.join(imgs_dir, img_fn)
            src_lbl = os.path.join(lbls_dir, base + '.txt')

            dst_img = os.path.join(output_dir, split_name, 'images', img_fn)
            dst_lbl = os.path.join(output_dir, split_name, 'labels', base + '.txt')

            shutil.copy2(src_img, dst_img)
            if os.path.exists(src_lbl):
                shutil.copy2(src_lbl, dst_lbl)

    _copy(train_files, 'train')
    _copy(test_files,  'test')
    for fname in ('classes.txt', 'notes.json'):
        src = os.path.join(dataset_dir, fname)
        dst = os.path.join(output_dir, fname)
        if os.path.exists(src):
            shutil.copy2(src, dst)

    print(f"Dataset split complete! → {len(train_files)} train / {len(test_files)} test")

split_dataset('datasett', 'datasett_split', train_ratio=0.8, seed=123)