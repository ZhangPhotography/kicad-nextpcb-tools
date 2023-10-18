import wx
import wx.xrc
import wx.dataview
import requests
import json
import math
import logging
import webbrowser
import io
# ID_MANUAL_MATCH = 7
# ID_REMOVE_PART = 8

from .ui_match_part_panel import UiMatchPartPanel
from kicad_nextpcb_new.button_id import  ID_MANUAL_MATCH, ID_REMOVE_PART, ID_TOGGLE_POS, ID_SAVE_MAPPINGS, ID_EXPORT


class MatchPartView(UiMatchPartPanel):
    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.TAB_TRAVERSAL, name=wx.EmptyString):
        super().__init__(parent, id=id, pos=pos, size=size, style=style, name=name)
        
        self.select_part_button.SetDefault()
        # self.select_part_button.Parent = self.down_toolbar
        self.select_part_button.SetId(ID_MANUAL_MATCH)
        self.down_toolbar.SetToolLongHelp(
            ID_MANUAL_MATCH,
            "Assign MPN number to a part by manual"
        )

        self.down_toolbar.AddControl(self.select_part_button)
        self.down_toolbar.AddSeparator()
        
        self.remove_part_button.SetDefault()
        # self.remove_part_button.Parent = self.down_toolbar
        self.remove_part_button.SetId(ID_REMOVE_PART)

        self.down_toolbar.AddControl(self.remove_part_button)
        self.down_toolbar.SetFocus()
        self.down_toolbar.AddStretchableSpace()

        self.down_toolbar.Realize()

        self.export_csv.SetId(ID_EXPORT)




