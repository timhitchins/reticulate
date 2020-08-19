
_callback = None

class ReticulateMetaLoader(object):
  
  @classmethod
  def find_spec(cls, fullname, path=None, target=None):
    global _callback
    _callback(fullname, path)
    return None
  
  @classmethod
  def find_module(fullname, path=None):
    global _callback
    _callback(fullname, path)
    return None

def set_callback(callback):
  global _callback
  _callback = callback
