# SynthUnprofile: An Add-on for nvda that does <Insert thing here>
#Copyright (C) 2016 derek riemer
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.

"""synthUnprofile:
A global plugin to make the synth settings ring intuitive.
"""

import addonHandler
import config
import synthSettingsRing
import globalVars
import synthDriverHandler
import globalPluginHandler
#We need to initialize translation and localization support:
addonHandler.initTranslation()

oldSynthSetting = synthSettingsRing.SynthSetting
class SynthSetting(oldSynthSetting):
	def _set_value(self,value):
		setattr(self.synth,self.setting.name,value)
		config.conf.profiles[0]["speech"][self.synth.name][self.setting.name]=value

synthSettingsRing.SynthSetting = SynthSetting

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def __init__(self):
		super(GlobalPlugin, self).__init__()
		globalVars.settingsRing = synthSettingsRing.SynthSettingsRing(synthDriverHandler.getSynth())
