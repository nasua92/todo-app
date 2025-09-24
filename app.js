
let lists = {};

function createList() {
    const name = document.getElementById("newListName").value;
    if (!name || lists[name]) return;
    lists[name] = [];
    renderLists();
    document.getElementById("newListName").value = "";
}

function addTask(listName, taskText) {
    if (!taskText) return;
    lists[listName].push({ text: taskText, done: false });
    renderLists();
}

function toggleTask(listName, index) {
    lists[listName][index].done = !lists[listName][index].done;
    renderLists();
}

function renderLists() {
    const container = document.getElementById("lists");
    container.innerHTML = "";
    for (const name in lists) {
        const listDiv = document.createElement("div");
        listDiv.className = "list";
        listDiv.innerHTML = `<h2>${name}</h2>`;

        lists[name].forEach((task, i) => {
            const taskDiv = document.createElement("div");
            taskDiv.className = "task";
            taskDiv.innerHTML = `<span class="${task.done ? 'completed' : ''}" onclick="toggleTask('${name}', ${i})">${task.text}</span>`;
            listDiv.appendChild(taskDiv);
        });

        const input = document.createElement("input");
        input.placeholder = "New task";
        input.onkeypress = function(e) {
            if (e.key === "Enter") addTask(name, input.value);
        };
        listDiv.appendChild(input);

        container.appendChild(listDiv);
    }
}
