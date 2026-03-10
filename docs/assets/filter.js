// RSS AI Digest - Filter functionality

document.addEventListener('DOMContentLoaded', function() {
    const filterSelect = document.getElementById('source-filter');
    const articlesList = document.getElementById('articles-list');

    if (!filterSelect || !articlesList) {
        return;
    }

    filterSelect.addEventListener('change', function() {
        const selectedSource = this.value;
        const articleCards = articlesList.querySelectorAll('.article-card');

        articleCards.forEach(card => {
            const cardSource = card.getAttribute('data-source');

            if (selectedSource === 'all' || cardSource === selectedSource) {
                card.classList.remove('hidden');
            } else {
                card.classList.add('hidden');
            }
        });

        // Hide empty date sections
        const dateGroups = articlesList.querySelectorAll('.date-group');
        dateGroups.forEach(group => {
            const visibleCards = group.querySelectorAll('.article-card:not(.hidden)');
            if (visibleCards.length === 0) {
                group.style.display = 'none';
            } else {
                group.style.display = 'block';
            }
        });
    });
});