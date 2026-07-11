document.addEventListener("DOMContentLoaded", () => {
    const searchInput = document.getElementById("search-input");
    const searchResults = document.getElementById("search-results");
    
    if (!searchInput || !searchResults) return;

    let searchIndex = [];

    // Fetch the search index
    fetch("/search-index.json")
        .then(response => response.json())
        .then(data => {
            searchIndex = data;
        })
        .catch(error => console.error("Error loading search index:", error));

    searchInput.addEventListener("input", (e) => {
        const query = e.target.value.toLowerCase().trim();
        
        if (query.length < 2) {
            searchResults.style.display = "none";
            searchResults.innerHTML = "";
            return;
        }

        const filtered = searchIndex.filter(item => {
            return item.title.toLowerCase().includes(query) || 
                   item.keywords.some(k => k.toLowerCase().includes(query));
        }).slice(0, 8); // Limit to 8 results

        if (filtered.length > 0) {
            searchResults.innerHTML = filtered.map(item => `
                <a href="${item.url}" class="search-result-item">
                    <div style="font-weight: 500;">${item.title}</div>
                    <div class="text-sm text-muted">${item.type}</div>
                </a>
            `).join("");
            searchResults.style.display = "block";
        } else {
            searchResults.innerHTML = `
                <div class="search-result-item text-muted">
                    No results found for "${query}"
                </div>
            `;
            searchResults.style.display = "block";
        }
    });

    // Close search results when clicking outside
    document.addEventListener("click", (e) => {
        if (!searchInput.contains(e.target) && !searchResults.contains(e.target)) {
            searchResults.style.display = "none";
        }
    });
});
