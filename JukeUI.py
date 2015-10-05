#!/usr/bin/env python3

"""This script contains the GUI builder for the jukebox program. It is powered
by GTK for simplicity. It contains classes for all the screens that might be
required by the main script."""

from gi.repository import Gtk

class jukeBox(Gtk.Window):
  """The class for the main screen"""
  
  def __init__(self):
    Gtk.Window(self, title='2MuchFunk')
    
    self.mainBox = Gtk.Box(spacing=0)
    self.add(self.mainBox)
    
    self.topBar = Gtk.Box(spacing=6)
    self.mainBox.pack_start(self.topBar)
    
    self.sep1 = Gtk.Separator(orientation='horizontal')
    self.mainBox.pack_start(self.sep1)
    
    