document.addEventListener('DOMContentLoaded', function() {
    const taskForm = document.getElementById('task-form');
    const taskList = document.getElementById('task-list');
    const overdueCount = document.getElementById('overdue-count');

    // Function to update overdue tasks count
    function updateOverdueCount() {
        const tasks = Array.from(taskList.children);
        const overdueTasks = tasks.filter(task => {
            const dueDate = new Date(task.dataset.dueDate);
            return dueDate < new Date() && !task.classList.contains('completed');
        });
        overdueCount.textContent = overdueTasks.length;
    }

    // Event listener for task form submission
    taskForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const taskInput = document.getElementById('task-input');
        const dueDateInput = document.getElementById('due-date-input');

        const newTask = document.createElement('li');
        newTask.textContent = taskInput.value;
        newTask.dataset.dueDate = dueDateInput.value;
        newTask.classList.add('task-item');

        // Add completion status toggle
        newTask.addEventListener('click', function() {
            newTask.classList.toggle('completed');
            updateOverdueCount();
        });

        taskList.appendChild(newTask);
        taskInput.value = '';
        dueDateInput.value = '';
        updateOverdueCount();
    });

    // Initial update of overdue tasks count
    updateOverdueCount();
});