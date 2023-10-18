import wx
import wx.xrc
import wx.dataview
from .ui_part_details_panel import UiPartDetailsPanel
import wx.dataview as dv


class PartDetailsView(UiPartDetailsPanel):
    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.TAB_TRAVERSAL, name=wx.EmptyString):
        super().__init__(parent, id=id, pos=pos, size=size, style=style, name=name)


           
        self.property = self.data_list.AppendTextColumn(
            "Property",width=200, mode=dv.DATAVIEW_CELL_ACTIVATABLE, align=wx.ALIGN_LEFT
        )
        self.value = self.data_list.AppendTextColumn(
            "Value",width=-1, mode=dv.DATAVIEW_CELL_ACTIVATABLE, align=wx.ALIGN_LEFT
        )

        self.info = {"","",""}
        parameters = {
            "goodsName": "MPN",
            "providerName": "Manufacturer",
            "goodsDesc": "Description",
            "encap": "Package / Footprint",
            "categoryName": "Category",
            "stockNumber": "Stock",
            "minBuynum": "Minimum Order Quantity(MOQ)",
        }
        for k, v in parameters.items():
            # val = self.info.get(k, "-")
            # if val != "null" and val:
            #     self.data_list.AppendItem([v, str(val)])
            # else:
                self.data_list.AppendItem([v, "-"])





