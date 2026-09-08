Tutorial with NetBox
====================

After the setup, you can use NetBox and ISDuBa. Do not start the ``csafsync``, ``assetsync``, and ``csaf_matcher`` APIs yet. 
For tutorial purposes, a small asset setup in NetBox as well as some sample CSAF document data are provided to demonstrate the workflow and features of the NetBox plugins.


Provide ISDuBA Source
----------------------

Instead, go to the ISDuBa setup server (``isduba.localhost`` in dev-setup) in your browser and log in with the provided credentials (``user/user`` in dev-setup).
After logging in, navigate to **Sources** via the left menu bar and select **Upload Documents**. Select the JSON files provided in the ``dev/test-cases/csaf_files`` folder.

.. figure:: images/tutorial-isduba-setup-1.png
   :width: 600px
   :align: center
   :name: isduba-files
   :alt: Upload documents

   Upload documents for a small test setup


Alternatively, you can choose an aggregator. However, keep in mind that this will provide many more CSAF documents. 
For the provided tutorial assets, this is not recommended. 
Use this option only if you have your own asset database and want to check it against a large number of documents. 

.. figure:: images/tutorial-isduba-setup-2.png
   :width: 600px
   :align: center
   :name: aggregators
   :alt: List of aggregators

   List of aggregators. 

In the settings for this :ref:`csaf-aggregator`, delete the IT feed since we focuses on the OT part. 

.. figure:: images/tutorial-isduba-setup-3.png
   :width: 600px
   :align: center
   :name: csaf-aggregator
   :alt: Save Source

   Save a selected source. Here the IT feed of CISA was delisted.

After this, the source is not active yet. Here, the :ref:`checkbox <csaf-cisa-active>` has to be selected.

.. figure:: images/tutorial-isduba-setup-4.png
   :width: 600px
   :align: center
   :name: csaf-cisa-active
   :alt: Activate Source

   Activate source by setting the checkbox by "Active". Also the document age was set to 5 years (default 2 years).


Provide NetBox Database
------------------------

In order to have a small test sample of assets, execute the ``db_overwrite.sh`` script in the ``dev/test-cases`` folder.
The SQL file provides data for device types, module types, and software. Every asset is linked in some way to a device,
which allows possible matches to be displayed there at the end.


NetBox
-------

Start the engine
~~~~~~~~~~~~~~~~


Assuming the setup is completed and the password for ``csaf_matcher_cli`` is set, run the following command to create a user:

.. code-block:: bash

    uv run csaf_matcher_cli user create -u admin

Start the services (see :ref:`Running the services <running-services>`) or via ``script_api.sh`` script in the ``dev/scripts-install`` folder. Navigate to NetBox in your browser.
After logging in (``admin/admin`` in dev-setup), check if the synchronizers are working properly. 
If you encounter any trouble, refer to the provided hints on the screen, consult the :doc:`troubleshooting section <troubleshooting>`, or open an issue.

Investigate the matches
~~~~~~~~~~~~~~~~~~~~~~~~

The CSAF Plugin provides different kinds of views to process CSAF documents and potential matches:


.. list-table::
   :widths: 35 65
   :class: borderless

   * - .. figure:: images/csaf-menu.png
         :width: 300px
         :align: left
         :name: csaf-menu
         :alt: Activate Source

     - **Dashboard**: Overview of all subpages of the models

       **CSAF Documents**: Shows basic information about the documents and matches (new, confirmed, and False Positives)

       **CSAF Matches**: Shows all matches with assets and CSAF documents, including remediation status and the matching reason.

       **CSAF Vulnerabilities**: tbd

       **Devices/Modules/Software with Matches**: Asset list with a summary of matches (new, confirmed, and False Positives).

Alternatively, a single device can be selected via the device view. The process is similar for software and modules.
The user can accept a potential match or mark it as a False Positive. In this small test case, there are 77 potential matches, mostly False Positives.
You can use the filter option to set up rules for a specific device.

.. figure:: images/filter-match-1.png
   :width: 600px
   :align: center
   :name: s
   :alt: Set up a filter rule for potential match results.

   Set up a filter rule for potential match results.

.. figure:: images/filter-match-result-1.png
   :width: 600px
   :align: center
   :name: filtered results
   :alt: Filtered results for particular software, minimum score and description pattern.

   Filtered results for particular software, minimum score and description pattern.

For example, taking the device Nr.5 *Modicon LMC* with the device type *Schneider Electric Modicon Controllers LMC058 5.0.4.19*, CSAFID 6 should be a match.
The other matches should be evaluated due to the wrong series (M241, M251, and M258 for CSAFID 1, CSAFID 2, and CSAFID 4, respectively). 

