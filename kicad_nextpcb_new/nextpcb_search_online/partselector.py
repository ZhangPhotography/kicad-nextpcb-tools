import wx
import wx.xrc
# from kicad_nextpcb_new.page_layout.ui_part_details_panel.ui_part_details_panel import UiPartDetailsPanel
# from kicad_nextpcb_new.page_layout.ui_part_list_panel.ui_part_list_panel import UiPartListPanel
#from kicad_nextpcb_new.page_layout.ui_search_panel.ui_search_panel import UiSearchPanel

from .ui_search_panel.search_view import SearchView
from .ui_part_details_panel.part_details_view import PartDetailsView
from .ui_part_list_panel.part_list_view import PartListView


class PartSelectorDialog(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY,
                          title=u"NextPCB Search Online", pos=wx.DefaultPosition,
                          size=wx.Size(1200, 800), style=wx.DEFAULT_DIALOG_STYLE)
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
      
        # self.search_panel = UiSearchPanel(self)
        # self.part_details_panel = UiPartDetailsPanel(self) 
        # self.part_list_panel = UiPartListPanel(self)  
        self.search_view = SearchView(self)
        self.part_details_view = PartDetailsView(self)
        self.part_list_view = PartListView(self) 

        main_sizer = wx.BoxSizer( wx.VERTICAL )
        main_sizer.Add( self.search_view, 1, wx.EXPAND |wx.ALL, 5 )

        bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
        bSizer2.Add( self.part_list_view, 2, wx.EXPAND |wx.ALL, 5 )
        bSizer2.Add( self.part_details_view, 1, wx.EXPAND |wx.ALL, 5 )
        main_sizer.Add( bSizer2, 20, wx.EXPAND, 5 )
        self.SetSizer( main_sizer )
        self.Layout()
        self.Centre( wx.BOTH )
        