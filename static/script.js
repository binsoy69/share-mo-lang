function refreshFileList() {
  fetch("/files")
    .then((response) => response.json())
    .then((files) => {
      const list = document.getElementById("file-list");
      list.innerHTML = "";

      files.forEach((file) => {
        const li = document.createElement("li");
        const container = document.createElement("div");
        container.className = "file-entry-vertical";

        const link = document.createElement("a");
        link.href = `/download/${file.name}`;
        link.textContent = `📎 ${file.name}`;
        link.target = "_blank";

        const size = document.createElement("span");
        size.className = "file-size";
        size.textContent = `(${file.size_kb} KB)`;

        const form = document.createElement("form");
        form.method = "POST";
        form.action = `/delete/${encodeURIComponent(file.name)}`;
        form.onsubmit = () => confirm(`Delete ${file.name}?`);

        const button = document.createElement("button");
        button.type = "submit";
        button.className = "delete-btn";
        button.textContent = "🗑️ Delete";

        form.appendChild(button);

        container.appendChild(link);
        container.appendChild(size);
        container.appendChild(form);
        li.appendChild(container);
        list.appendChild(li);
      });
    });
}

// ✅ Load immediately on page load
document.addEventListener("DOMContentLoaded", refreshFileList);

// ✅ Continue refreshing every 5s
setInterval(refreshFileList, 5000);
