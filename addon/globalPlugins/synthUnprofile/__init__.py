# SynthUnprofile: An Add-on for nvda that makes the synth settings ring intuitive
#Copyright (C) 2016 derek riemer
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.

"""synthUnprofile:
A global plugin to make the synth settings ring intuitive.
"""

import config
import globalVars
import globalPluginHandler
import synthDriverHandler
import synthSettingsRing
import tones

class SynthSetting(synthSettingsRing.SynthSetting):
	def _set_value(self,value):
		setattr(self.synth,self.setting.name,value)
		try:
			config.conf.profiles[0]["speech"][self.synth.name][self.setting.name]=value
		except KeyError:
			#Well, this setting doesn't exist at base level, this profile must be for voice, I.E. reading.
			super(SynthSetting, self)._set_value(value)

class SynthSettingsRing(synthSettingsRing.SynthSettingsRing):
	def _get_currentSettingName(self):
		""" returns the current setting's name """
		if self._current is not None and hasattr(self,'settings'):
			name =  self.settings[self._current].setting.displayName
			if isinstance(self.settings[self._current], synthSettingsRing.StringSynthSetting):
				tones.beep(80, 80)
			return name
		return None


synthSettingsRing.SynthSetting = SynthSetting
synthSettingsRing.SynthSettingsRing = SynthSettingsRing

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def __init__(self):
		super(GlobalPlugin, self).__init__()
		globalVars.settingsRing = synthSettingsRing.SynthSettingsRing(synthDriverHandler.getSynth())
