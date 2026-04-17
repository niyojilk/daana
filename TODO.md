# TODO List

## Features to Implement
1. **User Authentication System**
   - Implement secure login/registration system
   - Add session management and token-based authentication
   - Priority: High
   - Technical Debt: Needs secure password storage and rate limiting

2. **Monk/Helper Management System**
   - Create CRUD operations for managing temple staff
   - Add availability calendar for monks/helpers
   - Priority: Medium
   - Testing: Requires unit tests for all CRUD operations

3. **Booking System Enhancements**
   - Implement payment integration
   - Add booking confirmation emails
   - Priority: High
   - CI/CD: Needs integration with payment gateway APIs

## Technical Debt
1. **Refactor Server Configuration**
   - Move hardcoded values to environment variables
   - Improve error handling in server.py
   - Priority: Medium

2. **Improve Test Coverage**
   - Add missing unit tests for core functionality
   - Implement integration tests for API endpoints
   - Priority: High

## Documentation
1. **Update API Documentation**
   - Create Swagger/OpenAPI spec
   - Add examples for all endpoints
   - Priority: Medium