import sys
import os

try:
    PLUGIN_ROOT =os.path.dirname(os.path.abspath(__file__))
    if PLUGIN_ROOT not in sys.path:
            sys.path.append(PLUGIN_ROOT)
    from kicad_nextpcb_new.plugin import JLCPCBPlugin
    JLCPCBPlugin().register()
except Exception as e:
    import logging
    logger = logging.getLogger()
    logger.debug(repr(e))

# from kicad_nextpcb_new.plugin import JLCPCBPlugin

# JLCPCBPlugin().register()
# # except Exception as e:
# # LOGGER.debug(repr(e))