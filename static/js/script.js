// AJAX form submission to dynamically load results without refreshing the page
document.querySelector('form').addEventListener('submit', function (event) {
    event.preventDefault();  // Prevent form from submitting normally
    const query = document.querySelector('input[name="q"]').value;  // Get the search query

    // Fetch results and replace the #results section content
    fetch(`/search/?q=${query}`)
        .then(response => response.text())
        .then(html => {
            const parser = new DOMParser();
            const doc = parser.parseFromString(html, 'text/html');
            const results = doc.querySelector('#results').innerHTML;
            document.getElementById('results').innerHTML = results;
        });
});