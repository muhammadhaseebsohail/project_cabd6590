Here is how you can create unit tests for the UserRegistrationForm component using Jest and React Testing Library:

```jsx
import React from 'react';
import { render, fireEvent, waitFor } from '@testing-library/react';
import UserRegistrationForm from './UserRegistrationForm';

describe('UserRegistrationForm', () => {
    const mockSubmit = jest.fn();

    beforeEach(() => {
        mockSubmit.mockClear();
    });

    it('renders correctly', () => {
        const { getByPlaceholderText } = render(<UserRegistrationForm onSubmit={mockSubmit} />);
        expect(getByPlaceholderText('Name')).toBeInTheDocument();
        expect(getByPlaceholderText('Email')).toBeInTheDocument();
        expect(getByPlaceholderText('Password')).toBeInTheDocument();
    });

    it('validates user inputs and shows error messages', async () => {
        const { getByPlaceholderText, getByText, getByRole } = render(<UserRegistrationForm onSubmit={mockSubmit} />);
        fireEvent.input(getByPlaceholderText('Name'), { target: { value: 'ab' } });
        fireEvent.input(getByPlaceholderText('Email'), { target: { value: 'invalidEmail' } });
        fireEvent.input(getByPlaceholderText('Password'), { target: { value: '1234' } });
        fireEvent.click(getByRole('button'));
        await waitFor(() => {
            expect(getByText('Name should be at least 3 characters long')).toBeInTheDocument();
            expect(getByText('Invalid email')).toBeInTheDocument();
            expect(getByText('Password should be at least 5 characters long')).toBeInTheDocument();
        });
    });

    it('submits the form when all fields are valid', () => {
        const { getByPlaceholderText, getByRole } = render(<UserRegistrationForm onSubmit={mockSubmit} />);
        fireEvent.input(getByPlaceholderText('Name'), { target: { value: 'abc' } });
        fireEvent.input(getByPlaceholderText('Email'), { target: { value: 'validEmail@test.com' } });
        fireEvent.input(getByPlaceholderText('Password'), { target: { value: '12345' } });
        fireEvent.click(getByRole('button'));
        expect(mockSubmit).toHaveBeenCalledWith({
            name: 'abc',
            email: 'validEmail@test.com',
            password: '12345',
        });
    });

    it('does not submit the form when onSubmit prop is not provided', () => {
        const consoleSpy = jest.spyOn(console, 'error');
        const { getByRole } = render(<UserRegistrationForm />);
        expect(consoleSpy).toHaveBeenCalledWith('Warning: Failed prop type: The prop `onSubmit` is marked as required in `UserRegistrationForm`, but its value is `undefined`.');
        fireEvent.click(getByRole('button'));
        expect(consoleSpy).toHaveBeenCalledWith('Warning: Failed prop type: The prop `onSubmit` is marked as required in `UserRegistrationForm`, but its value is `undefined`.');
        consoleSpy.mockRestore();
    });
});
```

In these tests, we are checking for:

- Component rendering: We are using the getByPlaceholderText function to check if the inputs are rendered correctly.
- User interactions: We are simulating user input and button click events using the fireEvent function.
- Props validation: We are checking if the component logs an error when the required onSubmit prop is not provided.
- Edge cases: We are testing the edge case where the user inputs are not valid and the form should display error messages.