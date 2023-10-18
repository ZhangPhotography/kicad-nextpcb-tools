# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class UiSearchPanel
###########################################################################

class UiSearchPanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"MPN", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		bSizer2.Add( self.m_staticText7, 1, wx.ALL|wx.BOTTOM, 5 )

		self.mpn_textctrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), wx.TE_PROCESS_ENTER )
		bSizer2.Add( self.mpn_textctrl, 1, wx.ALL, 5 )


		bSizer8.Add( bSizer2, 2, wx.EXPAND, 5 )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.manufacturer_label = wx.StaticText( self, wx.ID_ANY, u"Manufacturer", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.manufacturer_label.Wrap( -1 )

		bSizer3.Add( self.manufacturer_label, 1, wx.ALL, 5 )

		self.manufacturer = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), wx.TE_PROCESS_ENTER )
		bSizer3.Add( self.manufacturer, 1, wx.ALL, 5 )


		bSizer8.Add( bSizer3, 2, wx.EXPAND, 5 )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.description_label = wx.StaticText( self, wx.ID_ANY, u"Description", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.description_label.Wrap( -1 )

		bSizer4.Add( self.description_label, 1, wx.ALL, 5 )

		self.description = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), wx.TE_PROCESS_ENTER )
		bSizer4.Add( self.description, 1, wx.ALL, 5 )


		bSizer8.Add( bSizer4, 2, wx.EXPAND, 5 )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.package_label = wx.StaticText( self, wx.ID_ANY, u"Package/Footprint", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.package_label.Wrap( -1 )

		bSizer5.Add( self.package_label, 1, wx.ALL, 5 )

		self.package = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), wx.TE_PROCESS_ENTER )
		bSizer5.Add( self.package, 1, wx.ALL, 5 )


		bSizer8.Add( bSizer5, 2, wx.EXPAND, 5 )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		self.search_button = wx.Button( self, wx.ID_ANY, u"Search", wx.DefaultPosition, wx.Size( 100,30 ), 0 )
		bSizer6.Add( self.search_button, 0, wx.TOP, 15 )


		bSizer8.Add( bSizer6, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer8 )
		self.Layout()
		bSizer8.Fit( self )

	def __del__( self ):
		pass
