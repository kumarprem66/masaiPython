const saveBtn = document.getElementById('save_btn') as HTMLButtonElement;
const titleInput = document.getElementById('title') as HTMLInputElement;
const descripInput = document.getElementById('descrip') as HTMLInputElement;
const priorityInput = document.getElementById('priority') as HTMLInputElement;
const tableBody = document.querySelector('.content-table tbody') as HTMLTableSectionElement;

interface Todo {
  title: string;
  description: string;
  priority: string;
  isCompleted: boolean;
}

const todos: Todo[] = [];

// Function to add a new todo
function addTodo() {
  const newTodo: Todo = {
    title: titleInput.value,
    description: descripInput.value,
    priority: priorityInput.value,
    isCompleted: false
  };

  todos.push(newTodo);

  // Clear input fields
  titleInput.value = '';
  descripInput.value = '';

  // Update the table
  updateTable();
}

// Function to handle checkbox change
function handleCheckboxChange(index: number) {
  if (!todos[index].isCompleted) {
    todos.splice(index, 1);
    updateTable();
  }
}


function updateTable() {
    tableBody.innerHTML = '';
    todos.forEach((todo, index) => {
      const row = document.createElement('tr');
      row.innerHTML = `
        <td>${index + 1}</td>
        <td>${todo.title}</td>
        <td>${todo.description}</td>
        <td>${todo.priority}</td>
        <td><input type="checkbox" ${todo.isCompleted ? 'checked' : ''} data-index="${index}"></td>
      `;
      const checkbox = row.querySelector('input[type="checkbox"]');
      if (checkbox) {
        checkbox.addEventListener('change', () => {
          handleCheckboxChange(index);
        });
      }
      tableBody.appendChild(row);
    });
  }
saveBtn.addEventListener('click', addTodo);
