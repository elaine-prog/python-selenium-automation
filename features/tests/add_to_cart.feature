Feature: Cart Tests

  Scenario: Add product to cart

    Given Open Target main page
    When Search for "toothpaste"
    And Open first product
    And Add product to cart
    Then Verify cart updated
