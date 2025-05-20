Sure, here's a comprehensive set of unit tests for the ForgetPassword component using Jest and React Testing Library:

```jsx
import React from 'react';
import { render, fireEvent, cleanup } from '@testing-library/react';
import '@testing-library/jest-dom/extend-expect';
import ForgetPassword from './ForgetPassword'; 

afterEach(cleanup);

describe('ForgetPassword', () => {
  const onSubmit = jest.fn();

  it('renders without crashing', () => {
    const { getByPlaceholderText } = render(<ForgetPassword onSubmit={onSubmit} />);
    expect(getByPlaceholderText('Email')).toBeInTheDocument();
  });

  it('calls onSubmit prop on form submission', () => {
    const { getByPlaceholderText, getByText } = render(<ForgetPassword onSubmit={onSubmit} />);
    const input = getByPlaceholderText('Email');
    const button = getByText('Reset Password');

    fireEvent.change(input, { target: { value: 'test@example.com' } });
    fireEvent.click(button);

    expect(onSubmit).toHaveBeenCalled();
  });

  it('shows an error message if the email is not valid', () => {
    const { getByPlaceholderText, getByText } = render(<ForgetPassword onSubmit={onSubmit} />);
    const input = getByPlaceholderText('Email');
    const button = getByText('Reset Password');

    fireEvent.change(input, { target: { value: 'not a valid email' } });
    fireEvent.click(button);

    expect(getByText('Please enter a valid email')).toBeInTheDocument();
  });

  it('does not call onSubmit prop if the email is not valid', () => {
    const { getByPlaceholderText, getByText } = render(<ForgetPassword onSubmit={onSubmit} />);
    const input = getByPlaceholderText('Email');
    const button = getByText('Reset Password');

    fireEvent.change(input, { target: { value: 'not a valid email' } });
    fireEvent.click(button);

    expect(onSubmit).not.toHaveBeenCalled();
  });
});
```

This set of tests covers:

1. Component rendering: The first test checks if the component renders without crashing and if the input field for the email is present in the document.
2. User interactions: The second and third tests check if the form behaves correctly when the user interacts with it. They simulate user input with the fireEvent.change method and form submission with fireEvent.click.
3. Props validation: The second and fourth tests check if the onSubmit prop is called or not called correctly depending on the validity of the input.
4. Edge cases: The third and fourth tests cover the edge case where the user inputs an invalid email. They check if the error message is shown correctly and if the onSubmit prop is not called in this case.