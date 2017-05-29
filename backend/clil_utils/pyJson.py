'''
pyJson.py
@author: Nicholas Sollazzo
@version: 1.0
@date: 8/05/17
'''

import json
import os
import os.path


class pyJson(object):
    """docstring for pyJson."""

    def __init__(self, path):
        super(pyJson, self).__init__()
        self.path = path

    def read(self, key=None):
        with open(self.path, 'r') as tmpj:
            data_str = tmpj.read()

        if key is None:
            return json.loads(data_str)  # return all the json
        else:
            return json.loads(data_str)[key]

    def write(self, args, path=None):
        if path is None:
            with open(self.path, 'w') as f:
                f.write(json.dump(args, f))
        else:
            with open(path, 'w') as f:
                f.write(json.dump(args, f))

    def copy(self, ext='copy'):
        with open(self.path, 'r') as f:
            json_data = json.load(f)

        ext = '.' + ext

        newPath = self.path + ext

        if os.path.isfile(newPath):
            newPath = newPath + ext

        with open(newPath, 'w') as f:
            f.write(json.dumps(json_data))

        return newPath

    def edit(self, key, new_val):
        with open(self.path, 'r') as f:
            json_data = json.load(f)
            json_data[key] = new_val

        new_path = self.copy('tmp')

        with open(new_path, 'w') as f:  # temporary json with new changes
            f.write(json.dumps(json_data))

        os.remove(self.path)
        # rename the temporary file onto the original file
        os.rename(new_path, self.path)

    def add(self, key, args):
        with open(self.path, 'r') as f:
            json_data = json.load(f)
            json_elements = json_data[key]

        json_elements.append(args)

        self.edit(key, json_elements)

    def remove(self, key, arg):  # developing

        data = self.read()

        i = -1
        for element in data[key]:
            i += 1
            if arg in element.values():
                del data[key][i]
                break

        self.edit(key, data[key])


'''
test

# edit
jay = pyJson('../../data/data.json')
jay.edit('description', 'description test')
print jay.read('description')

# read a specific element
print jay.read('links')[0]['url']

# write
jay = pyJson('./test.json')
jay.write({'one':1, 'two':2})

# add
new_link = {'title':'test', 'url':'test.com'}
jay.add('links', new_link)

# remove
jay = pyJson('../../data/data.json')
jay.remove('links', 'test')
'''
