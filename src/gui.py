# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Oct  8 2012)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import v4l2
import fcntl
import pygame.camera


###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"SimpleGUI", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_FRAME_STYLE ^ wx.MAXIMIZE_BOX ^ wx.RESIZE_BORDER|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.MenuBar = wx.MenuBar( 0 )
		self.FileMenu = wx.Menu()
		self.AboutMenu = wx.MenuItem( self.FileMenu, wx.ID_ANY, u"About", wx.EmptyString, wx.ITEM_NORMAL )
		self.FileMenu.AppendItem( self.AboutMenu )
		
		self.ExitMenu = wx.MenuItem( self.FileMenu, wx.ID_ANY, u"Exit", wx.EmptyString, wx.ITEM_NORMAL )
		self.FileMenu.AppendItem( self.ExitMenu )
		
		self.MenuBar.Append( self.FileMenu, u"File" ) 
		
		self.SetMenuBar( self.MenuBar )
		
		bSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.staticText1 = wx.StaticText( self, wx.ID_ANY, u"Image From Camera:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText1.Wrap( -1 )
		bSizer.Add( self.staticText1, 0, wx.ALL, 5 )
		
		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )
				
		self.PreviewButton = wx.Button( self, wx.ID_ANY, u"Preview", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.PreviewButton, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.CaptureButton = wx.Button( self, wx.ID_ANY, u"Capture", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.CaptureButton, 0, wx.ALL, 5 )
		
		
		bSizer.Add( gSizer1, 1, wx.EXPAND, 5 )
		
		self.staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer.Add( self.staticline1, 0, wx.EXPAND |wx.ALL, 5 )
		
		gSizer2 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.staticText2 = wx.StaticText( self, wx.ID_ANY, u"Image From File:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText2.Wrap( -1 )
		gSizer2.Add( self.staticText2, 0, wx.ALL, 5 )
		
		self.FilePicker = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.jpg", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		gSizer2.Add( self.FilePicker, 0, wx.ALL, 5 )
		
		
		bSizer.Add( gSizer2, 1, wx.EXPAND, 5 )
		
		self.staticline2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer.Add( self.staticline2, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.ImageDisplay = wx.StaticBitmap( self, wx.ID_ANY, wx.BitmapFromImage(wx.EmptyImage(640,480)), wx.DefaultPosition, wx.Size( 640,480 ), 0 )
		bSizer.Add( self.ImageDisplay, 0, wx.ALL, 5 )
		
		self.staticline3 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer.Add( self.staticline3, 0, wx.EXPAND |wx.ALL, 5 )
		
		FeatureComboboxChoices = [u"Rotate 270 degree", u"Rotate 90 degree", u"Rotate 180 degree"]
		self.FeatureCombobox = wx.ComboBox( self, wx.ID_ANY, u"Select Feature", wx.DefaultPosition, wx.DefaultSize, FeatureComboboxChoices, 0 )
		bSizer.Add( self.FeatureCombobox, 0, wx.ALL, 5 )
		
		gSizer3 = wx.GridSizer( 0, 4, 0, 0 )
		
		self.OkButton = wx.Button( self, wx.ID_ANY, u"Ok", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.OkButton, 0, wx.ALL, 5 )
		
		self.ResetButton = wx.Button( self, wx.ID_ANY, u"Reset", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.ResetButton, 0, wx.ALL, 5 )
		
		self.SaveButton = wx.Button( self, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.SaveButton, 0, wx.ALL, 5 )
		
		
		bSizer.Add( gSizer3, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer )
		self.Layout()
		bSizer.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_MENU, self.OnAbout, id = self.AboutMenu.GetId() )
		self.Bind( wx.EVT_MENU, self.OnExit, id = self.ExitMenu.GetId() )
		self.PreviewButton.Bind( wx.EVT_BUTTON, self.OnPreview )
		self.CaptureButton.Bind( wx.EVT_BUTTON, self.OnCapture )
		self.FilePicker.Bind( wx.EVT_FILEPICKER_CHANGED, self.OnFileChange )
		self.OkButton.Bind( wx.EVT_BUTTON, self.OnOk )
		self.ResetButton.Bind( wx.EVT_BUTTON, self.OnReset )
		self.SaveButton.Bind( wx.EVT_BUTTON, self.OnSave )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnAbout( self, event ):
		event.Skip()
	
	def OnExit( self, event ):
		event.Skip()
	
	def OnPreview( self, event ):
		event.Skip()
	
	def OnCapture( self, event ):
		event.Skip()
	
	def OnFileChange( self, event ):
		event.Skip()
	
	def OnOk( self, event ):
		event.Skip()
	
	def OnReset( self, event ):
		event.Skip()
	
	def OnSave( self, event ):
		event.Skip()
	

###########################################################################
## Class CameraDialog
###########################################################################

class CameraDialog ( wx.Dialog ):
	search = dict()
	CameraComboboxChoices = []
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Choose Camera...", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE|wx.STAY_ON_TOP  )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		CameraDialog.camInit(self)
		self.CameraCombobox = wx.ComboBox( self, wx.ID_ANY, u"Select Camera", wx.DefaultPosition, wx.DefaultSize, CameraDialog.CameraComboboxChoices, 0 )
		bSizer2.Add( self.CameraCombobox, 0, wx.ALL, 5 )
		
		self.OkButton = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.OkButton, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer2 )
		self.Layout()
		bSizer2.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.OkButton.Bind( wx.EVT_BUTTON, self.OnOk )
	
	def __del__( self ):
		pass
	
	def camInit(self):
		pygame.camera.init()
		camlist = pygame.camera.list_cameras()
		pygame.quit()
		i=0
		for item in camlist:
			vd = open(item, 'r')
			cp = v4l2.v4l2_capability()
			fcntl.ioctl(vd, v4l2.VIDIOC_QUERYCAP, cp)
			CameraDialog.search[cp.card] = int(item[len(item)-1])
			CameraDialog.CameraComboboxChoices.append(cp.card)
			i=i+1
	# Virtual event handlers, overide them in your derived class
	def OnOk( self, event ):
		event.Skip()
	

