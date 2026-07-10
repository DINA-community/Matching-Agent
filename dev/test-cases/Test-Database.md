# Test-Case

The `MatchingTestsample.sql` provides assets for testing the functionality of the matching process. The following products are in the CSAF documents
`icsa-24-352-04` and `icsa-24-338-04`. Therefore, be certain that in ISDuBA the source is set properly to include files from 2024.

In order to load the database into netbox, the `db_overwrite.sh` script can be used. Before using it, docker containers has to be stopped.

| source | vendor | product_name | product_version(_range) | full_product_name_branch | product_id |
|----------|----------|----------|----------|----------|----------|
| icsa-24-338-04 | Mitsubishi Electric | GENESIS64 | <=10.97.3 | Mitsubishi Electric GENESIS64: <= 10.97.3 | CSAFPID-0001 |
| icsa-24-338-04 | Mitsubishi Electric | GENESIS64 | 10.97.2\|10.97.2_CFR1\|10.97.2_CFR2\|10.97.3 | Mitsubishi Electric GENESIS64: 10.97.2\|10.97.2 CFR1\|10.97.2 CFR2\|10.97.3 | CSAFPID-0002 |
| icsa-24-338-04 | Mitsubishi Electric | ICONICS Suite | <=10.97.3 | Mitsubishi Electric ICONICS Suite: <=10.97.3 | CSAFPID-0003 |
| icsa-24-338-04 | Mitsubishi Electric | ICONICS Suite | 10.97.2\|10.97.2_CFR1\|10.97.2_CFR2\|10.97.3 | Mitsubishi Electric ICONICS Suite: 10.97.2\|10.97.2 CFR1\|10.97.2 CFR2\|10.97.3 | CSAFPID-0004 |
| icsa-24-338-04 | Mitsubishi Electric | MC Works64 | vers:all/* | Mitsubishi Electric MC Works64: vers:all/* | CSAFPID-0005 |
| icsa-24-338-04 | Mitsubishi Electric | GENESIS32 | vers:all/* | Mitsubishi Electric GENESIS32: vers:all/* | CSAFPID-0006 |
| icsa-24-338-04 | Mitsubishi Electric | Hyper Historian | <=10.97.3 | Mitsubishi Electric Hyper Historian: <=10.97.3 | CSAFPID-0007 |
| icsa-24-338-04 | Mitsubishi Electric Iconics Digital Solutions | GENESIS64 | <=10.97.3 | Mitsubishi Electric Iconics Digital Solutions GENESIS64: <=10.97.3 | CSAFPID-0008 |
| icsa-24-338-04 | Mitsubishi Electric Iconics Digital Solutions | GENESIS64 | 10.97.2\|10.97.2_CFR1\|10.97.2_CFR2\|10.97.3 | Mitsubishi Electric Iconics Digital Solutions GENESIS64: 10.97.2\|10.97.2 CFR1\|10.97.2 CFR2\|10.97.3 | CSAFPID-0009 |
| icsa-24-338-04 | Mitsubishi Electric Iconics Digital Solutions | ICONICS Suite | <=10.97.3 | Mitsubishi Electric Iconics Digital Solutions ICONICS Suite: <=10.97.3 | CSAFPID-0010 |
| icsa-24-338-04 | Mitsubishi Electric Iconics Digital Solutions | ICONICS Suite | 10.97.2\|10.97.2_CFR1\|10.97.2_CFR2\|10.97.3 | Mitsubishi Electric Iconics Digital Solutions ICONICS Suite: 10.97.2\|10.97.2 CFR1\|10.97.2 CFR2\|10.97.3 | CSAFPID-0011 |
| icsa-24-338-04 | Mitsubishi Electric Iconics Digital Solutions | GENESIS32 | vers:all/* | Mitsubishi Electric Iconics Digital Solutions GENESIS32: vers:all/* | CSAFPID-0012 |
| icsa-24-338-04 | Mitsubishi Electric Iconics Digital Solutions | Hyper Historian | <=10.97.3 | Mitsubishi Electric Iconics Digital Solutions Hyper Historian: <=10.97.3 | CSAFPID-0013 |
| icsa-24-352-04 | Schneider Electric | Modicon Controllers M241 | <5.2.11.29 | Schneider Electric Modicon Controllers M241 Versions prior to 5.2.11.29 | CSAFPID-0001 |
| icsa-24-352-04 | Schneider Electric | Modicon Controllers M251 | <5.2.11.29 | Schneider Electric Modicon Controllers M251 Versions prior to 5.2.11.29 | CSAFPID-0002 |
| icsa-24-352-04 | Schneider Electric | Modicon Controllers M258 | <5.0.4.19 | Modicon Controllers M258 Versions prior to v5.0.4.19 | CSAFPID-0003 |
| icsa-24-352-04 | Schneider Electric | Modicon Controllers M258 | 5.0.4.19 | Modicon Controllers M258 Version v5.0.4.19 | CSAFPID-0004 |
| icsa-24-352-04 | Schneider Electric | Modicon Controllers LMC058 | <5.0.4.19 | Modicon Controllers LMC058 Versions prior to v5.0.4.19 | CSAFPID-0005 |
| icsa-24-352-04 | Schneider Electric | Modicon Controllers LMC058 | 5.0.4.19 | Modicon Controllers LMC058 Version v5.0.4.19 | CSAFPID-0006 |
| icsa-24-352-04 | Schneider Electric | Modicon Controllers M241 | 5.2.11.29 | Schneider Electric Modicon Controllers M241 Version 5.2.11.29 | CSAFPID-0007 |
| icsa-24-352-04 | Schneider Electric | Modicon Controllers M251 | 5.2.11.29 | Schneider Electric Modicon Controllers M251 Version 5.2.11.29 | CSAFPID-0008 |
| icsa-24-352-04 | Schneider Electric | Modicon Controllers M241 |  | Modicon Controllers M241 | CSAFPID-0009 |
| icsa-24-352-04 | Schneider Electric | Modicon Controllers M251 |  | Modicon Controllers M251 | CSAFPID-0010 |
| icsa-24-352-04 | Schneider Electric | Modicon Controllers M258 |  | Modicon Controllers M258 | CSAFPID-0011 |
| icsa-24-352-04 | Schneider Electric | Modicon Controllers LMC058 |  | Modicon Controllers LMC058 | CSAFPID-0012 |