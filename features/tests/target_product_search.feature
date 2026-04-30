# Created by elain at 4/29/2026
Feature: Test cases for Product Search on Target

  Scenario: User can search for a product on Target
    Given Open Target main page
    When Search for tea
    Then Verify search results for tea shown

  Scenario: User sees empty cart message
    Given Open Target main page
    When Click on cart icon
    Then Verify cart is empty message is shown

  Scenario: User can navigate to Sign In
      Given Open Target main page
      When Click Sign In
      And Click Sign In from right side navigation
      Then Verify Sign In form opened


