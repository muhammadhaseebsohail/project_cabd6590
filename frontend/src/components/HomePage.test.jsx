Here are the unit tests for the HomePage component:

```jsx
import React from 'react';
import { render, fireEvent, waitFor, screen } from '@testing-library/react';
import '@testing-library/jest-dom/extend-expect';
import HomePage from './HomePage';

describe("HomePage", () => {
    const mockFetchHomePageData = jest.fn();

    beforeEach(() => {
        jest.clearAllMocks();
    });

    it("renders without crashing", () => {
        render(<HomePage title="Test Title" fetchHomePageData={mockFetchHomePageData} />);
        expect(screen.getByText("Test Title")).toBeInTheDocument();
    });

    it("shows loading state before data is fetched", () => {
        render(<HomePage title="Test Title" fetchHomePageData={mockFetchHomePageData} />);
        expect(screen.getByText("Loading...")).toBeInTheDocument();
    });

    it("displays data when fetched successfully", async () => {
        mockFetchHomePageData.mockResolvedValueOnce("Test data");
        render(<HomePage title="Test Title" fetchHomePageData={mockFetchHomePageData} />);
        await waitFor(() => expect(screen.getByText("Test data")).toBeInTheDocument());
    });

    it("displays error when data fetch fails", async () => {
        mockFetchHomePageData.mockRejectedValueOnce(new Error("Fetch error"));
        render(<HomePage title="Test Title" fetchHomePageData={mockFetchHomePageData} />);
        await waitFor(() => expect(screen.getByText("Error: Fetch error")).toBeInTheDocument());
    });

    it('validates props with PropTypes', () => {
        const error = jest.spyOn(global.console, 'error');
        render(<HomePage />);
        expect(error).toBeCalledWith(expect.stringContaining('Failed prop type'));
    });
});
```

In the above tests, we are:
- Rendering the component and asserting that it doesn't crash
- Asserting that the component shows a loading state before the data is fetched
- Asserting that the component displays fetched data correctly
- Asserting that the component displays an error message when the data fetch fails
- Checking if the component validates its props using PropTypes

And before each test, we are clearing all mocks to ensure a fresh test environment.

Note: Please ensure that you have the necessary dependencies installed (jest, testing-library/react, and testing-library/jest-dom) and you have set up your Jest configuration to run these tests.