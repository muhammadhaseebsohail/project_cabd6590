Here is a simple registration form component using React, hooks, and PropTypes. It includes form creation, input validation, and error handling.

1. The complete component code with all imports:

```jsx
import React, { useState } from 'react';
import PropTypes from 'prop-types';
import './UserRegistrationForm.css';

/**
 * User Registration Form
 * @param {*} props 
 * @returns 
 */
const UserRegistrationForm = (props) => {
    const [formData, setFormData] = useState({
        name: '',
        email: '',
        password: '',
    });

    const [formError, setFormError] = useState({
        name: '',
        email: '',
        password: '',
    });

    const handleInputChange = (event) => {
        const { name, value } = event.target;
        setFormData({...formData, [name]: value});
    }

    const handleSubmit = (event) => {
        event.preventDefault();
        const error = validateData();
        if (Object.keys(error).length === 0) {
            props.onSubmit(formData);
        } else {
            setFormError(error);
        }
    }

    const validateData = () => {
        let error = {};
        if (formData.name.trim().length < 3) {
            error.name = "Name should be at least 3 characters long";
        }
        if (!formData.email.includes('@')) {
            error.email = "Invalid email";
        }
        if (formData.password.length < 5) {
            error.password = "Password should be at least 5 characters long";
        }
        return error;
    }

    return (
        <form onSubmit={handleSubmit} className="user-registration-form">
            <input type="text" name="name" value={formData.name} onChange={handleInputChange} placeholder="Name"/>
            {formError.name && <p className="error-message">{formError.name}</p>}
            <input type="email" name="email" value={formData.email} onChange={handleInputChange} placeholder="Email"/>
            {formError.email && <p className="error-message">{formError.email}</p>}
            <input type="password" name="password" value={formData.password} onChange={handleInputChange} placeholder="Password"/>
            {formError.password && <p className="error-message">{formError.password}</p>}
            <button type="submit">Register</button>
        </form>
    )
}

export default UserRegistrationForm;
```

2. Any necessary CSS/styling:

```css
/* UserRegistrationForm.css */
.user-registration-form {
    display: flex;
    flex-direction: column;
    width: 300px;
    margin: 0 auto;
}

.user-registration-form input {
    margin-bottom: 10px;
    padding: 10px;
    border-radius: 5px;
    border: 1px solid #ccc;
}

.user-registration-form button {
    padding: 10px;
    border-radius: 5px;
    border: none;
    background-color: #007BFF;
    color: #fff;
}

.error-message {
    color: red;
    margin-bottom: 10px;
}
```

3. PropTypes or TypeScript interfaces:

```jsx
UserRegistrationForm.propTypes = {
    onSubmit: PropTypes.func.isRequired,
}
```

4. Export statements:

```jsx
export default UserRegistrationForm;
```