// RSS AI Digest - Filter and Search functionality

document.addEventListener('DOMContentLoaded', function() {
    const filterSelect = document.getElementById('source-filter');
    const searchInput = document.getElementById('search-input');
    const articlesList = document.getElementById('articles-list');

    if (!filterSelect || !articlesList) {
        return;
    }

    function filterArticles() {
        const selectedSource = filterSelect.value;
        const searchTerm = searchInput ? searchInput.value.toLowerCase().trim() : '';
        const articleCards = articlesList.querySelectorAll('.article-card');

        articleCards.forEach(card => {
            const cardSource = card.getAttribute('data-source');
            const title = card.querySelector('h3')?.textContent.toLowerCase() || '';
            const summary = card.querySelector('.summary-full')?.textContent?.toLowerCase() || '';

            const matchesSource = selectedSource === 'all' || cardSource === selectedSource;
            const matchesSearch = searchTerm === '' || title.includes(searchTerm) || summary.includes(searchTerm);

            if (matchesSource && matchesSearch) {
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

        // Show "no results" message if needed
        const visibleCards = articlesList.querySelectorAll('.article-card:not(.hidden)');
        let noResultsMsg = document.getElementById('no-results');

        if (visibleCards.length === 0) {
            if (!noResultsMsg) {
                noResultsMsg = document.createElement('div');
                noResultsMsg.id = 'no-results';
                noResultsMsg.className = 'no-results';
                noResultsMsg.innerHTML = '<h3>No articles found</h3><p>Try adjusting your filters or search terms</p>';
                articlesList.insertBefore(noResultsMsg, articlesList.firstChild);
            }
            noResultsMsg.style.display = 'block';
        } else if (noResultsMsg) {
            noResultsMsg.style.display = 'none';
        }
    }

    // Filter by source
    filterSelect.addEventListener('change', filterArticles);

    // Search functionality
    if (searchInput) {
        searchInput.addEventListener('input', filterArticles);
    }
});