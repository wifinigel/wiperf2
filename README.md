# wiperf V2.5

*(Looking for the old pre-v2 docs? Try this: [link](https://github.com/wifinigel/wiperf/tree/v0.10))*

![wiperf hardware](mkdocs/docs/images/hardware.png)

(Main wiperf documentation site : https://wifinigel.github.io/wiperf/)

Wiperf is a utility that can be installed on to a WLAN Pi or a Raspberry Pi to act as a network probe running a series of  network performance tests. It is primarily intended to provide an indication of the end-user experience on a wireless network, but may also be used as a standalone ethernet-connected probe to allow a wired experience to also be tested.

The probe can run the following tests to give an indication of the performance of the network environment into which it has been deployed:

- Wireless connection health check (if wireless connected)
- Speedtest (Ookla/Librespeed)
- iperf3 (TCP & UDP tests)
- ICMP ping
- HTTP
- DNS
- DHCP
- SMB

![Probe Report](mkdocs/docs/images/probe_summary.jpg)

Tests may be performed over the wireless or ethernet interface of the probe unit. The results must then be sent back to a Splunk or InfluxDB server (which we'll call the "data server") to provide a reporting capability. (*NOTE: There is no graphing/reporting capability on the wiperf probe itself*)

Wiperf has been primarily designed to be a tactical tool for engineers to deploy on to a wireless network where perhaps issues are being experienced and some longer term monitoring may be required. It is not designed to replace large-scale commercial offerings that provide wireless and end-user experience monitoring in a far more comprehensive and user-friendly fashion.

Tests are run on the wiperf probe at a configured interval (usually 5 minutes) and collected data is sent back to a data server over a network connection between the probe and data server (no connection = no data collection). The data server must be an instance of either:

- Splunk, or
- InfluxDB with Grafana  

For more information about wiperf, please visit the [wiperf documentation site](https://wifinigel.github.io/wiperf/)

## Further Documentation References

- [wiperf documentation site](https://wifinigel.github.io/wiperf/)

# Credits

- Thanks to [Kristian Roberts](https://uk.linkedin.com/in/krisalexroberts) for his invaluable input, testing and guidance on Splunk. He kicked this whole thing off and it definitely wouldn't have happened without him. A top bloke.
- Thank you to Eric Garnel & James Whitehead for their invaluable contributions to the Grafana dashboards included in this distribution. I could not have put them together without your ideas and JSON code - thank you so much!
- The MOS score code in the UDP iperf test results was kindly donated by Mario Gingras - his time and effort in developing this are very much appreciated. (I wish I'd thought of that!!! Lol).
- Thanks again to Mario Gingras for the SMB testing idea and code - another valuable addition to the feature set of the tool.
- A special mention to Tris Kipling who has been valuable source of feedback and ideas through his field experience of using wiperf. Your efforts, ideas and patience are very much appreciated my friend, thank you.
- Thanks to Neil Mac for constantly kicking the tyres on wiperf and making me think twice about stuff ;-)

# Contributions

Please, get in touch before starting work on any code you'd like to submit as a PR. I love feedback and ideas, but each new feature costs me more cycles to support. Let's agree it can be included before submitting.

# Caveats

This free software is provided for you to use at your own risk. There are no guarantees around its operation, suitability or the data that it provides. Please consult the [license file](License.txt) shipped with this software.

# Developer

Nigel Bowden (WifiNigel): https://wifinigel.blogspot.com
