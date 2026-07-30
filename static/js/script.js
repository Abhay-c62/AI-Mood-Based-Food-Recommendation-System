// Toggle Dark Mode
function toggleTheme() {
    document.body.classList.toggle("dark");

    // Change button text
    const btn = document.getElementById("themeBtn");

    if (btn) {
        if (document.body.classList.contains("dark")) {
            btn.innerHTML = "☀️ Light Mode";
        } else {
            btn.innerHTML = "🌙 Dark Mode";
        }
    }
}
// Fade in cards when page loads
window.addEventListener("load", () => {
    const cards = document.querySelectorAll(".food-card");

    cards.forEach((card, index) => {
        card.style.opacity = "0";
        card.style.transform = "translateY(30px)";

        setTimeout(() => {
            card.style.transition = "all 0.6s ease";
            card.style.opacity = "1";
            card.style.transform = "translateY(0)";
        }, index * 120);
    });
});