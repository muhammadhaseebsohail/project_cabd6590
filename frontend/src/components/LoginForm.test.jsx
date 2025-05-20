Sure, here's how you could write comprehensive tests for this LoginForm component using Jest and React Testing Library:

```jsx
import React from 'react';
import { render, fireEvent, screen } from '@testing-library/react';
import LoginForm from './LoginForm'; // Path to your LoginForm component
import '@testing-library/jest-dom/extend-expect';

// Test for component rendering
test('renders LoginForm component', () => {
  render(<LoginForm onSubmit={jest.fn()} />);
  expect(screen.getByPlaceholderText('Username')).toBeInTheDocument();
  expect(screen.getByPlaceholderText('Password')).toBeInTheDocument();
  expect(screen.getByRole('button', { name: /login/i })).toBeInTheDocument();
});

// Test for user interactions
test('allows the user to fill the form and submit', () => {
  const mockSubmit = jest.fn();
  render(<LoginForm onSubmit={mockSubmit} />);

  fireEvent.change(screen.getByPlaceholderText('Username'), {
    target: { value: 'test-user' },
  });
  fireEvent.change(screen.getByPlaceholderText('Password'), {
    target: { value: 'test-password' },
  });

  fireEvent.click(screen.getByRole('button', { name: /login/i }));

  expect(mockSubmit).toHaveBeenCalledWith({
    username: 'test-user',
    password: 'test-password',
  });
});

// Test for props validation
test('shows an error message if a field is empty', () => {
  const mockSubmit = jest.fn();
  render(<LoginForm onSubmit={mockSubmit} />);

  fireEvent.change(screen.getByPlaceholderText('Username'), {
    target: { value: 'test-user' },
  });

  fireEvent.click(screen.getByRole('button', { name: /login/i }));

  expect(screen.getByText('Both fields are required')).toBeInTheDocument();
  expect(mockSubmit).not.toHaveBeenCalled();
});

// Test for edge cases
test('clears the error message when the form is valid', () => {
  const mockSubmit = jest.fn();
  render(<LoginForm onSubmit={mockSubmit} />);

  fireEvent.change(screen.getByPlaceholderText('Username'), {
    target: { value: '' },
  });

  fireEvent.click(screen.getByRole('button', { name: /login/i }));

  fireEvent.change(screen.getByPlaceholderText('Username'), {
    target: { value: 'test-user' },
  });
  fireEvent.change(screen.getByPlaceholderText('Password'), {
    target: { value: 'test-password' },
  });

  fireEvent.click(screen.getByRole('button', { name: /login/i }));

  expect(screen.queryByText('Both fields are required')).toBeNull();
  expect(mockSubmit).toHaveBeenCalledWith({
    username: 'test-user',
    password: 'test-password',
  });
});
```

In these tests, we're rendering the LoginForm component with a mock onSubmit function, simulating user interactions, and checking that the component behaves as expected. We're also testing that the component validates its props correctly and handles edge cases.