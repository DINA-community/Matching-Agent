Confidence
=============

In case that asset data is not labeled sufficiently for a direct match, the product name is used (see:ref: `see algorithm workflow<_fig-algo-workflow>`).
Here, the aim is to identify the core elements of a product excluding PIH and product_version:

.. list-table:: String-Matcher for product name
   :header-rows: 1
   :width: 65%
   :widths: auto
   :align: center

   * - Attributes to identify
     - Attributes excluded
   * - ``manufacturer_name``
     - ``version`` (any kind)
   * - ``device_family``
     - ``serial_number``
   * - ``model``
     - ``CPE``
   * - ``model_series``
     - ``PURL``
   * - ``model_specification``
     - ``sbom_urls``
   * -  -
     - ``part_numbers``

Each attributes gets a confidence level for a match with a csaf document equal String-Matcher

.. image:: https://img.shields.io/badge/Manufacturer-green?style=plastic
.. image:: https://img.shields.io/badge/Device_Family-darkgreen?style=plastic
.. image:: https://img.shields.io/badge/Model-orange?style=plastic
.. image:: https://img.shields.io/badge/Model_Numbers-grey?style=plastic
.. image:: https://img.shields.io/badge/Model_Specification-red?style=plastic


In this way, the user can see visual the confidence. The color indicate different matching reasons which is essential 
determining if a match is correct or a False Positive. 

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Confidence
     - Description
   * - .. image:: https://img.shields.io/badge/Exact-darkgreen?style=plastic
        :alt: Exact
     - Exact match. This included direct matching by user lookup-tables.
   * - .. image:: https://img.shields.io/badge/Indirect-green?style=plastic
        :alt: Indirect
     -  Indirect match e.g. manufacturer is Siemens for model SCALANCE
   * - .. image:: https://img.shields.io/badge/Partial-orange?style=plastic
        :alt: 
     -  partial match. The string-comparison strategies provide a match above the
        provided threshold.
   * - .. image:: https://img.shields.io/badge/Inconclusive-grey?style=plastic
        :alt: Inconclusive 
     -  No match with sufficient confidence. Normally given
        when this is the last attribute (e.g. Model Specifications) or if no match 
        was found and the next best case was taken instead.
   * - .. image:: https://img.shields.io/badge/No_Match-red?style=plastic
        :alt: No Match
     -  Confidence is below a threshold value 


Note: The confidence take either case-sensitive nor dashes into account, sicne it is assumed that in a human maintained database it is not meaningfull maintained. 
This is not the case, if PIH are investigated (see https://github.com/oxisto/csaf/blob/guidance-sbom-matching/csaf_2.0/guidance/sbom-matching-interface.md)


Version
-------

.. csv-table:: Version matching confidence
   :header: "CSAF Version","Asset Version","Explanation","Confidence"

   "Empty","Empty","Both csaf_version and asset_version are Empty","default_affected"
   "Invalid/None","Invalid/None","Either csaf_version or asset_version is invalid or None.","invalid_version"
   "Empty","Valid","CSAF is missing, asset is given","default_affected"
   "Valid","Empty","CSAF given, asset empty","default_affected"
   "Valid","Valid","Check if asset version ranges are contained within CSAF version ranges.","verified_not-affected | verified_affected"

Missing version information (empty,invalid) should not lead automatically to a mismatch. The only case, where it should be is when it is
definitely not a match (valid valid case). Then, the match should also be marked as no match with matching reason ``verified_not-affected``.