Ponmocup Indicators of Compromise
==================================

This repository contains the indicators of compromise for Ponmocup.

Ponmocup is one of the most successful and longest running botnets of the past decade. First detected in 2006, as Vundo or Virtumonde, and detected as Ponmocup starting in 2011, we believe this is one of the most underestimated botnets still under continuous development.

Though Ponmocup has received a minimal amount of attention from the security community, it is in fact a sophisticated botnet serving different purposes. Though these purposes have often been described as low-risk functionalities, the malware is actually used by a group of sophisticated criminals who use the botnet for various (financials) gains, and are likely conducting a limited amount of targeted attacks.

Full report on the Ponmocup botnet can be found here:

 * http://f0x.nl/ponmocup (short link)
 * http://blog.fox-it.com/2015/12/02/ponmocup-a-giant-hiding-in-the-shadows

### Available IOCs

| filename                                      | description                                                                                              |
|-----------------------------------------------|----------------------------------------------------------------------------------------------------------|
| *[domains.txt](domains.txt)*             | The hardcoded domains used by Ponmocup (used to calculated the real C2 ip) |
| *[resolving_ips.txt](resolving_ips.txt)* | Resolved ip addresses of the ponmocup domains (used to calculate the real C2 ip) |
| *[actual_ips.txt](actual_ips.txt)*  | Calculated C2 ip addresses that Ponmocup will connect to for C2 traffic |
| *[registry_keys.txt](registry_keys.txt)* | Known Windows Registry keys used by Ponmocup |
 
### Available signatures
| filename                                      | description                                                                                              |
|-----------------------------------------------|----------------------------------------------------------------------------------------------------------|
| *[snort_signatures.txt](snort_signatures.txt)* | Contains Snort signatures for detecting Ponmocup |
| *[yara_signatures.txt](yara_signatures.txt)* | Contains Yara signatures to detect Ponmocup (in memory) |


### Availabe STIX Package
| filename                                      | description                                                                                              |
|-----------------------------------------------|------------------------------------------
| *[FoxIT_Ponmocup_STIX_1_2.xml](FoxIT_Ponmocup_STIX_1_2.xml)* | STIX package containing all the indicators and signatures |


