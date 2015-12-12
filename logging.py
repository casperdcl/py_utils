"""
Simple logging similar to BOOST_LOG_TRIVIAL(lvl)

# Example Usage:

```
>>> from logging import *
>>> LOG = logger(debug, sys.stdout)  # optional: max output level and redirect
>>> LOG(info, 'Some message: %.2f, %d/%d', 3.141592, 3, 10)
info | Some message: 3.14, 3/10

>>> LOG(trace, 'More')
>>> LOG(warning, 'Even More')
warning | Even More

```
"""

import sys
__all__ = ['trace', 'debug', 'info', 'warning', 'error', 'fatal', 'logger']
__author__ = 'Casper da Costa-Luis <casper.dcl@physics.org>'
__copyright__ = 'CC-BY-3.0'


trace, debug, info, warning, error, fatal = range(6)


def logger(max_lvl=trace, fp=sys.stdout):
  """
  Parameters
  ----------
  max_lvl  : Enum, optional
    levels: [default: trace], debug, info, warning, error, fatal.
  fp  : ostream, optional
    Output stream (must have `write` method) [default: sys.stdout].

  Returns
  -------
  LOG  : function

    Parameters
    ~~~~~~~~~~
    lvl  : Enum
        Current message level.
    fmt  : str
        Format string.
    *args  : Format string arguments.
  """
  def LOG(lvl, fmt, *args):
    if len(__all__) > lvl >= max_lvl >= 0:
      fp.write(__all__[lvl] + ' | ' + (fmt % args) + '\n')
  return LOG
