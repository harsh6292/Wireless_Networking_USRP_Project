#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Video Transmitter Loopback
# Generated: Tue Apr 22 12:38:23 2014
##################################################

from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import forms
from grc_gnuradio import blks2 as grc_blks2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import wx

class video_transmitter_loopback(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Video Transmitter Loopback")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.signal = signal = 5000
        self.samp_rate = samp_rate = 384000
        self.rfgain = rfgain = 0
        self.freq = freq = 12e6

        ##################################################
        # Blocks
        ##################################################
        _signal_sizer = wx.BoxSizer(wx.VERTICAL)
        self._signal_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_signal_sizer,
        	value=self.signal,
        	callback=self.set_signal,
        	label='signal',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._signal_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_signal_sizer,
        	value=self.signal,
        	callback=self.set_signal,
        	minimum=0,
        	maximum=32e6,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_signal_sizer)
        _rfgain_sizer = wx.BoxSizer(wx.VERTICAL)
        self._rfgain_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_rfgain_sizer,
        	value=self.rfgain,
        	callback=self.set_rfgain,
        	label='rfgain',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._rfgain_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_rfgain_sizer,
        	value=self.rfgain,
        	callback=self.set_rfgain,
        	minimum=0,
        	maximum=50,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_rfgain_sizer)
        self.digital_ofdm_mod_0 = grc_blks2.packet_mod_b(digital.ofdm_mod(
        		options=grc_blks2.options(
        			modulation="qpsk",
        			fft_length=512,
        			occupied_tones=200,
        			cp_length=128,
        			pad_for_usrp=True,
        			log=None,
        			verbose=None,
        		),
        	),
        	payload_length=0,
        )
        self.digital_ofdm_demod_0 = grc_blks2.packet_demod_b(digital.ofdm_demod(
        		options=grc_blks2.options(
        			modulation="qpsk",
        			fft_length=512,
        			occupied_tones=200,
        			cp_length=128,
        			snr=10,
        			log=None,
        			verbose=None,
        		),
        		callback=lambda ok, payload: self.digital_ofdm_demod_0.recv_pkt(ok, payload),
        	),
        )
        self.blocks_throttle_0_0 = blocks.throttle(gr.sizeof_char*1, samp_rate,True)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, "/home/ece775/video1.ts", True)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, "/home/ece775/sink.ts", False)
        self.blocks_file_sink_0.set_unbuffered(False)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.digital_ofdm_demod_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_throttle_0_0, 0))
        self.connect((self.digital_ofdm_mod_0, 0), (self.digital_ofdm_demod_0, 0))
        self.connect((self.blocks_throttle_0_0, 0), (self.digital_ofdm_mod_0, 0))


# QT sink close method reimplementation

    def get_signal(self):
        return self.signal

    def set_signal(self, signal):
        self.signal = signal
        self._signal_slider.set_value(self.signal)
        self._signal_text_box.set_value(self.signal)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0_0.set_sample_rate(self.samp_rate)

    def get_rfgain(self):
        return self.rfgain

    def set_rfgain(self, rfgain):
        self.rfgain = rfgain
        self._rfgain_slider.set_value(self.rfgain)
        self._rfgain_text_box.set_value(self.rfgain)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = video_transmitter_loopback()
    tb.Start(True)
    tb.Wait()

