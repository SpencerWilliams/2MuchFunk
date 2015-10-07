#!/usr/bin/env python3

  """This script contains the GUI builder for the jukebox program. It is powered
  by GTK for simplicity. It contains classes for all the screens that might be
  required by the main script.
  Copyright (C) {2015}  {Spencer R Williams}

  This program is free software; you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation; either version 2 of the License, or
  (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License along
  with this program; if not, write to the Free Software Foundation, Inc.,
  51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA."""

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
    
    