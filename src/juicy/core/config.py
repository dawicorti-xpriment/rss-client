import os
import json


class Config(object):

    def __init__(self, path, defaults=None):
        self._path = os.path.join(
            os.path.expanduser('~'),
            '.juicy',
            path
        )
        if defaults is not None:
            self._data = defaults
        else:
            self._data = {}
        if os.path.exists(self._path):
            with open(self._path) as input_file:
                self._data.update(json.loads(input_file.read()))
        self.save()

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


config = Config('config.json', {
    'juice': {
        'width': 300,
        'height': 600
    },
    'pitchersboard': {
        'width': 600,
        'height': 300,
        'pitchers_url':
        'https://raw.github.com/dawicorti/juicy/master/pitchers.json'
    }
})
