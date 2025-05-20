It seems like there's a misunderstanding. Setting up a testing suite for a frontend is not about creating a React component, it's about configuring your project to use testing tools like Jest, Enzyme or React Testing Library.

However, I can show you how to create a simple React component with a list of requirements for a task and create a test for it using Jest and React Testing Library.

Let's create a simple `Task` component:

```jsx
// Task.js

import React from 'react';
import PropTypes from 'prop-types';

/**
 * Task component
 * @param {Object} props - Component props
 * @param {string} props.task - Task description
 * @param {string[]} props.requirements - List of task requirements
 */
const Task = ({ task, requirements }) => (
  <div>
    <h1>{task}</h1>
    <ul>
      {requirements.map((requirement, index) => (
        <li key={index}>{requirement}</li>
      ))}
    </ul>
  </div>
);

Task.propTypes = {
  task: PropTypes.string.isRequired,
  requirements: PropTypes.arrayOf(PropTypes.string).isRequired,
};

export default Task;
```

For the styling, let's use CSS modules:

```css
/* Task.module.css */

h1 {
  color: #333;
  font-size: 24px;
}

ul {
  list-style: none;
  padding: 0;
}

li {
  margin: 10px 0;
}
```

Then, import the CSS module in the component:

```jsx
// Task.js

import React from 'react';
import PropTypes from 'prop-types';
import styles from './Task.module.css';

// ...
<div className={styles.Task}>
  <h1 className={styles.title}>{task}</h1>
  <ul className={styles.list}>
    {requirements.map((requirement, index) => (
      <li key={index} className={styles.listItem}>{requirement}</li>
    ))}
  </ul>
</div>
// ...
```

Now, let's write a test for this component:

```jsx
// Task.test.js

import React from 'react';
import { render } from '@testing-library/react';
import Task from './Task';

test('renders the task and its requirements', () => {
  const task = 'Set up testing suite for frontend';
  const requirements = ['Unit tests', 'Integration tests'];

  const { getByText } = render(<Task task={task} requirements={requirements} />);

  expect(getByText(task)).toBeInTheDocument();
  requirements.forEach(requirement => {
    expect(getByText(requirement)).toBeInTheDocument();
  });
});
```

In this test, we render the `Task` component with a task and its requirements, then we use `getByText` function from React Testing Library to find these texts in the document.