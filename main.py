import time
from happy import Happy

smiley = Happy()

# This is a form of polymorphis, as the Happy smiley class
# does not have a method called .show(). This means that
# the method .show() of the base class {Smiley} will be
# used in stead. There is no need to specify the base
# class, like in other, statically typed, languages.
smiley.show()

time.sleep(1)
smiley.blink()
