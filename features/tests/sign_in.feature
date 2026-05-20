Feature: Sign In Tests

  Scenario: Logged out user can access Sign In page

    Given Open Target main page
    When Click Account button
    And Click Sign In or Create Account
    Then Verify Sign In form opened