.. figure:: images/ICSA-24-352-04-matches.png
   :width: 600px
   :align: center
   :name: ICSA-24-352-04-matches
   :alt: Potential matches for device Modicon LMC and the document ICSA-24-352-04

   Potential matches for device ``Modicon LMC`` and the document ICSA-24-352-04

Since we are certain of the False Positives, use the bulk option to mark these CSAFIDs as such. 

.. figure:: images/matches-bulk-operation-fp.png
   :width: 600px
   :align: center
   :name: bulk.-option-fp
   :alt: Set the acceptance status as False Positive by Bulk-option

   Set the acceptance status as False Positive by Bulk-option

If you need the details, the compare function can be used to show further information.

.. figure:: images/ICSA-24-352-04-matches-compare.png
   :width: 600px
   :align: center
   :name: compare-match
   :alt: Compare match with asset and csaf information

   Compare match with asset and csaf information

One upcoming feature is that the user feedback of a match is fed back to the matching agent. 
This improves the reliability of the matching process over time, as the algorithms become better 
at distinguishing between `exact matches` and `partial matches`.

Test Data Set
------------------------

In the present `dev/test-cases/tutorial-1.sql` matches should be seen for the following devices, modules and software.
In order to use this data set, use the `dev/test-cases/db_overwrite.sh` after shut down running API of the matching-agent. 
Be aware, that this will delete your current netbox entries.

Matches
~~~~~~~~~~~~~~~~~~~~~~~~

Running the Matcher should lead to the following matches. 

+-----------------+-------+-----------+----------+---------------------------------------------------------+----------------------+
| CSAF            | ID    | Netbox-ID | Asset    | Type                                                    | Match                |
+=================+=======+===========+==========+=========================================================+======================+
| icsa-24-352-04  | 6     | 5         | Device   | Schneider Electric Modicon Controllers LMC058 5.0.4.19  | right model          |
+-----------------+-------+-----------+----------+---------------------------------------------------------+----------------------+
| icsa-25-007-01  | 7     | 3         | Device   | ABB Nexus Series Nex-2 3.08.00                          | affected version     |
+-----------------+-------+-----------+----------+---------------------------------------------------------+----------------------+
| icsa-25-007-01  | 9     | 3         | Device   | ABB Nexus Series Nex-2 3.08.00                          | affected version     |
+-----------------+-------+-----------+----------+---------------------------------------------------------+----------------------+
| icsa-25-007-01  | 12    | 3         | Device   | ABB Nexus Series Nex-2 3.08.00                          | exact version        |
+-----------------+-------+-----------+----------+---------------------------------------------------------+----------------------+
| icsa-25-007-01  | 7     | 5         | Device   | ABB Nexus Series Nex-2 3.08.01                          | affected version     |
+-----------------+-------+-----------+----------+---------------------------------------------------------+----------------------+
| icsa-25-007-01  | 9     | 5         | Device   | ABB Nexus Series Nex-2 3.08.01                          | exact version        |
+-----------------+-------+-----------+----------+---------------------------------------------------------+----------------------+
| ssa-674753      | 13    | 2         | Module 1 | IM 155-6 PN HF 4.2.0 6AG1155-6AU01-2CN0                 | affected version     |
+-----------------+-------+-----------+----------+---------------------------------------------------------+----------------------+
| ssa-674753      | 16    | 2         | Module 3 | IM 155-6 PN HF TX RAIL 4.2.2 (6AG2155-6AU01-4CN0)       | affected version     |
+-----------------+-------+-----------+----------+---------------------------------------------------------+----------------------+
| icsa-26-008-01  | 1     | 1         | Software | Asset Suite 9.7                                         | affected version     |
+-----------------+-------+-----------+----------+---------------------------------------------------------+----------------------+
| icsa-24-338-04  | 1     | 3         | Software | Mitsubishi Electric GENESIS64: <= 10.97.3               | affected version     |
+-----------------+-------+-----------+----------+---------------------------------------------------------+----------------------+
| icsa-24-338-04  | 2     | 3         | Software | Mitsubishi Electric GENESIS64: x + 10.97.3              | version schema unkown|
+-----------------+-------+-----------+----------+---------------------------------------------------------+----------------------+
| icsa-24-338-04  | 8     | 4         | Software | GENESIS64 10.97.3 (ME Iconics Digital Solutions)        | affected version     |
+-----------------+-------+-----------+----------+---------------------------------------------------------+----------------------+
| icsa-24-338-04  | 9     | 4         | Software | GENESIS64 x + 10.97.3 (ME Iconics Digital Solutions)    | version schema unkown|
+-----------------+-------+-----------+----------+---------------------------------------------------------+----------------------+
| icsa-25-007-01  | 6     | 1,3,6     | Software | ASPECT Enterprise 3.08.00 (ABB)                         | affected version     |
+-----------------+-------+-----------+----------+---------------------------------------------------------+----------------------+

