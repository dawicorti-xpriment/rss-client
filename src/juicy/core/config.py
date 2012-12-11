import os
import json

import juicy


class Config(object):

    def __init__(self, path, defaults=None, fixed=None):
        self._path = os.path.join(
            juicy.homepath,
            path
        )
        if defaults is not None:
            self._data = defaults
        else:
            self._data = {}
        if os.path.exists(self._path):
            with open(self._path) as input_file:
                self._data.update(json.loads(input_file.read()))
        if fixed is not None:
            self._data.update(fixed)
        self.save()

    def data(self):
        return self._data

    def save(self):
        parent_dir = os.path.dirname(self._path)
        if not os.path.exists(parent_dir):
            try:
                os.makedirs(parent_dir)
            except:
                pass
        with open(self._path, 'w') as output_file:
            output_file.write(json.dumps(self._data, indent=4))

    def set(self, name, value):
        self._data[name] = value
        self.save()

    def get(self, name, default=None):
        return self._data.get(name, default)

    def __getitem__(self, name, default=None):
        return self.get(name, default)


config = Config(
    'config.json',
    defaults={
        'juice_height': 600
    },
    fixed={
        'juice_width': 300,
        'pitchersboard_width': 640,
        'pitchersboard_height': 480,
    }
)
