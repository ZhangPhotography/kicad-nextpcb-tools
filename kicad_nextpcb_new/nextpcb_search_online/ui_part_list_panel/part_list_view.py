import wx
import wx.xrc
import wx.dataview
from .ui_part_list_panel import UiPartListPanel
import wx.dataview as dv
# from kicad_nextpcb_new.nextpcb_search_online.ui_search_panel.search_view import SearchView


class PartListView(UiPartListPanel):
    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.TAB_TRAVERSAL, name=wx.EmptyString):
        super().__init__(parent, id=id, pos=pos, size=size, style=style, name=name)
        self.MPN_stockID_dict = {}
        self.current_page = 0
        self.total_pages = 0

        self.part_list.AppendTextColumn(
            "index",
            width=60, mode=dv.DATAVIEW_CELL_ACTIVATABLE, align=wx.ALIGN_LEFT)
        self.part_list.AppendTextColumn(
            "MPN",
            width=150, mode=dv.DATAVIEW_CELL_ACTIVATABLE, align=wx.ALIGN_CENTER
        )
        self.part_list.AppendTextColumn(
            "Manufacturer",
            width=300, mode=dv.DATAVIEW_CELL_ACTIVATABLE, align=wx.ALIGN_CENTER
        )
        self.part_list.AppendTextColumn(
            "Description",
            width=200, mode=dv.DATAVIEW_CELL_ACTIVATABLE, align=wx.ALIGN_CENTER
        )
        self.part_list.AppendTextColumn(
            "Package/Footprint",
            width=300, mode=dv.DATAVIEW_CELL_ACTIVATABLE, align=wx.ALIGN_CENTER
        )
        self.part_list.AppendTextColumn(
            "Price($)",
            width=150, mode=dv.DATAVIEW_CELL_ACTIVATABLE, align=wx.ALIGN_CENTER
        )
        self.part_list.AppendTextColumn(
            "Stock",
            width=60, mode=dv.DATAVIEW_CELL_ACTIVATABLE, align=wx.ALIGN_CENTER
        )
        self.part_list.AppendTextColumn(
            "Supplier",
            width=60, mode=dv.DATAVIEW_CELL_ACTIVATABLE, align=wx.ALIGN_CENTER
        )

        self.part_list.Bind(
            wx.dataview.EVT_DATAVIEW_COLUMN_HEADER_CLICK, self.OnSortPartList
        )

    def OnSortPartList(self, e):
        """Set order_by to the clicked column and trigger list refresh."""
        self.parent.library.set_order_by(e.GetColumn())
        self.search(None)

    def populate_part_list(self,total_num,search_part_list):
        """Populate the list with the result of the search."""
        self.search_part_list = search_part_list
        #wx.MessageBox(f"data:{self.search_part_list}", "Help", style=wx.ICON_INFORMATION)
        self.part_list.DeleteAllItems()
        # self.MPN_stockID_dict.clear()
        if self.search_part_list is None:
            return
        
        self.result_count.SetLabel(f"{total_num} Results")

        parameters = [
            "goodsName",
            "providerName",
            "goodsDesc",
            "encap",
            "stockNumber"
        ]
        self.item_list = []
        wx.MessageBox(f"self.search_part_list_json{self.search_part_list}", "Help", style=wx.ICON_INFORMATION)
        for idx, part_info in enumerate(self.search_part_list, start=1):
            # if idx > 50 :
                # break
            part = []
            #wx.MessageBox(f"partinfo{part_info}", "Help", style=wx.ICON_INFORMATION)
            for k in parameters:
                #wx.MessageBox(f"k{k}", "Help", style=wx.ICON_INFORMATION)
                val = part_info.get(k, "")
                val = "-" if val == "" else val
                #wx.MessageBox(f"val{val}", "Help", style=wx.ICON_INFORMATION)
                part.append(val)
                #wx.MessageBox(f"row arg{part}", "Help", style=wx.ICON_INFORMATION)
            pricelist = part_info.get("priceStair", [])
            if pricelist:
                stair_num = len(pricelist)
                min_price = (pricelist[stair_num - 1]).get("hkPrice", 0)
            else:
                min_price = 0
            #wx.MessageBox(f"min_price:{min_price}", "Help", style=wx.ICON_INFORMATION)
            part.insert(4, str(min_price))
            suppliername = part_info.get("supplierName", "")
            suppliername = "-" if suppliername == "" else suppliername
            part.insert(6, suppliername)
            #wx.MessageBox(f"part:{part}", "Help", style=wx.ICON_INFORMATION)
            #self.item_list.append(part)
            part.insert(0, f'{idx}')
            self.MPN_stockID_dict["".join(part[:4])] = part_info.get("stockId", 0)
            self.part_list.AppendItem(part)









