from kicad_nextpcb_new.mainwindow import NextPCBTools
import wx
app = wx.App(False, None)

t = NextPCBTools(None)
t.Show()
app.MainLoop()