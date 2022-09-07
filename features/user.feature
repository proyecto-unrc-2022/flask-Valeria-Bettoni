Feature: Handle storing, retrieving and deleting customer details # test/features/user.feature:1

  Scenario: Retrieve a customers details
    Given some users are in the system
    When I retrieve the customer 'jasonb'
    Then I should get a '200' response
    And the following user details are returned:
      | name        |
      | Jason Borne |


  Scenario: Add a new user
    Given a user that is not in the system
    When I add the new user 'Katy Perry'
    Then I should get a '200' response
    And the following user details are returned:
      | new user   |
      | Katy Perry |


  Scenario: Update a user from USERS
    Given A list of customers and a new data from customer
    When I update customer
    Then I should get a '200' response
    And update user details are returned:
      | name        |
      | Jhon Bourne |


  Scenario: Delete a existing user
    Given A list of users and a user to delete
    When delete user
    Then I should get a '200' response
    And user are not in the list of users 


Scenario: List all the users 
      Given a list of customers stored in the system
      When i want to show them 
      Then i want a '200' response
      And the following list:
        | names                  |
        | Jason Bourne           |
        | Katy Perry             |