#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Video Receiver
# Generated: Mon Apr 21 22:48:36 2014
##################################################

from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import uhd
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from grc_gnuradio import blks2 as grc_blks2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import time
import wx

class video_receiver(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Video Receiver")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 1000000
        self.variable_slider_0 = variable_slider_0 = 50
        self.freq_slider = freq_slider = 4900e6
        self.freq = freq = 2450e6
        self.FILT_0 = FILT_0 = firdes.low_pass(1, samp_rate, 10000, 1000, firdes.WIN_HAMMING, 6.76)
        self.FILT = FILT = firdes.low_pass(1, samp_rate, 10000, 1000, firdes.WIN_HAMMING, 6.76)

        ##################################################
        # Blocks
        ##################################################
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
        	self.GetWin(),
        	baseband_freq=90e6,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=1024,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title="FFT Plot",
        	peak_hold=False,
        )
        self.Add(self.wxgui_fftsink2_0.win)
        _variable_slider_0_sizer = wx.BoxSizer(wx.VERTICAL)
        self._variable_slider_0_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_variable_slider_0_sizer,
        	value=self.variable_slider_0,
        	callback=self.set_variable_slider_0,
        	label='variable_slider_0',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._variable_slider_0_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_variable_slider_0_sizer,
        	value=self.variable_slider_0,
        	callback=self.set_variable_slider_0,
        	minimum=0,
        	maximum=100,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_variable_slider_0_sizer)
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	device_addr="",
        	stream_args=uhd.stream_args(
        		cpu_format="fc32",
        		otw_format="sc16",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_center_freq(90e6, 0)
        self.uhd_usrp_source_0.set_gain(15, 0)
        self.uhd_usrp_source_0.set_antenna("J2", 0)
        _freq_slider_sizer = wx.BoxSizer(wx.VERTICAL)
        self._freq_slider_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_freq_slider_sizer,
        	value=self.freq_slider,
        	callback=self.set_freq_slider,
        	label='freq_slider',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._freq_slider_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_freq_slider_sizer,
        	value=self.freq_slider,
        	callback=self.set_freq_slider,
        	minimum=2450e6,
        	maximum=5000e6,
        	num_steps=10,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_freq_slider_sizer)
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
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, "/home/csc773/vid1.ts", False)
        self.blocks_file_sink_0.set_unbuffered(False)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.digital_ofdm_demod_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.digital_ofdm_demod_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.wxgui_fftsink2_0, 0))


# QT sink close method reimplementation

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_FILT(firdes.low_pass(1, self.samp_rate, 10000, 1000, firdes.WIN_HAMMING, 6.76))
        self.set_FILT_0(firdes.low_pass(1, self.samp_rate, 10000, 1000, firdes.WIN_HAMMING, 6.76))
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)
        self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate)

    def get_variable_slider_0(self):
        return self.variable_slider_0

    def set_variable_slider_0(self, variable_slider_0):
        self.variable_slider_0 = variable_slider_0
        self._variable_slider_0_slider.set_value(self.variable_slider_0)
        self._variable_slider_0_text_box.set_value(self.variable_slider_0)

    def get_freq_slider(self):
        return self.freq_slider

    def set_freq_slider(self, freq_slider):
        self.freq_slider = freq_slider
        self._freq_slider_slider.set_value(self.freq_slider)
        self._freq_slider_text_box.set_value(self.freq_slider)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq

    def get_FILT_0(self):
        return self.FILT_0

    def set_FILT_0(self, FILT_0):
        self.FILT_0 = FILT_0

    def get_FILT(self):
        return self.FILT

    def set_FILT(self, FILT):
        self.FILT = FILT

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
    tb = video_receiver()
    tb.Start(True)
    tb.Wait()

