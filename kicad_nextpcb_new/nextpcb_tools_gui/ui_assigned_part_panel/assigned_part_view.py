import wx
import wx.xrc
import wx.dataview
import requests
import json
import math
import logging
import webbrowser
import io

from .ui_assigned_part_panel import UiAssignedPartPanel
import wx.dataview as dv
from requests.exceptions import Timeout


parameters = {
    "goodsName": "MPN",
    "providerName": "Manufacturer",
    "goodsDesc": "Description",
    "encap": "Package / Footprint",
    "categoryName": "Category",
    "stockNumber": "Stock",
    "minBuynum": "Minimum Order Quantity(MOQ)",
}

class AssignedPartView(UiAssignedPartPanel):
    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.TAB_TRAVERSAL, name=wx.EmptyString):
        super().__init__(parent, id=id, pos=pos, size=size, style=style, name=name)

        
        # ---------------------------------------------------------------------
        # ----------------------- Properties List -----------------------------
        # ---------------------------------------------------------------------
        self.property = self.data_list.AppendTextColumn(
            "Property",width=160, mode=dv.DATAVIEW_CELL_ACTIVATABLE, align=wx.ALIGN_LEFT
        )
        self.value = self.data_list.AppendTextColumn(
            "Value",width=-1, mode=dv.DATAVIEW_CELL_ACTIVATABLE, align=wx.ALIGN_LEFT
        )

        for k,v in parameters.items():
            self.data_list.AppendItem([v, " "])
        self.data_list.AppendItem(
            ["Datasheet", " "]
        )
            

    def on_open_pdf(self, e):
        """Open the linked datasheet PDF on button click."""
        item = self.data_list.GetSelection()
        row = self.data_list.ItemToRow(item)
        Datasheet = self.data_list.GetTextValue(row, 0)
        if self.pdfurl != "-" and Datasheet == "Datasheet":
            self.logger.info("opening %s", str(self.pdfurl))
            webbrowser.open("https:" + self.pdfurl)    

    def get_scaled_bitmap(self, url):
        """Download a picture from a URL and convert it into a wx Bitmap"""
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.9999.999 Safari/537.36'
        }

        content = requests.get(url,headers=header).content
        #content = requests.get(url).content
        io_bytes = io.BytesIO(content)
        image = wx.Image(io_bytes, type=wx.BITMAP_TYPE_ANY)
        # self.part_image.SetSize((width, height+20))
        # image = image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
        result = wx.Bitmap(image)
        return result

    def get_part_data(self,stockID):
        """fetch part data from NextPCB API and parse it into the table, set picture and PDF link"""
        self.stockID =stockID
        if self.stockID == 0:
            # for child in self.GetChildren():
            #     child.Destroy()
            # sizer = self.GetSizer()
            # sizer.Clear()
            for i in range(self.data_list.GetItemCount()):
                self.data_list.DeleteItem(0)
            for k,v in parameters.items():
                self.data_list.AppendItem([v, " "])
            self.data_list.AppendItem(
                ["Datasheet", " "]
            )  
            self.part_image.SetBitmap(wx.NullBitmap)          
            # self.Refresh()
            self.Layout()
            return 
        headers = {
            "Content-Type": "application/json",
        }
        body = {
            "stockId": self.stockID
        }
        body_json = json.dumps(body, indent=None, ensure_ascii=False)
        try:
            response = requests.post(
                "https://edaapi.nextpcb.com/edapluginsapi/v1/stock/detail",
                headers=headers,
                data=body_json,
                timeout=5
            )
            # wx.MessageBox(f"body_json:{body_json}", "Help", style=wx.ICON_INFORMATION)
        except Timeout:
            self.Destroy()
            self.EndModal(wx.ID_OK)
        except Exception as e:
            self.Destroy()
            self.EndModal(wx.ID_OK)

        if response.status_code != 200:
            self.report_part_data_fetch_error("non-OK HTTP response status")

        data = response.json()
        # wx.MessageBox(f"return data detail:{data}", "Help", style=wx.ICON_INFORMATION)
        if not data.get("result"):
            self.report_part_data_fetch_error(
                "returned JSON data does not have expected 'result' attribute"
            )
        if not data.get("result").get("stock"):
            self.report_part_data_fetch_error(
                "returned JSON data does not have expected 'stock' attribute"
            )

        self.info = data.get("result").get("stock", {})
        # parameters = {
        #     "goodsName": "MPN",
        #     "providerName": "Manufacturer",
        #     "goodsDesc": "Description",
        #     "encap": "Package / Footprint",
        #     "categoryName": "Category",
        #     "stockNumber": "Stock",
        #     "minBuynum": "Minimum Order Quantity(MOQ)",
        # }
        for i in range(self.data_list.GetItemCount()):
            self.data_list.DeleteItem(0)
        for k, v in parameters.items():
            val = self.info.get(k, "-")
            if val != "null" and val:
                self.data_list.AppendItem([v, str(val)])
            else:
                self.data_list.AppendItem([v, "-"])
        prices_stair = self.info.get("priceStair", [])
        #wx.MessageBox(f"priceStair:{prices_stair}", "Help", style=wx.ICON_INFORMATION)
        if prices_stair:
            for price in prices_stair:
                moq = price.get("purchase")
                if moq < self.info.get("minBuynum"):
                    continue
                else:
                    self.data_list.AppendItem(
                        [
                            f"NextPCB Stair Price ($) for >{moq}",
                            str(price.get("hkPrice", "0")),
                        ]
                    )
        else:
            self.data_list.AppendItem(
                [
                    f"NextPCB Stair Price ($)",
                    "0",
                ]
            )

        self.pdfurl = self.info.get("docUrl", "-")
        self.pdfurl = "-" if self.pdfurl == "" else self.pdfurl
        self.data_list.AppendItem(
            [
                "Datasheet",
                self.pdfurl,
            ]
        )
        self.data_list.Bind(wx.dataview.EVT_DATAVIEW_ITEM_ACTIVATED, self.on_open_pdf)

        picture = self.info.get("goodsImage", [])
        # wx.MessageBox(f"self.pdfurl{self.pdfurl}", "Help", style=wx.ICON_INFORMATION)
        #wx.MessageBox(f"picture:{picture}", "Help", style=wx.ICON_INFORMATION)
        if picture: 
            picture = "https:" + picture[0]
            #webbrowser.open(picture)
            # Print(self, str(picture)).ShowModal()
            # wx.MessageBox(f"picture:{picture}", "Help", style=wx.ICON_INFORMATION)
            self.part_image.SetBitmap(
                self.get_scaled_bitmap(
                    picture,
                    # 320,
                    # 260,
                )
            )
        self.Layout()

    def report_part_data_fetch_error(self, reason):
        wx.MessageBox(
            f"Failed to download part detail from the NextPCB API ({reason})\r\n"
            f"We looked for a part named:\r\n{self.stockID}\r\n[hint: did you fill in the NextPCB field correctly?]",
            "Error",
            style=wx.ICON_ERROR,
        )
        self.Destroy()
        