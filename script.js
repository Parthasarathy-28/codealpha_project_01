document.addEventListener("DOMContentLoaded", () => {
  const searchInput = document.getElementById("search");
  const categoryFilter = document.getElementById("category-filter");
  const cards = document.querySelectorAll(".card");
  const themeToggle = document.getElementById("theme-toggle");
  const body = document.body;

  function filterResources() {
    const searchText = searchInput.value.toLowerCase();
    const category = categoryFilter.value;

    cards.forEach((card) => {
      const text = card.textContent.toLowerCase();
      const cardCategory = card.getAttribute("data-category");

      const matchesSearch = text.includes(searchText);
      const matchesCategory = category === "all" || category === cardCategory;

      card.style.display = matchesSearch && matchesCategory ? "" : "none";
    });
  }

  searchInput.addEventListener("keyup", filterResources);
  categoryFilter.addEventListener("change", filterResources);

  // Dark Mode Toggle
  themeToggle.addEventListener("click", () => {
    body.classList.toggle("dark-mode");
    themeToggle.textContent = body.classList.contains("dark-mode")
      ? "☀️ Light Mode"
      : "🌙 Dark Mode";
  });
});
