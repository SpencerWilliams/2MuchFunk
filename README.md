# 2MuchFunk
Software for the WTSC Jukebox

Background:
This is to be the full high-level programming for the WTSC jukebox, running Debian Jessie with Cinnamon. Ideally, it will
run without a dektop environment to conserve resources (and make it that much harder to hack). The program is to be
written in a high-level, easily readable and modifiable scripting language (Python 3). The audio will be played by VLC,
and GTK will be used for graphics.

Operation:
It will be controlled by a simple interface, with only volume control accessable at all times. By default it will play
the WTSC online stream (http://radio.clarkson.edu/wtsc.m3u). When a quarter is inserted, it will present the user with
two options: choose {some selected number} of songs, or pass through an auxiliary signal for {some selected number} of
minutes.

Maintenance:
Status notifications will be sent to maintainers by email, and usage stats will be stored locally. Eventually a website
interface would be more convenient, but this is not a priority. The exact frequency of email updates depends on usage,
but daily might be a good place to start.
