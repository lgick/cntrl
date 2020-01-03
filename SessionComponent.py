# uncompyle6 version 3.4.1
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  2 2019, 14:32:10) 
# [GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.57)]
# Embedded file name: /Users/versonator/Jenkins/live/output/mac_64_static/Release/python-bundle/MIDI Remote Scripts/Launch_Control_XL/MixerComponent.py
# Compiled at: 2019-04-09 19:23:44
from __future__ import absolute_import, print_function, unicode_literals
from itertools import izip_longest
from _Framework.Control import control_list, ButtonControl
from _Framework.SessionComponent import SessionComponent as SessionComponentBase
from _Framework.ScrollComponent import ScrollComponent

import functools, logging, traceback
logger = logging.getLogger(__name__)
#logger.error('#### !!!!!!!!!!! #########')

class SessionComponent(SessionComponentBase):
    _clip_horisontal_buttons = None
    scene_play_button = ButtonControl()
    scene_stop_button = ButtonControl()

    def __init__(self, *a, **k):
        super(SessionComponent, self).__init__(*a, **k)

        self._clip_horisontal_buttons = ScrollComponent()

        self._clip_horisontal_buttons.scroll_up_button.color = 'Color.NavButtonOn'
        self._clip_horisontal_buttons.scroll_down_button.color = 'Color.NavButtonOn'
        self._clip_horisontal_buttons.scroll_up_button.disabled_color = 'Color.NavButtonOff'
        self._clip_horisontal_buttons.scroll_down_button.disabled_color = 'Color.NavButtonOff'
        self._clip_horisontal_buttons.scroll_up_button.pressed_color = None
        self._clip_horisontal_buttons.scroll_down_button.pressed_color = None

        self._clip_horisontal_buttons.can_scroll_up = self.can_clip_left
        self._clip_horisontal_buttons.can_scroll_down = self.can_clip_right
        self._clip_horisontal_buttons.scroll_up = self.clip_left
        self._clip_horisontal_buttons.scroll_down = self.clip_right

    @scene_play_button.pressed
    def scene_play_button(self, button):
        tracks = self.song().tracks
        track_offset = self.track_offset()
        scene_offset = self.scene_offset()

        for x in xrange(self._num_tracks):
            clip = tracks[track_offset + x].clip_slots[scene_offset]
            if clip.has_clip:
                clip.fire()

    @scene_stop_button.pressed
    def scene_stop_button(self, button):
        scenes = self.song().scenes
        tracks = self.song().tracks
        track_offset = self.track_offset()
        scene_offset = self.scene_offset()

        for x in xrange(self._num_tracks):
            clip = tracks[track_offset + x].clip_slots[scene_offset]
            if clip.is_playing:
                clip.stop()

    def on_selected_scene_changed(self):
        super(SessionComponent, self).on_selected_scene_changed()
        if self._clip_horisontal_buttons:
            self._clip_horisontal_buttons.update()

    def can_clip_left(self):
        selected_track = self.song().view.selected_track
        tracks = self.song().tracks
        return selected_track != tracks[0]

    def can_clip_right(self):
        selected_track = self.song().view.selected_track
        tracks = self.song().tracks
        return selected_track != tracks[(-1)]

    def clip_left(self):
        selected_track = self.song().view.selected_track
        tracks = self.song().tracks

        if selected_track in tracks:
            index = list(tracks).index(selected_track) - 1
        else:
            index = self.track_offset()

        for track in tracks:
            track.arm = False

        self.song().view.selected_track = tracks[index]
        self.song().view.selected_track.arm = True

    def clip_right(self):
        selected_track = self.song().view.selected_track
        tracks = self.song().tracks

        if selected_track in tracks:
            index = list(tracks).index(selected_track) + 1
        else:
            index = self.track_offset()

        for track in tracks:
            track.arm = False

        self.song().view.selected_track = tracks[index]
        self.song().view.selected_track.arm = True

    def clear_buttons(self):
        return

    def set_clip_left_button(self, button):
        self._clip_horisontal_buttons.set_scroll_up_button(button)

    def set_clip_right_button(self, button):
        self._clip_horisontal_buttons.set_scroll_down_button(button)

    def set_page_left_button(self, button):
        if button:
            button.set_on_off_values('Color.NavButtonOn', 'Color.NavButtonOff')

        self._page_left_button = button
        self._horizontal_paginator.set_scroll_up_button(button)

    def set_page_right_button(self, button):
        if button:
            button.set_on_off_values('Color.NavButtonOn', 'Color.NavButtonOff')

        self._page_right_button = button
        self._horizontal_paginator.set_scroll_down_button(button)

    def set_track_bank_left_button(self, button):
        if button:
            button.set_on_off_values('Color.NavButtonOn', 'Color.NavButtonOff')

        self._bank_left_button = button
        self._horizontal_banking.set_scroll_up_button(button)

    def set_track_bank_right_button(self, button):
        if button:
            button.set_on_off_values('Color.NavButtonOn', 'Color.NavButtonOff')

        self._bank_right_button = button
        self._horizontal_banking.set_scroll_down_button(button)

    def set_scene_play_button(self, button):
        if button:
            self.scene_play_button.set_control_element(button)

    def set_scene_stop_button(self, button):
        if button:
            self.scene_stop_button.set_control_element(button)

    def set_offsets(self, track_offset, scene_offset):
        super(SessionComponent, self).set_offsets(track_offset, scene_offset)
        if scene_offset != None:
            scenes = self.song().scenes
            self.song().view.selected_scene = scenes[scene_offset]

