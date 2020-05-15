from regCompile import *
from classRef.localCache import *
data = local_cache('tmp/reg/forest/400')
tree = data['tree']

regCompiler(tree, 0, 'tmp/regExe.py')

