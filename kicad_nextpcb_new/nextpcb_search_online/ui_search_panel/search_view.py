import wx
import wx.xrc
import threading
import requests
import json
from requests.exceptions import Timeout
from kicad_nextpcb_new.icons import GetImagePath

from .ui_search_panel import UiSearchPanel
from ..ui_part_list_panel.part_list_view import PartListView


class SearchView(UiSearchPanel):
    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.TAB_TRAVERSAL, name=wx.EmptyString):
        super().__init__(parent, id=id, pos=pos, size=size, style=style, name=name)
        self.part_list_view = PartListView(self)


        self.mpn_textctrl.SetHint("e.g. 123456")
        self.manufacturer.SetHint("e.g. Vishay")
        self.description.SetHint("e.g. 100nF")
        self.package.SetHint("e.g. 0806")
        self.search_button.SetBitmap( wx.Bitmap((self.GetImagePath("nextpcb-search.png")), wx.BITMAP_TYPE_ANY ) )


        self.mpn_textctrl.Bind(wx.EVT_TEXT_ENTER, self.search)
        self.manufacturer.Bind(wx.EVT_TEXT_ENTER, self.search)
        self.description.Bind(wx.EVT_TEXT_ENTER, self.search)
        self.package.Bind(wx.EVT_TEXT_ENTER, self.search)
        self.search_button.Bind(wx.EVT_BUTTON, self.search)


    def search(self, e):
        """Search the library for parts that meet the search criteria."""
        search_keyword = ""
        # for word in self.part_info:
        for word in [
            self.mpn_textctrl.GetValue(),
            self.manufacturer.GetValue(),
            self.description.GetValue(),
            self.package.GetValue()
        ]:
            if word:
                search_keyword += str(word + " ")
        # if self.current_page == 0:
        #     self.page = 1 
        # else:
        #     self.page = self.current_page
        self.page = 1 
        body = {
            # "keyword": search_keyword,
            # "limit": 150,
            # "page": self.page,
            # "supplier": [],
            # "supplierSort": []
            "keyword": "C",
            "limit": 150,
            "page": self.page,
            "supplier": [],
            "supplierSort": []
        }
        
        url = "http://127.0.0.1:8080/edapluginsapi/v1/stock/search"
        self.search_button.Disable()
        try:
            #wx.MessageBox(f"explain：{self.search_api_request(url, body)}", "Help", style=wx.ICON_INFORMATION)
            threading.Thread(target=self.search_api_request(url, body)).start()
        finally:
            wx.EndBusyCursor()
            self.search_button.Enable()



    def search_api_request(self, url, data):
        wx.CallAfter(wx.BeginBusyCursor)

        headers = {
            "Content-Type": "application/json",
        }
        body_json = json.dumps(data, indent=None, ensure_ascii=False)
        #wx.MessageBox(f"{body_json}", "Help", style=wx.ICON_INFORMATION)
        try:
            response = requests.post(
                url,
                headers=headers,
                data=body_json,
                timeout=10
            )
            
        except Timeout:

            self.report_part_search_error("HTTP response timeout")

        if response.status_code != 200:
            self.report_part_search_error("non-OK HTTP response status")
            return
        data = response.json()
        ##wx.MessageBox(f"data{data}", "Help", style=wx.ICON_INFORMATION)
        if not data.get("result", {}):
            self.report_part_search_error(
                "returned JSON data does not have expected 'result' attribute"
            )
        if not data.get("result").get("stockList"):
            self.report_part_search_error(
                "returned JSON data does not have expected 'stockList' attribute"
            )
        self.total_num = data.get("result").get("total", 0)
        
        self.search_part_list = data.get("result").get("stockList", [])
        # self.part_list_view.populate(self.search_part_list)
        wx.CallAfter(self.part_list_view.populate_part_list(self.total_num,self.search_part_list))
        wx.CallAfter(wx.EndBusyCursor)   


    def report_part_search_error(self, reason):
        wx.MessageBox(
            f"Failed to download part detail from the NextPCB API ({reason})\r\n"
            # f"We looked for a part named:\r\n{self.part}\r\n[hint: did you fill in the NextPCB field correctly?]",
            "Error",
            style=wx.ICON_ERROR,
        )
        wx.CallAfter(wx.EndBusyCursor)
        wx.CallAfter(self.search_button.Enable())
        return
    



    def GetImagePath(self, bitmap_path):
        return GetImagePath(bitmap_path)