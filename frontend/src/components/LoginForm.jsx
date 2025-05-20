Sure, here's a simple example of a React login form component. For this task, I am going to use React hooks, prop-types, styled-components for CSS-in-JS and React's controlled components concept for form handling. I am also going to include basic input validation and error handling.

Here is the complete code for the component:

```jsx
import React, { useState } from 'react';
import PropTypes from 'prop-types';
import styled from 'styled-components';

const Form = styled.form`
  display: flex;
  flex-direction: column;
`;

const Input = styled.input`
  margin-bottom: 10px;
`;

const ErrorMessage = styled.div`
  color: red;
  margin-bottom: 10px;
`;

/**
 * User login form component
 * @param {Object} props - Component props
 * @param {Function} props.onSubmit - Function to call when the form is submitted
 */
const LoginForm = ({ onSubmit }) => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState(null);

  const validateForm = () => {
    if (!username || !password) {
      setError('Both fields are required');
      return false;
    }
    setError(null);
    return true;
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    if (validateForm()) {
      onSubmit({ username, password });
    }
  };

  return (
    <Form onSubmit={handleSubmit}>
      {error && <ErrorMessage>{error}</ErrorMessage>}
      <Input
        type="text"
        placeholder="Username"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
      />
      <Input
        type="password"
        placeholder="Password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />
      <button type="submit">Login</button>
    </Form>
  );
};

LoginForm.propTypes = {
  onSubmit: PropTypes.func.isRequired,
};

export default LoginForm;
```

This LoginForm component initializes username and password to an empty string and error to null. The validateForm function checks if both username and password are provided, if not, it sets an error message. The handleSubmit function calls the validateForm function and if the form is valid, it calls the onSubmit prop function with the username and password as its argument.

The component renders a form with two inputs for username and password and a submit button. It also renders an error message if there's an error. The inputs' values are bound to the component's state and their onChange handlers update the state with the input's current value.

Finally, the component specifies that it expects a function prop named onSubmit.