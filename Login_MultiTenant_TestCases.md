Test Case 01 – Verify Successful User Login

Description:
This test case verifies that a user is able to log in successfully using valid credentials.

Precondition:

User account exists and is active

Application login page is accessible

Test Steps:

Navigate to the WorkflowPro login page

Enter a valid email ID and password

Click on the Login button

Expected Result:

User is successfully authenticated

User is redirected to the dashboard page

A welcome message or user-specific indicator is displayed on the dashboard

Test Case 02 – Verify Multi-Tenant Data Isolation

Description:
This test case ensures that tenant-level data isolation is maintained and users can access only their own organization’s data.

Precondition:

Multiple tenant accounts (e.g., Company1 and Company2) are available

User credentials for Company2 are valid

Test Steps:

Navigate to the WorkflowPro login page

Log in using valid credentials of a Company2 user

Navigate to the dashboard or projects section

Expected Result:

User is logged in successfully

Only Company2-specific projects and data are visible

No data belonging to other tenants is accessible or displayed
