# Created by elain at 4/30/2026
Feature: Cart Test Cases
  # Enter feature description here

  Scenario: User sees empty cart message
    Given Open Target main page
    When Click on cart icon
    Then Verify cart is empty message is shown
    # Enter steps here