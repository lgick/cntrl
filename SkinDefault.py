# uncompyle6 version 3.4.1
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  2 2019, 14:32:10) 
# [GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.57)]
# Embedded file name: /Users/versonator/Jenkins/live/output/mac_64_static/Release/python-bundle/MIDI Remote Scripts/Launch_Control_XL/SkinDefault.py
# Compiled at: 2019-04-09 19:23:44
from __future__ import absolute_import, print_function, unicode_literals
from _Framework.Skin import Skin
from _Framework.ButtonElement import Color

class BiLedColors:
    class Color:
        On = Color(127)
        Off = Color(0)

        #13 - red l
        #15 - red h

        #29 - yellow l
        #62 - yellow h

        #47 - amber

        #28 - green l
        #60 - green h

        #controls
        SendsA = Color(13)
        SendsB = Color(15)

        SendControls = Color(62)
        VolumeControls = Color(47)

        DeviceControlOn = Color(15)
        DeviceControlOff = Color(13)

        ToggleView = Color(15)
        SendsVolumesToggle = Color(15)

        TempoControlOn = Color(0)
        TempoControlOff = Color(0)

        CrossControlOn = Color(60)
        CrossControlOff = Color(28)

        PrehearVolumeOn = Color(60)
        PrehearVolumeOff = Color(28)

        MasterVolumeOn = Color(60)
        MasterVolumeOff = Color(28)

        # Device mode
        TrackSelected = Color(60)
        TrackUnselected = Color(62)

        SendSelected = Color(60)
        SendUnselected = Color(29)

        MasterSelected = Color(15)
        MasterUnselected = Color(13)

        DeviceOn = Color(15)
        DeviceOff = Color(13)

        ChangeDeviceOn = Color(60)
        ChangeDeviceOff = Color(28)

        BankOn = Color(60)
        BankOff = Color(28)


        # Mute mode
        SoloOn = Color(60)
        SoloOff = Color(62)

        MuteOn = Color(62)
        MuteOff = Color(60)

        MetronomeOn = Color(62)
        MetronomeOff = Color(29)

        NavButtonOn = Color(60)
        NavButtonOff = Color(28)

        ClipDelete = Color(47)
        ClipStop = Color(47)
        ClipPlay = Color(62)
        RecOn = Color(15)
        RecOff = Color(13)


        # Send mode
        TrackActivatedSend = Color(15)
        TrackUnactivatedSend = Color(47)

        TracksActivatedSend = Color(15)
        TracksUnactivatedSend = Color(47)

        SendMuteOn = Color(28)
        SendMuteOff = Color(60)

        ArmSelected = Color(15)
        ArmUnselected = Color(13)


        # Cross mode
        CrossOn = Color(15)
        CrossOff = Color(0)


def make_biled_skin():
    return Skin(BiLedColors)
