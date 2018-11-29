########################################################################################
# Cute is a minimal Cucumber feature/steps implementation, without pretty much anything
# that can be called 'implementation'. Parts borrowed from 'pea' by Tim Cuthbertson,
# removed dependencies to Nose, World and unittest (so in other words, cut it loose).
#
# Rudi Niemeijer - april 2018
# Todo:
# - Use colors
# - Catch the Fails and Successes of each RUN
# - Write output to log
########################################################################################

__all__ = [
    'step',
    'steps',
    'Given',
    'When',
    'Then',
    'And'
]

class stepCollection(object):
    def __setattr__(self, attr, val):
        if hasattr(self, attr):
            raise RuntimeError("Step %s is already in use!" % (attr,))
        return super(stepCollection, self).__setattr__(attr, val)

class object(object): pass

steps = stepCollection()

class stepCollectionWrapper(object):
    def __init__(self, prefix):
        self._prefix = prefix

    def __getattr__(self, a):
        attr = getattr(steps, a)
        return attr(self._prefix)

Given = stepCollectionWrapper('Given')
When = stepCollectionWrapper('When')
Then = stepCollectionWrapper('Then')
And = stepCollectionWrapper('And')

def step(func):
    #print('Added stepdescription %s' % (func.__name__))
    setattr(steps, func.__name__, lambda prefix: withFormatting(prefix, func))
    return func

def withFormatting(prefix, func):
    def _run(*arguments, **kw):
        name = func.__name__.replace('_', ' ')
        
        def formattedStepResult():
            formattedString = prefix + ' ' + name
            if prefix == 'Given':
                formattedString = '\n' + formattedString    

            if not 'undisclosed arguments' in name: #another crude hack to prevent long lists from being printed
                if arguments:
                    a = 1
                    for arg in arguments:
                        if type(arg) is list:
                            argtext = "(list)"
                        elif type(arg) is tuple:
                            argtext = "(tuple)"
                        elif type(arg) is set:
                            argtext = "(set)"
                        elif type(arg) is dict:
                            argtext = "(dictionary)"
                        else:
                            argtext = str(arg)
                        if a == 2:
                            if len(arguments) == 2:
                                formattedString = formattedString + " with value '" + argtext + "'"
                            else:
                                formattedString = formattedString + " with values '" + argtext + "'"
                                
                        if a > 2:
                            if ('credentials' in formattedString) and (a == 3): # Crude hack, but now we're KSP compliant
                                formattedString = formattedString + ", '********'"
                            else:
                                formattedString = formattedString + ", '" + argtext + "'"

                        a = a + 1



            return formattedString
        
        try:
            returnValue = func(*arguments, **kw)
            print(formattedStepResult())
            return returnValue
        except:
            print(formattedStepResult())
            raise
    return _run
