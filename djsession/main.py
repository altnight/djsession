from importlib import import_module

import_module('hello')
import_module('app_a.hello')
import_module('app_a.level1.hello')
import_module('app_a.level1.level2.hello')

#__import__('hello')
#__import__('app_a.hello')
#__import__('app_a.level1.hello')
#__import__('app_a.level1.level2.hello')

#import_module('app_a')
#import_module('app_a.level1')
#import_module('app_a.level1.level2')

#__import__('app_a')
#__import__('app_a.level1')
#__import__('app_a.level1.level2')