False Positive Matches
~~~~~~~~~~~~~~~~~~~~~~~~

The Matcher probably will also provide the following matches as False Positives. The reason for this is given briefly in the column "Reject MAtch".

+-----------------+-------+-----------+----------+---------------------------------------------------------+-----------------------------------+
| CSAF            | ID    | Netbox-ID | Asset    | Type                                                    | Reject Match                      |
+=================+=======+===========+==========+=========================================================+===================================+
| icsa-24-352-04  | 1     | 5         | Device   | Schneider Electric Modicon Controllers LMC058 5.0.4.19  | wrong model                       |
+-----------------+-------+-----------+----------+---------------------------------------------------------+-----------------------------------+
| icsa-24-352-04  | 2     | 5         | Device   | Schneider Electric Modicon Controllers LMC058 5.0.4.19  | wrong model                       |
+-----------------+-------+-----------+----------+---------------------------------------------------------+-----------------------------------+
| icsa-24-352-04  | 4     | 5         | Device   | Schneider Electric Modicon Controllers LMC058 5.0.4.19  | wrong model                       |
+-----------------+-------+-----------+----------+---------------------------------------------------------+-----------------------------------+
| icsa-24-352-04  | 5     | 5         | Device   | Schneider Electric Modicon Controllers LMC058 5.0.4.19  | version not affected              |
+-----------------+-------+-----------+----------+---------------------------------------------------------+-----------------------------------+
| icsa-24-352-04  | 4     | 5         | Device   | Schneider Electric Modicon Controllers LMC058 5.0.4.19  | wrong model                       |
+-----------------+-------+-----------+----------+---------------------------------------------------------+-----------------------------------+
| icsa-25-007-01  | 8     | 3         | Device   | ABB Nexus Series Nex-2 3.08.00                          | wrong version                     |
+-----------------+-------+-----------+----------+---------------------------------------------------------+-----------------------------------+
| icsa-25-007-01  | 10    | 3         | Device   | ABB Nexus Series Nex-2 3.08.00                          | wrong version                     |
+-----------------+-------+-----------+----------+---------------------------------------------------------+-----------------------------------+
| icsa-25-007-01  | 11    | 3         | Device   | ABB Nexus Series Nex-2 3.08.00                          | wrong version                     |
+-----------------+-------+-----------+----------+---------------------------------------------------------+-----------------------------------+
| icsa-25-007-01  | 13-16 | 3         | Device   | ABB Nexus Series Nex-2 3.08.00                          | wrong model                       |
+-----------------+-------+-----------+----------+---------------------------------------------------------+-----------------------------------+
| ssa-674753      | x     | 1         | N/A      | Siemens SIPLUS ET 200SP                                 | missing modules                   |
+-----------------+-------+-----------+----------+---------------------------------------------------------+-----------------------------------+
| ssa-674753      | 14    | 2         | Module 1 | IM 155-6 PN HF 4.2.0 6AG1155-6AU01-2CN0                 | wrong series / part number        |
+-----------------+-------+-----------+----------+---------------------------------------------------------+-----------------------------------+
| ssa-674753      | 15    | 2         | Module 1 | IM 155-6 PN HF 4.2.0 6AG1155-6AU01-2CN0                 | wrong series / part number        |
+-----------------+-------+-----------+----------+---------------------------------------------------------+-----------------------------------+
| ssa-674753      | 11    | 2         | Module 2 | IM 155-5 PN HF 4.2.0 (6AG1155-5AA00-7AC0)               | wrong model but right part number |
+-----------------+-------+-----------+----------+---------------------------------------------------------+-----------------------------------+
| ssa-674753      | 10-16 | 2         | Device   | Siemens SIPLUS ET 200SP                                 | no model                          |
+-----------------+-------+-----------+----------+---------------------------------------------------------+-----------------------------------+
| icsa-25-345-03  | 1     | 2         | Software | DAQFactory 20.7_Build_2555                              | not installed                     |
+-----------------+-------+-----------+----------+---------------------------------------------------------+-----------------------------------+
| icsa-24-338-04  | 8     | 3         | Software | Mitsubishi Electric GENESIS64: 10.97.3                  | wrong vendor                      |
+-----------------+-------+-----------+----------+---------------------------------------------------------+-----------------------------------+

All products of the provided CSAF documents can be found under `dev/test-cases/tutorial-1_csaf-products.csv` in case the user wants to generate
own test cases based on the given CSAF documents available in this test setup.