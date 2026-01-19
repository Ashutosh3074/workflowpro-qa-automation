Objective

The objective of this test plan is to ensure the reliability and correctness of the WorkflowPro application’s login process and multi-tenant access control. Automated tests will be executed to confirm that users can authenticate successfully and access only the data and dashboards associated with their respective tenants.

Scope

The testing scope includes the following functional areas:

User Authentication:
Verification of login functionality using valid and invalid credentials.

Dashboard Access:
Validation that authenticated users are redirected to the correct dashboard after login.

Tenant-Specific Data Visibility:
Ensuring users can view only the data and resources assigned to their tenant and cannot access data from other tenants.

Out of Scope

The following areas are excluded from this test plan:

Performance Testing: Load, stress, and scalability testing

Security Testing: Vulnerability assessment and penetration testing

Mobile Testing: Validation on mobile devices or mobile browsers

Test Types

The following testing types will be performed:

Smoke Testing:
To verify that critical functionalities such as login and dashboard access work as expected after each build.

Functional Testing:
To validate all defined functional requirements related to authentication and tenant access.

Regression Testing:
To ensure that new changes do not break existing functionality.

Test Environment

Tests will be executed in the following environment:

Browser: Chromium (Headless mode)

Operating System: Linux and Windows

Automation Framework: Playwright integrated with PyTest

Entry and Exit Criteria

Entry Criteria:

WorkflowPro application is deployed and accessible

Test environment is stable

Valid test user accounts for multiple tenants are available

Exit Criteria:

All planned and critical test cases are executed

No open blocker or critical defects remain

Test results are reviewed and approved
