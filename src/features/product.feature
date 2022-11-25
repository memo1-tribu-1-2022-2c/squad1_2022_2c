Feature: Product and asociated versions


Scenario: A new product cant be added without having a version
    Given A new product with name ERP and id 4322
    When It is tried to add it the system
    Then It fails because it has no versions

Scenario: New version gets associated with a product
    Given A new product with name ERP and id 3452
    When A version 1.1 is added to it
    Then The version is associated with the product

Scenario: A new product can be added when it has at least one version
    Given A new product with name CRM and id 9999
    When A version 0.5 is added to it
    And It is tried to add it the system
    Then The product gets added to the system

Scenario: All versions of a product are returned
    Given A new product with name CRM and id 231
    And Versions [2.3, 4.5, 6.7, 10.8] associated to it
    When The product versions are retrieved
    Then All versions of the product are shown