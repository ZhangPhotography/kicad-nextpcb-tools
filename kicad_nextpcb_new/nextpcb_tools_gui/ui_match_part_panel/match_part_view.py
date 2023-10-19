import wx
import wx.xrc
import wx.dataview
import os
import csv
import tempfile

bomFileName = 'bom.csv'

from .ui_match_part_panel import UiMatchPartPanel
from kicad_nextpcb_new.button_id import  ID_MANUAL_MATCH, ID_REMOVE_PART, ID_EXPORT


class MatchPartView(UiMatchPartPanel):
    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.TAB_TRAVERSAL, name=wx.EmptyString):
        super().__init__(parent, id=id, pos=pos, size=size, style=style, name=name)

        self.bom = [{
            'Designator': 'C1',
            'Footprint' :'CP_Axial_L10.0mm_D4.5mm_P15.00mm_Horizontal',
            'Quantity': 1,
            'Value':'10uF'
         }]
        
        
        self.select_part_button.SetDefault()
        self.select_part_button.SetId(ID_MANUAL_MATCH)
        self.down_toolbar.SetToolLongHelp(
            ID_MANUAL_MATCH,
            "Assign MPN number to a part by manual"
        )

        self.down_toolbar.AddControl(self.select_part_button)
        self.down_toolbar.AddSeparator()
        
        self.remove_part_button.SetDefault()
        self.remove_part_button.SetId(ID_REMOVE_PART)

        self.down_toolbar.AddControl(self.remove_part_button)
        self.down_toolbar.SetFocus()
        self.down_toolbar.AddStretchableSpace()
        self.down_toolbar.Realize()

        self.export_csv.SetId(ID_EXPORT)

        self.Bind(wx.EVT_BUTTON, self.generate_bom, self.export_csv)


    def generate_bom(self,temp_dir):
        '''Generate the bom file.'''
        # temp_dir = tempfile.mkdtemp()
        temp_dir = 'D:\\KiCad\\7.0\\share\\kicad\\csvdome'
        if len(self.bom) > 0:
            with open((os.path.join(temp_dir, bomFileName)), 'w', newline='', encoding='utf-8-sig') as outfile:
                csv_writer = csv.writer(outfile)
                # writing headers of CSV file
                csv_writer.writerow(self.bom[0].keys())

                # Output all of the component information
                for component in self.bom:
                    # writing data of CSV file
                    if ('**' not in component['Designator']):
                        csv_writer.writerow(component.values())
                # wx.MessageBox(f"outfile:{outfile}", "Help", style=wx.ICON_INFORMATION)



