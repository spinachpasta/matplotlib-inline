from matplotlib.pyplot import figure
import InlineWrapper
import traceback
import program
wrapper=InlineWrapper.InlineWrapper()
try:
    program.main(wrapper)
except Exception:
    traceback.print_exc()
wrapper.serve()
