import os
import errno
import yaml
import h5py


# echoes the behaviour of mkdir -p
# from http://stackoverflow.com/questions/600268/mkdir-p-functionality-in-python
def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:  
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


EMOTIONS = [
    "neutral",
    "calm",
    "happy",
    "sad",
    "angry",
    "fearful",
    "disgust",
    "surprised"
]


EMOTION_NUMBERS = {
    'neutral': 0,
    'calm': 1,
    'happy': 2,
    'sad': 3,
    'angry': 4,
    'fearful': 5,
    'disgust': 6,
    'surprised': 7,
}

def ttv_yaml_to_dict(path):
    with open(path, 'r') as f:
        return yaml.load(f.read())


def get_emotion_from_filename(filename):
    return filename.split('/')[-1].split('.')[0].split('_')[1]


def get_emotion_number_from_filename(filename):
    return EMOTION_NUMBERS[filename.split('/')[-1].split('.')[0].split('_')[1]]

def get_cached_ttv_data(path):
    f = h5py.File(path, 'r')

    return (
    {
        'x': f['test']['x'][:],
        'y': f['test']['y'][:]
    },
    {
        'x': f['train']['x'][:],
        'y': f['train']['y'][:],
    },
    {
        'x': f['validation']['x'][:],
        'y': f['validation']['y'][:],
    }
    )

def cache_ttv_data(path, ttv_data):
    test_data, train_data, validation_data = ttv_data

    f = h5py.File(path, 'w')

    f.create_dataset('test/x', data=test_data['x'])
    f.create_dataset('test/y', data=test_data['y'])

    f.create_dataset('train/x', data=train_data['x'])
    f.create_dataset('train/y', data=train_data['y'])

    f.create_dataset('validation/x', data=validation_data['x'])
    f.create_dataset('validation/y', data=validation_data['y'])
    f.close()