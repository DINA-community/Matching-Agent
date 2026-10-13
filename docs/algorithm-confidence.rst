Confidence
==========

Product
^^^^^^^

When asset data is not labeled sufficiently for a direct match, the product name is used (see :ref:`algorithm workflow <fig-algo-workflow>`).
The goal is to identify the core elements of a product by excluding PIH (Product Identification Helper) and product versioning.

.. list-table:: String-Matcher for Product Name
   :widths: 50 50
   :header-rows: 1

   * - Attributes to Identify
     - Attributes Excluded
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
   * - -
     - ``part_numbers``

Each attribute is assigned a confidence level for matching against a CSAF document, following the logic of the String-Matcher.

.. image:: https://img.shields.io/badge/Manufacturer-green?style=plastic
   :alt: Manufacturer

.. image:: https://img.shields.io/badge/Device_Family-darkgreen?style=plastic
   :alt: Device Family

.. image:: https://img.shields.io/badge/Model-orange?style=plastic
   :alt: Model

.. image:: https://img.shields.io/badge/Model_Numbers-grey?style=plastic
   :alt: Model Numbers

.. image:: https://img.shields.io/badge/Model_Specification-red?style=plastic
   :alt: Model Specification

The colors provide a visual representation of the confidence level. These colors indicate different matching reasons, which is critical for determining whether a match is a true positive or a false positive.

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Confidence
     - Description
   * - .. image:: https://img.shields.io/badge/Exact-darkgreen?style=plastic
        :alt: Exact
       
     - **Exact match.** Includes direct matching via user-defined lookup tables.
   * - .. image:: https://img.shields.io/badge/Indirect-green?style=plastic
        :alt: Indirect
       
     -  **Indirect match.** e.g., the manufacturer is identified as Siemens for a SCALANCE model.
   * - .. image:: https://img.shields.io/badge/Partial-orange?style=plastic
        :alt: Partial
       
     -  **Partial match.** String comparison strategies yield a match score above the defined threshold.
   * - .. image:: https://img.shields.io/badge/Inconclusive-grey?style=plastic
        :alt: Inconclusive
       
     -  **Inconclusive.** No match with sufficient confidence. This typically occurs when evaluating the final attribute (e.g., Model Specifications) or when the next best available case was selected by default.
   * - .. image:: https://img.shields.io/badge/No_Match-red?style=plastic
        :alt: No Match
       
     -  **No Match.** The confidence score is below the required threshold.

.. note::
   The matching process is case-insensitive and ignores dashes, as these are not consistently maintained in human-managed databases. However, this does not apply to PIH-based investigations (see `SBOM Matching Interface <https://github.com/oxisto/csaf/blob/guidance-sbom-matching/csaf_2.0/guidance/sbom-matching-interface.md>`_).

Version
^^^^^^^

.. csv-table:: Version Matching Confidence
   :header: "CSAF Version","Asset Version","Explanation","Confidence"

   "Empty","Empty","Both csaf_version and asset_version are Empty","default_affected"
   "Invalid/None","Invalid/None","Either csaf_version or asset_version is invalid or None.","invalid_version"
   "Empty","Valid","CSAF is missing, but asset version is provided.","default_affected"
   "Valid","Empty","CSAF is provided, but asset version is empty.","default_affected"
   "Valid","Valid","Check if asset version ranges are contained within CSAF version ranges.","verified_not-affected | verified_affected"

Missing or invalid version information (empty/invalid) should not automatically trigger a mismatch.
A mismatch should only be declared when a definitive conflict is identified (the "valid/valid" case).
In such instances, the match should be explicitly marked as a no-match with the reason ``verified_not-affected``.