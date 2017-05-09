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

    def read(self, key):
        with open(self.path, 'r') as tmpj:
            data_str = tmpj.read()

        return json.loads(data_str)[key]

    def write(self, args):
        with open(self.path, 'w') as f:
            json.dump(args,f)

    def copy(self, path, ext='.copy'):
        with open(self.path, 'r') as f:
            json_data = json.load(f)

        newPath = self.path + ext

        if os.path.isfile(newPath):
            newPath = newPath + ext

        with open(newPath, 'w') as f:
            f.write(json.dumps(json_data))

    def edit(self, key, newVal):
        with open(self.path, 'r') as f:
            json_data = json.load(f)
            json_data[key] = newVal        

        newPath = self.path + '.tmp'

        if os.path.isfile(newPath):
            os.remove(newPath)

        with open(newPath, 'w') as f: # temporary json with new changes
            f.write(json.dumps(json_data))

        os.remove(self.path)
        os.rename(newPath, self.path) # rename the temporary file onto the original file


'''
test
jsn = pyJson('../../data/data.json')
jsn.edit('description', 'description test')
print jsn.read('description')

print jsn.read('links')[0]['url']

jay = pyJson('./test.json')
jay.write({'one':1, 'two':2})
'''
