var saveBtn = document.getElementById('save_btn');
var titleInput = document.getElementById('title');
var descripInput = document.getElementById('descrip');
var priorityInput = document.getElementById('priority');
var tableBody = document.querySelector('.content-table tbody');
var todos = [];
// Function to add a new todo
function addTodo() {
    var newTodo = {
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
function handleCheckboxChange(index) {
    if (!todos[index].isCompleted) {
        todos.splice(index, 1);
        updateTable();
    }
}

function updateTable() {
    tableBody.innerHTML = '';
    todos.forEach(function (todo, index) {
        var row = document.createElement('tr');
        row.innerHTML = "\n        <td>".concat(index + 1, "</td>\n        <td>").concat(todo.title, "</td>\n        <td>").concat(todo.description, "</td>\n        <td>").concat(todo.priority, "</td>\n        <td><input type=\"checkbox\" ").concat(todo.isCompleted ? 'checked' : '', " data-index=\"").concat(index, "\"></td>\n      ");
        var checkbox = row.querySelector('input[type="checkbox"]');
        if (checkbox) {
            checkbox.addEventListener('change', function () {
                handleCheckboxChange(index);
            });
        }
        tableBody.appendChild(row);
    });
}
saveBtn.addEventListener('click', addTodo);
