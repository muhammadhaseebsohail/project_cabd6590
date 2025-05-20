Sure, here is a simple ForgetPassword component built with React, React Hook Form for form handling and validation, and styled-components for styling:

1. Component Code:

```jsx
import React from "react";
import { useForm } from "react-hook-form";
import styled from "styled-components";
import PropTypes from "prop-types";

const Form = styled.form`
  display: flex;
  flex-direction: column;
  width: 100%;
  max-width: 400px;
`;

const Input = styled.input`
  margin-bottom: 20px;
  padding: 10px;
  border: 1px solid #ccc;
`;

const Button = styled.button`
  padding: 10px;
  color: #fff;
  background-color: #007bff;
  border: none;
  cursor: pointer;
`;

const Error = styled.div`
  color: #ff0000;
  margin-bottom: 10px;
`;

const ForgetPassword = ({ onSubmit }) => {
  const { register, handleSubmit, errors } = useForm();

  return (
    <Form onSubmit={handleSubmit(onSubmit)}>
      <Input
        name="email"
        placeholder="Email"
        ref={register({ required: true, pattern: /^\S+@\S+$/i })}
      />
      {errors.email && <Error>Please enter a valid email</Error>}

      <Button type="submit">Reset Password</Button>
    </Form>
  );
};

ForgetPassword.propTypes = {
  onSubmit: PropTypes.func.isRequired,
};

export default ForgetPassword;
```

2. CSS/Styling: CSS-in-JS is used for styling in the above code (with styled-components).

3. PropTypes:
```jsx
ForgetPassword.propTypes = {
  onSubmit: PropTypes.func.isRequired,
};
```

4. Export statement:
```jsx
export default ForgetPassword;
```

This component accepts a function as a prop which will be called upon form submission. The function should handle the actual logic of password resetting. The form validates the email input and provides an error message if the input is not a valid email.