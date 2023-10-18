import wx
app = wx.App(False, None)
from kicad_nextpcb_new.nextpcb_search_online.partselector import PartSelectorDialog

t = PartSelectorDialog(None)
t.Show()
app.MainLoop()