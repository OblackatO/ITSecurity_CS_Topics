# Definition
The Common Vulnerability Scoring System rates vulnerabilites(CVEs) according to their seveirity, based on established criteria: Base, Temporal and Environmental metrics.

There are different versions of the CVSS system. The most recent one is CVSSv3.1.
CVSSv2 is still used and it is good to be familiar with both versions and their main differences.

# CVSS metrics
- Base score metrics: Represent characteristics of the vulnerability itself. These characteristics **do not change over time, and are not dependent on real world exploitability or on compensating factors** that an enterprise has put into place to prohibit exploit.
- Temporal score metrics: Measure the **current state of exploit techniques or code availability, the existence of any patches or workarounds**, or the confidence in the description of a vulnerability.
- Environmental metrics: **Aspects that might increase or decrease the net severity of a vulnerability.** Environmental metrics are made up of Modified Base Metrics and of Security Requirements.

## CVSSv2 metrics
![CVSSv2 metrics](/CVSS_system/cvss_v2_scoring.png)

## CVSSv3.1 metrics
![CVSSv3 metrics](/CVSS_system/cvss_v3_scoring.png)

Each sub-category of metrics, such as the Attack Vector has its own choices. In this case of the Attack vector there are the following choices:
- Local (AV:L)
- Ajdacent Network (AV:A)
- Network (AV:N)

In order to calculate and see more details about each value available for each metrics category, see:
- NVD [CVSSv2 scoring calculator](https://nvd.nist.gov/vuln-metrics/cvss/v2-calculator)
- NVD [CVSSv3 scoring calculator](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator)


Finally, all the details about the attack vector choices and the remaining sub-sections can be found at:
- [CVSSv2 full documentation](https://www.first.org/cvss/v2/guide)
- [CVSSv3 full documentation](https://www.first.org/cvss/specification-document)


# References  
- [Differences Between CVSSv2 and CVSSv3](https://www.balbix.com/insights/cvss-v2-vs-cvss-v3/)
- [CVSS base score explained](https://www.balbix.com/insights/base-cvss-scores/)
- [CVSS temporal metrics explained](https://www.balbix.com/insights/temporal-cvss-scores/)
- [Environmental CVSS Scores](https://www.balbix.com/insights/environmental-cvss-scores/)
- [A Complete Guide to the Common Vulnerability Scoring System v2.0](https://www.first.org/cvss/v2/guide)
- [Common Vulnerability Scoring System version 3.1: Specification Document CVSS Version 3.1 Release](https://www.first.org/cvss/specification-document)