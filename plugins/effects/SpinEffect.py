#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# Xibo - Digitial Signage - http://www.xibo.org.uk
# Copyright (C) 2011 Alex Harrington
#
# This file is part of Xibo.
#
# Xibo is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version. 
#
# Xibo is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with Xibo.  If not, see <http://www.gnu.org/licenses/>.
#

from XiboEffect import XiboEffect
from threading import Thread
import math

class SpinEffect(XiboEffect):

    def run(self):
        ## Options
        
        if self.options == {}:
            self.options['speed'] = -5

        # Convert degrees/second speed value in config to radians/second for libavg
        self.options['speed'] = math.radians(float(self.options['speed']))

        self.p.enqueue('anim',('continuous',
                                 self.media,
                                 'angle',
                                 0,
                                 float(self.options['speed'])))

        if self.callback != None:
            try:
                self.callback()
            except:
                self.log.log(0,"error","Exception thrown calling the callback " + self.callback)
